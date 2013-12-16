#GUI at its baby steps!

from CC import *
from Tkinter import *
import os, sys

newWindow = Tkinter.Tk()           #Creates an empty window
newWindow.geometry('1024x768')     #Standard Definition

loginButton = Tkinter.Button(top, text = "Login", command = CC.login)
loginButton.pack()

newWindow.mainloop()
