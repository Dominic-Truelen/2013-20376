from Tkinter import *
import shutil, os
from datetime import date

try:
	from PIL import ImageTk, Image

except ImportError:
	raise ImportError

profilePic = 175		#Square profile picture frame
profilePicBgColor = "#CCCCFF"

backgroundColor = "#EEEEEE"

class profilePageGUI(Frame):													# This is the GUI for the Profile Page. Included: Self Statuses, Profile Picture, Information, Friends List, Relationships Lists, etc...
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.place(in_=master)
		self.createWidgets()

	def setProfilePicture(self, databaseFile):
		b = Image.open(databaseFile)
		b.thumbnail((175,175))		
		self.DP = ImageTk.PhotoImage(b)
		self.labelDP.config(image=self.DP)
		self.labelDP.image = self.DP

	def receiveDatabase(self, database):		
		self.importer = database
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
		
		if self.school.get() == "":
			self.schoolDisplay.set("")
		else:
			self.schoolDisplay.set("Goes to " + self.school.get() + ".")
					
		if len(database.get_friends()) == 1:
			self.friendsNumber.set(str(len(database.get_friends())) + " friend. =(")
		else:
			self.friendsNumber.set(str(len(database.get_friends())) + " friends.")	

	def createWidgets(self):
		profileMainWindow = Frame(self, width=1000, height=550, bg=backgroundColor)	#Profile container
		profileMainWindow.pack()

		homeShadow = Canvas(profileMainWindow, width=1000, height=550, highlightthickness=0, bg=backgroundColor)
		homeShadow.pack()
		shadow = ImageTk.PhotoImage(file="GUIE/activePageShadow.png")
		homeShadow.create_image(500, 275, image=shadow)
		homeShadow.image = shadow

		profilePictureFrame = Frame(profileMainWindow, cursor="hand2", width=profilePic, height=profilePic, bg=backgroundColor) #ProfPic
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

		detailsWindow = Frame(profileMainWindow, bg=backgroundColor)
		detailsWindow.place(anchor=W, relx=0.36, rely=0.105)

		displayName = Label(detailsWindow, font=("Tahoma", 18, "bold"), bg=backgroundColor, textvariable=self.displayNameVariable)
		displayName.grid(row=0, column=0, sticky=W, columnspan=4) #Name

		gender = Label(detailsWindow, font=("Tahoma", 11), bg=backgroundColor, textvariable=self.gender)
		gender.grid(row=1, column=0, sticky=W) #Gender

		age = Label(detailsWindow, font=("Tahoma", 11), bg=backgroundColor, textvariable=self.age)
		age.grid(row=1, column=1, sticky=W, padx=(5, 2))

		self.birthdayDisplay = StringVar()	
		
		Label(detailsWindow, font=("Tahoma", 11), bg=backgroundColor, textvariable=self.birthdayDisplay).grid(row=1, column=2, padx=(3,5), sticky=W)
		
		self.jobsName = StringVar()
		
		Label(detailsWindow, font=("Tahoma", 11), bg=backgroundColor, textvariable=self.jobsName).grid(row=1, column=3, sticky=W)	
		
		self.schoolDisplay = StringVar()
		Label(detailsWindow, font=("Tahoma", 11), bg=backgroundColor, textvariable=self.schoolDisplay).grid(row=2, column=0, columnspan=3, sticky=W)
		
		self.friendsNumber = StringVar()
		Label(detailsWindow, font=("Tahoma", 11), bg=backgroundColor, textvariable=self.friendsNumber).grid(row=2, column=3, padx=(5,0), sticky=W)


		self.wall = LabelFrame(profileMainWindow, text="Wall", width=470, height=400, padx=7, pady=7, bg=backgroundColor)
		self.wall.place(anchor=NW, relx=0.36, rely=0.2)
		self.wall.pack_propagate(False)

		# code below is courtesy of tkinter.unpythonic.net/wiki/VerticalScrolledFrame

		wallScroll = Scrollbar(self.wall, orient=VERTICAL, relief=FLAT)
		wallScroll.pack(fill=Y, side=RIGHT)

		self.wallCanvas = Canvas(self.wall, highlightthickness=0, bg=backgroundColor, yscrollcommand=wallScroll.set)
		self.wallCanvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
		wallScroll.config(command=self.wallCanvas.yview)

		self.wallCanvas.xview_moveto(0)
		self.wallCanvas.yview_moveto(0)

		self.wallFrame = wframe = Frame(self.wallCanvas, bg=backgroundColor)
		wallFrameID = self.wallCanvas.create_window(0, 0, window=wframe, anchor=NW)
		
		def _configFrame(event):
			size = (wframe.winfo_reqwidth(), wframe.winfo_reqheight())
			self.wallCanvas.config(scrollregion="0 0 %s %s" % size)
			if wframe.winfo_reqheight() != self.wallCanvas.winfo_width():
				self.wallCanvas.config(width=wframe.winfo_reqwidth())
		wframe.bind("<Configure>", _configFrame)

		def _configCanvas(event):
			if wframe.winfo_reqwidth() != self.wallCanvas.winfo_width():
				self.wallCanvas.itemconfigure(wallFrameID, width=self.wallCanvas.winfo_width())
		self.wallCanvas.bind("<Configure>", _configCanvas)

		self.links = LabelFrame(profileMainWindow, text="Links", width=175, height=268, padx=3, pady=3, bg=backgroundColor)
		self.links.place(anchor=NW, relx=0.1625, rely=0.44)
		self.links.pack_propagate(False)

		self.friendsPageButton = Button(self.links, text="My Friends", relief=FLAT)
		self.friendsPageButton.pack()

		self.messagesPageButton = Button(self.links, text="My Messages", relief=FLAT, pady=10)
		self.messagesPageButton.pack()

		self.poolPageButton = Button(self.links, text="Coffee Pool", relief=FLAT)
		self.poolPageButton.pack()

		

