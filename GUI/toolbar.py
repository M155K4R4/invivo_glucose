import Tkinter
from Tkinter import *
import ttk
import time
import Tkinter,tkFileDialog
import datetime


def create_folder(): #{
	# popup window that asks for
	win2 = Toplevel()
	textoBar = Label(win2, text="Please input the following data:")
	textoBar.grid(row=0, column=0, columnspan=2, pady=(5,5))
	
	# Directory location
	
	
	# Date? - will be retrieved from desktop
	today = str(datetime.date.today()) # will return 2015-07-01 as a string
	
	DateLbl2 = Tkinter.Label(win2, text="Date:", pady=2)
	DateLbl2.grid(row=1, column=0, sticky='E')
	DateTxt2 = Tkinter.Entry(win2)
	DateTxt2.grid(row=1, column=1)
	
	DateTxt2.delete(0, END)
	DateTxt2.insert(0, today)
	
	# Place?
	nameLbl2 = Tkinter.Label(win2, text="Location:")
	nameLbl2.grid(row=2, sticky='E')

	nameTxt2 = Tkinter.Entry(win2)
	nameTxt2.grid(row=2, column=1)
	
	nameLbl3 = Tkinter.Button(win2, text="Press to Generate Folder", command=doNothing)
	nameLbl3.grid(row=3, columnspan=2, sticky='WE', padx=5, pady=5)

	
#}

def load_directory(): #{
	dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
	if len(dirname ) > 0:
		inFileTxt.delete(0, END)
		inFileTxt.insert(0, dirname)
		print "You chose %s" % dirname
#}

def doNothing(): #{
	print("This command does nothing at the moment.\n")
#}

def Zurich_asynch_SINGLE(): #{
	print("COLLECTING DATA.....")
#}


def handle_click():
	win = Toplevel()
	textoBar = Label(win, text="Taking data, please, wait 10 seconds")
	textoBar.grid(row=0, column=0, pady=(5,5))
	progressbar = ttk.Progressbar(win, orient = HORIZONTAL, mode = 'indeterminate',length=250)
	progressbar.grid(row=1, column=0, pady=(5,5))
	progressbar.start()
	root.after(10000, win.destroy)		# wait 10 seconds and then close

root = Tk()
root.wm_title('CLINICAL')

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Create New Project...", command=create_folder)
#subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Switch to SOLUTIONS View", command=doNothing)

#-------------
#toolbar = Frame(root, bg="blue")

#insertButt = Button(toolbar, text="Run Sim Bar", command=handle_click)
#insertButt.grid(row=2, sticky="W", padx=2, pady=2)
#printButt = Button(toolbar, text="Print", command=handle_click)
#printButt.grid(row=2, column=1, sticky="W", padx=2, pady=2)
#runButt = Button(toolbar, text="      RUN      ", command=Zurich_asynch_SINGLE)
#runButt.grid(row=2, column=2, sticky="W", padx=2, pady=2)
#toolbar.grid(sticky="N")


#---------------
stepZero = Tkinter.LabelFrame(root, text=" 1. Store Data: ")
stepZero.grid(row=0, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

inFileLbl = Tkinter.Label(stepZero, text="Select the Folder to Store Data:")
inFileLbl.grid(row=0, column=0, columnspan=2, sticky='E')

inFileTxt = Tkinter.Entry(stepZero)
inFileTxt.grid(row=0, column=3, columnspan=2, padx=5, pady=2)

inFileBtn = Tkinter.Button(stepZero, text="Browse ...", command=load_directory)
inFileBtn.grid(row=0, column=5)

#---------------
stepOne = Tkinter.LabelFrame(root, text=" 2. Basic Information: ")
stepOne.grid(row=1, columnspan=7, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

#helpLf = Tkinter.LabelFrame(root, text=" Description ")
#helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, sticky='NS', padx=5, pady=5)

#helpLbl = Tkinter.Label(helpLf,text="If we want to put help text here, we could go and do that. IDK what to put here for now")
#helpLbl.grid(row=0)

# Name --------
nameLbl = Tkinter.Label(stepOne, text="Name:")
nameLbl.grid(row=1, column=0, sticky='E')

nameTxt = Tkinter.Entry(stepOne)
nameTxt.grid(row=1, column=1)

	# Height --------
heightLbl = Tkinter.Label(stepOne, text="Height:")
heightLbl.grid(row=2, column=0, sticky='E')

heightTxt = Tkinter.Entry(stepOne)
heightTxt.grid(row=2, column=1)

outEncLbl = Tkinter.Label(stepOne, text="ft")
outEncLbl.grid(row=2, column=2)

outEncTxt = Tkinter.Entry(stepOne)
outEncTxt.grid(row=2, column=3)

outEncLbl2 = Tkinter.Label(stepOne, text="inches")
outEncLbl2.grid(row=2, column=4)

	# Weight --------
weightLbl = Tkinter.Label(stepOne, text="Weight:")
weightLbl.grid(row=3, column=0, sticky='E')

weightTxt = Tkinter.Entry(stepOne)
weightTxt.grid(row=3, column=1)

	# Age --------
AgeLbl = Tkinter.Label(stepOne, text="Age:")
AgeLbl.grid(row=4, column=0, sticky='E')

AgeTxt = Tkinter.Entry(stepOne)
AgeTxt.grid(row=4, column=1)

	# Date --------
DateLbl1 = Tkinter.Label(stepOne, text="Date:")
DateLbl1.grid(row=5, column=0, sticky='E')

DateTxt1 = Tkinter.Entry(stepOne)
DateTxt1.grid(row=5, column=1)

today = str(datetime.date.today()) # will return 2015-07-01 as a string
DateTxt1.delete(0, END)
DateTxt1.insert(0, today)

	# Concentration --------
ConcentrationLbl = Tkinter.Label(stepOne, text="Concentration:")
ConcentrationLbl.grid(row=6, column=0, sticky='E')

ConcentrationTxt = Tkinter.Entry(stepOne)
ConcentrationTxt.grid(row=6, column=1)

ConcentrationLbl = Tkinter.Label(stepOne, text="mg/L")
ConcentrationLbl.grid(row=6, column=2)

#---------------
stepTwo = Tkinter.LabelFrame(root, text=" 3. Run: ")
stepTwo.grid(row=2, columnspan=7, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

zaSBtn = Tkinter.Button(stepTwo, text="Load Data", command=Zurich_asynch_SINGLE)
zaSBtn.grid(row=7, column=0, sticky='WE', padx=5, pady=2)
inFileBtn = Tkinter.Button(stepTwo, text="          BEGIN SENSING          ", command=handle_click)
inFileBtn.grid(row=7, column=1, sticky='WE', padx=5, pady=2)

#for r in range(3,10):
#    for c in range(3,10):
#        Tkinter.Label(root, text='R%s/C%s'%(r,c),
#            borderwidth=1 ).grid(row=r,column=c)




#===========================
root.mainloop()
