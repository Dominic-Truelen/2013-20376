from Tkinter import *
from PIL import ImageTk
import Image, shutil, os
from datetime import date

profilePic = 175		#Square profile picture frame
profilePicBgColor = "#CCCCFF"

backgroundColor = "#EEEEEE"

class profilePageGUI(Frame):													# This is the GUI for the Profile Page. Included: Self Statuses, Profile Picture, Information, Friends List, Relationships Lists, etc...
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.place(in_=master)
		self.dp = PhotoImage(file="GUIE/maleDP.gif") # I think proxy should be implemented now...
		self.createWidgets()

	def setProfilePicture(self, databaseFile):
		b = Image.open(databaseFile)
		b.thumbnail((175,175))
		#b = b.resize((profilePic, profilePic))
		self.DP = ImageTk.PhotoImage(b)
		self.labelDP.config(image=self.DP)
		self.labelDP.image = self.dp

	def receiveDatabase(self, database):
		self.username = database.get_name()
		self.password = database.get_password()

		self.setProfilePicture(database.get_DP())

		self.displayNameVariable.set(database.get_display_name())
		
		self.gender.set(database.get_details()[0] + ".")
		age = date.today().year - int(database.get_details()[1][2])
		self.age.set(str(age) + ".")
		self.monthDate.set(database.get_details()[1][0])
		self.dayDate.set(database.get_details()[1][1])
		self.yearDate.set(database.get_details()[1][2])
		self.position.set(database.get_details()[2][0])
		self.company.set(database.get_details()[2][1])
		self.yearsWorked.set(database.get_details()[2][2])
		self.school.set(database.get_details()[3][0])
		self.yearGraduated.set(database.get_details()[3][1])
		self.birthdayDisplay.set("Born on " + self.monthDate.get() + " " + str(self.dayDate.get()) + ", " + str(self.yearDate.get()) + ".")
		if self.position.get() == "":
			self.jobsName.set("")
		else:
			self.jobsName.set("Works at " + self.company.get() + ".")	

	def createWidgets(self):
		profileMainWindow = Frame(self, width=1000, height=550, bg="#eeeeee")	#Profile container
		profileMainWindow.pack()

		homeShadow = Canvas(profileMainWindow, width=1000, height=550, highlightthickness=0, bg=backgroundColor)
		homeShadow.pack()
		shadow = ImageTk.PhotoImage(file="GUIE/activePageShadow.png")
		homeShadow.create_image(500, 275, image=shadow)
		homeShadow.image = shadow

		profilePictureFrame = Frame(profileMainWindow, cursor="hand2", width=profilePic, height=profilePic, bg="#eeeeee") #ProfPic
		profilePictureFrame.place(anchor=CENTER, relx=0.25, rely=0.25)

		changeDPLabelFrame = Frame(profilePictureFrame, width=175, height=20, bg="#111111")
		changeDPLabelFrame.place(anchor=S, relx=0.5, rely=1)	

		changeDPLabel = Label(changeDPLabelFrame, text="Change my DP", bg="#111111", fg="white")
		changeDPLabel.place(anchor=CENTER, relx=0.5, rely=0.5)				

		self.labelDP = Label(profilePictureFrame, width=profilePic, height=profilePic, highlightthickness=0, bg="white")
		self.labelDP.place(anchor=CENTER, relx=0.5, rely=0.5)

		profilePictureFrame.bind("<Enter>", lambda event: changeDPLabelFrame.lift())		
		profilePictureFrame.bind("<Leave>", lambda event: changeDPLabelFrame.lower())

		self.displayNameVariable = StringVar()
		self.age = IntVar()
		self.gender = StringVar()
		self.monthDate = StringVar()
		self.dayDate = IntVar()
		self.yearDate = IntVar()
		self.position = StringVar()
		self.company = StringVar()
		self.yearsWorked = IntVar()
		self.school = StringVar()
		self.yearGraduated = IntVar()

		detailsWindow = Frame(profileMainWindow, bg="#eeeeee")
		detailsWindow.place(anchor=W, relx=0.36, rely=0.105)

		displayName = Label(detailsWindow, font=("Tahoma", 18, "bold"), bg="#eeeeee", textvariable=self.displayNameVariable)
		displayName.grid(row=0, column=0, sticky=W, columnspan=4) #Name

		gender = Label(detailsWindow, font=("Tahoma", 11), bg="#eeeeee", textvariable=self.gender)
		gender.grid(row=1, column=0, sticky=W) #Gender

		age = Label(detailsWindow, font=("Tahoma", 11), bg="#eeeeee", textvariable=self.age)
		age.grid(row=1, column=1, sticky=W, padx=(5, 2))

		self.birthdayDisplay = StringVar()	
		
		Label(detailsWindow, font=("Tahoma", 11), bg="#eeeeee", textvariable=self.birthdayDisplay).grid(row=1, column=2, padx=(3,5), sticky=W)
		
		self.jobsName = StringVar()
		
		Label(detailsWindow, font=("Tahoma", 11), bg="#eeeeee", textvariable=self.jobsName).grid(row=1, column=3, sticky=W)	
		

		wall = LabelFrame(profileMainWindow, text="Wall", width=450, height=400, padx=5, pady=5, bg="#eeeeee")
		wall.place(anchor=NW, relx=0.36, rely=0.2)

		wall = LabelFrame(profileMainWindow, text="Links", width=175, height=268, padx=3, pady=3, bg="#eeeeee")
		wall.place(anchor=NW, relx=0.1625, rely=0.44)