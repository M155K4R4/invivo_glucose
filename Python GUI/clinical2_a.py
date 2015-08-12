import Tkinter
from Tkinter import *
import ttk
import Tkinter,tkFileDialog
import datetime
from PIL import Image, ImageTk
import os, sys
import time, math
#import zhinst.ziPython, zhinst.utils
#import matplotlib
#import matplotlib.pyplot as plt
#from numpy import *

# =====================================================================================================================
title_size_variable = 14
size_variable = 16
header_size_variable = 12
font_type = "Helvetica"
fg_color = "#98a2a0"
DEFAULT_NAME = "Sabbir"
DEFAULT_CONCENTRATION = "80"
# =====================================================================================================================

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
# Creates a pop-up window that creates a new folder for collecting data
def create_folder(): #{
	win2 = Toplevel(bg = "white")
	textoBar = Label(win2, text="Please input the following data:", font=(font_type, size_variable, "bold"), bg="white")
	textoBar.grid(row=0, column=0, columnspan=2, pady=(5,5))
	
	# Directory location
	inFileBtn = Tkinter.Button(win2, text="Select Parent Diretory", font=(font_type, size_variable), bg="white", command=load_directory(inFileTxt))
	inFileBtn.grid(row=1, columnspan=2)
	
	# Date? - will be retrieved from desktop
	today = str(datetime.date.today()) # will return YEAR-MO-DA as a string
	
	DateLbl2 = Tkinter.Label(win2, text="Date:", font=(font_type, size_variable), fg = fg_color, bg="white", pady=2)
	DateLbl2.grid(row=2, column=0, sticky='E')
	DateTxt2 = Tkinter.Entry(win2, font=(font_type, size_variable), bg="white")
	DateTxt2.grid(row=2, column=1)
	
	DateTxt2.delete(0, END)
	DateTxt2.insert(0, today)
	
	# Place?
	nameLbl2 = Tkinter.Label(win2, text="Location:", fg = fg_color, font=(font_type, size_variable), bg="white")
	nameLbl2.grid(row=3, sticky='E')

	nameTxt2 = Tkinter.Entry(win2, font=(font_type, size_variable), bg="white")
	nameTxt2.grid(row=3, column=1)
	
	nameLbl3 = Tkinter.Button(win2, text="Press to Generate Folder", font=(font_type, size_variable), bg="white", command=create_directory)
	nameLbl3.grid(row=4, columnspan=2, sticky='WE', padx=5, pady=5)
#}

# ---------------------------------------------------------------------------------------------------------------------
# Creates a popup with a list of what to do to begin using the Lock-In and the laser system
def startupFunction(): #{
	sWin = Toplevel(bg = "white")
	sWin.wm_title("How to Setup the Lock-In and Laser System for Usage")
	tutorialString = "1.\tNavigate to the folder where the data is stored. The files should appear under current folder.\r\n2.\tFind the file you hope to plot and double-click the mat file.\r\n\t>> load('Sand_60_1_070915') will show up in the command window. \r\n\tDouble-clicking the file is equivalent to typing the above command. After loading the file, all variables in this\r\n\tmat file will be displayed in the workspace as they are added to your current workspace. (If a new variable has\r\n\tthe same name of a variable that already exists in the workspace, the old one will be overwritten.)\r\n3.\tIn the files we work with, the variable \"out\" always stores the spectra in a matrix with the dimension of 182401\r\n\tby 10. (182401 is the number of data points in each spectrum, and we have 10 spectra because there are 5\r\n\truns, each including two scans.)\r\n\t\ta.\tresult1 = out(:,1); stores the first spectrum out of the 10 in a variable called result1. The colon inside the \r\n\t\t\tparenthesis represents the entire column, and 1 indicates the first element of a row. Together result1 = \r\n\t\t\tout(:,1) means taking the first column of the variable out and assigning it to a variable called result1.\r\n\t\tb.\tresult2 =mean(out')'; averages all the spectra and stores the resulting spectrum in the variable result2. \r\n\t\t\tThe apostrophe is an operator to transpose the matrix, changing an m*n matrix to an n*m matrix. We first \r\n\t\t\ttranspose the matrix so that we can take the average of the spectra and then we transpose it back to \r\n\t\t\tpreserve its shape (that's why there're two apostrophes). This practice is preferred, but it's slightly slower \r\n\t\t\tthan (a).\r\n4.\tIf another file needs to be loaded, simply double-click that mat file under current folder. All variables including\r\n\t\"out\" will be overwritten except those that don't exist in this new mat file like result1 and result2 we just\r\n\tcreated. Now repeat step 3 but assign different variable names like result3 = mean(out')'; so that we can store\r\n\tthe spectrum information in the file we just loaded. \r\n5.\tThe commend plot(wave, result1) will plot the graph for you. Wave is the variable on the x-axis, and results1 is\r\n\tthe variable on the y-axis. If two spectra need to be plotted in the same graph, the command should be\r\n\tplot(wave, result1, wave, result2)\r\n6.\tWe can also add legend and labels to make the graph prettier. plot(wave, result1, wave, result3);\r\n\tlegend(\'60ml\/dl\',\'100ml\/`dl\'); xlabel(\'wavenumber cm^{-1}\'); ylabel(\'signal (a.u.)\')\r\n\tThe graph is editable after it's been plotted. For example, you can drag the legend to wherever you want,\r\n\tchange its shape or color, add a title for the graph, etc.\r\n7.\tSave the graph in the format in pdf or jpg is convenient. The fig format is also recommended because the\r\n\tgraph can be edited later (it can only opened in MATLAB though).\r\n\r\nA few remarks:\r\n1.\tPutting a semicolon after each command is important because it suppresses the output and prevents the\r\n\tprogram from printing out everything in the command window. \r\n2.\tYou can get help by typing \"help\" in the command window. For example \"help plot\" can show you all\r\n\tinformation about the plot function.\r\n3.\tTo stop executing a command in the middle of a test, press Ctrl+C. On a Mac, use Command+. (the\r\n\tCommand key and the period key)."
	sWin.columnconfigure(0, weight=1)
	text = Text(sWin, width = 136)
	text.grid()
	text.insert(END, tutorialString)
	scrl = Scrollbar(sWin, command=text.yview)
	text.config(yscrollcommand=scrl.set)
	scrl.grid(row=0, column=1, sticky='ns')
