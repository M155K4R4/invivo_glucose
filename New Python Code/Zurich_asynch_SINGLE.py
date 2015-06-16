# =====================================================================================================================
# Kathryn DiPippo
# 6/15/2015
# Zurich_asynch_SINGLE.py: 
# - To use, the ziDAQ library needs to be installed for Python: http://www.zhinst.com/blogs/schwizer/2011/05/controlling-the-hf2-li-lock-in-with-python/
# - Creates the data structure to store data from lock-in
# - Reads the lock-in amplifier
# =====================================================================================================================

import zhinst.ziPython, zhinst.utils
from numpy import *
import time

# ---------------------------------------------------------------------------------------------------------------------
def Zurich_asynch_SINGLE(a): #{
	daq = zhinst.ziPython.ziDAQServer('localhost',8005)#;	#Open connection to ziServer
	device = zhinst.utils.autoDetect()#;					# Detect device

	# get the device type and its options (in order to set correct device-specific configuration)
	# # devtype = ziDAQ('getByte',[ '/' device '/features/devtype' ] );
	# # options = ziDAQ('getByte',[ '/' device '/features/options' ] );

	print 'Will run the example on an ' + str(devtype) + ' with options ' + str(regexprep(options,'\n','|')) + '.\n'#;

	# # % the length of time we'll record data (asynchronously) for
	# # recording_time = 7.0; % [s]
	# # obj1=obj;
	# # [data] = run_example(device,devtype,options,recording_time,obj1);
	# # %test_example(device,data,recording_time);
#}

# ---------------------------------------------------------------------------------------------------------------------
def run_example(device,devtype,options,recording_time,obj): #{
  
# # demod_c = '0'; % demod channel
# # out_c = '0'; % signal output channel
# # in_c = '0'; % signal input channel
# # osc_c = '0'; % oscillator

# # %demod_d='3';
# # %in_d='1'; %signal input 2

# # % define the output mixer channel based on the device type and its options
# # if strfind(devtype,'UHF') & isempty(strfind(options,'MF'))
    # # out_mixer_c = '3';
# # elseif strfind(devtype,'HF2') & isempty(strfind(options,'MF'))
    # # out_mixer_c = '6';
# # else
  # # out_mixer_c = '0';
# # end

# # tc = 0.01; % [s]
# # demod_rate = 150e3;
# # % create a base configuration: disable all outputs, demods and scopes
# # ziDAQ('setDouble',['/' device '/demods/*/rate'], 0.0);
# # ziDAQ('setInt',['/' device '/demods/*/trigger'], 0);
# # ziDAQ('setInt',['/' device '/sigouts/*/enables/*'], 0);
# # if strfind(devtype,'UHF')
# # % if the device is a UHF additionally disable all demodulators
    # # ziDAQ('setInt',['/' device '/demods/*/enable'], 0);
    # # ziDAQ('setInt',['/' device '/scopes/*/enable'], 0);
# # elseif strfind(devtype,'HF2')
    # # ziDAQ('setInt',['/' device '/scopes/*/trigchannel'],-1)
# # end

# # % configure the device ready for this experiment
# # %Set inputs 1 and 2 to the same settings.
# # ziDAQ('setInt',['/' device '/sigins/' in_c '/imp50'], 0);
# # ziDAQ('setInt',['/' device '/sigins/' in_c '/ac'], 1);
# # % ziDAQ('setInt',['/' device '/sigins/' in_d '/imp50'], 0);
# # % ziDAQ('setInt',['/' device '/sigins/' in_d '/ac'], 1);
# # ziDAQ('setDouble',['/' device '/sigins/' in_c '/range'], 2);
# # % ziDAQ('setDouble',['/' device '/sigins/' in_d '/range'], 2);
# # ziDAQ('setInt',['/' device '/sigouts/' out_c '/on'], 1);
# # ziDAQ('setDouble',['/' device '/sigouts/' out_c '/range'], 1);
# # ziDAQ('setDouble',['/' device '/sigouts/' out_c '/amplitudes/*'], 0);
# # ziDAQ('setDouble',['/' device '/sigouts/' out_c '/amplitudes/' out_mixer_c], 1);
# # ziDAQ('setDouble',['/' device '/sigouts/' out_c '/enables/' out_mixer_c], 1);
# # if strfind(devtype,'HF2')
    # # ziDAQ('setInt',['/' device '/sigins/' in_c '/diff'], 0);
