import os #for deleting and renaming files
import glob

class CC(object): #profile management #superclass
	def __init__(self):
		self.name = ''
		self.password = ''

	def set_name(self, name): #mutator
		self.name = name

	def set_password(self, password): #mutator
		self.password = password

	def get_name(self): #accessor
		return self.name

	def get_password(self): #accessor
		return self.password

class create(CC): #profile creation
	def ask_name(self): #GUI imput of username
		if glob.glob("DATABASE") != []:
			f = open("DATABASE", 'w')
			f.close()
		while True:
			counter = 1
			self.set_name(raw_input("Enter username: "))
			if os.path.isdir(os.getcwd() + "/" + self.get_name()) is True:
				counter = 0
			if counter == 1:
				break
		f.close()

	def ask_password(self): #GUI imput of password
		self.set_password(raw_input("Enter password: "))

	def create(self): #creating the database and adding the username and password
		if glob.glob("DATABASE") != []:
			f = open("DATABASE")
			f.close()
		f = open("DATABASE", 'a')
		f.write(self.get_name() + ': ' + self.get_password() + '\n')
		f.close()
		os.makedirs(os.getcwd() + "/" + str(self.get_name()) + "/pictures")
		f = open(os.getcwd() + "/" + self.get_name() + "/" + self.get_name(), 'w')
		f.write("Details 2013-20376\n" + self.get_name() + '\n' + self.get_password() + '\n\n' + "Friends 2013-20376\n[]\n\n" + "Status 2013-20376\n\n" + "Messages Recieved 2013-20376\n{}\n\n" + "Messages Sent 2013-20376\n{}\n\n" + "Friend Requests Recieved 2013-20376\n[]\n\n" + "Friend Requests Sent 2013-20376\n[]\n\n" + "Wall 2013-20376\n\n")
		f.close()

	def guic(self, usernameInput, password1, password2):
		self.set_name(usernameInput)
		self.set_password(password1)
		if self.get_name() == "":
			return "USERNAME IS BLANK"
		elif os.path.isdir(os.getcwd() + "/" + self.get_name()) is True:
				return "USERNAME IS ALREADY TAKEN"
		elif self.get_password() == "":
				return "PASSWORD REQUIRED"
		elif password2 == "":
			return "PLEASE RETYPE THE PASSWORD"
		else:
			if len(self.get_password()) < 8:
				return "PASSWORD MUST HAVE AT LEAST\n8 CHARACTERS"
			elif self.get_password() == password2:
				return 1
			return "RETYPE YOUR PASSWORD\nCORRECTLY"

class validation(CC): #validation for logging in and deleting profiles
	def guiv(self, usernameInput, passwordInput):							# GUI Version
		self.set_name(usernameInput)
		self.set_password(passwordInput)
		if self.get_name() == "":
			return "USERNAME IS BLANK"
		elif self.get_password() == "":
				return "PASSWORD IS BLANK"
		else:
			if os.path.isdir(os.getcwd() + "/" + self.get_name()) is False:
				return "ACCOUNT DOES NOT EXIST"
			else:
				f = open(self.get_name())
				f.readline()
				f.readline()
				if (self.get_password() + '\n') == f.readline():
					return 1
				else:
					return "INVALID PASSWORD"

	def validation(self):													# Console Version
		self.set_name(str(raw_input("Username: ")))
		if os.path.isdir(os.getcwd() + "/" + self.get_name()) is False:
			return 0
		f = open(os.getcwd() + "/" + self.get_name() + "/" + self.get_name())
		f.readline()
		f.readline()
		self.set_password(str(raw_input("Password: ")))
		if (self.get_password() + '\n') == f.readline():
			return 1
		return 0

class delete(CC): #profile deletion
	def __init__(self):
		super(delete, self).__init__()
		self.valid = validation()
	def delete(self):
		temp = self.valid.validation() #will return 1 if valid and 0 if invalid
		if temp == 1:
			os.removedirs(os.getcwd() + '/' + self.valid.get_name()) #deletes the filename with name of profile
			f = open("DATABASE")
			g = open("DATABASE1")
			for line in f:
				line1 = None
				if ':' in line:
					line = line.split(':')
					line = line[0]
					line1 = line[1]
				if self.valid.get_name() in line:
					f.readline()
				if line1 == None:
					g.write(line)
				else:
					g.write(line + ':' + line1)
			f.close()
			g.close()
			os.remove("DATABASE")
			os.rename("DATABASE1", "DATABASE")
		else:
		  print "NO SUCH PROFILE EXISTS"