#}

# ---------------------------------------------------------------------------------------------------------------------
# Creates a pop-up of the text document that Michelle made for using the matlab code
def michelleFunction(): #{
	mWin = Toplevel(bg = "white")
	mWin.wm_title("A brief MATLAB tutorial for the glucose project")
	tutorialString = "1.\tNavigate to the folder where the data is stored. The files should appear under current folder.\r\n2.\tFind the file you hope to plot and double-click the mat file.\r\n\t>> load('Sand_60_1_070915') will show up in the command window. \r\n\tDouble-clicking the file is equivalent to typing the above command. After loading the file, all variables in this\r\n\tmat file will be displayed in the workspace as they are added to your current workspace. (If a new variable has\r\n\tthe same name of a variable that already exists in the workspace, the old one will be overwritten.)\r\n3.\tIn the files we work with, the variable \"out\" always stores the spectra in a matrix with the dimension of 182401\r\n\tby 10. (182401 is the number of data points in each spectrum, and we have 10 spectra because there are 5\r\n\truns, each including two scans.)\r\n\t\ta.\tresult1 = out(:,1); stores the first spectrum out of the 10 in a variable called result1. The colon inside the \r\n\t\t\tparenthesis represents the entire column, and 1 indicates the first element of a row. Together result1 = \r\n\t\t\tout(:,1) means taking the first column of the variable out and assigning it to a variable called result1.\r\n\t\tb.\tresult2 =mean(out')'; averages all the spectra and stores the resulting spectrum in the variable result2. \r\n\t\t\tThe apostrophe is an operator to transpose the matrix, changing an m*n matrix to an n*m matrix. We first \r\n\t\t\ttranspose the matrix so that we can take the average of the spectra and then we transpose it back to \r\n\t\t\tpreserve its shape (that's why there're two apostrophes). This practice is preferred, but it's slightly slower \r\n\t\t\tthan (a).\r\n4.\tIf another file needs to be loaded, simply double-click that mat file under current folder. All variables including\r\n\t\"out\" will be overwritten except those that don't exist in this new mat file like result1 and result2 we just\r\n\tcreated. Now repeat step 3 but assign different variable names like result3 = mean(out')'; so that we can store\r\n\tthe spectrum information in the file we just loaded. \r\n5.\tThe commend plot(wave, result1) will plot the graph for you. Wave is the variable on the x-axis, and results1 is\r\n\tthe variable on the y-axis. If two spectra need to be plotted in the same graph, the command should be\r\n\tplot(wave, result1, wave, result2)\r\n6.\tWe can also add legend and labels to make the graph prettier. plot(wave, result1, wave, result3);\r\n\tlegend(\'60ml\/dl\',\'100ml\/`dl\'); xlabel(\'wavenumber cm^{-1}\'); ylabel(\'signal (a.u.)\')\r\n\tThe graph is editable after it's been plotted. For example, you can drag the legend to wherever you want,\r\n\tchange its shape or color, add a title for the graph, etc.\r\n7.\tSave the graph in the format in pdf or jpg is convenient. The fig format is also recommended because the\r\n\tgraph can be edited later (it can only opened in MATLAB though).\r\n\r\nA few remarks:\r\n1.\tPutting a semicolon after each command is important because it suppresses the output and prevents the\r\n\tprogram from printing out everything in the command window. \r\n2.\tYou can get help by typing \"help\" in the command window. For example \"help plot\" can show you all\r\n\tinformation about the plot function.\r\n3.\tTo stop executing a command in the middle of a test, press Ctrl+C. On a Mac, use Command+. (the\r\n\tCommand key and the period key)."
	mWin.columnconfigure(0, weight=1)
	text = Text(mWin, width = 136)
	text.grid()
	text.insert(END, tutorialString)
	scrl = Scrollbar(mWin, command=text.yview)
	text.config(yscrollcommand=scrl.set)
	scrl.grid(row=0, column=1, sticky='ns')