# # %     ziDAQ('setInt',['/' device '/sigins/' in_d '/diff'], 0);
    # # ziDAQ('setInt',['/' device '/sigouts/' out_c '/add'], 0);
# # end
# # ziDAQ('setDouble',['/' device '/demods/*/phaseshift'], 0);
# # ziDAQ('setInt',['/' device '/demods/*/order'], 8);
# # ziDAQ('setDouble',['/' device '/demods/' demod_c '/rate'], demod_rate);
# # ziDAQ('setInt',['/' device '/demods/' demod_c '/harmonic'], 1);
# # %ziDAQ('setDouble',['/' device '/demods/' demod_d '/rate'], demod_rate);
# # %ziDAQ('setInt',['/' device '/demods/' demod_d '/harmonic'], 1);

# # if strfind(devtype,'UHF')
    # # ziDAQ('setInt',['/' device '/demods/' demod_c '/enable'], 1);
# # end
# # if strfind(options,'MF')
# # % HF2IS and HF2LI multi-frequency option do not support the node oscselect.
    # # ziDAQ('setInt',['/' device '/demods/*/oscselect'], str2double(osc_c));
    # # ziDAQ('setInt',['/' device '/demods/*/adcselect'], str2double(in_c));
# # end
# # ziDAQ('setDouble',['/' device '/demods/*/timeconstant'], tc);
# # % NOTE for final device setting use a syncSet, this waits for the setting to
# # % have taken effect on the device before returning.
# # ziDAQ('syncSetDouble',['/' device '/oscs/' osc_c '/freq'], 30e5); % [Hz]

# # % unsubscribe all streaming data
# # ziDAQ('unsubscribe','*');
# # % clean queue
# # ziDAQ('flush');
# # % pause to get a settled lowpass filter
# # pause(10*tc);


# # % Create a recorder thread
# # % The function call will return a handle to that recorder (thread)
# # h = ziDAQ('record', 1, int64(10000));
# # % Subscribe nodes to be recorded
# # % Set trigger parameter
# # ziDAQ('set', h, 'trigger/0/count', 1);
# # % Trigger type is 0 = continous recording
# # ziDAQ('set', h, 'trigger/0/type', 0);
# # ziDAQ('set', h, 'trigger/0/duration', 0.5);
# # ziDAQ('set', h, 'trigger/0/path', ['/' device '/demods/' demod_c '/sample'] )
# # %ziDAQ('set', h, 'trigger/0/path', ['/' device '/demods/' demod_d '/sample'] )
# # % Subscribe all nodes that should be recorded
# # ziDAQ('subscribe', h, ['/' device '/demods/' demod_c '/sample']);
# # %ziDAQ('subscribe', h, ['/' device '/demods/' demod_d '/sample']);

#Now start the thread -> ready to be triggered
# # ziDAQ('execute', h);
time.sleep(0.5)#;	pause(0.5)

# # figure(1); 
# # % axes(handles.axes1);
# # clf;
# # grid on; box on; hold on;
t = time.time()		#python equivalent for tic
# # %dat=[];

#Activate Laser
# # %fprintf(obj, ':SCAN:MODE 3');
# # fprintf(obj, ':SCAN:RUN 1');

while ((time.time() - t) < recording_time): #{		(time.time() - t) is toc
    # # data = ziDAQ('read', h);
    # # % plot the data
    # # %style = 'black-';
    # # plot_data(data,device,str2double(demod_c)+1);
    # # %dat=[dat; tmp];
     time.sleep(0.1)#; 		pause(0.1)
#}
# # fprintf('Recording finished. Will finish.\n')
# # ziDAQ('finish', h);
# # ziDAQ('clear',h);
	return [data]#;
#}

# ---------------------------------------------------------------------------------------------------------------------
# # function plot_data(data,device,channel_1)
# # if isfield(data,device)
    # # if isfield(data.(device),'demods')
        # # if length(data.(device).demods) >= channel_1
            # # if ~isempty(data.(device).demods(channel_1).sample)
                # # % If we specified trigger criteria, we may get several trigger segments back
                # # % so we use cells to address the individual segments
                # # if data.(device).demods(channel_1).sample{1}.time.dataloss
                    # # fprintf('Sample loss detected.');
                # # end
                # # r = sqrt(data.(device).demods(channel_1).sample{1}.x.^2 + data.(device).demods(channel_1).sample{1}.y.^2);
                # # t = data.(device).demods(channel_1).sample{1}.timestamp;
                # # plot(t,r);
            # # end
        # # end
    # # end
# # end

# # end

