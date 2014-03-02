from Tkinter import *
from PIL import ImageTk

profilePic = 175		#Square profile picture frame
profilePicBgColor = "#CCCCFF"

backgroundColor = "#EEEEEE"

class profilePageGUI(Frame):													# This is the GUI for the Profile Page. Included: Self Statuses, Profile Picture, Information, Friends List, Relationships Lists, etc...
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.place(in_=master)
		self.dp = PhotoImage(file="GUIE/maleDP.gif") # I think proxy should be implemented now...
		self.createWidgets()		

	def receiveDatabase(self, database):
		self.displayNameVariable.set(database.get_display_name())
		self.DP = PhotoImage(file=database.get_DP())
		self.labelDP.config(image=self.DP)		

	def createWidgets(self):
		profileMainWindow = Frame(self, width=1000, height=550, bg="#eeeeee")	#Profile container
		profileMainWindow.pack()

		homeShadow = Canvas(profileMainWindow, width=1000, height=550, highlightthickness=0, bg=backgroundColor)
		homeShadow.pack()
		shadow = ImageTk.PhotoImage(file="GUIE/activePageShadow.png")
		homeShadow.create_image(500, 275, image=shadow)
		homeShadow.image = shadow

		profilePicture = Frame(profileMainWindow, width=profilePic, height=profilePic, bg="#eeeeee") #ProfPic
		profilePicture.place(anchor=CENTER, relx=0.25, rely=0.25)

		self.labelDP = Label(profilePicture, width=profilePic, height=profilePic, highlightthickness=0, bg="#eeeeee", image=self.dp)
		self.labelDP.pack()		
		self.labelDP.image = self.dp

		self.displayNameVariable = StringVar()

		self.displayName = Label(profileMainWindow, font=("Tahoma", 18, "bold"), bg="#eeeeee", textvariable=self.displayNameVariable)
		self.displayName.place(anchor=W, relx=0.36, rely=0.105) #Name
		
		#Label(profileMainWindow, text="WELCOME TO PROFILE PAGE!", font=("Tahoma", 30, "bold"), fg="#000000", bg=bag).place(anchor=CENTER, relx=0.5, rely=0.5)

		wall = LabelFrame(profileMainWindow, text="Wall", width=450, height=400, padx=5, pady=5, bg="#eeeeee")
		wall.place(anchor=NW, relx=0.36, rely=0.2)

		wall = LabelFrame(profileMainWindow, text="Links", width=175, height=268, padx=3, pady=3, bg="#eeeeee")
		wall.place(anchor=NW, relx=0.1625, rely=0.44)