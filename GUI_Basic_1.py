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
		
		usernameLabel = Label(topLayer, text="Username", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle)	# Labels for the entry fields
		usernameLabel.place(anchor=CENTER, relx=0.5379, rely=0.28)
		passwordLabel = Label(topLayer, text="Password", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle)	# Labels for the entry fields	
		passwordLabel.place(anchor=CENTER, relx=0.7163, rely=0.28)

		self.usernameVariable = StringVar()
		usernameInput = Entry(topLayer, width=17, textvariable=self.usernameVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the username
		usernameInput.place(anchor=CENTER,relx=0.59, rely=0.59)
		usernameInput.focus()													# Puts the cursor automatically at the user_name field

		self.passwordVariable = StringVar()
		passwordInput = Entry(topLayer, width=17, show="•", textvariable=self.passwordVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the password
		passwordInput.place(anchor=CENTER, relx=0.77, rely=0.59)		
		
		midLayer = Frame(self, width=1000, height=490, bg=backgroundColor)		# Code here for the CREATE class
		midLayer.pack()

		bottomLayer = Frame(self, width=1000, height=30, bg=toplayerColor)		# Code here for the extra details
		bottomLayer.pack()			

class homePageClass(Page):														# Code for the News Feed
	def __init__(self):
		Frame.__init__(self)		
		blank = Frame(self, width=1000, height=600, bg="#FFF000")
		blank.pack()		
		
class navClass(Frame):															# navClass because of navigation (button fxns)
	def __init__(self):
		Frame.__init__(self)
		
		self.val = validation()													# Initial functions for the verifications
		self.loginCC = CC()
		homepage = homePageClass()
		login = loginPageClass()
		
		def _accept(userName, passWord):										# Method executed whenever "Log In" button is pressed
			self.responses=["USERNAME IS BLANK", "PASSWORD IS BLANK", "ACCOUNT DOES NOT EXIST", "INVALID PASSWORD"]
			self.loginCC.set_name(userName)										# Accessors!
			self.loginCC.set_password(passWord)
			if self.val.guiv(self.loginCC.get_name(), self.loginCC.get_password()) in self.responses:	# If return value from imported class CC is inside the list,		
				verifyLabel.config(text=self.val.guiv(self.loginCC.get_name(), self.loginCC.get_password())) # Display the possible warnings;
			else:
				homepage.show()													# otherwise, if entries are correct, execute & display the home page
		
		container = Frame(width=1000, height=600)								# Frame for all the to-be-children pages
		container.place(anchor=NW)		
		
		homepage.place(in_=container)		
		login.place(in_=container)
		
		verifyLabel = Label(login, text="", fg="#FFF000", bg=toplayerColor, font=defaultLabelStyle) 	# For warning purposes of login entries
		verifyLabel.place(anchor=E, relx=0.5, rely=0.0786)
		
		loginButton = Button(login, text="Log In", width=7, height=1, font=("Tahoma", 9, "bold"), relief=GROOVE, fg="#FFFFFF", bg=signatureColor, command=lambda: _accept(login.usernameVariable.get(), login.passwordVariable.get()))
		loginButton.place(anchor=CENTER, relx=0.904, rely=0.0786)				# Button of the LoginPage (click to verify entries)
		
		login.show()															# Displays first ever page w/c is the login page
		
Window = Tk()        		 													# Creates an empty window
Main = navClass()
Window.geometry('1000x600+170+80')												# Set dimensions to 1000x600 pos @ screen center
Window.resizable(0,0)			 												# Does not resize the window, ever 	
Window.wm_iconbitmap('CoffeeCup.ico')											# Adds a little mug icon over the top left corner
Window.mainloop()																# Executes code above in a loop

os.remove('CC.pyc')																# Removes the temporary files inside the (" ")
#os.remove('Main.pyc')															# (For Git uploading purposes only)