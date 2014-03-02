#!/usr/bin/python																# Allows the use of Non-ASCII characters (password) in app
# -*- coding: utf-8 -*-
 
from CC import *																# pack() is for stacking, while place() is for a more
from Tkinter import *															# accurate placing of widgets. grid() is for tables
from profilePageGUI import profilePageGUI
import os, sys, glob, time, subprocess, tkMessageBox, ctypes


def isPlatform(x):
	if sys.platform.startswith(x):
		return 1
	return 0

try:
	from PIL import ImageTk
except:
	if isPlatform("linux") or isPlatform("mac"):
		Window = Tk()        		 													# Creates an empty window
		Window.withdraw()
		tkMessageBox.showerror("Error", "Please install PIL.")		
	elif isPlatform("win32"):
		ctypes.windll.user32.MessageBoxA(None, "Please install PIL.", "Error", 0)
		
	eval(exit())


defaultEntryStyle = ("Tahoma", 12)												# Initial font settings for styling
defaultLabelStyle = ("Tahoma", 9)
defaultCreateStyle = ("Tahoma", 14)
defaultLogoStyle = ("Verdana", 18)
defaultSetupStyle = ("Segoe UI Light", 16)
signatureColor = "orange"														# Shortcut labels for custom color styling
toplayerColor = "#555555"														# Dark gray signature color
backgroundColor = "#EEEEEE"														# Grayish-white color
greenColor = "#52A41D"


a =- 0.05																		# Adjuster for widget's y-value placement
b = 0.075


def anotherUser():																# Instantiate multiple users
	try:
		subprocess.Popen("GUI_Basic_1.exe")
	except:
		subprocess.Popen("python GUI_Basic_1.py")


