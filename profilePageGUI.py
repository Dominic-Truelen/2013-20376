from Tkinter import *
from PIL import *

profilePic = 175		#Square profile picture frame
profilePicBgColor = "#CCCCFF"

class profilePageGUI(Frame):													# This is the GUI for the Profile Page. Included: Self Statuses, Profile Picture, Information, Friends List, Relationships Lists, etc...
	def __init__(self, master=None, bag=None):
		Frame.__init__(self, master)
		self.place(in_=master)
		self.createWidgets(bag)
		
	def createWidgets(self, bag):
		profileMainWindow = Frame(self, width=1000, height=550)	#Profile container
		profileMainWindow.pack()

		profilePicture = Frame(profileMainWindow, width=profilePic, height=profilePic, bg=profilePicBgColor) #ProfPic
		profilePicture.place(anchor=CENTER, relx=0.25, rely=0.25)

		Label(profilePicture, text="Insert DP Here", bg=profilePicBgColor).place(anchor=CENTER, relx=0.5, rely=0.5) 


		Label(profileMainWindow, text="NAME HERE", font=("Tahoma", 18, "bold")).place(anchor=N, relx=0.45, rely=0.075) #Name
		
		#Label(profileMainWindow, text="WELCOME TO PROFILE PAGE!", font=("Tahoma", 30, "bold"), fg="#000000", bg=bag).place(anchor=CENTER, relx=0.5, rely=0.5)