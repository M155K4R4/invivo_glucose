import Tkinter
from Tkinter import *
import ttk
import time
import Tkinter,tkFileDialog
import datetime
from PIL import Image, ImageTk

title_size_variable = 28
size_variable = 30
font_type = "Helvetica"

def create_folder(): #{
	# popup window that asks for
	win2 = Toplevel()
	textoBar = Label(win2, text="Please input the following data:", font=(font_type, size_variable, "bold"), bg="white")
	textoBar.grid(row=0, column=0, columnspan=2, pady=(5,5))
	
	myvar2=Tkinter.Label(win2,image = tkimage)
	myvar2.place(x=0, y=0, relwidth=1, relheight=1)
	
	# Directory location
	inFileBtn = Tkinter.Button(win2, text="Select Parent Diretory", font=(font_type, size_variable), bg="white", command=load_directory)
	inFileBtn.grid(row=1, columnspan=2)
	
	# Date? - will be retrieved from desktop
	today = str(datetime.date.today()) # will return 2015-07-01 as a string
	
	DateLbl2 = Tkinter.Label(win2, text="Date:", font=(font_type, size_variable), bg="white", pady=2)
	DateLbl2.grid(row=2, column=0, sticky='E')
	DateTxt2 = Tkinter.Entry(win2, font=(font_type, size_variable), bg="white")
	DateTxt2.grid(row=2, column=1)
	
	DateTxt2.delete(0, END)
	DateTxt2.insert(0, today)
	
	# Place?
	nameLbl2 = Tkinter.Label(win2, text="Location:", font=(font_type, size_variable), bg="white")
	nameLbl2.grid(row=3, sticky='E')

	nameTxt2 = Tkinter.Entry(win2, font=(font_type, size_variable), bg="white")
	nameTxt2.grid(row=3, column=1)
	
	nameLbl3 = Tkinter.Button(win2, text="Press to Generate Folder", font=(font_type, size_variable), bg="white", command=doNothing)
	nameLbl3.grid(row=4, columnspan=2, sticky='WE', padx=5, pady=5)

	
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
	textoBar = Label(win, text="Taking data, please, wait 10 seconds", font=(font_type, size_variable), bg="white")
	textoBar.grid(row=0, column=0, pady=(5,5))
	myvar3=Tkinter.Label(win,image = tkimage)
	myvar3.place(x=0, y=0, relwidth=1, relheight=1)
	progressbar = ttk.Progressbar(win, orient = HORIZONTAL, mode = 'indeterminate',length=250)
	progressbar.grid(row=1, column=0, pady=(5,5))
	progressbar.start()
	root.after(10000, win.destroy)		# wait 10 seconds and then close

root = Tk()
root.wm_title('CLINICAL')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))


im = Image.open('GUI_BACKGROUND.gif')
tkimage = ImageTk.PhotoImage(im)
myvar=Tkinter.Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)