class loginPageGUI(Frame):														# The login GUI class Interface!
	def __init__(self, master=None):	
		Frame.__init__(self, master)
		self.login_logout = CC()
		self.createWidgets()
		
	def createWidgets(self):
		self.master.title("Welcome to Caffy!")
		topLayer = Frame(self, height=80, width=1000, bg=toplayerColor)			# Code here for the Log-in classes
		topLayer.pack()		
		Label(topLayer, text="Username", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle).place(anchor=CENTER, relx=0.5379, rely=0.28)	# Labels for the entry fields
		Label(topLayer, text="Password", fg="#FFF", bg=toplayerColor, font=defaultLabelStyle).place(anchor=CENTER, relx=0.7163, rely=0.28)	# Labels for the entry fields	
		self.usernameVariable = StringVar()
		self.usernameInput = Entry(topLayer, highlightthickness=0, fg=toplayerColor, width=17, textvariable=self.usernameVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the username
		self.usernameInput.place(anchor=CENTER,relx=0.59, rely=0.59)
		self.usernameInput.focus()												# Puts the cursor automatically at the user_name field
		
		self.passwordVariable = StringVar()
		self.passwordInput = Entry(topLayer, highlightthickness=0, fg=toplayerColor, width=17, show="•", textvariable=self.passwordVariable, font=defaultEntryStyle, relief=FLAT)	# Entry field for the password
		self.passwordInput.place(anchor=CENTER, relx=0.77, rely=0.59)
		
		Label(topLayer, text="caffy", font=("Verdana", 28), justify=LEFT, bg=toplayerColor, fg=signatureColor).place(anchor=W, relx=0.08, rely=0.5)
		self.coffcup = Label(topLayer, text="☕", font=("Tahoma", 28), justify=LEFT, bg=toplayerColor, fg="#FFFFFF")
		self.coffcup.place(anchor=W, relx=0.175, rely=0.48)
		self.verifyLoginLabel = Label(topLayer, text="", fg=signatureColor, bg=toplayerColor, font=defaultLabelStyle) 	# For warning purposes of login entries
		self.verifyLoginLabel.place(anchor=E, relx=0.5, rely=0.59)
		self.coffcup.bind("<Enter>", lambda f: self.coffcup.config(fg=signatureColor))
		self.coffcup.bind("<Leave>", lambda f: self.coffcup.config(fg="white"))
		
		midLayer = Frame(self, width=1000, height=490)		# Code here for the CREATE class
		midLayer.pack()
		
		loginSky = Canvas(midLayer, width=1000, height=490, highlightthickness=0, bg=backgroundColor)
		loginSky.pack()
		sky = PhotoImage(file="GUIE/LoginSky.gif")
		loginSky.create_image(500, 245, image=sky)
		loginSky.image = sky								#Reference to image so that garbage wont be collected
		
		layer1 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer1.place(anchor=CENTER, relx=0.7, rely=0.3+a)
		layer2 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer2.place(anchor=CENTER, relx=0.7, rely=0.45+a)
		layer3 = Frame(midLayer, width=379, height=40, bg="#FFFFFF")
		layer3.place(anchor=CENTER, relx=0.7, rely=0.6+a)
		self.newUsernameVariable = StringVar()
		self.newUsernameInput = Entry(layer1, highlightthickness=0, fg=toplayerColor, width=35, textvariable=self.newUsernameVariable, font = defaultCreateStyle, relief=FLAT)
		self.newUsernameInput.place(anchor=CENTER, relx=0.5, rely=0.5)		
		self.newPasswordVariable = StringVar()
		self.newPasswordInput = Entry(layer2, highlightthickness=0, fg=toplayerColor, width=35, show="•", textvariable=self.newPasswordVariable, font = defaultCreateStyle, relief=FLAT)
		self.newPasswordInput.place(anchor=CENTER, relx=0.5, rely=0.5)
		self.newPasswordVerifyVariable = StringVar()
		self.newPasswordVerifyInput = Entry(layer3, highlightthickness=0, fg=toplayerColor, width=35, show="•", textvariable=self.newPasswordVerifyVariable, font = defaultCreateStyle, relief=FLAT)
		self.newPasswordVerifyInput.place(anchor=CENTER, relx=0.5, rely=0.5)
		Label(midLayer, text="Pick a username:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.23+a)
		Label(midLayer, text="Create a password:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.38+a)
		Label(midLayer, text="Reenter your password:", bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.508, rely=0.53+a)
		Label(midLayer, text="Take a    break!\nSign up!", font=("Tahoma", 35), justify=LEFT, bg=backgroundColor, fg="#222222").place(anchor=W, relx=0.08, rely=0.345+a)
		self.coffcup2 = Label(midLayer, text="☕", font=("Tahoma", 35), justify=LEFT, bg=backgroundColor, fg="#222222")
		self.coffcup2.place(anchor=W, relx=0.23, rely=0.28+a)
		self.coffcup2.bind("<Enter>", lambda f: self.coffcup2.config(fg=signatureColor))
		self.coffcup2.bind("<Leave>", lambda f: self.coffcup2.config(fg="#222222"))
		Label(midLayer, text="Caffy lets you connect and share with\nfriends from around the corner.", font=("Tahoma", 15), justify=LEFT, bg=backgroundColor, fg=toplayerColor).place(anchor=W, relx=0.08, rely=0.58+a)
		Label(midLayer, text="By signing up, you agree with our Terms and Conditions.", font=("Tahoma", 9), justify=RIGHT, bg=backgroundColor, fg="#999999").place(anchor=E, relx=0.8956, rely=0.7+a)
		self.verifyCreateLabel = Label(midLayer, text="", bg=backgroundColor, justify=LEFT)		# Initialization of the create warnings
		self.verifyCreateLabel.place(anchor=W, relx=0.509, rely=0.75)		
		
		bottomLayer = Frame(self, width=1000, height=30, bg=toplayerColor)		# Code here for the extra details
		bottomLayer.pack()
		Label(bottomLayer, text="Thank you for choosing Caffy™ | Copyright © 2014. All rights are reserved", fg="#FFFFFF", bg=toplayerColor, font=("Tahoma", 8)).place(anchor=CENTER, relx=0.5, rely=0.45)

	def reset(self, x, y):
		if tkMessageBox.askyesno("Logging-out", "Are you sure you want to log-out?"):
			if y.notifWindow.getWindowVisibility() == 1:
				y.notifWindow.lower()
				y.notifWindow.setWindowVisibility(0)
				y.topLayerObject.brewingNotifButton.config(image=y.topLayerObject.brewingNotifImage)
				y.topLayerObject.msgNotifButton.config(image=y.topLayerObject.msgNotifImage)			
				y.topLayerObject.friendNotifButton.config(image=y.topLayerObject.friendNotifImage)
				
			self.usernameInput.delete(0, END)									# Delete any text from login
			self.passwordInput.delete(0, END)
			self.usernameInput.focus()
			self.master.title("Welcome to Caffy!")			
			self.login_logout.logout()											# Puts user "offline"
			x.lift()															# Lifts the original login page (passed as argument)
			y.profilepageLift()													# Reset original starting page to profile page
		else:
			return


class notifSystemGUI(Frame):													# The TOPLAYER GUI. Included here are mainly the Notifications bar, along with the Logout / Profile / Home Navigation Buttons
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		notifLayer = Frame(self, width=1000, height=50, bg=toplayerColor)
		notifLayer.pack(anchor=NW)

		Label(notifLayer, text="caffy", font=defaultLogoStyle, bg=toplayerColor, fg=signatureColor).place(anchor=CENTER, relx=0.2, rely=0.5)
		self.coff = Label(notifLayer, text="☕", font=defaultLogoStyle, bg=toplayerColor, fg="#FFFFFF")
		self.coff.place(anchor=CENTER, relx=0.245, rely=0.48)
		self.coff.bind("<Enter>", lambda f: self.coff.config(fg=signatureColor))
		self.coff.bind("<Leave>", lambda f: self.coff.config(fg="white"))

		self.brewingNotifImage = PhotoImage(file="GUIE/brewingNotif.gif")
		self.brewingNotifImageRed = PhotoImage(file="GUIE/brewingNotifRed.gif")
		self.brewingNotifButton = Button(notifLayer, bg=toplayerColor, relief=FLAT, image=self.brewingNotifImage)
		self.brewingNotifButton.place(anchor=CENTER, relx=0.6+b, rely=0.5)
		self.brewingNotifButton.image = self.brewingNotifImage

		self.msgNotifImage = PhotoImage(file="GUIE/msgNotif.gif")
		self.msgNotifImageRed = PhotoImage(file="GUIE/msgNotifRed.gif")
		self.msgNotifButton = Button(notifLayer, bg=toplayerColor, relief=FLAT, image=self.msgNotifImage)
		self.msgNotifButton.place(anchor=CENTER, relx=0.56+b, rely=0.5)
		self.msgNotifButton.image = self.msgNotifImage

		self.friendNotifImage = PhotoImage(file="GUIE/friendNotif.gif")
		self.friendNotifImageRed = PhotoImage(file="GUIE/friendNotifRed.gif")
		self.friendNotifButton = Button(notifLayer, bg=toplayerColor, relief=FLAT, image=self.friendNotifImage)
		self.friendNotifButton.place(anchor=CENTER, relx=0.52+b, rely=0.5)
		self.friendNotifButton.image = self.friendNotifImage

		self.profilepageButton = Button(notifLayer, text="☺ Profile", width=7, font=("Tahoma", 10, "bold"), relief=FLAT, fg="#FFFFFF", bg=toplayerColor)
		self.profilepageButton.place(anchor=CENTER, relx=0.6875+b, rely=0.5)

		self.homepageButton = Button(notifLayer, text="⌂ Home", width=7, font=("Tahoma", 10, "bold"), relief=FLAT, fg="#FFFFFF", bg=toplayerColor)
		self.homepageButton.place(anchor=CENTER, relx=0.76+b, rely=0.5)

		
class homePageGUI(Frame):														# This is the GUI for the Newsfeed sections
	def __init__(self, master=None, database=None):
		Frame.__init__(self, master)
		self.place(in_=master)
		self.createWidgets(database)

	def receiveDatabase(self, database):
		self.homePageDisplayNameVariable.set(database.get_first_name())
	
	def createWidgets(self, database):
		homepageMainWindow = Frame(self, width=1000, height=550)
		homepageMainWindow.pack()

		homeShadow = Canvas(homepageMainWindow, width=1000, height=550, highlightthickness=0, bg=backgroundColor)
		homeShadow.pack()
		shadow = PhotoImage(file="GUIE/activePageShadow.gif")
		homeShadow.create_image(500, 275, image=shadow)
		homeShadow.image = shadow

		wall = Frame(homepageMainWindow, width=700, height=500, bg="#eeeeee", highlightthickness=1, highlightbackground="#AAAAAA")
		wall.place(anchor=CENTER, relx=0.63, rely=0.5)

		smallDP = Frame(homepageMainWindow, width=75, height=75, bg="#555555")
		smallDP.place(anchor=N, relx=0.06, rely=0.04)

		self.homePageDisplayNameVariable = StringVar()
		self.homePageDisplayNameVariable.set("")

		self.homePageDisplayName = Label(homepageMainWindow, textvariable=self.homePageDisplayNameVariable, font=("Tahoma", 13), bg="#eeeeee")
		self.homePageDisplayName.place(anchor=NW, relx=0.11, rely=0.025)


class notificationWindow(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.enabled = 0				

		bgimage = PhotoImage(file="GUIE/notifWindowBG2.gif")
		notifCanvas = Canvas(self, width=400, height=300, highlightthickness=0, bg="#eeeeee")
		notifCanvas.pack()		
		notifCanvas.create_image(200, 150, image=bgimage)
		notifCanvas.image = bgimage

		container = Frame(self, width=381, height=282, highlightthickness=0, bg="white")
		container.place(anchor=CENTER, relx=0.5, rely=0.5)

		self.notifTitleVar = StringVar()

		self.notifTitle = Label(container, textvariable = self.notifTitleVar, bg="white", font=("Tahoma", 16))
		self.notifTitle.place(anchor=NW)

	def setWindowVisibility(self, onoroff):
		self.enabled = onoroff

	def getWindowVisibility(self):
		return self.enabled

	def setState(self, state, notifSystem):
		if state == "brewing":
			self.notifTitleVar.set("What's brewing for today?")
			notifSystem.brewingNotifButton.config(image=notifSystem.brewingNotifImageRed)

		elif state == "msg":
			self.notifTitleVar.set("My messages")
			notifSystem.msgNotifButton.config(image=notifSystem.msgNotifImageRed)
		else:		# state == "friends"
			self.notifTitleVar.set("Wanna-be friends")
			notifSystem.friendNotifButton.config(image=notifSystem.friendNotifImageRed)


class setupPageGUI(Frame, CC):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		CC.__init__(self)
		self.createWidgets()

	def get_birthday(self):
		return list([self.monthvar.get(), self.dayvar.get(), self.yearvar.get()])

	def get_job(self):
		return list([self.position.get(), self.company.get(), self.workyears.get()])

	def get_educ(self):
		return list([self.school.get(), self.graduateyear.get()])

	def export_setup_data(self):
		self.exporter.export_details(self.get_name(), self.get_password(), firstname=self.FirstNameVariable.get(), lastname=self.LastNameVariable.get(), gender=self.genderradio.get(), birthday=self.get_birthday(),  jobs=self.get_job(), education=self.get_educ())
		self.set_OnOrOff("Offline")

	def createWidgets(self):
		temp = Frame(self, width=1000, height=600, bg=backgroundColor)
		temp.pack()

		topLayer = Frame(temp, width=1000, height=80, bg=toplayerColor)		# Code here for the extra details
		topLayer.place(anchor=N, relx=0.5, rely=0)
		Label(topLayer, text="Setup your account", font=("Segoe UI Light", 28), bg=toplayerColor, fg="#FFFFFF").place(anchor=CENTER, relx=0.5, rely=0.45)

		setupSky = Canvas(temp, width=1000, height=490, highlightthickness=0, bg=backgroundColor)
		setupSky.place(anchor=CENTER, relx=0.5, rely=0.541)
		sky = PhotoImage(file="GUIE/SetupSky.gif")
		setupSky.create_image(500, 245, image=sky)
		setupSky.image = sky 
		
		Label(temp, text="Display Name: ", font = defaultSetupStyle, bg=backgroundColor).place(anchor=E, relx=0.3, rely=0.3)
		Label(temp, text="Birthday: ", font = defaultSetupStyle, bg=backgroundColor).place(anchor=E, relx=0.3, rely=0.4)
		Label(temp, text="Sex: ", font = defaultSetupStyle, bg=backgroundColor).place(anchor=E, relx=0.3, rely=0.5)		
		Label(temp, text="Education: ", font = defaultSetupStyle, bg=backgroundColor).place(anchor=E, relx=0.3, rely=0.7)
		Label(temp, text="Jobs: ", font = defaultSetupStyle, bg=backgroundColor).place(anchor=E, relx=0.3, rely=0.6)

		self.FirstNameVariable = StringVar()
		self.LastNameVariable = StringVar()
		layer1 = Frame(temp, width=550, height=40, bg="#FFFFFF")
		layer1.place(anchor=W, relx=0.33, rely=0.3)
		firstNameDisplayInput = Entry(layer1, highlightthickness=1, fg=toplayerColor, width=25, textvariable=self.FirstNameVariable, font = defaultCreateStyle, relief=FLAT)
		firstNameDisplayInput.grid(row=0, column=0, padx=(10, 5), pady=5)
		lastNameDisplayInput = Entry(layer1, highlightthickness=1, fg=toplayerColor, width=25, textvariable=self.LastNameVariable, font = defaultCreateStyle, relief=FLAT)
		lastNameDisplayInput.grid(row=0, column=1, padx=(5, 10), pady=5)

		
		months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
		days31 = ["Day"] + range(1,32)		
		years = ["Year"] + range(int(time.strftime("%Y")), 1949, -1)

		self.monthvar = StringVar()
		self.dayvar = StringVar()
		self.yearvar = StringVar()
		self.monthvar.set("Month")
		self.dayvar.set("Day")
		self.yearvar.set("Year")

		layer2 = Frame(temp, width=550, height=40, bg=backgroundColor)
		layer2.place(anchor=W, relx=0.33, rely=0.4)

		OptionMenu(layer2, self.yearvar, *years).grid(row=0, column=1)
		OptionMenu(layer2, self.monthvar, *months).grid(row=0, column=2, padx=6)
		OptionMenu(layer2, self.dayvar, *days31).grid(row=0, column=3)	

		
		self.genderradio = StringVar()		
		male = Radiobutton(temp, text="Male", variable=self.genderradio, value="Male", font=defaultCreateStyle, bg=backgroundColor)
		male.place(anchor=W, relx=0.33, rely=0.5)
		male.select()
		female = Radiobutton(temp, text="Female", variable=self.genderradio, value="Female", font=defaultCreateStyle, bg=backgroundColor)
		female.place(anchor=W, relx=0.43, rely=0.5)
		female.deselect()


		self.jobsCheckboxVariable = IntVar()
		includeJobsCheckbox = Checkbutton(temp, text="Include", bg=backgroundColor, variable=self.jobsCheckboxVariable, command=lambda: self.CheckboxState(self.jobsCheckboxVariable, entrya, entryb, entryc, label1, label2, label3))
		includeJobsCheckbox.place(anchor=W, relx=0.33, rely=0.6)

		self.position = StringVar()
		self.company = StringVar()
		self.workyears = StringVar() 	#NB: Could be IntVar()				
		label1 = Label(temp, text="Work:", bg=backgroundColor, state=DISABLED)
		label1.place(anchor=W, relx=0.417, rely=0.555)
		label2 = Label(temp, text="at the company:", bg=backgroundColor, state=DISABLED)
		label2.place(anchor=W, relx=0.58, rely=0.555)
		label3 = Label(temp, text="for __ years:", bg=backgroundColor, state=DISABLED)
		label3.place(anchor=W, relx=0.782, rely=0.555)
		entrya = Entry(temp, width=14, relief=FLAT, textvariable = self.position, font=defaultCreateStyle, fg=toplayerColor, state=DISABLED)
		entrya.place(anchor=W, relx=0.42, rely=0.6)
		entryb = Entry(temp, width=18, relief=FLAT, textvariable = self.company, font=defaultCreateStyle, fg=toplayerColor, state=DISABLED)
		entryb.place(anchor=W, relx=0.5825, rely=0.6)
		entryc = Entry(temp, width=9, relief=FLAT, textvariable = self.workyears, font=defaultCreateStyle, fg=toplayerColor, state=DISABLED)
		entryc.place(anchor=W, relx=0.785, rely=0.6)

		self.school = StringVar()
		self.graduateyear = StringVar()
		self.educCheckboxVariable = IntVar()
		includeEducCheckbox = Checkbutton(temp, text="Include", bg=backgroundColor, variable=self.educCheckboxVariable, command=lambda: self.CheckboxState(self.educCheckboxVariable, entry1, entry2, labela, labelb))
		includeEducCheckbox.place(anchor=W, relx=0.33, rely=0.7)
		labela = Label(temp, text="School:", bg=backgroundColor, state=DISABLED)
		labela.place(anchor=W, relx=0.417, rely=0.655)
		labelb = Label(temp, text="Year graduated:", bg=backgroundColor, state=DISABLED)
		labelb.place(anchor=W, relx=0.775, rely=0.655)		
		entry1 = Entry(temp, width=34, relief=FLAT, textvariable = self.school, font=defaultCreateStyle, fg=toplayerColor, state=DISABLED)
		entry1.place(anchor=W, relx=0.42, rely=0.7)
		entry2 = Entry(temp, width=9, relief=FLAT, textvariable = self.graduateyear, font=defaultCreateStyle, fg=toplayerColor, state=DISABLED)
		entry2.place(anchor=W, relx=0.78, rely=0.7)

		self.verifySetupLabel = Label(temp, text="", bg=backgroundColor, fg="red", font=("Tahoma", 9, "bold"), justify=LEFT)
		self.verifySetupLabel.place(anchor=W, relx=0.6, rely=0.85)		

		bottomLayer = Frame(temp, width=1000, height=30, bg=toplayerColor)		# Code here for the extra details
		bottomLayer.place(anchor=S, relx=0.5, rely=1)

	def CheckboxState(self, var, *widgets):
		if var.get() == 0:
			for x in widgets:
				x.config(state=DISABLED)
		else:
			for x in widgets:
				x.config(state=NORMAL)	

	def reset(self, x):
		if tkMessageBox.askyesno("Quitting Setup", "Are you sure you want to quit setup?"):			
			self.master.title("Welcome to Caffy!")
			x.login_logout.set_name("")
			x.login_logout.set_password("")
			self.set_name("")
			self.set_password("")
			x.usernameInput.delete(0, END)
			x.passwordInput.delete(0, END)
			x.usernameInput.focus()			
			x.lift()															# Lifts the original login page (passed as argument)
		else:
			return


class Singleton:																# Singleton Design Pattern retrieved from
    __single = None																# Python Help Manual Website: http://www.python.org/workshops/1997-10/proceedings/savikko.html
    def __init__(self):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self  
		

class activePageGUI(Frame, Singleton):											# This is basically a SINGLETON class or maybe a FACADE for containing all the active sessions of a user... Included: Profile Page, Newspage, and everything else while logged in.
	def __init__(self, master=None):
		Frame.__init__(self, master)
		Singleton.__init__(self)

		self.topLayerObject = notifSystemGUI(self)
		self.notifWindow = notificationWindow(self)
		self.notifWindow.place(anchor=N, relx=0.785, rely=0.11)

		container2 = Frame(self, width=1000, height=550)
		container2.pack()

		self.profilePageObject = profilePageGUI(container2)		
		self.homePageObject = homePageGUI(container2)
				
		self.createWidgets()
		self.homepageLift()

	def turnNotifWindowOnOrOff(self, state, notifSystem):
		if self.notifWindow.getWindowVisibility() == 0:
			self.notifWindow.setState(state, notifSystem)
			self.notifWindow.lift()
			self.notifWindow.setWindowVisibility(1)
		else:
			self.notifWindow.lower()
			notifSystem.brewingNotifButton.config(image=notifSystem.brewingNotifImage)
			notifSystem.msgNotifButton.config(image=notifSystem.msgNotifImage)
			notifSystem.friendNotifButton.config(image=notifSystem.friendNotifImage)
			self.notifWindow.setWindowVisibility(0)
	
	def setDatabase(self, database):		
		self.profilePageObject.receiveDatabase(database)
		self.homePageObject.receiveDatabase(database)
			
	def createWidgets(self):
		self.topLayerObject.profilepageButton.config(command=self.profilePageObject.lift)
		self.topLayerObject.homepageButton.config(command=self.homePageObject.lift)

		self.topLayerObject.brewingNotifButton.config(command=lambda: self.turnNotifWindowOnOrOff("brewing", self.topLayerObject))
		self.topLayerObject.msgNotifButton.config(command=lambda: self.turnNotifWindowOnOrOff("msg", self.topLayerObject))
		self.topLayerObject.friendNotifButton.config(command=lambda: self.turnNotifWindowOnOrOff("friend", self.topLayerObject))	
		

	def homepageLift(self):
		self.homePageObject.lift()

	def profilepageLift(self):
		self.profilePageObject.lift()	


class navClass(Frame):															# A GUI that combines the Login and Active Windows. Basically another Faҫade design pattern. Called navClass because of navigation (button fxns)
	def __init__(self, master=None):
		Frame.__init__(self, master)
		
		self.val = validation()													# Initial functions for the verifications
		self.loginCC = CC()
		self.cre = creation()
		self.master = master

		self.usernameVerifyObject = usernameVerify()							#Chain of Responsibility
		self.passwordVerifyObject = passwordVerify()
		self.val.handler(self.usernameVerifyObject)
		self.usernameVerifyObject.handler(self.passwordVerifyObject)

		container = Frame(self, width=1000, height=600)							# Frame for all the to-be-children pages
		container.pack()	

		self.activePageObject = activePageGUI()
		self.activePageObject.place(in_=container)

		self.setupPageObject = setupPageGUI()
		self.setupPageObject.place(in_=container)

		self.loginPageObject = loginPageGUI()
		self.loginPageObject.place(in_=container)
		self.loginPageObject.lift()												# Displays first ever page, which is the login page	

		self.pack()
		self.createWidgets()
		
	def createWidgets(self):			
		
		self.loginButton = Button(self.loginPageObject, highlightthickness=0, text="Log In", width=7, height=1, font=("Tahoma", 9, "bold"), relief=FLAT, fg="#FFFFFF", bg=signatureColor, command=self.verifyLogin)
		self.loginButton.place(anchor=CENTER, relx=0.904, rely=0.0786)			# Button of the LoginPage (click to verify entries)
		
		self.loginPageObject.usernameInput.bind("<Return>", lambda event: self.loginButton.invoke())	#Allows the use of the Enter key when loggin in
		self.loginPageObject.passwordInput.bind("<Return>", lambda event: self.loginButton.invoke())

		newCaffyButton = PhotoImage(file="GUIE/switchButton.gif")
		self.anotherUserButton = Button(self.loginPageObject, highlightthickness=0, image=newCaffyButton, relief=FLAT, bg=toplayerColor, command=anotherUser)
		self.anotherUserButton.place(anchor=CENTER, relx=0.04, rely=0.07)
		self.anotherUserButton.image = newCaffyButton
		
		self.createButton = Button(self.loginPageObject, text="Sign Me Up!", width=12, font=("Tahoma", 13, "bold"), relief=FLAT, fg="#FFFFFF", bg=greenColor, command=self.verifyCreate)
		self.createButton.place(anchor=CENTER, relx=0.82, rely=0.75)
		
		self.loginPageObject.newUsernameInput.bind("<Return>", lambda event: self.createButton.invoke())	#Allows the use of the Enter key when creating accounts
		self.loginPageObject.newPasswordInput.bind("<Return>", lambda event: self.createButton.invoke())
		self.loginPageObject.newPasswordVerifyInput.bind("<Return>", lambda event: self.createButton.invoke())

		self.logoutButton = Button(self.activePageObject, text="Log Out", width=6, height=1, font=("Tahoma", 10, "bold"), relief=FLAT, fg="#FFFFFF", bg=toplayerColor, command=lambda: self.loginPageObject.reset(self.loginPageObject, self.activePageObject))
		self.logoutButton.place(anchor=CENTER, relx=0.83+b, rely=0.042)

		self.master.protocol("WM_DELETE_WINDOW", self.exit)

		self.setupBackButton = Button(self.setupPageObject, text="Back", width=6, height=1, font=("Tahoma", 16, "bold"), relief=FLAT, fg="white", bg=toplayerColor, command=lambda: self.setupPageObject.reset(self.loginPageObject))
		self.setupBackButton.place(anchor=CENTER, relx=0.1, rely=0.069)

		self.setupSubmitButton = Button(self.setupPageObject, text="I'm Ready", font=("Tahoma", 16, "bold"), fg="#FFFFFF", bg=greenColor, relief=FLAT, command=self.verifySetup)
		self.setupSubmitButton.place(anchor=CENTER, relx=0.81, rely=0.85)
			
	def exit(self):
		if self.loginPageObject.login_logout.get_name() != "":					# If log in is occupied
			if self.setupPageObject.get_name() != "":							# and if setup page is occupied
				self.setupPageObject.reset(self.loginPageObject)				# whenever x button is pressed, display the exit setup message
				return
			self.loginPageObject.reset(self.loginPageObject, self.activePageObject)		#Otherwise when setup is skipped, display the logout message (there's a big difference)
		else:
			if tkMessageBox.askyesno("Exiting", "You are leaving caffy. Continue?"):	#Otherwise if user is logged-out, when x button is pressed, show the exit application message
				self.master.destroy()											# Function to destroy the whole application
		return 

	def eraseContents(self, *args):												# Function allows unlimited number of arguments by the *args keyword
		for x in args:															# The *args is a tuple, so every element in it must be iterated
			x.delete(0, END)													# to delete the value of all the 3 Create Entries
	
	def verifyLogin(self):

		def waitLabel():																# For removing the WARNING messages after 1.5 second
			self.loginPageObject.verifyLoginLabel.config(text="")														# Method executed whenever "Log In" button is pressed
		
		responses=["USERNAME IS BLANK", "PASSWORD IS BLANK", "ACCOUNT DOES NOT EXIST", "INVALID PASSWORD"]

		self.loginCC.set_name(self.loginPageObject.usernameVariable.get())
		self.loginCC.set_password(self.loginPageObject.passwordVariable.get())

		answer = self.val.guiv(self.loginCC.get_name(), self.loginCC.get_password())
		
		if answer in responses:											# If return value from imported class CC is inside the list,		
			self.loginPageObject.verifyLoginLabel.config(text=answer)				# display the possible warnings and perform some formatting actions like clear the entry field:
			self.loginPageObject.verifyLoginLabel.after(2000, waitLabel)
			if answer == responses[0]:
				self.eraseContents(self.loginPageObject.passwordInput)
				self.loginPageObject.usernameInput.focus()
			elif answer == responses[1]:
				self.loginPageObject.passwordInput.focus()
			elif answer == responses[2]:
				self.eraseContents(self.loginPageObject.usernameInput, self.loginPageObject.passwordInput)
				self.loginPageObject.usernameInput.focus()
			elif answer == responses[3]:
				self.eraseContents(self.loginPageObject.passwordInput)
				self.loginPageObject.passwordInput.focus()			
		
		elif answer == "SETUP":
			self.setupPageObject.lift()														# CODE HERE SO THAT OUT OF NOWHERE REGISTERED LINES (FROM TESTFILE) MAY HAVE THEIR OWN INDIVIDUAL DATABASES AT LAST. ALSO,
			#Code here to input registry info into setup page (USE CREATION.CREATE() BUT MIND THE REGISTRY.REGISTER())		# NOTE TO CODE: DATABASE WOULD NO LONGER HAVE "OFFLINE SETUP" AS ONOROFF STATUS. INSTEAD, GO DIRECTLY TO OFFLINE.

		else:	#answer == 1
			self.loginButton.flash()
			self.loginPageObject.login_logout.set_name(self.loginCC.get_name())
			self.loginPageObject.login_logout.set_password(self.loginCC.get_password())

			a = self.loginPageObject.login_logout.login()
			if a == "SETUPCREATED":															# IF SETUPCREATED (Meaning account is newly created), show the setup window
				self.setupPageObject.lift()
				self.setupPageObject.set_name(self.loginCC.get_name())
				self.setupPageObject.set_password(self.loginCC.get_password())				
			elif a == "OLREADY":
				self.loginPageObject.login_logout.set_name("")
				self.loginPageObject.login_logout.set_password("")
				self.loginPageObject.verifyLoginLabel.config(text="ALREADY LOGGED IN")				# display the possible warnings and perform some formatting actions like clear the entry field:
				self.loginPageObject.verifyLoginLabel.after(2000, waitLabel)
			else: 	#If database is set, go normal log in
				self.activePageObject.setDatabase(a)
				self.activePageObject.lift()												# otherwise, if entries are correct, execute & display the home page
				self.master.title("%s is logged in!" % (self.loginPageObject.login_logout.get_name()))

	def verifyCreate(self):	
		
		def waitLabel():																# For removing the WARNING messages after 1.5 second
			self.loginPageObject.verifyCreateLabel.config(text="")

		responses = ["USERNAME IS BLANK", "PASSWORD REQUIRED", "PLEASE RETYPE THE PASSWORD", "USERNAME IS ALREADY TAKEN", "RETYPE YOUR PASSWORD\nCORRECTLY", "PASSWORD MUST HAVE AT LEAST\n6 CHARACTERS", "MUST NOT CONTAIN\nSPECIAL CHARACTERS"]
		
		self.cre.set_name(self.loginPageObject.newUsernameVariable.get())
		self.cre.set_password(self.loginPageObject.newPasswordVariable.get())
		self.cre.set_password_retyped(self.loginPageObject.newPasswordVerifyVariable.get())

		answer = self.cre.validate(self.cre.get_name(), self.cre.get_password(), self.cre.get_password_retyped())		# Assign the return value of this very long function into variable answer! (actually, answer)
		if answer in responses:																									# If the answer is included in the list above,
			self.loginPageObject.verifyCreateLabel.config(text=answer, fg="red", font=("Tahoma", 9, "bold"))
			self.loginPageObject.verifyCreateLabel.after(2000, waitLabel)
			if answer == responses[0] or answer == responses[3] or answer == responses[6]:											# Display that message from the list, then format some widgets
				self.eraseContents(self.loginPageObject.newUsernameInput, self.loginPageObject.newPasswordInput, self.loginPageObject.newPasswordVerifyInput)
				self.loginPageObject.newUsernameInput.focus()
			elif answer == responses[1]:
				self.eraseContents(self.loginPageObject.newPasswordVerifyInput)
				self.loginPageObject.newPasswordInput.focus()
			elif answer == responses[2]:
				self.loginPageObject.newPasswordVerifyInput.focus()
			elif answer == responses[5]:
				self.eraseContents(self.loginPageObject.newPasswordInput, self.loginPageObject.newPasswordVerifyInput)
				self.loginPageObject.newPasswordInput.focus()
			else:
				self.eraseContents(self.loginPageObject.newPasswordVerifyInput)
		else:																																# Otherwise, if create entries are valid, proceed to some formatting, then create the database! YAY!
			self.createButton.flash()
			self.cre.create()
			self.eraseContents(self.loginPageObject.newUsernameInput, self.loginPageObject.newPasswordInput, self.loginPageObject.newPasswordVerifyInput, self.loginPageObject.usernameInput)
			self.loginPageObject.usernameInput.focus()
			self.loginPageObject.verifyLoginLabel.config(text="")
			self.loginPageObject.verifyCreateLabel.config(text="SUCCESSFUL! YOU CAN NOW\nLOG-IN!", fg="#52A41D", font=("Tahoma", 9, "bold"))
			self.loginPageObject.verifyCreateLabel.after(2000, waitLabel)		# An event delayer for changing the label of SUCCESSFUL CREATIONS

	def verifySetup(self):

		def waitLabel():																# For removing the WARNING messages after 1.5 second
			self.setupPageObject.verifySetupLabel.config(text="")		

		t = self.setupPageObject
		responses = ["DISPLAY NAME IS\nBLANK", "MUST NOT CONTAIN\nSPECIAL CHARACTERS", "DATE INCOMPLETE", "INVALID DATE", "JOB INFORMATION\nINCOMPLETE", "EDUCATION INFORMATION\nINCOMPLETE"]
		answer = self.val.guis(t.FirstNameVariable.get(), t.LastNameVariable.get(), t.monthvar.get(), t.dayvar.get(), t.yearvar.get(), t.genderradio.get(), t.jobsCheckboxVariable.get(), t.position.get(), t.company.get(), t.workyears.get(), t.educCheckboxVariable.get(), t.school.get(), t.graduateyear.get())

		if answer in responses:																												# If the answer is included in the list above,
			self.setupPageObject.verifySetupLabel.config(text=answer)
			self.setupPageObject.verifySetupLabel.after(2000, waitLabel)						
		
		else:						
			self.setupPageObject.export_setup_data()							#Export the data from setup into newly created database
			b = self.setupPageObject.login()									#Log-in and assign the returned importer database to b
			self.activePageObject.setDatabase(b)								#Database information will be passed to activepage
			self.setupPageObject.set_name("")									#Clears the setup garbage
			self.setupPageObject.set_password("")
			self.activePageObject.lift()										# otherwise, if entries are correct, execute & display the home page
			self.master.title("Congratulations and Welcome!")


Window = Tk()        		 													# Creates an empty window
Main = navClass(Window)
Window.geometry('1000x600+170+80')												# Set dimensions to 1000x600 pos @ screen center
Window.resizable(0,0)			 												# Does not resize the window, ever 	
if isPlatform("win32"):
	Window.wm_iconbitmap('GUIE/CoffeeCup.ico')									# Adds a little mug icon over the top left corner
Window.mainloop()																# Executes code above in a loop
