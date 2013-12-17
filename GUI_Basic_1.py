#GUI at its baby steps!

from CC import *
from Tkinter import *
import os, sys

loginWindow = Tkinter.Tk()           #Creates an empty window
loginWindow.geometry('1024x768')     #Standard Definition

#All the other codes / widgets for the Login Page (still inc)

loginButton = Tkinter.Button(top, text = "Login", command = CC.login)
loginButton.pack()

loginWindow.mainloop()