#}

# ---------------------------------------------------------------------------------------------------------------------
def load_directory(inFileTxt): #{
	dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
	if len(dirname ) > 0:
		inFileTxt.delete(0, END)
		inFileTxt.insert(0, dirname)
		#print "You chose %s" % dirname		Uncomment to click directory of location
#}

# ---------------------------------------------------------------------------------------------------------------------
def create_directory(): #{
	# Path to be created
	# Format for this is DATE_LOCATION
	inFile_pathname = ''
	date_pathname = ''
	name_pathname = ''
	if len(inFileTxt.get()) == 0:
		inFile_pathname = DEFAULT_FILE_LOCATION
	else:
		inFile_pathname = inFileTxt.get()
	date_pathname = DateTxt2.get()
	if len(nameTxt2.get()) == 0:
		name_pathname = DEFAULT_NAME
	else:
		name_pathname = nameTxt2.get()
	path = inFile_pathname + date_pathname + '_' + name_pathname
	os.makedirs(path, 0755)
#}

# ---------------------------------------------------------------------------------------------------------------------
# A temp function created when developing the gui as a placeholder for future functions
def doNothing(): #{
	print("This command does nothing at the moment.\n")
#}

# =====================================================================================================================
# PRIMARY FUNCTIONALITY. This function manages other functions to control the laser glucose sensing system. Variables
#   from the entry fields are read through here, stored, and then executed. The following code can also be executed
#   separate in the zaS_rewritten.py code.
def Zurich_asynch_SINGLE(): #{
	# initialize pop-up window that tracks data
	win = Toplevel(bg = "white")
	textoBar = Label(win, text="Taking data, please, wait 10 seconds", font=(font_type, size_variable), bg="white")
	textoBar.grid(row=0, column=0, pady=(5,5))
	progressbar = ttk.Progressbar(win, orient = HORIZONTAL, mode = 'indeterminate',length=250)
	progressbar.grid(row=1, column=0, pady=(5,5))
	
	# PRIMARY VARIABLES (later to be read in from a GUI
	# The inputs below determine the name of the text file
	date = DateTxt1.get()
	name = ''
	concentration = ''
	
	if len(nameTxt.get()) == 0:
		name = DEFAULT_NAME
	else:
		name_pathname = nameTxt.get()
	if len(ConcentrationTxt.get()) == 0:
		concentration = DEFAULT_CONCENTRATION
	else:
		concentration = ConcentrationTxt.get()
	
	outlier_removal_flag = 0	# 0 if data wishes to be left as is
								# 1 if data will be reduced to num_of_final_runs
	total_initial_runs = 10
	num_of_final_runs = 1		# this value will not matter if orf above is 0
	plot_flag = 0				# variable that determines if a plot will be generated
	
	#-----------------------------------
	#filename_array will contain the names of all the .txt files used for the trials
	filename_array = []
	for i in range(1,(total_initial_runs+1)): #{
		#filenames will differ by an appended number at the end of the name
		temp_string = name + str(date) + '_' + str(concentration) + '_' + str(i) + '.txt'
		filename_array.append(temp_string)
	#}
	
	#-----------------------------------
	# Open connection to ziServer
	daq = zhinst.ziPython.ziDAQServer('localhost', 8005)
	# Detect device
	device = zhinst.utils.autoDetect(daq, exclude=None)
	for i in range(0, len(filename_array)): #{
		measureSynchronousFeedback(daq, device, 1, 1e5, filename_array[i], plot_flag)
		progressbar.step(250/len(filename_array))
	#}
	
	if outlier_removal_flag == 1: #{
		outlier_removal(filename_array)
	#}
