import sys
sys.path.append("pycocoevalcap")
sys.path.append("pycocoevalcap/bleu")
sys.path.append("pycocoevalcap/cider")
from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap
import json
from json import encoder



encoder.FLOAT_REPR = lambda o: format(o, '.3f')

print("")
print("Figure 4A) Candidate A")

# set up file names and pathes
annFile = "annotations/referencia4A.json"
resFile = "results/prediction_4A_A.json"

coco = COCO(annFile)
cocoRes = coco.loadRes(resFile)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate results
cocoEval.evaluate()

# print output evaluation scores
for metric, score in cocoEval.eval.items():
    print ('%s: %.3f'%(metric, score))
    
    
print("")
print("Figure 4A) Candidate B")

# set up file names and pathes
annFile = "annotations/referencia4A.json"
resFile = "results/prediction_4A_B.json"

coco = COCO(annFile)
cocoRes = coco.loadRes(resFile)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate results
cocoEval.evaluate()

# print output evaluation scores
for metric, score in cocoEval.eval.items():
    print ('%s: %.3f'%(metric, score))



print("")
print("Figure 4B) Candidate A")

# set up file names and pathes
annFile = "annotations/referencia4B.json"
resFile = "results/prediction_4B_A.json"

coco = COCO(annFile)
cocoRes = coco.loadRes(resFile)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate results
cocoEval.evaluate()

# print output evaluation scores
for metric, score in cocoEval.eval.items():
    print ('%s: %.3f'%(metric, score))
    
    
print("")
print("Figure 4B) Candidate B")

# set up file names and pathes
annFile = "annotations/referencia4B.json"
resFile = "results/prediction_4B_B.json"

coco = COCO(annFile)
cocoRes = coco.loadRes(resFile)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate results
cocoEval.evaluate()

# print output evaluation scores
for metric, score in cocoEval.eval.items():
    print ('%s: %.3f'%(metric, score))
    
    
    

print("")
print("Figure 4C) Candidate A")

# set up file names and pathes
annFile = "annotations/referencia4C.json"
resFile = "results/prediction_4C_A.json"

coco = COCO(annFile)
cocoRes = coco.loadRes(resFile)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate results
cocoEval.evaluate()

# print output evaluation scores
for metric, score in cocoEval.eval.items():
    print ('%s: %.3f'%(metric, score))
    
    
print("")
print("Figure 4C) Candidate B")

# set up file names and pathes
annFile = "annotations/referencia4C.json"
resFile = "results/prediction_4C_B.json"

coco = COCO(annFile)
cocoRes = coco.loadRes(resFile)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate results
cocoEval.evaluate()

# print output evaluation scores
for metric, score in cocoEval.eval.items():
    print ('%s: %.3f'%(metric, score))
    
    

print("")
print("Figure 5 Candidate A")

# set up file names and pathes
annFile = "annotations/referencia5.json"
resFile = "results/prediction_5_A.json"

coco = COCO(annFile)
cocoRes = coco.loadRes(resFile)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate results
cocoEval.evaluate()

# print output evaluation scores
for metric, score in cocoEval.eval.items():
    print ('%s: %.3f'%(metric, score))
    
    
print("")
print("Figure 5 Candidate B")

# set up file names and pathes
annFile = "annotations/referencia5.json"
resFile = "results/prediction_5_B.json"

coco = COCO(annFile)
cocoRes = coco.loadRes(resFile)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate results
cocoEval.evaluate()

# print output evaluation scores
for metric, score in cocoEval.eval.items():
    print ('%s: %.3f'%(metric, score))
    
