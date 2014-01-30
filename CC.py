import os, shutil #for deleting and renaming files
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

class creation(CC): #profile creation
    
    def __init__(self):
        self.val = validation()
        self.usernameVerifyObject = usernameVerify()                                    #Chain of Responsibility
        self.passwordVerifyObject = passwordVerify()
        self.val.handler(self.usernameVerifyObject)
        self.usernameVerifyObject.handler(self.passwordVerifyObject)

    def set_password_retyped(self, x):
        self.password_retyped = x

    def get_password_retyped(self):
        return self.password_retyped

    def ask_name(self): #GUI imput of username
		if glob.glob("DATABASE") == []:
			os.makedirs(os.getcwd() + "\\DATABASE")
		elif glob.glob("DATABASE") != []:
			if glob.glob("DATABASE\\DATABASE") != []:
				f = open("DATABASE\\DATABASE")
				f.close()
		while True:
			counter = 1
			self.set_name(raw_input("Enter username: "))
			if os.path.isdir(os.getcwd() + "\\DATABASE\\" + self.get_name()) is True:
				counter = 0
			if counter == 1:
				break		
	
    def ask_password(self): #GUI imput of password
		self.set_password(raw_input("Enter password: "))
        
    def create(self): #creating the database, adding necessary folders, and adding the username and password
		if glob.glob("DATABASE") == []:
			os.makedirs(os.getcwd() + "\\DATABASE")
		elif glob.glob("DATABASE") != []:
			if glob.glob("DATABASE\\DATABASE") != []:
				f = open("DATABASE\\DATABASE")
				f.close()
		f = open("DATABASE\\DATABASE", 'a')
		f.write(self.get_name() + ': ' + self.get_password() + '\n')
		f.close()
		os.makedirs(os.getcwd() + "\\DATABASE\\" + str(self.get_name()) + "\\pictures")
		f = open(os.getcwd() + "\\DATABASE\\" + self.get_name() + "\\" + self.get_name(), 'w')
		f.write("Details 2013-20376\n" + self.get_name() + '\n' + self.get_password() + '\nOffline\n\n' + "Friends 2013-20376\n[]\n\n" + "Status 2013-20376\n{}\n\n" + "Messages Recieved 2013-20376\n{}\n\n" + "Messages Sent 2013-20376\n{}\n\n" + "Friend Requests Recieved 2013-20376\n[]\n\n" + "Friend Requests Sent 2013-20376\n[]\n\n" + "Wall 2013-20376\n{}\n")
		f.close()
    
    def validate(self, username, password1, password2):
		return self.val.guic(username, password1, password2)
    
class validation(CC): #validation for logging in and deleting profiles
    
    def handler(self, successor):
        self.successor = successor

    def guiv(self, username, password):							# GUI Version when Logging in
        self.set_name(username)
        self.set_password(password)
        if self.get_name() == "":
            return "USERNAME IS BLANK"
        elif self.get_password() == "":
                return "PASSWORD IS BLANK"
        else:
            return self.successor.handleLogin(self.get_name(), self.get_password())           
    
    def guic(self, username, password1, password2):             # GUI Version when creating a new account
        self.set_name(username)
        self.set_password(password1)
        if self.get_name() == "":
            return "USERNAME IS BLANK"
        else:
            return self.successor.handleCreate(self.get_name(), self.get_password(), password2)
          
    def validation(self):													# Console Version
        self.set_name(str(raw_input("Username: ")))
        if os.path.isdir(os.getcwd() + "\\DATABASE\\" + self.get_name()) is False:
            return 0
        f = open(os.getcwd() + "\\DATABASE\\" + self.get_name() + "\\" + self.get_name())
        f.readline()
        f.readline()
        self.set_password(str(raw_input("Password: ")))
        if (self.get_password() + '\n') == f.readline():
            return 1
        return 0         

class usernameVerify(validation):
    
    def handleLogin(self, x, y):
        if os.path.isdir(os.getcwd() + "\\DATABASE\\" + x) is False:    #Check if Logging in a username DNE
                return "ACCOUNT DOES NOT EXIST"
        else:
            f = open(os.getcwd() + "\\DATABASE\\" + x + "\\" + x)
            f.readline()
            f.readline()
            if (y + '\n') == f.readline():
                return 1
            else:
                return self.successor.handleLogin(y)                    #Handle the Password

    def handleCreate(self, username, password1, password2):
        for x in set(username):                             #Check for special characters in creating usernames
            if x in set([" ","^", "&", "!", "$", ",", "/", "?", "\\", "|", "+", "#", "*", "\"", "<", ">", ";", "=", "[", "]", "%", "~", "`", "{", "}"]):
                return "MUST NOT CONTAIN\nSPECIAL CHARACTERS"
        if os.path.isdir(os.getcwd() + "\\DATABASE\\" + username) is True:      #Check if username is already in use
            return "USERNAME IS ALREADY TAKEN"        
        else:
            return self.successor.handleCreate(password1, password2)    #Handle the Password

