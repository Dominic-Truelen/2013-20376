#!/usr/bin/python																# Allows the use of Non-ASCII characters in window
# -*- coding: utf-8 -*-
 
from CC import validation, CC													# pack() is for stacking, while place() is for a more
from Tkinter import *															# accurate placing of widgets. grid() is for tables
import os, sys, glob

defaultEntryStyle = ("Tahoma", 12)												# Initial font settings for styling
defaultLabelStyle = ("Tahoma", 9)
signatureColor = "#AB3700"														# Shortcut labels for custom color styling
toplayerColor = "#433833"
backgroundColor = "#FFEEE5"

'''
def guiValidation(event):														# Used alternatively for the button press
	loginButton.flash()															# Basically executes the same validate method, but
	if usernameInput.get() == "":												# this "event" accepts the <Return> key as input
		print "YOU DID NOT INPUT A USERNAME"
	elif passwordInput.get() == "":
			print "YOU DID NOT INPUT A PASSWORD"
	else:																		# If entry inputs are incorrect, display catches
		if glob.glob(usernameInput.get()) == []:
			print "INVALID USERNAME"
		else:
			f = open(usernameInput.get())
			f.readline()
			f.readline()
			if (passwordInput.get() + '\n') == f.readline():					# If both inputs are correct, display success!
				print "SUCCESSFUL"
			else:
				print "INVALID PASSWORD"
'''

#All the other codes / widgets for the Login Page (still inc)

class Page(Frame):																# Parent Frame that lets all children have show()
	def __init__(self):
		Frame.__init(self)
	def show(self):
		self.lift()

class loginPage(Page):															# The login class!
	def __init__(self):	
		Frame.__init__(self)
		Window.wm_title('Welcome to Caffy')										# Initial title text in the title bar
		
		self.val = validation()													# Initial functions for the topLayer
		self.loginCC = CC()
		
		topLayer = Frame(self, height=80, width=1000, bg=toplayerColor)			# Code here for the Log-in classes
		topLayer.pack()

		usernameLabel = Label(topLayer, text="Username", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle)
		usernameLabel.place(anchor=CENTER, relx=0.5379, rely=0.28)
		passwordLabel = Label(topLayer, text="Password", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle)
		passwordLabel.place(anchor=CENTER, relx=0.7163, rely=0.28)

		usernameInput = Entry(topLayer, width=17, font=defaultEntryStyle, relief=FLAT)	# Entry field for the username
		usernameInput.place(anchor=CENTER,relx=0.59, rely=0.59)
		usernameInput.focus()													# Puts the cursor automatically at the username field

		passwordInput = Entry(topLayer, width=17, show="•", font=defaultEntryStyle, relief=FLAT)	#Entry field for the password
		passwordInput.place(anchor=CENTER, relx=0.77, rely=0.59)
		
		verifyLabel = Label(topLayer, text="", fg="#FFF000", bg=toplayerColor, font=defaultLabelStyle)
		verifyLabel.place(anchor=E, relx=0.5, rely=0.59)
		
		loginButton = Button(topLayer, text="Log In", width=7, height=1, font=("Tahoma", 9, "bold"), relief=GROOVE, fg="#FFFFFF", bg=signatureColor, command=lambda: _accept(usernameInput.get(), passwordInput.get()))
		#usernameInput.bind("<Return>", guiValidation)		#If user presses enter key on usr, execute the Login (This is a secret function)
		#passwordInput.bind("<Return>", guiValidation)		#If user presses enter key on pwd, execute the Login (This is also a secret function)
		loginButton.place(anchor=CENTER, relx=0.904, rely=0.59)

		midLayer = Frame(self, width=1000, height=490, bg="#FFF")				# Code here for the CREATE class
		midLayer.pack()

		bottomLayer = Frame(self, width=1000, height=30, bg=toplayerColor)		# Code here for the extra details
		bottomLayer.pack()	
		
		def _accept(userName, passWord):		
			self.responses=["YOU DID NOT INPUT A USERNAME", "YOU DID NOT INPUT A PASSWORD", "USERNAME NOT FOUND", "INVALID PASSWORD"]
			self.loginCC.set_name(userName)
			self.loginCC.set_password(passWord)
			if self.val.guiv(self.loginCC.get_name(), self.loginCC.get_password()) in self.responses:			
				verifyLabel.config(text=self.val.guiv(self.loginCC.get_name(), self.loginCC.get_password()))
			else:
				print "SUCCESSFUL"


Window = Tk()          		 													# Creates an empty window			
Window.geometry('1000x600+170+80')
Window.resizable(0,0)			 												# Do not resize the window, ever 	
Window.wm_iconbitmap('CoffeeCup.ico')											# Add a little mug icon over the top left corner
Main = loginPage()
Main.place(x=0, y=0)
Window.mainloop()																# Executes code above in a loop

os.remove('CC.pyc')																# Removes temporary files
#os.remove('Main.pyc')	