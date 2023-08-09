#!/bin/sh
eval "$(conda shell.bash hook)"
conda create -n vilbertscore python=3.6
conda activate vilbertscore
conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
cd ViLBERTScore
pip install -r requirements.txt
python3 setup.py develop

python3 generate_pickle_files.py
python3 script/extract_features.py --model_file data/detectron_model.pth --config_file data/detectron_config.yaml --image_dir img_avaliacao --output_folder data/avaliacao/

#python script/convert_to_lmdb.py --features_dir data/avaliacao/features --lmdb_file data/avaliacao/imgs_rcnn.pkl
python3 generatepks_file_imgs.py
cp data/avaliacao/cand_caps_bad.pkl data/avaliacao/cand_caps.pkl
python3 compute_vilbertscore.py --dataset avaliacao --result_name bad

cp data/avaliacao/cand_caps_good.pkl data/avaliacao/cand_caps.pkl
python3 compute_vilbertscore.py --dataset avaliacao --result_name good

cd ..
