from Tkinter import *
from PIL import ImageTk, Image

profilePic = 175		#Square profile picture frame
profilePicBgColor = "#CCCCFF"

class profilePageGUI(Frame):													# This is the GUI for the Profile Page. Included: Self Statuses, Profile Picture, Information, Friends List, Relationships Lists, etc...
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.place(in_=master)
		self.dp = ImageTk.PhotoImage(file="GUIE\\maleDP.png") # I think proxy should be implemented now...
		self.createWidgets()		

	def receiveDatabase(self, database):
		self.displayName.config(text=database.get_name())
		DP = ImageTk.PhotoImage(file=database.get_DP())
		self.dp = DP

	def createWidgets(self):
		profileMainWindow = Frame(self, width=1000, height=550)	#Profile container
		profileMainWindow.pack()

		profilePicture = Frame(profileMainWindow, width=profilePic, height=profilePic) #ProfPic
		profilePicture.place(anchor=CENTER, relx=0.25, rely=0.25)

		canvasDP = Canvas(profilePicture, width=profilePic, height=profilePic, highlightthickness=0)
		canvasDP.pack()
		canvasDP.create_image(profilePic/2, profilePic/2, image=self.dp)
		canvasDP.image = self.dp


		#Label(profilePicture, text="Insert DP Here", bg=profilePicBgColor).place(anchor=CENTER, relx=0.5, rely=0.5) 


		self.displayName = Label(profileMainWindow, font=("Tahoma", 18, "bold"))
		self.displayName.place(anchor=W, relx=0.36, rely=0.105) #Name
		
		#Label(profileMainWindow, text="WELCOME TO PROFILE PAGE!", font=("Tahoma", 30, "bold"), fg="#000000", bg=bag).place(anchor=CENTER, relx=0.5, rely=0.5)

		wall = LabelFrame(profileMainWindow, text="Wall", width=450, height=400, padx=5, pady=5)
		wall.place(anchor=NW, relx=0.36, rely=0.2)

		wall = LabelFrame(profileMainWindow, text="Links", width=175, height=268, padx=3, pady=3)
		wall.place(anchor=NW, relx=0.1625, rely=0.44)