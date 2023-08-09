
import io
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
from scipy import spatial

stop_words = set(stopwords.words('english'))

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = list(map(float, tokens[1:]))
    return data



embedding = load_vectors('crawl-300d-2M.vec')
embedding_keys = embedding.keys()
def compute_MOWE(description):
	word_tokens = word_tokenize(description)
	w_embedding = np.zeros(300)
	for aWord in word_tokens:
		if aWord not in stop_words and aWord in embedding_keys:
			w_embedding = np.sum([w_embedding, np.array(embedding[aWord])], axis=0)
	return w_embedding



cand_bad = ['a man in a blue shirt and black pants is working out in a gym']


cand_good = ['a person is mopping the gym floor']

ref = ['the person cleans a gym with the large dust mop', 'a man sweeps the floor of a gym', 'a man sweeps the gymnasium floor with a dust broom', 'a man in a blue shirt and black trousers sweeping a gym floor', 'a man in a blue shirt is sweeping a classroom', 'a man in black pants is mopping the floor of a gym room']

references = [ref]


for i in range(len(cand_bad)):
	bad_candidate = cand_bad[i]
	good_candidate = cand_good[i]
	references_img = references[i]
	print("")
	print("")
	print("")
	print("bad_candidate", bad_candidate)
	print("good_candidate", good_candidate)
	print("references_img", references_img)
	print("")
	
	
	vector_bad = compute_MOWE(bad_candidate)
	vector_good = compute_MOWE(good_candidate)
	
	sum_score_bad = 0
	sum_score_good = 0
	
	for a_ref in references_img:
		vector_ref = compute_MOWE(a_ref)
		sum_score_bad += spatial.distance.cosine(vector_bad, vector_ref)
		sum_score_good += spatial.distance.cosine(vector_good, vector_ref)
	score_bad = sum_score_bad / len(references_img)
	score_good = sum_score_good / len(references_img)
	print("Score good", score_good)
	print("Score bad", score_bad)
	

