#!/usr/bin/env sh

cd wembsim/

FILE=crawl-300d-2M.vec.zip
if [ ! -f "$FILE" ]; then
    wget https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M.vec.zip
    unzip crawl-300d-2M.vec.zip
fi
python compute_wembsim.py
cd ..

