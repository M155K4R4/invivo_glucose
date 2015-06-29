def outlier_removal(filename): #{
	# read in the text document that stores the data into an array
	#data_array = [];
	
	#read in data from the recent .txt file
	#so will there be one text file per run then....
	data_array = []
	with open(filename) as f:
		information = f.read().splitlines()
	
	max_std = 0 # maximum standard deviation per round
	for i in range (0, len(data_array)):
		# calculate the standard deviation of it
	
#}