class login(CC): #logging in
	def __init__(self):
		super(login, self).__init__()
		self.valid = validation()
		self.database = import_database()

	def login(self):
		temp = self.valid.validation()#will return 1 if valid and 0 if invalid
		if temp == 1:
			self.name = self.valid.get_name()
			self.database.set_name(self.name) #see import_database
			self.database.set_password(self.valid.get_password())
			self.database.import_friends(self.name)
			self.database.import_status(self.name)
			self.database.import_messages(self.name)
			self.database.import_friend_requests(self.name)
			self.database.import_friend_requests_sent(self.name)
			self.database.import_messages_sent(self.name)
			return 1
		else:
			return 0

class import_database(object): #importing data from the profile's database
	def __init__(self):
		self.name = ''
		self.password = ''
		self.friends = []
		self.status = ''
		self.wall = {}
		self.messages = {}
		self.messages_sent = {}
		self.friend_requests = []
		self.friend_requests_sent = []

	def set_name(self, name): #mutator
		self.name = name

	def set_password(self, password): #mutator
		self.password = password

	def get_name(self):
		return self.name

	def get_password(self):
		return self.password

	def get_friends(self):
		return self.friends

	def get_status(self):
		return self.status

	def get_messages(self): #accessor
		return self.messages

	def get_messages_sent(self):
		return self.messages_sent

	def get_friend_requests(self):
		return self.friend_requests

	def get_friend_requests_sent(self):
		return self.friend_requests_sent

	def import_friends(self, name): #importing friends list
		f = open(os.getcwd() + "/" + name + "/" + name)
		while True: #scanning untill it reaches the friends list
			temp = f.readline()
			if "Friends 2013-20376" in temp:
				break
		temp = f.readline()
		self.friends = eval(temp)
		f.close()

	def import_status(self, name): #importing status
		f = open(os.getcwd() + "/" + name + "/" + name)
		while True: #scanning untill it reaches the status
			temp = f.readline()
			if "Status 2013-20376" in temp:
				break
		self.status = f.readline()
		f.close()

	def import_messages(self, name): #importing messages
		self.messages = {}
		friend = {}
		f = open(os.getcwd() + "/" + name + "/" + name)
		while True: #scanning untill it reaches the messages
			temp = f.readline()
			if "Messages Recieved 2013-20376" in temp:
				break
		self.messages = f.readline()
		f.close()

	def import_messages_sent(self, name):
		self.messages_sent = {}
		friend = {}
		f = open(os.getcwd() + "/" + name + "/" + name)
		while True: #scanning untill it reaches the messages
			temp = f.readline()
			if "Messages Sent 2013-20376" in temp:
				break
		self.messages_sent = f.readline()
		f.close()

	def import_friend_requests(self, name):
		f = open(os.getcwd() + "/" + name + "/" + name)
		while True:
			temp = f.readline()
			if "Friend Requests Recieved 2013-20376" in temp:
				break
		temp = f.readline()
		self.friend_requests = temp

	def import_friend_requests_sent(self, name):
		f = open(os.getcwd() + "/" + name + "/" + name)
		while True:
			temp = f.readline()
			if "Friend Requests Sent 2013-20376" in temp:
				break
		temp = f.readline()
		temp = temp.split('\n')
		temp = temp[0]
		self.friend_requests_sent = temp

