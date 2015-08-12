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
size_variable = 8
header_size_variable = 12
font_type = "Helvetica"
fg_color = "#98a2a0"
DEFAULT_NAME = "Sabbir"
DEFAULT_CONCENTRATION = "80"
#tutorialString = "1.\tNavigate to the folder where the data is stored. The files should appear under current folder.\r\n2.\tFind the file you hope to plot and double-click the mat file.\r\n\t>> load(\u2018Sand_60_1_070915\u2019) will show up in the command window. \r\n\tDouble-clicking the file is equivalent to typing the above command. After loading the file, all variables in this\r\n\tmat file will be displayed in the workspace as they are added to your current workspace. (If a new variable has\r\n\tthe same name of a variable that already exists in the workspace, the old one will be overwritten.)\r\n3.\tIn the files we work with, the variable \u201Cout\u201D always stores the spectra in a matrix with the dimension of 182401\r\n\tby 10. (182401 is the number of data points in each spectrum, and we have 10 spectra because there are 5\r\n\truns, each including two scans.)\r\n\t\ta.\tresult1 = out(:,1); stores the first spectrum out of the 10 in a variable called result1. The colon inside the \r\n\t\t\tparenthesis represents the entire column, and 1 indicates the first element of a row. Together result1 = \r\n\t\t\tout(:,1) means taking the first column of the variable out and assigning it to a variable called result1.\r\n\t\tb.\tresult2 =mean(out\u2019)\u2019; averages all the spectra and stores the resulting spectrum in the variable result2. \r\n\t\t\tThe apostrophe is an operator to transpose the matrix, changing an m*n matrix to an n*m matrix. We first \r\n\t\t\ttranspose the matrix so that we can take the average of the spectra and then we transpose it back to \r\n\t\t\tpreserve its shape (that\u2019s why there\u2019re two apostrophes). This practice is preferred, but it\u2019s slightly slower \r\n\t\t\tthan (a).\r\n4.\tIf another file needs to be loaded, simply double-click that mat file under current folder. All variables including\r\n\t\u201Cout\u201D will be overwritten except those that don\u2019t exist in this new mat file like result1 and result2 we just\r\n\tcreated. Now repeat step 3 but assign different variable names like result3 = mean(out\u2019)\u2019; so that we can store\r\n\tthe spectrum information in the file we just loaded. \r\n5.\tThe commend plot(wave, result1) will plot the graph for you. Wave is the variable on the x-axis, and results1 is\r\n\tthe variable on the y-axis. If two spectra need to be plotted in the same graph, the command should be\r\n\tplot(wave, result1, wave, result2)\r\n6.\tWe can also add legend and labels to make the graph prettier. plot(wave, result1, wave, result3);\r\n\tlegend(\'60ml\/dl\',\'100ml\/`dl\'); xlabel(\'wavenumber cm^{-1}\'); ylabel(\'signal (a.u.)\')\r\n\tThe graph is editable after it\u2019s been plotted. For example, you can drag the legend to wherever you want,\r\n\tchange its shape or color, add a title for the graph, etc.\r\n7.\tSave the graph in the format in pdf or jpg is convenient. The fig format is also recommended because the\r\n\tgraph can be edited later (it can only opened in MATLAB though).\r\n\r\nA few remarks:\r\n1.\tPutting a semicolon after each command is important because it suppresses the output and prevents the\r\n\tprogram from printing out everything in the command window. \r\n2.\tYou can get help by typing \u201Chelp\u201D in the command window. For example \u201Chelp plot\u201D can show you all\r\n\tinformation about the plot function.\r\n3.\tTo stop executing a command in the middle of a test, press Ctrl+C. On a Mac, use Command+. (the\r\n\tCommand key and the period key)."
tutorialArray = [ "1.\tNavigate to the folder where the data is stored. The files should appear under current folder.\r", "2.\tFind the file you hope to plot and double-click the mat file.\r", "\t>> load(\u2018Sand_60_1_070915\u2019) will show up in the command window. \r", "\tDouble-clicking the file is equivalent to typing the above command. After loading the file, all variables in this\r", "\tmat file will be displayed in the workspace as they are added to your current workspace. (If a new variable has\r", "\tthe same name of a variable that already exists in the workspace, the old one will be overwritten.)\r", "3.\tIn the files we work with, the variable \u201Cout\u201D always stores the spectra in a matrix with the dimension of 182401\r", "\tby 10. (182401 is the number of data points in each spectrum, and we have 10 spectra because there are 5\r", "\truns, each including two scans.)\r", "\t\ta.\tresult1 = out(:,1); stores the first spectrum out of the 10 in a variable called result1. The colon inside the \r", "\t\t\tparenthesis represents the entire column, and 1 indicates the first element of a row. Together result1 = \r", "\t\t\tout(:,1) means taking the first column of the variable out and assigning it to a variable called result1.\r", "\t\tb.\tresult2 =mean(out\u2019)\u2019; averages all the spectra and stores the resulting spectrum in the variable result2. \r", "\t\t\tThe apostrophe is an operator to transpose the matrix, changing an m*n matrix to an n*m matrix. We first \r", "\t\t\ttranspose the matrix so that we can take the average of the spectra and then we transpose it back to \r", "\t\t\tpreserve its shape (that\u2019s why there\u2019re two apostrophes). This practice is preferred, but it\u2019s slightly slower \r", "\t\t\tthan (a).\r", "4.\tIf another file needs to be loaded, simply double-click that mat file under current folder. All variables including\r", "\t\u201Cout\u201D will be overwritten except those that don\u2019t exist in this new mat file like result1 and result2 we just\r", "\tcreated. Now repeat step 3 but assign different variable names like result3 = mean(out\u2019)\u2019; so that we can store\r", "\tthe spectrum information in the file we just loaded. \r", "5.\tThe commend plot(wave, result1) will plot the graph for you. Wave is the variable on the x-axis, and results1 is\r", "\tthe variable on the y-axis. If two spectra need to be plotted in the same graph, the command should be\r", "\tplot(wave, result1, wave, result2)\r", "6.\tWe can also add legend and labels to make the graph prettier. plot(wave, result1, wave, result3);\r", "\tlegend(\'60ml\/dl\',\'100ml\/`dl\'); xlabel(\'wavenumber cm^{-1}\'); ylabel(\'signal (a.u.)\')\r", "\tThe graph is editable after it\u2019s been plotted. For example, you can drag the legend to wherever you want,\r", "\tchange its shape or color, add a title for the graph, etc.\r", "7.\tSave the graph in the format in pdf or jpg is convenient. The fig format is also recommended because the\r", "\tgraph can be edited later (it can only opened in MATLAB though).\r", "\r", "A few remarks:\r", "1.\tPutting a semicolon after each command is important because it suppresses the output and prevents the\r", "\tprogram from printing out everything in the command window. \r", "2.\tYou can get help by typing \u201Chelp\u201D in the command window. For example \u201Chelp plot\u201D can show you all\r", "\tinformation about the plot function.\r", "3.\tTo stop executing a command in the middle of a test, press Ctrl+C. On a Mac, use Command+. (the\r", "\tCommand key and the period key)." ]
# =====================================================================================================================