#}

# =====================================================================================================================
# Test replacement function that does a simple calculation instead of running the laser
# Used for debugging purposes
def Zurich_asynch_SINGLE_test(): #{
	# initialize pop-up window that tracks data
	win = Toplevel(bg = "white")
	textoBar = Label(win, text="Taking data, please, wait 10 seconds", font=(font_type, size_variable), bg="white")
	textoBar.grid(row=0, column=0, pady=(5,5))
	progressbar = ttk.Progressbar(win, orient = HORIZONTAL, mode = 'indeterminate',length=250)
	progressbar.grid(row=1, column=0, pady=(5,5))
	
	# PRIMARY VARIABLES (later to be read in from a GUI
	# The inputs below determine the name of the text file
	date = str(datetime.date.today())
	name = ''
	concentration = ''
	
	if len(nameTxt.get()) == 0:
		name = DEFAULT_NAME
	else:
		name_pathname = nameTxt.get()
	if len(ConcentrationTxt.get()) == 0:
		concentration = DEFAULT_CONCENTRATION
	else:
		concentration = ConcentrationTxt.get()
	
	outlier_removal_flag = 0	# 0 if data wishes to be left as is
								# 1 if data will be reduced to num_of_final_runs
	total_initial_runs = 10
	num_of_final_runs = 1		# this value will not matter if orf above is 0
	plot_flag = 0				# variable that determines if a plot will be generated
	
	#-----------------------------------
	#filename_array will contain the names of all the .txt files used for the trials
	filename_array = []
	for i in range(1,(total_initial_runs+1)): #{
		#filenames will differ by an appended number at the end of the name
		temp_string = name + str(date) + '_' + str(concentration) + '_' + str(i) + '.txt'
		filename_array.append(temp_string)
	#}
	
	for i in range(0, len(filename_array)): #{
		print ("Done with this calculation!!!")
		progressbar.step(250/len(filename_array))
	#}
	
	if outlier_removal_flag == 1: #{
		outlier_removal(filename_array)
	#}
#}

# ---------------------------------------------------------------------------------------------------------------------
# A dummy loading bar function. It creates a loading bar that lasts for 10 seconds before quitting out the window.
def handle_click():
	win = Toplevel(bg = "white")
	textoBar = Label(win, text="Taking data, please, wait 10 seconds", font=(font_type, size_variable), bg="white")
	textoBar.grid(row=0, column=0, pady=(5,5))
	progressbar = ttk.Progressbar(win, orient = HORIZONTAL, mode = 'indeterminate',length=250)
	progressbar.grid(row=1, column=0, pady=(5,5))
	progressbar.start()
	root.after(10000, win.destroy)		# wait 10 seconds and then close

	
# =====================================================================================================================
#def CLINICAL_GUI(): #{	
#}