class export_database(import_database): #exporting data to the database by creating a temporary file, deleting the original file, then renaming the temporary file
	def export_details(self, name, password): #exporting username and password
		f = open(os.getcwd() + "/" + name + "/" + name)
		g = open(os.getcwd() + "/" + name + "/" + name + "1", 'w')
		g.write('Details 2013-2076' + '\n' + name + '\n' + password + '\n')
		f.readline()
		f.readline()
		f.readline()
		for line in f:
			g.write(line)
		f.close()
		g.close()
		os.remove(os.getcwd() + "/" + name + "/" + name)
		os.rename(os.getcwd() + "/" + name + "/" + name + '1', os.getcwd() + "/" + name + "/" + name)

	def export_friends(self, name, friends): #exporting friends list
		f = open(os.getcwd() + "/" + name + "/" + name)
		g = open(os.getcwd() + "/" + name + "/" + name + "1", 'w')
		while True:
			temp = f.readline()
			g.write(temp)
			if 'Friends 2013-20376' in temp:
				break
		g.write(str(friends) + '\n')
		f.readline()
		for line in f:
			g.write(line)
		f.close()
		g.close()
		os.remove(os.getcwd() + "/" + name + "/" + name)
		os.rename(os.getcwd() + "/" + name + "/" + name + '1', os.getcwd() + "/" + name + "/" + name)
		f = open("DATABASE")
		g = open("DATABASE" + '1', 'w')
		while True:
			temp = f.readline()
			g.write(temp)
			if name + ': ' in temp:
				break
		for counter in range(len(friends) - 1):
			f.readline()
		for counter in range(len(friends)):
			g.write('\t' + friends[counter] + '\n')
		for line in f:
			g.write(line)
		f.close()
		g.close()
		os.remove("DATABASE")
		os.rename("DATABASE" + '1', "DATABASE")

	def export_status(self, name, status): #exporting status
		f = open(os.getcwd() + "/" + name + "/" + name)
		g = open(os.getcwd() + "/" + name + "/" + name + "1", 'w')
		while True:
			temp = f.readline()
			g.write(temp)
			if "Status 2013-20376" in temp:
				break
		g.write(status + '\n')
		f.readline()
		for line in f:
			g.write(line)
		f.close()
		g.close()
		os.remove(os.getcwd() + "/" + name + "/" + name)
		os.rename(os.getcwd() + "/" + name + "/" + name + '1', os.getcwd() + "/" + name + "/" + name)

	def export_messages(self, name, message, time, reciever):
		message = str(message)
		time = str(time)
		reciever = str(reciever)
		f = open(os.getcwd() + "/" + name + "/" + name)
		g = open(os.getcwd() + "/" + name + "/" + name + '1', 'w')
		while True:
			temp = f.readline()
			g.write(temp)
			if "Messages Recieved 2013-20376" in temp:
				break
		temp = eval(f.readline())
		if reciever not in temp:
			temp[reciever] = []
		temp[reciever].append(time + ':' + message)
		g.write(str(temp) + '\n')
		for line in f:
			g.write(line)
		f.close()
		g.close()
		os.remove(os.getcwd() + "/" + name + "/" + name)
		os.rename(os.getcwd() + "/" + name + "/" + name + '1', os.getcwd() + "/" + name + "/" + name)

	def export_sent_messages(self, name, message, time, sender):
		message = str(message)
		time = str(time)
		sender = str(sender)
		f = open(os.getcwd() + "/" + name + "/" + name)
		g = open(os.getcwd() + "/" + name + "/" + name + '1', 'w')
		while True:
			temp = f.readline()
			g.write(temp)
			if "Messages Sent 2013-20376" in temp:
				break
		temp = eval(f.readline())
		if sender not in temp:
			temp[sender] = []
		temp[sender].append(time + ':' + message)
		g.write(str(temp) + '\n')
		for line in f:
			g.write(line)
		f.close()
		g.close()
		os.remove(os.getcwd() + "/" + name + "/" + name)
		os.rename(os.getcwd() + "/" + name + "/" + name + '1', os.getcwd() + "/" + name + "/" + name)

	def export_friend_request(self, name, friend_requests):
		f = open(os.getcwd() + "/" + name + "/" + name)
		g = open(os.getcwd() + "/" + name + "/" + name + '1', 'w')
		while True:
			temp = f.readline()
			g.write(temp)
			if "Friend Requests Recieved 2013-20376" in temp:
				break
		g.write(str(friend_requests) + '\n')
		f.readline()
		for line in f:
			g.write(line)
		f.close()
		g.close()
		os.remove(os.getcwd() + "/" + name + "/" + name)
		os.rename(os.getcwd() + "/" + name + "/" + name + '1', os.getcwd() + "/" + name + "/" + name)

	def export_friend_request_sent(self, name, friend_requests_sent):
		f = open(os.getcwd() + "/" + name + "/" + name)
		g = open(os.getcwd() + "/" + name + "/" + name + '1', 'w')
		while True:
			temp = f.readline()
			g.write(temp)
			if "Friend Requests Sent 2013-20376" in temp:
				break
		g.write(str(friend_requests_sent) + '\n')
		f.readline()
		for line in f:
			g.write(line)
		f.close()
		g.close()
		os.remove(os.getcwd() + "/" + name + "/" + name)
		os.rename(os.getcwd() + "/" + name + "/" + name + '1', os.getcwd() + "/" + name + "/" + name)

class logout(object): #will reset the name and password of CC after returning to the main GUI
	def __init__(self):
		self.quit = CC()

	def exit(self):
		self.quit.set_name('')
		self.quit.set_password('')