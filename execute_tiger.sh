#!/bin/sh

mkdir -p CapEval/data/

cp data/tiger/candidates CapEval/data/ -R
cp data/tiger/precomp CapEval/data/ -R

conda env create -f data/tiger/tiger_env.yml
conda env create -f data/tiger/tiger_features_env.yml

cd CapEval/

if [ ! -d "./runs/coco_scan/log/" ] 
then
 mkdir  -p ./runs/coco_scan/log/
 cd runs/coco_scan/log/
 pip install gdown
 gdown 1MbTqWVsl5QGbjRL5ClmY3Ns7uC7lJkSt
 cd ../../../
fi



eval "$(conda shell.bash hook)"


conda activate tiger_features
cd SCAN
touch __init__.py
#Extracting features from image using faster-R-CNN
git clone https://github.com/shilrley6/Faster-R-CNN-with-model-pretrained-on-Visual-Genome.git
cd Faster-R-CNN-with-model-pretrained-on-Visual-Genome
pip install -r requirements.txt
cd lib
rm -rf pycocotools/
git clone https://github.com/pdollar/coco.git
cd coco/PythonAPI/
make
make install 
cd ../../
python setup.py build develop
cd ..


if [! -d "models"]; 
then
 mkdir -p models
 cd models
 pip install gdown
 gdown 18n_3V1rywgeADZ3oONO0DsuuS9eMW6sN # download  faster_rcnn_res101_vg.pth from https://drive.google.com/u/0/uc?id=18n_3V1rywgeADZ3oONO0DsuuS9eMW6sN&export=download
 cd ..
fi

cp ../../../data/tiger/exec.sh ./exec.sh
cp ../../../data/tiger/pIUpJihiju0_frames_1040.jpg ./images/pIUpJihiju0_frames_1040.jpg
cp ../../../data/tiger/videos_ids.txt ./videos_ids.txt
cp ../../../data/tiger/generate_tsv_2.py ./generate_tsv_2.py
pip install Pillow==7.1.0
sh exec.sh
cp data_video_scan.npy ../../data/precomp/my_img/cand_ims.npy
cd ../../


conda deactivate

#Executing tiger score
conda activate tiger
sh install_requirement.sh
cp ../data/tiger/main.py ./main.py
cp ../data/tiger/data_util.py ./data_util.py

python main.py --data_name my --data_path $PWD/data/precomp/ --candidate_path $PWD/data/candidates --output_path $PWD/data/output/

cd ../
