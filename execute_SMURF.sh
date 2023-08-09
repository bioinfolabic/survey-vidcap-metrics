#!/bin/sh

cp data/smurf/*.json SMURF/data/

cp data/smurf/*.py SMURF/

cd SMURF

sh requirements/install.sh

echo "\n\nFigure 5 Candidate A\n\n"
python smurf_paper_predA.py

echo "\n\nFigure 5 Candidate B\n\n"

python smurf_paper_predB.py

cd ..
