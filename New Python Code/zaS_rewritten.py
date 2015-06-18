"""
Kathryn DiPippo
6/15/2015
zaS_rewritten.py
- To use, the ziDAQ library needs to be installed for Python: http://www.zhinst.com/blogs/schwizer/2011/05/controlling-the-hf2-li-lock-in-with-python/
- Creates the data structure to store data from lock-in
- Reads the lock-in amplifier
- This is the code directly from the website, as going through and editing
	the old code turned out to be too inconsistent
"""

import time, math
import zhinst.ziPython, zhinst.utils
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

# =====================================================================================================================
def main(): #{
	name = 'Michelle'
	concentration = 80
	date = 061815
	Zurich_asynch_SINGLE(name, concentration, date)
#}

# ---------------------------------------------------------------------------------------------------------------------
def Zurich_asynch_SINGLE(name, concentration, date): #{
	# Open connection to ziServer
	daq = zhinst.ziPython.ziDAQServer('localhost', 8005)
	# Detect device
	device = zhinst.utils.autoDetect()
	filename = name + date + '_' + concentration + '.txt'
	measureSynchronousFeedback(daq, device, 1, 1e5, filename);

# ---------------------------------------------------------------------------------------------------------------------
def measureSynchronousFeedback(daq, device, channel, frequency, filename): #{
	c=str(channel-1)
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
		[['/', device, '/sigins/',c,'/imp50'], 1],
		[['/', device, '/sigins/',c,'/ac'], 0],
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
		[['/', device, '/sigouts/',c,'/enables/',c], 1],
		[['/', device, '/sigouts/',c,'/range'], 1],
		[['/', device, '/sigouts/',c,'/amplitudes/',c], amplitude],
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
	data = dataDict[device]['demods'][c]['sample'][0]
	#data['x'] and data['y'] are two arrays to access data from
	text_file = open(filename, "w")
	for i in range (0,len(data['x']):
		text_file.write(str(data['x'][i]) + ',' + str(data['y'][i]) + '\n')
	text_file.close()
	#-----------------------------------
	
	# Recreate data
	plot_flag = 0			# variable that determines if a plot will be generated
	if plot_flag == 1:
		if device in dataDict:
			if dataDict[device]['demods'][c]['sample'][0]['time']['dataloss']:
				print 'Sample loss detected.'
			else:
				e=0.5*amplitude/sqrt(2)
				data = dataDict[device]['demods'][c]['sample'][0]
				rdata = sqrt(data['x']**2+data['y']**2)
				print 'Measured rms amplitude is %.5fV (expected: %.5fV).' %(mean(rdata),e)
				tdata= (data['timestamp']-data['timestamp'][0])/210e6
				plt.figure(channel)
				plt.grid(True)
				plt.plot(tdata,rdata)
				plt.title('Demodulator data')
				plt.xlabel('Time (s)')
				plt.ylabel(' R component (V)')
				plt.axis([tdata[0],tdata[-1],0.97*e,1.03*e])
				plt.show()
#}

# =====================================================================================================================
# Main function execution. This will be placed at the bottom of the file.
if __name__ == "__main__": #{
    main()#;
#}