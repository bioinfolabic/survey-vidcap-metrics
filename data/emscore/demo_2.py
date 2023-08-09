from emscore.scorer import EMScorer


if __name__ == '__main__':


	def calculate(desc_list, vids):


	    # you video's path list
	    
	    metric = EMScorer()
	    # the candidate caption
	    refs=['not used']
	    
	    for a in desc_list:
	        cands = [a]
	        results = metric.score(cands=cands, refs=refs, vids=vids, idf=True)
	    
	        """
	        only use video as groud truth
	        """
	        print("-----------------------------------------------------------------------")
	        print(a)
	        print('------------------------------------------------------------------------')
	        print('fine-grained EMScore(X,V), P: {}, R:{}, F:{}'.format(
	        results['EMScore(X,V)']['full_P'], results['EMScore(X,V)']['full_R'], results['EMScore(X,V)']['full_F']))
	        print(
		    'coarse-grained EMScore(X,V), {}'.format(results['EMScore(X,V)']['cogr']))
	        print('fine- and coarse-grained EMScore(X,V), P: {}, R:{}, F:{}'.format(
		    results['EMScore(X,V)']['full_P'], results['EMScore(X,V)']['full_R'], results['EMScore(X,V)']['full_F']))
	        
	        
	vids = ['videos/video7966.mp4']
	desc_list = [
	     'potatoes are slicing the man',
	     'a man demonstrates how to fry thin potatoes slices',
	     'this is a video of a potato and a man',
	     
	    'a guy slices a potato',
	    'a man is cutting a potato',
	    'a man slices a potato in the kitchen',
	    'a man is cutting a potato in a kitchen with knife and talking about that',
	    'a man shows how to thinly slice potatoes',
	    'a man slices potato into equal pieces'
	    ]
		
	calculate(desc_list, vids)
	print("")
	print("")
	print("")
	

	vids = ['videos/video5344.mp4']
	desc_list = [
	    'this is a video of a man watching TV',
	    'a fat man wearing a black shirt is cooking a sandwich in front of a camera',
	    'a video showing an obese man wearing a red sweater speaking in a documentary', 

	    'video of a man talking about an overweight man',
	    'an obese man is wearing a red sweater',
	    'a man is talking about how much a man weighs and what he has done',
	    'a male showing off his food while another male provides commentary',
	    'a guy talks about how another man is so fat',
	    'a man holds a big plate of food and he weighs 910 pounds'
	    
	    ]
		
	calculate(desc_list, vids)

	