#image = Image.open("tankmaids.jpg")
# backgroundImage = ImageTk.PhotoImage(file = "C:\Users\Kathryn\Desktop\MIRTHE-2015-Glucose-Sensor\GUI\tankmaids.gif")
# root.create_image(10,10, image = image, anchor = NW)
# #background_photo = ImageTk.PhotoImage(image)
# background_label = tk.Label(root, image=backgroundImage)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu, font=(font_type, size_variable))
subMenu.add_command(label="Create New Project...", command=create_folder, font=(font_type, size_variable))
#subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", font=(font_type, size_variable), command=root.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", font=(font_type, size_variable), menu=editMenu)
editMenu.add_command(label="Switch to SOLUTIONS View", font=(font_type, size_variable), command=doNothing)

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
stepZero = Tkinter.LabelFrame(root, text=" 1. Store Data: ", font=(font_type, title_size_variable, "bold"), bg="white")
stepZero.grid(row=0, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
stepZero.columnconfigure(0, weight=1)

inFileLbl = Tkinter.Label(stepZero, text="Select the Folder to Store Data:", font=(font_type, size_variable), bg="white")
inFileLbl.grid(row=0, column=0, columnspan=2, sticky='E')

inFileTxt = Tkinter.Entry(stepZero, font=(font_type, size_variable))
inFileTxt.grid(row=0, column=3, columnspan=2, padx=5, pady=2)

inFileBtn = Tkinter.Button(stepZero, text="Browse ...", font=(font_type, size_variable), bg="white", command=load_directory)
inFileBtn.grid(row=0, column=5)

#---------------
stepOne = Tkinter.LabelFrame(root, text=" 2. Basic Information: ", font=(font_type, title_size_variable, "bold"), bg="white")
stepOne.grid(row=1, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
stepOne.columnconfigure(0, weight=1)

#helpLf = Tkinter.LabelFrame(root, text=" Description ")
#helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, sticky='NS', padx=5, pady=5)

#helpLbl = Tkinter.Label(helpLf,text="If we want to put help text here, we could go and do that. IDK what to put here for now")
#helpLbl.grid(row=0)

# Name --------
nameLbl = Tkinter.Label(stepOne, text="Name:", font=(font_type, size_variable), bg="white")
nameLbl.grid(row=1, column=0, sticky='E')

nameTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
nameTxt.grid(row=1, column=1)

	# Height --------
heightLbl = Tkinter.Label(stepOne, text="Height:", font=(font_type, size_variable), bg="white")
heightLbl.grid(row=2, column=0, sticky='E')

heightTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
heightTxt.grid(row=2, column=1)

outEncLbl = Tkinter.Label(stepOne, text="ft", font=(font_type, size_variable), bg="white")
outEncLbl.grid(row=2, column=2)

outEncTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
outEncTxt.grid(row=2, column=3)

outEncLbl2 = Tkinter.Label(stepOne, text="inches", font=(font_type, size_variable), bg="white")
outEncLbl2.grid(row=2, column=4)

	# Weight --------
weightLbl = Tkinter.Label(stepOne, text="Weight:", font=(font_type, size_variable), bg="white")
weightLbl.grid(row=3, column=0, sticky='E')

weightTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
weightTxt.grid(row=3, column=1)

	# Age --------
AgeLbl = Tkinter.Label(stepOne, text="Age:", font=(font_type, size_variable), bg="white")
AgeLbl.grid(row=4, column=0, sticky='E')

AgeTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
AgeTxt.grid(row=4, column=1)

	# Date --------
DateLbl1 = Tkinter.Label(stepOne, text="Date:", font=(font_type, size_variable), bg="white")
DateLbl1.grid(row=5, column=0, sticky='E')

DateTxt1 = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
DateTxt1.grid(row=5, column=1)

today = str(datetime.date.today()) # will return 2015-07-01 as a string
DateTxt1.delete(0, END)
DateTxt1.insert(0, today)

	# Concentration --------
ConcentrationLbl = Tkinter.Label(stepOne, text="Concentration:", font=(font_type, size_variable), bg="white")
ConcentrationLbl.grid(row=6, column=0, sticky='E')

ConcentrationTxt = Tkinter.Entry(stepOne, font=(font_type, size_variable), bg="white")
ConcentrationTxt.grid(row=6, column=1)

ConcentrationLbl = Tkinter.Label(stepOne, text="mg/L", font=(font_type, size_variable), bg="white")
ConcentrationLbl.grid(row=6, column=2, columnspan=2, sticky='W')

#---------------
stepTwo = Tkinter.LabelFrame(root, text=" 3. Run: ", font=(font_type, title_size_variable, "bold"), bg="white")
stepTwo.grid(row=2, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
stepTwo.columnconfigure(0, weight=1)

zaSBtn = Tkinter.Button(stepTwo, text="Load Data", font=(font_type, size_variable), bg="white", command=Zurich_asynch_SINGLE)
zaSBtn.grid(row=7, column=0, sticky='WE', padx=5, pady=2)
inFileBtn = Tkinter.Button(stepTwo, text="          BEGIN SENSING          ", font=(font_type, size_variable), bg="white", command=handle_click)
inFileBtn.grid(row=7, column=1, sticky='WE', padx=5, pady=2)


#===========================
root.mainloop()
