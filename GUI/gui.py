"""
Kathryn DiPippo
6/22/2015
gui.py
- code to construct the gui for the software
- at the moment, this code will just take the data and store it into variables
- there is no function integration yet


https://www.zetcode.com/gui/tkinter/
See above for the tutorial that was used.

TO-DO
- enable a way to test this to see if the layout is work
- create a pop-up gif of a loading bar for used
"""

from PIL import Image, ImageTK			# supports images for GUI design
from Tkinter import Tk, Frame, BOTH		# import Tk (root window) and Frame (other widgets) classes
from ttk import Frame, Button, Style	# Tkinter support for widget theming from the ttk module

# ---------------------------------------------------------------------------------------------------------------------
# Example window that inherits from the Frame container widget
class Example(Frame): #{
	# call the constructor of our inherited class
	def __init__(self,parent): #{
		# background is the background color of the frame
		Frame.__init__(self, parent, background = "white")
		self.parent = parent				# save a reference to the parent widget
		#self.initUI()						# create user interface
		self.centerWindow()					# function to place the window in the center of the screen\\
		self.initUI()
	#}
	
	def centerWindow(self): #{
		w = 290
		h = 150
		
		sw = self.parent.winfo_screenwidth()	# returns the width of the screen
		sh = self.parent.winfo_screenheight()	# returns the height of the screen
		
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))	# set the size of the window and positions it on the screen
															# (" width x height + 'x' + 'y' ")
	#}
	
	def initUI(self): #{
		self.parent.title("Simple")							# set the title of the window
		self.pack(fill = BOTH, expand = 1)					# organize widgets into horizontal and vertical boxes
		
		self.style = Style()								# apply theme for widgets
		style.configure("TFrame", background = "#333")		# dark grey background theme
		#self.style.theme_use("default")
		
		# Button theming
		Style().configure("TButton", padding(0, 5, 0, 5), font = 'serif 10')
		
		# instance of the button widget
		quitButton = Button(self, text = "Quit", command = self.quit)
		quitButton.place(x = 50, y = 50)					# placement using absolute positioning
		
		# ok and close buttons
		closeButton = Button(self, text = "Close")			# button is put in a horizontal box. padx and pady puts some space
															# between button widgets and the surrounding frame
		closeButton.pack(side = RIGHT, padx = 5, pady = 5)
		okButton = Button(self, text = "OK")
		okButton.pack(side = RIGHT)							# okButton is placed next to closeButton with padx space between
		
		# Image placement code
		bard = Image.open("bardejov.jpg")
		bardejob = ImageTk.PhotoImage(bard)
		label1 = Label(self, image = bardejov)
		label1.image = bardejov
		label1.place(x = 20, y = 20)
	#}

#}

# ---------------------------------------------------------------------------------------------------------------------
# main function
def main(): #{
	root = Tk()
	app = Example(root)						# create instance of the application class
	root.mainloop()							# enter mainloop. Event handling begins below
#}

# =====================================================================================================================
if __name__ == '__main__': #{
	main()
#}