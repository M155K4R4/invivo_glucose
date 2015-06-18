import time, math
import zhinst.ziPython, zhinst.utils
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

def measureSynchronousFeedback(daq, device, channel, frequency):
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
   # Recreate data
   if device in dataDict:
       if dataDict[device]['demods'][c]['sample'][0]['time']['dataloss']:
           print 'Sample loss detected.'
       else:
           e=0.5*amplitude/sqrt(2)
           data = dataDict[device]['demods'][c]['sample'][0]
           rdata = sqrt(data['x']**2+data['y']**2)
           print 'Measured rms amplitude is %.5fV (expected: %.5fV).' %(mean(rdata),e)
           tdata= (data['timestamp']-data['timestamp'][0])/210e6
           # Create plot 
           plt.figure(channel)
           plt.grid(True)
           plt.plot(tdata,rdata)
           plt.title('Demodulator data')
           plt.xlabel('Time (s)')
           plt.ylabel(' R component (V)')
           plt.axis([tdata[0],tdata[-1],0.97*e,1.03*e])
           plt.show()
		   
		   
#----------------------------------------------------------------------------------
# Open connection to ziServer
daq = zhinst.ziPython.ziDAQServer('localhost', 8005)
# Detect device
device = zhinst.utils.autoDetect()
measureSynchronousFeedback(daq, device, 1, 1e5);