class passwordVerify(validation):
        
    def handleLogin(self, y):
        return "INVALID PASSWORD"

    def handleCreate(self, pwd1, pwd2):
        if pwd1 == "":
            return "PASSWORD REQUIRED"
        elif pwd2 == "":
            return "PLEASE RETYPE THE PASSWORD"
        else:
            if len(pwd1) < 6:                            # Check if password character count is less than 6
                return "PASSWORD MUST HAVE AT LEAST\n6 CHARACTERS"
            elif pwd1 == pwd2:
                return 1
            else:
                return "RETYPE YOUR PASSWORD\nCORRECTLY"

class deletion(CC): #profile deletion
	
    def __init__(self):
		super(deletion, self).__init__()
		self.valid = validation()
	
    def delete2(self):				   # ATTENTION! XD *** THIS IS THE ORIGINAL DELETE FUNCTION BY DOMINIC. (I CHANGED THE NAME TO DELETE 2 FOR BACKUP) def has errors & doesn't yet output as expected
		temp = self.valid.validation() #will return 1 if valid and 0 if invalid
		if temp == 1:            
			f = open("DATABASE\\DATABASE")
			g = open("DATABASE\\DATABASE1", 'w')	#Temp file name for deleting names in the registry
			for line in f:
				line1 = None
				if ':' in line:
					lineT = line.split(':')
					lineN = lineT[0]
					line1 = lineT[1]
				if self.valid.get_name() in lineT:
					pass
				if line1 == None:
					g.write(line)
				else:
					g.write(line + ':' + line1)
			f.close()
			g.close()
			os.remove("DATABASE\\DATABASE")
			os.rename("DATABASED\\DATABASE1", "DATABASE\\DATABASE")
			shutil.rmtree(os.getcwd() + '\\DATABASE\\' + self.valid.get_name()) #deletes the filename with name of profile
		else:
			print "NO SUCH PROFILE EXISTS"
			
    def delete(self):				   #  *** THIS IS MY VERSION OF THE DELETE FUNCTION. This code needs adding in terms of friend deletion (this code kinda works, but needs improvement)
		temp = self.valid.validation() #will return 1 if valid and 0 if invalid
		if temp == 1:            
			f = open("DATABASE\\DATABASE")
			g = open("DATABASE\\DATABASE1", 'w')	#Temp file name for deleting names in the registry
			lines = f.readlines()
			f.close()
			a = self.valid.get_name() + ": " + self.valid.get_password() + "\n"
			for x in lines:
				if x != a:
					g.write(x)			
			g.close()
			os.remove("DATABASE\\DATABASE")
			os.rename("DATABASE\\DATABASE1", "DATABASE\\DATABASE")
			shutil.rmtree(os.getcwd() + '\\DATABASE\\' + self.valid.get_name()) #deletes the filename folder and directory recursively with name of profile
		else:
			print "NO SUCH PROFILE EXISTS"

class login(CC): #logging in
    
    def __init__(self):
        super(login, self).__init__()
        self.valid = validation()
        self.database = import_database()
        self.export = export_database()

    def login(self):
        temp = self.valid.validation()#will return 1 if valid and 0 if invalid
        if temp == 1:
            self.name = self.valid.get_name()
            self.password = self.valid.get_password()
            self.database.set_name(self.name) #see import_database
            self.database.set_password(self.password)
            self.export.export_details(self.name, self.password, "Online")
            self.database.import_friends(self.name)
            self.database.import_status(self.name)
            self.database.import_messages(self.name)
            self.database.import_friend_requests(self.name)
            self.database.import_friend_requests_sent(self.name)
            self.database.import_messages_sent(self.name)
            return 1
        return 0

