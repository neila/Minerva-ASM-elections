from Tkinter import Tk # used for UI
from tkFileDialog import askopenfilename # used to pick a file
from Tkinter import *

def get_file_path():
	root = Tk() # creating a TK
	# we don't want a full GUI, so keep the root window from appearing
	root.withdraw()

	 # show an "Open" dialog box and return the path to the selected file
	filename = askopenfilename()
	# these two lines close the filepicker after selection
	root.update()
	root.destroy()

	return filename

def getvalue():
	raw_input()

def get_number_of_candidates():
	root = Tk() # creating a TK
	# we don't want a full GUI, so keep the root window from appearing
	# root.withdraw()

	root.title('how to get text from textbox')

	mystring = StringVar()

	Label(root, text="Text to get").grid(row=0, sticky=W)  #label
	Entry(root, textvariable = mystring).grid(row=0, column=1, sticky=E) #entry textbox

	WSignUp = Button(root, text="print text", command=getvalue).grid(row=3, column=0, sticky=W) #button

	# these two lines close the filepicker after selection
	root.update()

	return mystring



