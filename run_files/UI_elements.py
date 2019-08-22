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


class TextButton(Tk):

    def __init__(self, title="get", btnlabel="Confirm", txt=""):
        Tk.__init__(self)
        self.frame = Frame(self)
        self.entry = Entry(self)
        self.title = self.title(title)
        self.label = Label(self,text=txt)
        self.button = Button(self, text=btnlabel, command=self.on_button)
        self.frame.pack()
        self.label.pack()
        self.button.pack()
        self.entry.pack()

    def on_button(self):
    	self.mystring = self.entry.get()
    	self.destroy()
        return 

class YesNoButton(Tk):

    def __init__(self, title="get", btnlabel="Confirm", txt=""):
        Tk.__init__(self)
        self.frame = Frame(self)
        self.entry = Entry(self)
        self.title = self.title(title)
        self.label = Label(self,text=txt)
        self.button = Button(self, text=btnlabel, command=self.on_button)
        self.frame.pack()
        self.label.pack()
        self.button.pack()
        self.entry.pack()

    def on_button(self):
    	self.mystring = self.entry.get()
    	self.destroy()
        return 

def get_first_candidate_column():
	w = TextButton(title="Column",
		btnlabel="Confirm", txt="First Column With\nCandidate Names?\n(index 0)")
	w.mainloop()
	return w.mystring

def get_number_of_winners():
	w = TextButton(title="N Winners",
		btnlabel="Confirm", txt="Number of Winners?")
	w.mainloop()
	return w.mystring




