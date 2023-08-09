#!/bin/sh

cd bert_score

pip install .

mkdir ./data
cp ../data/bert_score data/ -R
echo "\n\nFigure 5 Candidate A\n\n"
bert-score -r data/bert_score/ref/referencia0.txt data/bert_score/ref/referencia1.txt data/bert_score/ref/referencia2.txt data/bert_score/ref/referencia3.txt data/bert_score/ref/referencia4.txt data/bert_score/ref/referencia5.txt -c data/bert_score/pred/predicao_5A.txt --lang en --rescale_with_baseline

echo "\n\nFigure 5 Candidate B\n\n"
bert-score -r data/bert_score/ref/referencia0.txt data/bert_score/ref/referencia1.txt data/bert_score/ref/referencia2.txt data/bert_score/ref/referencia3.txt data/bert_score/ref/referencia4.txt data/bert_score/ref/referencia5.txt -c data/bert_score/pred/predicao_5B.txt --lang en --rescale_with_baseline
