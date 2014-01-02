#!/usr/bin/python																# Allows the use of Non-ASCII characters in window
# -*- coding: utf-8 -*-
 
from CC import validation, CC													# pack() is for stacking, while place() is for a more
from Tkinter import *															# accurate placing of widgets. grid() is for tables
import os, sys, glob

defaultEntryStyle = ("Tahoma", 12)												# Initial font settings for styling
defaultLabelStyle = ("Tahoma", 9)
defaultCreateStyle = ("Tahoma", 14)
signatureColor = "#AB3700"														# Shortcut labels for custom color styling
toplayerColor = "#433833"
backgroundColor = "#FFEEE5"

#All the other codes / widgets for the Login Page (still inc)

class Page(Frame):																# Parent Frame that lets all children have show()
	def __init__(self):
		Frame.__init__(self)
	def show(self):																# Easy function for lifting a class from the stacking layers of classes
		self.lift()

class loginPageClass(Page):														# The login class!
	def __init__(self):	
		Frame.__init__(self)
		Window.wm_title('Welcome to Caffy')										# Initial title text in the title bar
		
		topLayer = Frame(self, height=80, width=1000, bg=toplayerColor)			# Code here for the Log-in classes
		topLayer.pack()		
		Label(topLayer, text="Username", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle).place(anchor=CENTER, relx=0.5379, rely=0.28)	# Labels for the entry fields
		Label(topLayer, text="Password", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle).place(anchor=CENTER, relx=0.7163, rely=0.28)	# Labels for the entry fields	
		self.usernameVariable = StringVar()
		self.usernameInput = Entry(topLayer, width=17, textvariable=self.usernameVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the username
		self.usernameInput.place(anchor=CENTER,relx=0.59, rely=0.59)
		self.usernameInput.focus()													# Puts the cursor automatically at the user_name field
		self.passwordVariable = StringVar()
		self.passwordInput = Entry(topLayer, width=17, show="•", textvariable=self.passwordVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the password
		self.passwordInput.place(anchor=CENTER, relx=0.77, rely=0.59)
		
		midLayer = Frame(self, width=1000, height=490, bg=backgroundColor)		# Code here for the CREATE class
		midLayer.pack()
		layer1 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer1.place(anchor=CENTER, relx=0.7, rely=0.3)
		layer2 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer2.place(anchor=CENTER, relx=0.7, rely=0.45)
		layer3 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer3.place(anchor=CENTER, relx=0.7, rely=0.6)
		self.newUsernameVariable = StringVar()
		newUsernameInput = Entry(layer1, width=35, textvariable=self.newUsernameVariable, font = defaultCreateStyle, relief=FLAT)
		newUsernameInput.place(anchor=CENTER, relx=0.5, rely=0.5)		
		self.newPasswordVariable = StringVar()
		newPasswordInput = Entry(layer2, width=35, show="•", textvariable=self.newPasswordVariable, font = defaultCreateStyle, relief=FLAT)
		newPasswordInput.place(anchor=CENTER, relx=0.5, rely=0.5)
		self.newPasswordVerifyVariable = StringVar()
		newPasswordVerifyInput = Entry(layer3, width=35, show="•", textvariable=self.newPasswordVerifyVariable, font = defaultCreateStyle, relief=FLAT)
		newPasswordVerifyInput.place(anchor=CENTER, relx=0.5, rely=0.5)
		Label(midLayer, text="Create your own username:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.23)
		Label(midLayer, text="Create a new password:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.38)
		Label(midLayer, text="Reenter your password:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.53)

		bottomLayer = Frame(self, width=1000, height=30, bg=toplayerColor)		# Code here for the extra details
		bottomLayer.pack()
		Label(bottomLayer, text="Thank you for choosing Caffy™ | Copyright © 2014. All rights are reserved", fg="#FFFFFF", bg=toplayerColor, font=("Tahoma", 8)).place(anchor=CENTER, relx=0.5, rely=0.5)

class homePageClass(Page):														# Code for the News Feed
	def __init__(self):
		Frame.__init__(self)		
		blank = Frame(self, width=1000, height=600, bg="#FFF000")
		blank.pack()		
		
class navClass(Frame):															# Faҫade design pattern navClass because of navigation (button fxns)
	def __init__(self):
		Frame.__init__(self)
		
		self.val = validation()													# Initial functions for the verifications
		self.loginCC = CC()
		self.homepage = homePageClass()
		self.login = loginPageClass()		
		
		container = Frame(width=1000, height=600)								# Frame for all the to-be-children pages
		container.place(anchor=NW)		
		
		self.homepage.place(in_=container)		
		self.login.place(in_=container)
		
		self.verifyLabel = Label(self.login, text="", fg="#FFF000", bg=toplayerColor, font=defaultLabelStyle) 	# For warning purposes of login entries
		self.verifyLabel.place(anchor=E, relx=0.5, rely=0.0786)
		
		self.loginButton = Button(self.login, text="Log In", width=7, height=1, font=("Tahoma", 9, "bold"), relief=FLAT, fg="#FFFFFF", bg=signatureColor, command=self.verifyLogin)
		self.loginButton.place(anchor=CENTER, relx=0.904, rely=0.0786)				# Button of the LoginPage (click to verify entries)
		
		self.login.usernameInput.bind("<Return>", lambda event: self.loginButton.invoke())	#Allows the use of the Enter key
		self.login.passwordInput.bind("<Return>", lambda event: self.loginButton.invoke())
		
		createButton = Button(self.login, text="Sign Me Up!", width=12, font=("Tahoma", 13, "bold"), relief=FLAT, fg="#FFFFFF", bg="#67AE55", command=self.verifyCreate)
		createButton.place(anchor=CENTER, relx=0.82, rely=0.75)
		
		self.login.show()														# Displays first ever page w/c is the login page
	
	def verifyLogin(self):														# Method executed whenever "Log In" button is pressed
		self.responses=["USERNAME IS BLANK", "PASSWORD IS BLANK", "ACCOUNT DOES NOT EXIST", "INVALID PASSWORD"]
		self.loginCC.set_name(self.login.usernameVariable.get())				# Accessors!
		self.loginCC.set_password(self.login.passwordVariable.get())
		if self.val.guiv(self.loginCC.get_name(), self.loginCC.get_password()) in self.responses:	# If return value from imported class CC is inside the list,		
			self.verifyLabel.config(text=self.val.guiv(self.loginCC.get_name(), self.loginCC.get_password()))	# Display the possible warnings;
		else:
			self.loginButton.flash()
			self.homepage.show()												# otherwise, if entries are correct, execute & display the home page
		
	def verifyCreate(self):
		pass
		
Window = Tk()        		 													# Creates an empty window
Main = navClass()
Window.geometry('1000x600+170+80')												# Set dimensions to 1000x600 pos @ screen center
Window.resizable(0,0)			 												# Does not resize the window, ever 	
Window.wm_iconbitmap('CoffeeCup.ico')											# Adds a little mug icon over the top left corner
Window.mainloop()																# Executes code above in a loop

os.remove('CC.pyc')																# Removes the temporary files inside the (" ")
#os.remove('Main.pyc')															# (For Git uploading purposes only)