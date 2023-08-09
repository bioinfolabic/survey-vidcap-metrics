#!/usr/bin/env sh
export LANG=en_US.UTF-8
if [ ! -d "emscore/videos/" ]; then
    mkdir emscore/videos/
fi

cp data/emscore/*.mp4 emscore/videos/

cp data/emscore/demo_2.py emscore/demo_2.py
cd emscore/

#conda install --yes -c pytorch pytorch=1.7.1 torchvision cudatoolkit=11.0
#pip install ftfy regex tqdm
git clone https://github.com/openai/CLIP.git
pip install CLIP
cp ../data/emscore/model.py CLIP/clip/model.py
python demo_2.py
cd ..
