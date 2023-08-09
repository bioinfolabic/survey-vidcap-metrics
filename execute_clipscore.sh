#!/bin/sh
cd clipscore/

if [ ! -d "pycocoevalcap" ] 
then
    git clone https://github.com/jmhessel/pycocoevalcap.git 
fi


if [ ! -d "CLIP" ] 
then
    #git clone https://github.com/openai/CLIP.git
    #conda install --yes -c pytorch pytorch=1.7.1 torchvision cudatoolkit=11.0
    #pip install ftfy regex tqdm
    pip install git+https://github.com/openai/CLIP.git
fi




echo "\n\nFigure 5) Candidate A\n\n"
python clipscore.py ../data/clipscore/0/bad_captions.json ../data/clipscore/0/img/

echo "\n\nFigure 5) Candidate B\n\n"
python clipscore.py ../data/clipscore/0/good_captions.json ../data/clipscore/0/img/

cd ..

