#!/usr/bin/env sh
export LANG=en_US.UTF-8
cp coco_caption_evaluation.py coco-caption/ 
cp data/annotations/* coco-caption/annotations/
cp data/results/* coco-caption/results/
cd coco-caption/
FILE=pycocoevalcap/spice/lib/stanford-corenlp-3.6.0.jar
if [ ! -f "$FILE" ]; then
    sh ./get_stanford_models.sh
fi
python2 coco_caption_evaluation.py
cd ..

