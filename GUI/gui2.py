import Tkinter

def gui(): #{
	getFld = Tkinter.IntVar()
	
	form.wm_title('CLINICAL')
	
	#---------------
	stepZero = Tkinter.LabelFrame(form, text=" 1. Store Data: ")
	stepZero.grid(row=0, columnspan=10, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	
	inFileLbl = Tkinter.Label(stepZero, text="Select the Folder to Store Data:")
	inFileLbl.grid(row=0, column=0, columnspan=3, sticky='E', padx=5, pady=2)
	
	inFileTxt = Tkinter.Entry(stepZero)
	inFileTxt.grid(row=0, column=3, columnspan=6, sticky="WE", pady=3)
	
	inFileBtn = Tkinter.Button(stepZero, text="Browse ...")
	inFileBtn.grid(row=0, column=9, sticky='W', padx=5, pady=2)
	
	#---------------
	stepOne = Tkinter.LabelFrame(form, text=" 2. Basic Information: ")
	stepOne.grid(row=1, columnspan=7, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	
	#helpLf = Tkinter.LabelFrame(form, text=" Description ")
	#helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, sticky='NS', padx=5, pady=5)
	
	#helpLbl = Tkinter.Label(helpLf,text="If we want to put help text here, we could go and do that. IDK what to put here for now")
	#helpLbl.grid(row=0)
	
		# Name --------
	nameLbl = Tkinter.Label(stepOne, text="Name:")
	nameLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)
	
	nameTxt = Tkinter.Entry(stepOne)
	nameTxt.grid(row=1, column=1, pady=2)
	
		# Height --------
	heightLbl = Tkinter.Label(stepOne, text="Height:")
	heightLbl.grid(row=2, column=0, sticky='E', padx=5, pady=2)
	
	heightTxt = Tkinter.Entry(stepOne)
	heightTxt.grid(row=2, column=1, pady=2)
	
	outEncLbl = Tkinter.Label(stepOne, text="ft")
	outEncLbl.grid(row=2, column=2, padx=5, pady=2)
	
	outEncTxt = Tkinter.Entry(stepOne)
	outEncTxt.grid(row=2, column=3, padx=5, pady=2)
	
	outEncLbl2 = Tkinter.Label(stepOne, text="inches")
	outEncLbl2.grid(row=2, column=4, padx=5, pady=2)
	
		# Weight --------
	weightLbl = Tkinter.Label(stepOne, text="Weight:")
	weightLbl.grid(row=3, column=0, sticky='E', padx=5, pady=2)
	
	weightTxt = Tkinter.Entry(stepOne)
	weightTxt.grid(row=3, column=1, padx=5, pady=2)
	
		# Age --------
	AgeLbl = Tkinter.Label(stepOne, text="Age:")
	AgeLbl.grid(row=4, column=0, sticky='E', padx=5, pady=2)
	
	AgeTxt = Tkinter.Entry(stepOne)
	AgeTxt.grid(row=4, column=1, padx=5, pady=2)
	
		# Date --------
	DateLbl1 = Tkinter.Label(stepOne, text="Date:")
	DateLbl1.grid(row=5, column=0, sticky='E', padx=5, pady=2)
	
	DateTxt1 = Tkinter.Entry(stepOne)
	DateTxt1.grid(row=5, column=1, padx=2, pady=2)
	
	DateLbl2 = Tkinter.Label(stepOne, text="/")
	DateLbl2.grid(row=5, column=2, padx=5, pady=2)
	
	DateTxt2 = Tkinter.Entry(stepOne)
	DateTxt2.grid(row=5, column=3, padx=2, pady=2)
	
	DateLbl3 = Tkinter.Label(stepOne, text="/")
	DateLbl3.grid(row=5, column=4, padx=5, pady=2)
	
	DateTxt3 = Tkinter.Entry(stepOne)
	DateTxt3.grid(row=5, column=5, padx=2, pady=2)

		# Concentration --------
	ConcentrationLbl = Tkinter.Label(stepOne, text="Concentration:")
	ConcentrationLbl.grid(row=6, column=0, sticky='E', padx=5, pady=2)
	
	ConcentrationTxt = Tkinter.Entry(stepOne)
	ConcentrationTxt.grid(row=6, column=1, columnspan=3, padx=5, pady=2)
	
	ConcentrationLbl = Tkinter.Label(stepOne, text="mg/L")
	ConcentrationLbl.grid(row=6, column=4, padx=5, pady=2)
	
	#---------------
	stepTwo = Tkinter.LabelFrame(form, text=" 3. Run: ")
	stepTwo.grid(row=2, columnspan=7, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	
	inFileBtn = Tkinter.Button(stepTwo, text="          BEGIN SENSING          ")
	inFileBtn.grid(row=7, sticky='WE', padx=5, pady=2)
	
	#outTblLbl = Tkinter.Label(stepTwo, text="Enter the name of the table to be used in the statements:")
	#outTblLbl.grid(row=7, column=0, sticky='W', padx=5, pady=2)
	
	#outTblTxt = Tkinter.Entry(stepTwo)
	#outTblTxt.grid(row=8, column=1, columnspan=3, pady=2, sticky='WE')
	
	#fldLbl = Tkinter.Label(stepTwo, text="Enter the field (column) names of the table:")
	#fldLbl.grid(row=9, column=0, padx=5, pady=2, sticky='W')
	
	#getFldChk = Tkinter.Checkbutton(stepTwo, text="Get fields automatically from input file", onvalue=1, offvalue=0)
	#getFldChk.grid(row=10, column=1, columnspan=3, pady=2, sticky='WE')
	
	#fldRowTxt = Tkinter.Entry(stepTwo)
	#fldRowTxt.grid(row=11, columnspan=5, padx=5, pady=2, sticky='WE')
	
	#---------------
	#stepThree = Tkinter.LabelFrame(form, text=" 4. Results: ")
	#stepThree.grid(row=3, columnspan=7, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
	
	#transChk = Tkinter.Checkbutton(stepThree, text="Enable Transaction", onvalue=1, offvalue=0)
	#transChk.grid(row=12, sticky='W', padx=5, pady=2)
	
	#transRwLbl = Tkinter.Label(stepThree, text=" => Specify number of rows per transaction:")
	#transRwLbl.grid(row=12, column=2, columnspan=2, sticky='W', padx=5, pady=2)
	
	#transRwTxt = Tkinter.Entry(stepThree)
	#transRwTxt. grid(row=12, column=4, sticky='WE')
#}

if __name__ == '__main__': #{
	form = Tkinter.Tk()
	gui()
	form.mainloop()
#}