# =====================================================================================================================
# MAIN FUNCTION
if __name__ == '__main__': #{
	root = Tk()
	root.wm_title('CLINICAL')
	#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	#root.overrideredirect(1)
	#root.geometry("%dx%d+0+0" % (w, h))

	#im = Image.open('GUI_BACKGROUND2.gif')
	#tkimage = ImageTk.PhotoImage(im)
	#myvar=Tkinter.Label(root,image = tkimage)
	#myvar.place(x=0, y=0, relwidth=1, relheight=1)

	menu = Menu(root)
	root.config(menu=menu)
	 
	subMenu = Menu(menu)
	menu.add_cascade(label="File", menu=subMenu, font=(font_type, size_variable))
	subMenu.add_command(label="Create New Project...", command=create_folder, font=(font_type, header_size_variable))
	subMenu.add_separator()
	subMenu.add_command(label="Exit", font=(font_type, header_size_variable), command=root.destroy)

	editMenu = Menu(menu)
	menu.add_cascade(label="Edit", font=(font_type, size_variable), menu=editMenu)
	editMenu.add_command(label="Switch to SOLUTIONS View (Not functional at the moment)", font=(font_type, header_size_variable), command=doNothing)
	editMenu.add_separator()
	editMenu.add_command(label="README for Setting Up Integrating Sphere", font=(font_type, header_size_variable), command=startupFunction)
	editMenu.add_command(label="README for MatLab calculations", font=(font_type, header_size_variable), command=michelleFunction)
	
	# ---------------------------------------------------------------------------------------------------------------------
	# Step Zero - Storing the data
	stepZero = Tkinter.LabelFrame(root, text=" 1. Store Data: ", font=(font_type, title_size_variable, "bold"), bg="white")
	stepZero.grid(row=0, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	stepZero.columnconfigure(0, weight=1)
	inFileLbl = Tkinter.Label(stepZero, text="Select the Folder to Store Data:", font=(font_type, size_variable), bg="white")
	inFileLbl.grid(row=0, column=0, columnspan=2, sticky='E')
	inFileTxt = Tkinter.Entry(stepZero, font=(font_type, size_variable))
	inFileTxt.grid(row=0, column=3, columnspan=2, padx=5, pady=2)
	inFileBtn = Tkinter.Button(stepZero, text="Browse ...", font=(font_type, size_variable), bg="white", command=load_directory(inFileTxt))
	inFileBtn.grid(row=0, column=5, padx = 10)

	# ---------------------------------------------------------------------------------------------------------------------
	# Step One - Gathering Basic Information
	stepOne = Tkinter.LabelFrame(root, text=" 2. Basic Information: ", font=(font_type, title_size_variable, "bold"), bg="white")
	stepOne.grid(row=1, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	stepOne.columnconfigure(0, weight=1)

	# Name --------
	nameLbl = Tkinter.Label(stepOne, text="Name:", font=(font_type, size_variable), fg = fg_color, bg="white")
	nameLbl.grid(row=1, column=0, sticky='E')
	nameTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	nameTxt.grid(row=1, column=1)

	# Height --------
	heightLbl = Tkinter.Label(stepOne, text="Height:", font=(font_type, size_variable), fg = fg_color, bg="white")
	heightLbl.grid(row=2, column=0, sticky='E')
	ftTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	ftTxt.grid(row=2, column=1)
	ftLbl = Tkinter.Label(stepOne, text="ft", font=(font_type, size_variable), fg = fg_color, bg="white")
	ftLbl.grid(row=2, column=2)
	inchesTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	inchesTxt.grid(row=2, column=3)
	inchesLbl = Tkinter.Label(stepOne, text="inches", font=(font_type, size_variable), fg = fg_color, bg="white")
	inchesLbl.grid(row=2, column=4)

	# Weight --------
	weightLbl = Tkinter.Label(stepOne, text="Weight:", font=(font_type, size_variable), fg = fg_color, bg="white")
	weightLbl.grid(row=3, column=0, sticky='E')
	weightTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	weightTxt.grid(row=3, column=1)

	# Age --------
	AgeLbl = Tkinter.Label(stepOne, text="Age:", font=(font_type, size_variable), fg = fg_color, bg="white")
	AgeLbl.grid(row=4, column=0, sticky='E')
	AgeTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	AgeTxt.grid(row=4, column=1)

	# Date --------
	DateLbl1 = Tkinter.Label(stepOne, text="Date:", font=(font_type, size_variable), fg = fg_color, bg="white")
	DateLbl1.grid(row=5, column=0, sticky='E')
	DateTxt1 = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	DateTxt1.grid(row=5, column=1)
	today = str(datetime.date.today()) # will return YEAR-MO-DA as a string
	DateTxt1.delete(0, END)
	DateTxt1.insert(0, today)

	# Concentration --------
	ConcentrationLbl = Tkinter.Label(stepOne, text="Concentration:", font=(font_type, size_variable), fg = fg_color, bg="white")
	ConcentrationLbl.grid(row=6, column=0, sticky='E')
	ConcentrationTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	ConcentrationTxt.grid(row=6, column=1)
	ConcentrationLbl2 = Tkinter.Label(stepOne, text="mg/L", font=(font_type, size_variable), fg = fg_color, bg="white")
	ConcentrationLbl2.grid(row=6, column=2, columnspan=2, sticky='W')

	# ---------------------------------------------------------------------------------------------------------------------
	# Step Two - Function for enabling Glucose Senseing System
	#stepTwo = Tkinter.LabelFrame(root, text=" 3. Run: ", font=(font_type, title_size_variable, "bold"), bg="white")
	#stepTwo.grid(row=2, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	#stepTwo.columnconfigure(0, weight=1)
	#####zaSBtn = Tkinter.Button(root, text="Load Data", font=(font_type, size_variable), bg="white", fg = 'red', command=Zurich_asynch_SINGLE)
	zaSBtn = Tkinter.Button(root, text="Load Data", font=(font_type, size_variable), bg="white", fg = 'red', command=Zurich_asynch_SINGLE_test)
	zaSBtn.grid(row=2, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	#dummyLoadingBarBtn = Tkinter.Button(stepTwo, text="          BEGIN SENSING          ", font=(font_type, size_variable), fg = fg_color, bg="white", command=handle_click)
	#dummyLoadingBarBtn.grid(row=7, column=1, sticky='WE', padx=5, pady=2)
	root.mainloop()
#}