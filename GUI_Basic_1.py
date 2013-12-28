#!/usr/bin/python											
# -*- coding: utf-8 -*-
#GUI at its baby steps!
 
from CC import *
from Tkinter import *
import os, sys, glob

val = validation()
loginCC = CC()

defaultEntryStyle = ("Tahoma", 13)
defaultLabelStyle = ("Tahoma", 9)
signatureColor = "#AB3700"
toplayerColor = "#433833"
backgroundColor = "#FFEEE5"
		
def guiValidation(event):
		loginButton.flash()
		if glob.glob(usernameInput.get()) == []:
			print "INVALID USERNAME"
		else:
			f = open(usernameInput.get())
			f.readline()
			f.readline()
			if (passwordInput.get() + '\n') == f.readline():
				print "SUCCESSFUL"
			else:
				print "INVALID PASSWORD"

loginWindow = Tk()          		 #Creates an empty window
loginWindow.geometry('1000x600')     #Standard Definition
loginWindow.resizable(0,0)			 #Do not resize the window ever 	
loginWindow.wm_iconbitmap('CoffeeCup.ico')
loginWindow.wm_title('Welcome to Caffy')
#loginWindow.configure(background="#FFEEE5")

#All the other codes / widgets for the Login Page (still inc)

topLayer = Frame(height=80, width=1000, bg=toplayerColor)
topLayer.pack()
usernameLabel = Label(text="Username", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle)
usernameLabel.place(anchor=CENTER, relx=0.5379, rely=0.035)
passwordLabel = Label(text="Password", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle)
passwordLabel.place(anchor=CENTER, relx=0.7163, rely=0.035)


usernameInput = Entry(width=17, font=defaultEntryStyle, relief=FLAT)
usernameInput.place(anchor=CENTER,relx=0.59, rely=0.08)
usernameInput.focus()

passwordInput = Entry(width=17, show="•", font=defaultEntryStyle, relief=FLAT)
passwordInput.place(anchor=CENTER, relx=0.77, rely=0.08)

loginButton = Button(text="Log In", width=7, font=("Tahoma", 9, "bold"), relief=GROOVE, fg="#FFFFFF", bg=signatureColor, command=lambda: val.guiv(usernameInput.get(), passwordInput.get()))
usernameInput.bind("<Return>", guiValidation)		#If user presses enter key on usr, execute the Login (This is a secret function)
passwordInput.bind("<Return>", guiValidation)		#If user presses enter key on pwd, execute the Login (This is also a secret function)
loginButton.place(anchor=CENTER, relx=0.9, rely=0.08)

loginWindow.mainloop()
#loginWindow.destroy()

os.remove('CC.pyc')
#os.remove('Main.pyc')	