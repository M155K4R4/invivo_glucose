import Tkinter
from Tkinter import *
import ttk
import time
import Tkinter,tkFileDialog
import datetime
from PIL import Image, ImageTk
import os, sys

# =====================================================================================================================
title_size_variable = 10
size_variable = 12
header_size_variable = 10
font_type = "Helvetica"
fg_color = "#98a2a0"
# =====================================================================================================================

# ---------------------------------------------------------------------------------------------------------------------
# Creates a pop-up window that creates a new folder for collecting data
def create_folder(): #{
	win2 = Toplevel(bg = "white")
	textoBar = Label(win2, text="Please input the following data:", font=(font_type, size_variable, "bold"), bg="white")
	textoBar.grid(row=0, column=0, columnspan=2, pady=(5,5))
	
	# Directory location
	inFileBtn = Tkinter.Button(win2, text="Select Parent Diretory", font=(font_type, size_variable), bg="white", command=load_directory)
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
def load_directory(): #{
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
	path = inFileTxt.get() + DateTxt2.get() + '_' + nameTxt2.get()
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
	win = Toplevel(bg = "white")
	textoBar = Label(win, text="Taking data, please, wait 10 seconds", font=(font_type, size_variable), bg="white")
	textoBar.grid(row=0, column=0, pady=(5,5))
	progressbar = ttk.Progressbar(win, orient = HORIZONTAL, mode = 'indeterminate',length=250)
	progressbar.grid(row=1, column=0, pady=(5,5))
	progressbar.start()
	root.after(5000, win.destroy)		# wait 5 extra seconds and then close
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
def SOLUTIONS_GUI(): #{
	#root = Tk()
	root.wm_title('CLINICAL')
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.overrideredirect(1)
	root.geometry("%dx%d+0+0" % (w, h))

	im = Image.open('GUI_BACKGROUND.gif')
	tkimage = ImageTk.PhotoImage(im)
	myvar=Tkinter.Label(root,image = tkimage)
	myvar.place(x=0, y=0, relwidth=1, relheight=1)

	menu = Menu(root)
	root.config(menu=menu)
	 
	subMenu = Menu(menu)
	menu.add_cascade(label="File", menu=subMenu, font=(font_type, size_variable))
	subMenu.add_command(label="Create New Project...", command=create_folder, font=(font_type, header_size_variable))
	subMenu.add_separator()
	subMenu.add_command(label="Exit", font=(font_type, header_size_variable), command=root.destroy)

	editMenu = Menu(menu)
	menu.add_cascade(label="Edit", font=(font_type, size_variable), menu=editMenu)
	editMenu.add_command(label="Switch to CLINICAL View (Not functional at the moment)", font=(font_type, header_size_variable), command=doNothing)


	# ---------------------------------------------------------------------------------------------------------------------
	# Step Zero - Storing the data
	stepZero = Tkinter.LabelFrame(root, text=" 1. Store Data: ", font=(font_type, title_size_variable, "bold"), bg="white")
	stepZero.grid(row=0, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	stepZero.columnconfigure(0, weight=1)
	inFileLbl = Tkinter.Label(stepZero, text="Select the Folder to Store Data:", font=(font_type, size_variable), fg = fg_color, bg="white")
	inFileLbl.grid(row=0, column=0, columnspan=2, sticky='E')
	inFileTxt = Tkinter.Entry(stepZero, font=(font_type, size_variable))
	inFileTxt.grid(row=0, column=3, columnspan=2, padx=5, pady=2)
	inFileBtn = Tkinter.Button(stepZero, text="Browse ...", font=(font_type, size_variable), fg = fg_color, bg="white", command=load_directory)
	inFileBtn.grid(row=0, column=5, padx = 10)

	# ---------------------------------------------------------------------------------------------------------------------
	# Step Alpha - Signal Processing Toggling
	stepAlpha = Tkinter.LabelFrame(root, text=" 2. Signal Processing: ", font=(font_type, title_size_variable, "bold"), bg="white")
	stepAlpha.grid(row=1, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

	# Number of Runs --------
	a_Lbl1 = Tkinter.Label(stepAlpha, text="Number of Runs:", font=(font_type, size_variable), fg = fg_color, bg="white")
	a_Lbl1.grid(row=0, column=0, sticky='E')
	a_Txt1 = Tkinter.Entry(stepAlpha, font=(font_type, size_variable), bg="white")
	a_Txt1.grid(row=0, column=1)

	# START --------
	b_Lbl1 = Tkinter.Label(stepAlpha, text="START Frequency:", font=(font_type, size_variable), fg = fg_color, bg="white")
	b_Lbl1.grid(row=1, column=0, sticky='E')
	b_Txt1 = Tkinter.Entry(stepAlpha, font=(font_type, size_variable), bg="white")
	b_Txt1.grid(row=1, column=1)

	# STOP --------
	c_Lbl1 = Tkinter.Label(stepAlpha, text="STOP Frequency:", font=(font_type, size_variable), fg = fg_color, bg="white")
	c_Lbl1.grid(row=2, column=0, sticky='E')
	c_Txt1 = Tkinter.Entry(stepAlpha, font=(font_type, size_variable), bg="white")
	c_Txt1.grid(row=2, column=1)

	# Number of Scans --------
	d_Lbl1 = Tkinter.Label(stepAlpha, text="Number of Scans:", font=(font_type, size_variable), fg = fg_color, bg="white")
	d_Lbl1.grid(row=3, column=0, sticky='E')
	d_Txt1 = Tkinter.Entry(stepAlpha, font=(font_type, size_variable), bg="white")
	d_Txt1.grid(row=3, column=1)

	# ---------------------------------------------------------------------------------------------------------------------
	# Step One - Gathering Basic Information
	stepOne = Tkinter.LabelFrame(root, text=" 3. Basic Information: ", font=(font_type, title_size_variable, "bold"), bg="white")
	stepOne.grid(row=2, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	stepOne.columnconfigure(0, weight=1)

	# Name --------
	nameLbl = Tkinter.Label(stepOne, text="Name:", font=(font_type, size_variable), fg = fg_color, bg="white")
	nameLbl.grid(row=1, column=0, sticky='W')
	nameTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	nameTxt.grid(row=1, column=1)

	# Concentration --------
	ConcentrationLbl = Tkinter.Label(stepOne, text="Concentration:", font=(font_type, size_variable), fg = fg_color, bg="white")
	ConcentrationLbl.grid(row=2, column=0, sticky='W')
	ConcentrationTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	ConcentrationTxt.grid(row=2, column=1)
	ConcentrationLbl = Tkinter.Label(stepOne, text="mg/L", font=(font_type, size_variable), fg = fg_color, bg="white")
	ConcentrationLbl.grid(row=2, column=2, columnspan=2, sticky='W')

	# Date --------
	DateLbl1 = Tkinter.Label(stepOne, text="Date:", font=(font_type, size_variable), fg = fg_color, bg="white")
	DateLbl1.grid(row=3, column=0, sticky='W')
	DateTxt1 = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
	DateTxt1.grid(row=3, column=1)
	today = str(datetime.date.today()) # will return YEAR-MO-DA as a string
	DateTxt1.delete(0, END)
	DateTxt1.insert(0, today)

	# ---------------------------------------------------------------------------------------------------------------------
	# Step Beta - Real-Time Calculation Toggling
	stepBeta = Tkinter.LabelFrame(root, text=" 4. Real-Time Calculation: ", font=(font_type, title_size_variable, "bold"), bg="white")
	stepBeta.grid(row=3, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

	outlierVar = IntVar()
	Checkbutton(stepBeta, text="Remove Outlier?", font=(font_type, size_variable), fg = fg_color, bg="white", variable=outlierVar).grid(row=0, sticky=W)

	runLbl1 = Tkinter.Label(stepBeta, text="Final Number of Runs:", font=(font_type, size_variable), fg = fg_color, bg="white")
	runLbl1.grid(row=1, column=0, sticky='E')
	runTxt1 = Tkinter.Entry(stepBeta, font=(font_type, size_variable), bg="white")
	runTxt1.grid(row=1, column=1)

	plotVar = IntVar()
	Checkbutton(stepBeta, text="Display Plot?", font=(font_type, size_variable), fg = fg_color, bg="white", variable=plotVar).grid(row=2, sticky=W)

	# ---------------------------------------------------------------------------------------------------------------------
	# Step Two - Function for enabling Glucose Senseing System
	stepTwo = Tkinter.LabelFrame(root, text=" 5. Run: ", font=(font_type, title_size_variable, "bold"), bg="white")
	stepTwo.grid(row=4, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	stepTwo.columnconfigure(0, weight=1)
	zaSBtn = Tkinter.Button(stepTwo, text="Load Data", font=(font_type, size_variable), bg="white", fg = fg_color, command=Zurich_asynch_SINGLE)
	zaSBtn.grid(row=7, column=0, sticky='WE', padx=5, pady=2)
	inFileBtn = Tkinter.Button(stepTwo, text="          BEGIN SENSING          ", font=(font_type, size_variable), fg = fg_color, bg="white", command=handle_click)
	inFileBtn.grid(row=7, column=1, sticky='WE', padx=5, pady=2)
	root.mainloop()
#}

# =====================================================================================================================
# MAIN FUNCTION
if __name__ == '__main__': #{
	root = Tk()
	SOLUTIONS_GUI()
#}