#GUI at its baby steps!

from CC import *
from Tkinter import *
import os, sys

loginWindow = Tk()           #Creates an empty window
loginWindow.geometry('1138x640')     #Standard Definition

#All the other codes / widgets for the Login Page (still inc)

loginButton = Button(text = "Login", command = login)
loginButton.pack()

loginWindow.mainloop()
loginWindow.destroy()