class import_database(object): #importing data from the profile's database
   
    def __init__(self):
        self.name = ''
        self.password = ''
        self.friends = []
        self.status = {}
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

    def get_wall(self):
        return self.wall

    def import_details(self, name):
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        f.readline()
        self.name = eval(f.readline())
        self.password = eval(f.readline())
        f.close()

    def import_friends(self, name): #importing friends list
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        while True: #scanning untill it reaches the friends list
            temp = f.readline()
            if "Friends 2013-20376" in temp:
                break
        temp = f.readline()
        self.friends = eval(temp)
        f.close()

    def import_status(self, name): #importing status
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        while True: #scanning untill it reaches the status
            temp = f.readline()
            if "Status 2013-20376" in temp:
                break
        self.status = f.readline()
        f.close()

    def import_messages(self, name): #importing messages
        self.messages = {}
        friend = {}
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        while True: #scanning untill it reaches the messages
            temp = f.readline()
            if "Messages Recieved 2013-20376" in temp:
                break
        self.messages = f.readline()
        f.close()

    def import_messages_sent(self, name):
        self.messages_sent = {}
        friend = {}
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        while True: #scanning untill it reaches the messages
            temp = f.readline()
            if "Messages Sent 2013-20376" in temp:
                break
        self.messages_sent = f.readline()
        f.close()

    def import_friend_requests(self, name):
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        while True:
            temp = f.readline()
            if "Friend Requests Recieved 2013-20376" in temp:
                break
        temp = f.readline()
        self.friend_requests = temp

    def import_friend_requests_sent(self, name):
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        while True:
            temp = f.readline()
            if "Friend Requests Sent 2013-20376" in temp:
                break
        temp = f.readline()
        temp = temp.split('\n')
        temp = temp[0]
        self.friend_requests_sent = temp

    def import_wall(self, name):
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        while True:
            if "Wall 2013-20376" in f.readline():
                break
        self.wall = f.readline()

class export_database(): #exporting data to the database by creating a temporary file, deleting the original file, then renaming the temporary file
    
    def export_details(self, name, password, status): #exporting username and password
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        g = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + "1", 'w')
        g.write('Details 2013-2076' + '\n' + name + '\n' + password + '\n' + status + '\n')
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        os.rename(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', os.getcwd() + "\\DATABASE\\" + name + "\\" + name)

    def export_friends(self, name, friends): #exporting friends list
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        g = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + "1", 'w')
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
        os.remove(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        os.rename(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        f = open("DATABASE\\DATABASE")
        g = open("DATABASE\\DATABASE" + '1', 'w')
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
        os.remove("DATABASE\\DATABASE")
        os.rename("DATABASE\\DATABASE" + '1', "DATABASE\\DATABASE")

    def export_status(self, name, status, time): #exporting status
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        g = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + "1", 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if "Status 2013-20376" in temp:
                break
        temp = eval(f.readline())
        temp[time] = status
        g.write(str(temp) + '\n')
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        os.rename(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', os.getcwd() + "\\DATABASE\\" + name + "\\" + name)

    def export_messages(self, name, message, time, reciever):
        message = str(message)
        time = str(time)
        reciever = str(reciever)
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        g = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', 'w')
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
        os.remove(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        os.rename(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', os.getcwd() + "\\DATABASE\\" + name + "\\" + name)

    def export_sent_messages(self, name, message, time, sender):
        message = str(message)
        time = str(time)
        sender = str(sender)
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        g = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', 'w')
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
        os.remove(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        os.rename(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', os.getcwd() + "\\DATABASE\\" + name + "\\" + name)

    def export_friend_request(self, name, friend_requests):
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        g = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', 'w')
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
        os.remove(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        os.rename(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', os.getcwd() + "\\DATABASE\\" + name + "\\" + name)

    def export_friend_request_sent(self, name, friend_requests_sent):
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        g = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', 'w')
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
        os.remove(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        os.rename(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', os.getcwd() + "\\DATABASE\\" + name + "\\" + name)

    def export_wall(self, name, wall):
        wall = str(wall)
        f = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        g = open(os.getcwd() + "\\DATABASE\\" + name + "\\" + name + '1', 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if "Wall 2013-20376" in temp:
                break
        g.write(wall + '\n')
        f.readline()
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.getcwd() + "\\DATABASE\\" + name + "\\" + name)
        os.rename(os.getcwd() + "\\DATABASE\\" + name + "\\" + name+ '1', os.getcwd() + "\\DATABASE\\" + name + "\\" + name)

class logout(object): #will reset the name and password of CC after returning to the main GUI
    
    def __init__(self):
        self.quit = CC()
        self.exporter = export_database()

    def exit(self, name, password):
        self.exporter.export_details(name, password, "Offline")
        self.quit.set_name('')
        self.quit.set_password('')