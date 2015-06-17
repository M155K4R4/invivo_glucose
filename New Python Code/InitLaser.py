'''
Kathryn DiPippo
6/15/2015
InitLaser.py: 
- Initializes the laser
- Documentation for this function is needed
'''

def InitLaser(): #{					function [obj] = InitLaser()
	#Find a GPIB object (Laser Tuner).
	# # obj1 = instrfind('Type', 'gpib', 'BoardIndex', 0, 'PrimaryAddress', 17, 'Tag', '');

	#Create the GPIB object if it does not exist
	if obj1 is none: #{
		# # obj1 = gpib('NI', 0, 17)#;
	#Otherwise use the object that was found.
	else:
		# # fclose(obj1)#;
		# # obj1 = obj1(1)
	#}

	#Connect to instrument object, obj1.
	# # fopen(obj1);
	# # obj=obj1;
#}
