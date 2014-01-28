from Tkinter import *
from PIL import *

class profilePageGUI(Frame):													# This is the GUI for the Profile Page. Included: Self Statuses, Profile Picture, Information, Friends List, Relationships Lists, etc...
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.place(in_=master)
		self.createWidgets()
		
	def createWidgets(self):
		profileMainWindow = Frame(self, width=1000, height=550)
		profileMainWindow.pack()
		Label(profileMainWindow, text="WELCOME TO PROFILE PAGE!", font=("Tahoma", 30, "bold"), fg="#000000").place(anchor=CENTER, relx=0.5, rely=0.5)