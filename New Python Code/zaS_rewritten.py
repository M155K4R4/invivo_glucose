"""
Kathryn DiPippo
6/15/2015
zaS_rewritten.py
- To use, the ziDAQ library needs to be installed for Python: http://www.zhinst.com/blogs/schwizer/2011/05/controlling-the-hf2-li-lock-in-with-python/
- Creates the data structure to store data from lock-in
- Reads the lock-in amplifier
- This is the code directly from the website, as going through and editing
	the old code turned out to be too inconsistent

TO-DO
- outlier_removal
- gui integration


"""

import time, math
import zhinst.ziPython, zhinst.utils
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

# =====================================================================================================================
def main(): #{
	# PRIMARY VARIABLES (later to be read in from a GUI
	# The inputs below determine the name of the text file
	name = 'Michelle'
	concentration = 80
	date = 062415
	outlier_removal_flag = 0	# 0 if data wishes to be left as is
								# 1 if data will be reduced to num_of_final_runs
	total_initial_runs = 1
	num_of_final_runs = 1		# this value will not matter if orf above is 0
	plot_flag = 0			# variable that determines if a plot will be generated
	
	#-----------------------------------
	#filename_array will contain the names of all the .txt files used for the trials
	filename_array = []
	for i in range(1,(total_initial_runs+1)): #{
		#filenames will differ by an appended number at the end of the name
		temp_string = name + str(date) + '_' + str(concentration) + '_' + str(i) + '.txt'
		filename_array.append(temp_string)
	#}
	
	Zurich_asynch_SINGLE(filename_array, plot_flag)
	if outlier_removal_flag == 1: #{
		outlier_removal(filename_array)
	#}
#}

# ---------------------------------------------------------------------------------------------------------------------
def Zurich_asynch_SINGLE(filename_array, plot_flag): #{
	# Open connection to ziServer
	daq = zhinst.ziPython.ziDAQServer('localhost', 8005)
	# Detect device
	device = zhinst.utils.autoDetect(daq, exclude=None)
	for i in range(0, len(filename_array)): #{
		measureSynchronousFeedback(daq, device, 1, 1e5, filename_array[i], plot_flag)
		print("Finished " + filename_array[i])
	#}
#}

# ---------------------------------------------------------------------------------------------------------------------
def measureSynchronousFeedback(daq, device, channel, frequency, filename, plot_flag): #{
	# filename in this case is the name stored in filename_array at the specified value from
	#    the for loop in Zurich_asynch_SINGLE
	c=str(channel-1)
	d=str(channel-1+6)
        # c+6
	amplitude=1
	rate=200
	tc=0.01
	
	# Disable all outputs and all demods
	general_setting = [
		[['/', device, '/demods/0/trigger'], 0],
		[['/', device, '/demods/1/trigger'], 0],
		[['/', device, '/demods/2/trigger'], 0],
		[['/', device, '/demods/3/trigger'], 0],
		[['/', device, '/demods/4/trigger'], 0],
		[['/', device, '/demods/5/trigger'], 0],
		[['/', device, '/sigouts/0/enables/*'], 0],
		[['/', device, '/sigouts/1/enables/*'], 0]
	]
	daq.set(general_setting)
	
	# Set test settings
	t1_sigOutIn_setting = [
		[['/', device, '/sigins/',c,'/diff'], 0],
		[['/', device, '/sigins/',c,'/imp50'], 0],
		[['/', device, '/sigins/',c,'/ac'], 1],
		[['/', device, '/sigins/',c,'/range'], 2],
		[['/', device, '/demods/',c,'/order'], 8],
		[['/', device, '/demods/',c,'/timeconstant'], tc],
		[['/', device, '/demods/',c,'/rate'], rate],
		[['/', device, '/demods/',c,'/adcselect'], channel-1],
		[['/', device, '/demods/',c,'/oscselect'], channel-1],
		[['/', device, '/demods/',c,'/harmonic'], 1],
		[['/', device, '/oscs/',c,'/freq'], frequency],
		[['/', device, '/sigouts/',c,'/add'], 0],
		[['/', device, '/sigouts/',c,'/on'], 1],
		[['/', device, '/sigouts/',c,'/enables/',d], 1],
		[['/', device, '/sigouts/',c,'/range'], 1],
		[['/', device, '/sigouts/',c,'/amplitudes/',d], amplitude],
	]
	daq.set(t1_sigOutIn_setting);
	# wait 1s to get a settled lowpass filter
	time.sleep(1)
	#clean queue
	daq.flush()
	
	# Subscribe to scope
	path0 = '/' + device + '/demods/',c,'/sample'
	daq.subscribe(path0)
	# Poll data 1s, second parameter is poll timeout in [ms]  
	# (recomended value is 500ms) 
	dataDict = daq.poll(1,500);
	# Unsubscribe to scope
	daq.unsubscribe(path0)
	
	#-----------------------------------
	# Save the data as a .txt file
	text_file = open(filename, "w")
	
	data_pathway = '/' + device + '/demods/' + c + '/sample'
	daq.subscribe(data_pathway)
	flat_dictionary_key = False
	data = daq.poll(0.1, 200, 1, flat_dictionary_key)
	continue_variable = 1
	
	x = data[device]['demods'][c]['sample']['x']
	y = data[device]['demods'][c]['sample']['y']
	timestamps = data[device]['demods'][c]['sample']['timestamp']
	distance_data = sqrt((x**2)+(y**2))
	ts_data = ((timestamps - timestamps[0])/210e6)
	for i in range(0, len(distance_data)): #{
		# the data will be stored as (sqrt(x^2 + y^2), time)
		text_file.write(str(distance_data[i]) + ',' + str(ts_data[i]) + '\n')
	#}
	text_file.close()
	
	#-----------------------------------
	# Recreate data as a plot
	if plot_flag == 1: # if plot_flag is enabled {
		e=0.5*amplitude/sqrt(2)
		x_data = dataDict[device]['demods'][c]['sample']['x']
		y_data = dataDict[device]['demods'][c]['sample']['y']
		timestamp_data = dataDict[device]['demods'][c]['sample']['timestamp']
		rdata = sqrt(x_data**2+y_data**2)
		print 'Measured rms amplitude is %.5fV (expected: %.5fV).' %(mean(rdata),e)
		tdata= (timestamp_data - timestamp_data[0])/210e6
		plt.figure(channel)
		plt.grid(True)
		plt.plot(tdata,rdata)
		plt.title('Demodulator data')
		plt.xlabel('Time (s)')
		plt.ylabel(' R component (V)')
		plt.axis([tdata[0],tdata[-1],0.97*e,1.03*e])
		plt.show()
	#}
#}

# ---------------------------------------------------------------------------------------------------------------------
#def outlier_removal(filename_array): #{
	# I have a feeling this is going to be a very expensive operation
	# so for the data set, there are x and y values. X correlates to the wavenumber (cm-1)
	# Y correlates to the scattering signal (a.u.). So we're taking the standard deviation of the y data sets
	
	# The first thing we have to do is go through filename_array and store just the y data sets into an arrays
	# As we go through and take out data sets, we will also go through and remove the names of them from the original filename_array
#}

# =====================================================================================================================
# Main function execution. This will be placed at the bottom of the file.
if __name__ == "__main__": #{
    import sys    
    main()#;
#}
