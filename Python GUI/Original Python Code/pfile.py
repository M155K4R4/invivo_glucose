"""
Kathryn DiPippo
6/15/2015
Pfile.py:
- Creates empty data sets to store data from the lock-in
- Does stuff with child handles. Unsure of for what purpose
- sets the range: total number of data points taken
- wave: creates an array with values between 1020 and 1220 for frequencies with (range + 1) between them, inclusive
- This is for 150k samples/sec

IMPORTANT NOTE
so the function of this code was that this was a separate function Sabbir made that took data points plotted by
Zurich_asynch_single.mat and then stored them in a new thing.

The challenge will then be to take this and be able to not only convert it to python but to also have it work simultaneously
with the Zurich_asynch_single code. That way, it stores data as it's plotting it.
"""




def pfile():
#function [Ydat,Ydat2,wave] = pfile1()

	#child_handles retrieves data stored in the plot created by Zurich_asynch_single
	child_handles = get(gca,'children')#;
	num_child = size(child_handles,1)#;
	choice = num_child#;
	Ydat = []#;
	while choice>0 #{
		x = get(child_handles(choice),'xdata')#;
		y = get(child_handles(choice),'ydata')#;
		Ydat = [Ydat; y.']#;
		choice = (choice - 1)#;
	#}
	#Ydat2=Ydat;
	close#;
	
	xpoint = 45000#;
	range = 182400#;
	tempy1 = Ydat(xpoint)#;
	val = 0#;
	xpoint = 150000#;
	
	while (val<1) #{
		if (tempy1 < Ydat(xpoint)) #{
			val = 1#;
		#}
		xpoint = xpoint + 1#;
	#}
	YdatA = Ydat(xpoint:(xpoint + range))#;
	dist = 25600#;
	xpointNew = (xpoint + range + dist)#;
	YdatB = Ydat(xpointNew:(xpointNew + range))#;
	YdatB = flipud(YdatB)#;

	wave = linspace(1020,1220,(range + 1))#;
	
	return [YdatA,YdatB,wave]#;
#}