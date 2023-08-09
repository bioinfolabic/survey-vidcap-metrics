#!/usr/bin/env sh


cp data/annotations/*cider.json cider/data
cp data/results/*.json cider/data


cd cider/
printf "\n\nFigure 4A) Candidate A\n\n"
cp ../data/cider/params_cider4A_A.json params.json
python2 cidereval.py

printf "\n\nFigure 4A) Candidate B\n\n"
cp ../data/cider/params_cider4A_B.json params.json
python2 cidereval.py


printf "\n\nFigure 4B) Candidate A\n\n"
cp ../data/cider/params_cider4B_A.json params.json
python2 cidereval.py

printf "\n\nFigure 4B) Candidate B\n\n"
cp ../data/cider/params_cider4B_B.json params.json
python2 cidereval.py

printf "\n\nFigure 4C) Candidate A\n\n"
cp ../data/cider/params_cider4C_A.json params.json
python2 cidereval.py

printf "\n\nFigure 4C) Candidate B\n\n"
cp ../data/cider/params_cider4C_B.json params.json
python2 cidereval.py

printf "\n\nFigure 5 Candidate A\n\n"
cp ../data/cider/params_cider5_A.json params.json
python2 cidereval.py

printf "\n\nFigure 5 Candidate B\n\n"
cp ../data/cider/params_cider5_B.json params.json
python2 cidereval.py