class Listbox(Tkinter.Listbox):
	def autowidth(self,maxwidth): #{
		f = font.Font(font=self.cget("font"))
		pixels = 0
		for item in self.get(0, "end"):
			pixels = max(pixels, f.measure(item))
		pixels = pixels + 10
		width = int(self.cget("width"))
		for w in range(0, maxwidth+1, 5):
			if self.winfo_reqwidth() >= pixels:
				break
			self.config(width = width+w)

class Application(Frame):
	def __init__(self, master=None): #{
		Frame.__init__(self,master)
		self.grid(sticky=N+S+E+W)
		self.mainframe()
	#}
	def autowidth(self,maxwidth): #{
		f = font.Font(font=self.cget("font"))
		pixels = 0
		for item in self.get(0, "end"):
			pixels = max(pixels, f.measure(item))
		pixels = pixels + 10
		width = int(self.cget("width"))
		for w in range(0, maxwidth+1, 5):
			if self.winfo_reqwidth() >= pixels:
				break
			self.config(width = width+w)
	#}
	def mainframe(self): #{
		self.data = Listbox(self,bg='red')
		self.scrollbar = Scrollbar(self.data, orient=VERTICAL)
		self.data.config(yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.data.yview)
		
		for item in tutorialArray:
			self.data.insert(END, item)
		
		self.run = Button(self, text='run')
		self.destroy = Button(self,text='stop')
		
		self.data.grid(row=1, column=0, columnspan = 1500, rowspan = 1000, sticky=N+S+E+W)
		self.data.columnconfigure(0, weight=1)
		
		self.run.grid(row=1001,column=0,sticky=EW)
		self.destroy.grid(row=1001,column=1, sticky=EW)
		
		self.scrollbar.grid(column=1501, sticky=N+S)

'''
class App(object):
    def __init__(self):
        self.root = Tk()

    # create a Frame for the Text and Scrollbar
        txt_frm = Tkinter.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = Tkinter.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = Tkinter.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
'''
'''
def Michelle_Matlab_Tutorial(): #{
	# create the pop-up window
	#mWin = Toplevel(bg = "white")
	
	#mWin.wm_title("A brief MATLAB tutorial for the glucose project")
	
	
	#Adding a scrollbar
	#canvas = Tkinter.Canvas(mWin, borderwidth = 0, background = "#ffffff")
	#frame = Tkinter.Frame(canvas, background = "#ffffff")
	#vsb = Tkinter.Scrollbar(mWin, orient="vertical", command=canvas.yview)
	#canvas.configure(yscrollcommand=vsb.set)
	
	vsb.pack(side="right", fill="y")
	canvas.pack(side = "left", fill="both", expand=True)
	canvas.create_window((4,4), window=frame, anchor="nw")
	
	frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
	# establish the text string
	
	# setup text bar to print string on word wrap
	Tkinter.Label(mWin, text=tutorialString, anchor=W, justify=LEFT, font=(font_type, size_variable), bg="white").grid(sticky='E')
	mWin.mainloop()
#}
'''
	
mWin = Tk()
listbox = Listbox(mWin, selectmode=Tkinter.SINGLE)

for item in tutorialArray:
	listbox.insert(Tkinter.END, item)

button = Tkinter.Button(mWin, text='execute')#, command=execute)
listbox.autowidth(250)
button.grid(row=0)
listbox.grid(row=1)
mWin.mainloop()
