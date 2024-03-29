import json
from smurf.eval import preprocess,smurf_eval_captions
from smurf.system_analysis import smurf_system_analysis

ref_file = 'data/ref.json'
cand_file = 'data/predB.json'
result_file = 'results/smurf_scores_predB.json'

#load and preprocess example caption set
ref_list = json.loads(open(ref_file, 'r').read())
cand_list = json.loads(open(cand_file, 'r').read())
cands = [preprocess(cap['caption']) for cap in cand_list]
ref_dict = {cap['image_id']:[] for cap in ref_list}
for i,cap in enumerate(ref_list):
    ref_dict[cap['image_id']].append(preprocess(cap['caption']))
refs = [ref_dict[cap['image_id']] for cap in cand_list]


#perform caption-level analysis of example caption set
meta_scorer = smurf_eval_captions(refs, cands, fuse=True)
scores = meta_scorer.evaluate()
with open(result_file, 'w') as outfile:
    json.dump(scores, outfile)


#perform system-level analysis from Figure 1 of SMURF paper
#standardization_file = 'smurf/standardize_estimates.txt'
#set based on the number of captioning systems you are comparing
#number_of_captioners = 4
#length of plot colors must be same as number_of_captioners
#plot_colors = ['saddlebrown', 'royalblue', 'crimson', 'lawngreen']
#plot_file = 'results/system_plot.png'
#analysis = smurf_system_analysis(in_file='results/smurf_scores.json',n_systems=number_of_captioners)
#analysis.load_standardized_scores(estimates_file=standardization_file)
#analysis.generate_plot(plot_colors,out_file=plot_file)
#model_penalties = analysis.compute_grammar_penalities()
#for num,total_penalty in enumerate(model_penalties):
#    print('Model %i Penalty: %f'%(num+1,total_penalty))
