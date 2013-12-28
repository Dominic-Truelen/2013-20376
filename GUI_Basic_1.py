#!/usr/bin/python
# -*- coding: utf-8 -*-
#http://www.python.org/dev/peps/pep-0263/
#GUI at its baby steps!
 
from CC import *
from Tkinter import *
import os, sys

defaultEntryStyle = ("Tahoma", 13)

loginWindow = Tk()          		 #Creates an empty window
loginWindow.geometry('1000x600')     #Standard Definition
loginWindow.resizable(0,0)			 #Do not resize the window ever 	
loginWindow.wm_iconbitmap('CoffeeCup.ico')
loginWindow.wm_title('Welcome to Caffy')
#loginWindow.configure(background="#FFEEE5")

#All the other codes / widgets for the Login Page (still inc)

usernameInput = Entry(width=17, font=defaultEntryStyle, relief=FLAT)
usernameInput.place(anchor=CENTER,relx=0.59, rely=0.1)
passwordInput = Entry(width=17, show="•", font=defaultEntryStyle, relief=FLAT)
passwordInput.place(anchor=CENTER, relx=0.77, rely=0.1)
loginButton = Button(text="Log In", width=7, font=("Tahoma", 9, "bold"), relief=GROOVE, fg="#FFFFFF", bg="#AB3700", command = validation.validation)
usernameInput.bind("<Return>", validation.validation)		#If user presses enter key on usr, execute the Login (This is a secret function)
passwordInput.bind("<Return>", validation.validation)		#If user presses enter key on pwd, execute the Login (This is also a secret function)
loginButton.place(anchor=CENTER, relx=0.9, rely=0.1)

loginWindow.mainloop()
#loginWindow.destroy()

os.remove('CC.pyc')
os.remove('Main.pyc')	