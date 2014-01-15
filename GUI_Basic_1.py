#!/usr/bin/python																# Allows the use of Non-ASCII characters in window
# -*- coding: utf-8 -*-
 
from CC import *																# pack() is for stacking, while place() is for a more
from Tkinter import *															# accurate placing of widgets. grid() is for tables
from PIL import ImageTk, Image
import os, sys, glob

defaultEntryStyle = ("Tahoma", 12)												# Initial font settings for styling
defaultLabelStyle = ("Tahoma", 9)
defaultCreateStyle = ("Tahoma", 14)
signatureColor = "orange"														# Shortcut labels for custom color styling
toplayerColor = "#555555"
backgroundColor = "#EEEEEE"

a=-0.05																			# Adjuster for widget's y-value placement

#All the other codes / widgets for the HOMEPAGE

class Page(Frame):																# Parent Frame that lets all children have show()
	def __init__(self):
		Frame.__init__(self)
	def show(self):																# Easy function for lifting a class from the stacking layers of classes
		self.lift()

class loginPageClass(Page):														# The login class!
	def __init__(self):	
		Frame.__init__(self)		
		
		topLayer = Frame(self, height=80, width=1000, bg=toplayerColor)			# Code here for the Log-in classes
		topLayer.pack()		
		Label(topLayer, text="Username", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle).place(anchor=CENTER, relx=0.5379, rely=0.28)	# Labels for the entry fields
		Label(topLayer, text="Password", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle).place(anchor=CENTER, relx=0.7163, rely=0.28)	# Labels for the entry fields	
		self.usernameVariable = StringVar()
		self.usernameInput = Entry(topLayer, width=17, textvariable=self.usernameVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the username
		self.usernameInput.place(anchor=CENTER,relx=0.59, rely=0.59)
		self.usernameInput.focus()												# Puts the cursor automatically at the user_name field
		self.passwordVariable = StringVar()
		self.passwordInput = Entry(topLayer, width=17, show="•", textvariable=self.passwordVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the password
		self.passwordInput.place(anchor=CENTER, relx=0.77, rely=0.59)
		Label(topLayer, text="caffy", font=("Verdana", 28), justify=LEFT, bg=toplayerColor, fg="orange").place(anchor=W, relx=0.08, rely=0.5)
		self.coffcup = Label(topLayer, text="☕", font=("Tahoma", 28), justify=LEFT, bg=toplayerColor, fg="#FFFFFF")
		self.coffcup.place(anchor=W, relx=0.175, rely=0.48)
		self.verifyLoginLabel = Label(topLayer, text="", fg="orange", bg=toplayerColor, font=defaultLabelStyle) 	# For warning purposes of login entries
		self.verifyLoginLabel.place(anchor=E, relx=0.5, rely=0.59)
		self.coffcup.bind("<Enter>", lambda f: self.coffcup.config(fg="orange"))
		self.coffcup.bind("<Leave>", lambda g: self.coffcup.config(fg="white"))
		
		midLayer = Frame(self, width=1000, height=490)		# Code here for the CREATE class
		midLayer.pack()
		
		canvasSky = Canvas(midLayer, width=1000, height=490, highlightthickness=0, bg=backgroundColor)
		canvasSky.pack()
		sky = ImageTk.PhotoImage(file="GUIE\\LoginSky.png")
		canvasSky.create_image(500, 245, image=sky)
		canvasSky.image = sky
		
		layer1 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer1.place(anchor=CENTER, relx=0.7, rely=0.3+a)
		layer2 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer2.place(anchor=CENTER, relx=0.7, rely=0.45+a)
		layer3 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer3.place(anchor=CENTER, relx=0.7, rely=0.6+a)
		self.newUsernameVariable = StringVar()
		self.newUsernameInput = Entry(layer1, width=35, textvariable=self.newUsernameVariable, font = defaultCreateStyle, relief=FLAT)
		self.newUsernameInput.place(anchor=CENTER, relx=0.5, rely=0.5+a)		
		self.newPasswordVariable = StringVar()
		self.newPasswordInput = Entry(layer2, width=35, show="•", textvariable=self.newPasswordVariable, font = defaultCreateStyle, relief=FLAT)
		self.newPasswordInput.place(anchor=CENTER, relx=0.5, rely=0.5+a)
		self.newPasswordVerifyVariable = StringVar()
		self.newPasswordVerifyInput = Entry(layer3, width=35, show="•", textvariable=self.newPasswordVerifyVariable, font = defaultCreateStyle, relief=FLAT)
		self.newPasswordVerifyInput.place(anchor=CENTER, relx=0.5, rely=0.5+a)
		Label(midLayer, text="Pick a username:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.23+a)
		Label(midLayer, text="Create a password:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.38+a)
		Label(midLayer, text="Reenter your password:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.53+a)
		Label(midLayer, text="Take a ☕ break!\nSign up!", font=("Tahoma", 35), justify=LEFT, bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.08, rely=0.345+a)
		Label(midLayer, text="Caffy lets you connect and share with\nfriends from around the corner.", font=("Tahoma", 15), justify=LEFT, bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.08, rely=0.58+a)
		Label(midLayer, text="By signing up, you agree with our Terms and Conditions.", font=("Tahoma", 9), justify=RIGHT, bg=backgroundColor, fg="#999999").place(anchor=E, relx=0.8956, rely=0.7+a)
		self.verifyCreateLabel = Label(midLayer, text="", bg=backgroundColor, justify=LEFT)		# Initialization of the create warnings
		self.verifyCreateLabel.place(anchor=W, relx=0.509, rely=0.75)
		
		
		bottomLayer = Frame(self, width=1000, height=30, bg=toplayerColor)		# Code here for the extra details
		bottomLayer.pack()
		Label(bottomLayer, text="Thank you for choosing Caffy™ | Copyright © 2014. All rights are reserved", fg="#FFFFFF", bg=toplayerColor, font=("Tahoma", 8)).place(anchor=CENTER, relx=0.5, rely=0.5)

class homePageClass(Page):														# Code for the News Feed
	def __init__(self):
		Frame.__init__(self)		
		blank = Frame(self, width=1000, height=600, bg="#FFFF00")
		blank.pack()
		Label(blank, text="YOU JUST GOT CAFFIED!", font=("Tahoma", 30, "bold"), bg="#FFFF00", fg="#000000").place(anchor=CENTER, relx=0.5, rely=0.5)
		
class navClass(Frame):															# Faҫade design pattern navClass because of navigation (button fxns)
	def __init__(self):
		Frame.__init__(self)
		
		self.val = validation()													# Initial functions for the verifications
		self.loginCC = CC()
		self.createCC = CC()
		self.cre = create()
		self.homepage = homePageClass()
		self.login = loginPageClass()		
		
		container = Frame(width=1000, height=600)								# Frame for all the to-be-children pages
		container.place(anchor=NW)		
		
		self.homepage.place(in_=container)		
		self.login.place(in_=container)
		
		self.loginButton = Button(self.login, text="Log In", width=7, height=1, font=("Tahoma", 9, "bold"), relief=FLAT, fg="#FFFFFF", bg=signatureColor, command=self.verifyLogin)
		self.loginButton.place(anchor=CENTER, relx=0.904, rely=0.0786)			# Button of the LoginPage (click to verify entries)
		
		self.login.usernameInput.bind("<Return>", lambda event: self.loginButton.invoke())	#Allows the use of the Enter key when loggin in
		self.login.passwordInput.bind("<Return>", lambda event: self.loginButton.invoke())
		
		self.createButton = Button(self.login, text="Sign Me Up!", width=12, font=("Tahoma", 13, "bold"), relief=FLAT, fg="#FFFFFF", bg="#52A41D", command=self.verifyCreate)
		self.createButton.place(anchor=CENTER, relx=0.82, rely=0.75)
		
		self.login.newUsernameInput.bind("<Return>", lambda event: self.createButton.invoke())	#Allows the use of the Enter key when creating accounts
		self.login.newPasswordInput.bind("<Return>", lambda event: self.createButton.invoke())
		self.login.newPasswordVerifyInput.bind("<Return>", lambda event: self.createButton.invoke())
		
		self.login.show()														# Displays first ever page w/c is the login page
		
	def eraseContents(self, *args):												# Function allows unlimited number of arguments by the *args keyword
		for x in args:															# The *args is a tuple, so every element in it must be iterated
			x.delete(0, END)													# to delete the value of all the 3 Create Entries
	
	def verifyLogin(self):														# Method executed whenever "Log In" button is pressed
		self.responses=["USERNAME IS BLANK", "PASSWORD IS BLANK", "ACCOUNT DOES NOT EXIST", "INVALID PASSWORD"]
		self.loginCC.set_name(self.login.usernameVariable.get())				# Accessors!
		self.loginCC.set_password(self.login.passwordVariable.get())
		self.answer = self.val.guiv(self.loginCC.get_name(), self.loginCC.get_password())
		if self.answer in self.responses:										# If return value from imported class CC is inside the list,		
			self.login.verifyLoginLabel.config(text=self.answer)				# display the possible warnings and perform some formatting actions like clear the entry field:
			if self.answer == self.responses[0]:
				self.eraseContents(self.login.passwordInput)
				self.login.usernameInput.focus()
			elif self.answer == self.responses[1]:
				self.login.passwordInput.focus()
			elif self.answer == self.responses[2]:
				self.eraseContents(self.login.usernameInput, self.login.passwordInput)
				self.login.usernameInput.focus()
			else:
				self.eraseContents(self.login.passwordInput)
				self.login.passwordInput.focus()
		else:
			self.loginButton.flash()
			self.homepage.show()												# otherwise, if entries are correct, execute & display the home page
	
	def verifyCreate(self):
		self.responses = ["USERNAME IS BLANK", "PASSWORD REQUIRED", "PLEASE RETYPE THE PASSWORD", "USERNAME IS ALREADY TAKEN", "RETYPE YOUR PASSWORD\nCORRECTLY", "PASSWORD MUST HAVE AT LEAST\n8 CHARACTERS"]
		self.createCC.set_name(self.login.newUsernameVariable.get())
		self.createCC.set_password(self.login.newPasswordVariable.get())
		self.answer = self.cre.guic(self.createCC.get_name(), self.createCC.get_password(), self.login.newPasswordVerifyVariable.get())		# Assign the return value of this very long function into variable answer! (actually, self.answer)
		if self.answer in self.responses:																									# If the answer is included in the list above,
			self.login.verifyCreateLabel.config(text=self.answer, fg="red", font=("Tahoma", 9, "bold"))
			if self.answer == self.responses[0] or self.answer == self.responses[3]:											# Display that message from the list, then format some widgets
				self.eraseContents(self.login.newUsernameInput, self.login.newPasswordInput, self.login.newPasswordVerifyInput)
				self.login.newUsernameInput.focus()
			elif self.answer == self.responses[1]:
				self.eraseContents(self.login.newPasswordVerifyInput)
				self.login.newPasswordInput.focus()
			elif self.answer == self.responses[2]:
				self.login.newPasswordVerifyInput.focus()
			elif self.answer == self.responses[5]:
				self.eraseContents(self.login.newPasswordInput, self.login.newPasswordVerifyInput)
				self.login.newPasswordInput.focus()
			else:
				self.eraseContents(self.login.newPasswordVerifyInput)
		else:																																# Otherwise, if create entries are valid, proceed to some formatting, then create the database! YAY!
			self.createButton.flash()
			self.cre.create()
			self.eraseContents(self.login.newUsernameInput, self.login.newPasswordInput, self.login.newPasswordVerifyInput, self.login.usernameInput)
			self.login.usernameInput.focus()
			self.login.verifyLoginLabel.config(text="")
			self.login.verifyCreateLabel.config(text="SUCCESSFUL! YOU CAN NOW\nLOG-IN!", fg="#52A41D")			
			
		
Window = Tk()        		 													# Creates an empty window
Window.wm_title('Welcome to Caffy!')											# Initial title text in the title bar
Main = navClass()
Window.geometry('1000x600+170+80')												# Set dimensions to 1000x600 pos @ screen center
Window.resizable(0,0)			 												# Does not resize the window, ever 	
Window.wm_iconbitmap('GUIE\\CoffeeCup.ico')										# Adds a little mug icon over the top left corner
Window.mainloop()																# Executes code above in a loop

os.remove('CC.pyc')																# Removes the temporary files inside the (" ")
#os.remove('Main.pyc')															# (For Git uploading purposes only)