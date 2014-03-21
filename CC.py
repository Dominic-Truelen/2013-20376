import os, glob, shutil, collections #for deleting and renaming files

class CC(object): #profile management #superclass

    def __init__(self):
        self.name = ''
        self.password = ''
        self.registry = registryDatabase()
        self.importer = import_database()
        self.exporter = export_database()

    def set_name(self, name): #mutator
        self.name = name

    def set_password(self, password): #mutator
        self.password = password

    def set_OnOrOff(self, status):
        self.exporter.export_onoroff(self.get_name(), status)

    def get_name(self): #accessor
        return self.name

    def get_password(self): #accessor
        return self.password

    def login(self):
        self.importer.import_onoroff(self.get_name())
        if self.importer.get_onoroff() == "Offline Setup":
            return "SETUPCREATED"
        elif self.importer.get_onoroff() == "Online":
            return "OLREADY"
        else:
            self.set_OnOrOff("Online")
            self.importer.set_name(self.get_name()) #username
            self.importer.set_password(self.get_password())            
            self.importer.import_all(self.get_name())            
            return self.importer

    def logout(self):
        self.set_OnOrOff("Offline")
        self.set_name("")
        self.set_password("")


class creation(CC): #profile creation

    def __init__(self):
        self.val = validation()
        self.usernameVerifyObject = usernameVerify()                                    #Chain of Responsibility
        self.passwordVerifyObject = passwordVerify()
        self.val.handler(self.usernameVerifyObject)
        self.usernameVerifyObject.handler(self.passwordVerifyObject)
        self.registry = registryDatabase()

    def set_name(self, x):                                                              # Overwritten method
        self.name = x                                                                   # To include mutators for registry
        self.registry.set_name(x)

    def set_password(self, x):
        self.password = x
        self.registry.set_password(x)

    def set_password_retyped(self, x):
        self.password_retyped = x

    def get_password_retyped(self):
        return self.password_retyped

    def ask_name(self): #GUI imput of username
        if glob.glob("DATABASE") == []:
            os.makedirs(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE")
        elif glob.glob("DATABASE") != []:
            if glob.glob("DATABASE/DATABASE") != []:
                f = open("DATABASE/DATABASE")
                f.close()
        while True:
            counter = 1
            self.set_name(raw_input("Enter username: "))
            if os.path.isdir(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.get_name()) is True:
                counter = 0
            if counter == 1:
                break

    def ask_password(self): #GUI imput of password
        self.set_password(raw_input("Enter password: "))

    def create(self): #creating the database, adding necessary folders, and adding the username and password        
        self.registry.register()
        os.makedirs(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + str(self.get_name()) + "/pictures")
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.get_name() + "/" + self.get_name(), 'w')
        f.write("Details\n") 
        f.write("<INSERT NAME HERE>\n")
        f.write(self.get_password())
        f.write("\n\n\n\n[[],[],[]]\n")
        f.write('Offline Setup\n\n')
        f.write("DP\n")
        f.write("GUIE/default.gif\n\n")
        f.write("Friends\n")
        f.write("[]\n\n")
        f.write("Status\n")
        f.write("{}\n\n")
        f.write("Messages Recieved\n")
        f.write("{}\n\n")
        f.write("Messages Sent\n")
        f.write("{}\n\n")
        f.write("Friend Requests Recieved\n")
        f.write("[]\n\n")
        f.write("Friend Requests Sent\n")
        f.write("[]\n\n")
        f.write("Wall\n")
        f.write("{}\n\n")
        f.write("Messages Copy\n")
        f.write("{}\n\n")
        f.write("Friend Requests Recieved Copy\n")
        f.write("[]")
        f.close()

    def createFromPreExisting(self):
        os.makedirs(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + str(self.get_name()) + "/pictures")
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.get_name() + "/" + self.get_name(), 'w')
        f.write("Details\n") 
        f.write("<INSERT NAME HERE>\n")
        f.write(self.get_password())
        f.write("\n\n\n\n[[],[],[]]\n")
        f.write('Offline Setup\n\n')
        f.write("DP\n")
        f.write("GUIE/default.gif\n\n")
        f.write("Friends\n")
        f.write("[]\n\n")
        f.write("Status\n")
        f.write("{}\n\n")
        f.write("Messages Recieved\n")
        f.write("{}\n\n")
        f.write("Messages Sent\n")
        f.write("{}\n\n")
        f.write("Friend Requests Recieved\n")
        f.write("[]\n\n")
        f.write("Friend Requests Sent\n")
        f.write("[]\n\n")
        f.write("Wall\n")
        f.write("{}\n\n")
        f.write("Messages Copy\n")
        f.write("{}\n\n")
        f.write("Friend Requests Recieved Copy\n")
        f.write("[]")
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

    def guis(self, firstname, lastname, month, day, year, gender, checkboxjobs, position, company, years, checkboxeduc, school, graduateyear):

        if firstname == "" or lastname == "":
            return "DISPLAY NAME IS\nBLANK"
        for x in set(firstname).union(set(lastname)):                              #Check for special characters in creating usernames
            if x in set([".", "^", "&", "!", "$", ",", "\\", "?", "/", "|", "+", "#", "*", "\"", "<", ">", ";", "=", "[", "]", "%", "~", "`", "{", "}", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
                return "MUST NOT CONTAIN\nSPECIAL CHARACTERS"                

        if month == "Month" or day == "Day" or year == "Year":  #If passed variables have no actual dates, return incomplete
            return "DATE INCOMPLETE"

        day = int(day)
        year = int(year)

        if month in ("September", "April", "June", "November"): #Else if they are complete:
            if day == 31:                                       #If at a 30 day month, day 31 was selected, return invalidity
                return "INVALID DATE"
        elif month == "February":                               #Else if february
            if year % 400 == 0:                                 #If inputted year is divisible by 400, then leap year
                if day in range(30,32): #Days 30 and 31 are excluded
                    return "INVALID DATE"            
            elif year % 100 == 0:                               #If inputted year is divisible by 100, then not leap year
                if day in range(29,32): #Days 29, 30, and 31 are excluded
                    return "INVALID DATE"
            elif year % 4 == 0:                                 #If inputted year is divisible by 4, then leap year
                if day in range(30,32): #Days 30 and 31 are excluded
                    return "INVALID DATE"
            else:
                if day in range(29,32): #Days 29, 30, and 31 are excluded
                    return "INVALID DATE"
        #                                                       #Else if 31 day month, continue
        if checkboxjobs == 1:                                   #If enabled, verify the jobs entry fields
            if position == "" or company == "" or years == "":
                return "JOB INFORMATION\nINCOMPLETE"
        
        if checkboxeduc == 1:
            if school == "" or graduateyear == "":
                return "EDUCATION INFORMATION\nINCOMPLETE"
        return 1

    def validation(self):													# Console Version
        self.set_name(str(raw_input("Username: ")))
        if os.path.isdir(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.get_name()) is False:
            return 0
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.get_name() + "/" + self.get_name())
        f.readline()
        f.readline()
        self.set_password(str(raw_input("Password: ")))
        if (self.get_password() + '\n') == f.readline():
            f.close()
            return 1
        f.close()
        return 0


class usernameVerify(validation):

    def handleLogin(self, x, y):
        if glob.glob("DATABASE") == []:
            os.makedirs(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE")

        if glob.glob("DATABASE/DATABASE") == []:                                       # For a first time user who logged in without creating an account first (error is handled by creating the database folder)
            f = open("DATABASE/DATABASE", "w")
            f.close()

        f = open("DATABASE/DATABASE")
        a = [line for line in f]
        if ((x + ": " + y + "\n") not in a):
            return self.successor.handleLoginPassword(x, y, a)  #Handle the Password in Registry
        f.close()

        if glob.glob(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + x + "/" + x) == []:          # From a pre-existing registry without user's individual databases
            return "SETUP"

        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + x + "/" + x)    # For users whose accounts were created from the Login page GUI
        f.readline()
        f.readline()
        if (y + '\n') == f.readline():
            return 1

    def handleCreate(self, username, password1, password2):
        if glob.glob("DATABASE") == []:
            os.makedirs(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE")

        if glob.glob("DATABASE/DATABASE") == []:                                       # For a first time user who logged in without creating an account first (error is handled by creating the database folder)
            f = open("DATABASE/DATABASE", "w")
            f.close()

        username = username.lower()                         #Uppercase letters during creation would'nt be allowed.
        for x in set(username):                             #Check for special characters in creating usernames
            if x in set([".", "^", "&", "!", "$", ",", "\\", "?", "/", "|", "+", "#", "*", "\"", "<", ">", ";", "=", "[", "]", "%", "~", "`", "{", "}"]):
                return "MUST NOT CONTAIN\nSPECIAL CHARACTERS"
        f = open("DATABASE/DATABASE")
        a = f.readlines()
        for line in a:
            b = line.split(": ")
            if username != b[0]:
                continue
            elif (username == b[0]) or (os.path.isdir(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + username) is True):
                f.close()
                return "USERNAME IS ALREADY TAKEN"
        f.close()
        return self.successor.handleCreate(password1, password2)    #Handle the Password


class passwordVerify(validation):

    def handleLoginPassword(self, x, y, f):
        for line in f:
            a = line.split(": ")
            if x != a[0]:
                continue
            elif x == a[0]:
                if y != a[1]:
                    return "INVALID PASSWORD"
        return "ACCOUNT DOES NOT EXIST"

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
            f = open("DATABASE/DATABASE")
            g = open("DATABASE/DATABASE1", 'w')	#Temp file name for deleting names in the registry
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
            os.remove("DATABASE/DATABASE")
            os.rename("DATABASED/DATABASE1", "DATABASE/DATABASE")
            shutil.rmtree(os.path.abspath(os.path.dirname(__file__)) + '/DATABASE/' + self.valid.get_name()) #deletes the filename with name of profile
        else:
            print "NO SUCH PROFILE EXISTS"

    def delete(self):				   #  *** THIS IS MY VERSION OF THE DELETE FUNCTION. This code needs adding in terms of friend deletion (this code kinda works, but needs improvement)
        temp = self.valid.validation() #will return 1 if valid and 0 if invalid
        if temp == 1:
            f = open("DATABASE/DATABASE")
            g = open("DATABASE/DATABASE1", 'w')	#Temp file name for deleting names in the registry
            lines = f.readlines()
            f.close()
            a = self.valid.get_name() + ": " + self.valid.get_password() + "\n"
            for x in lines:
                if x != a:
                    g.write(x)
            g.close()
            os.remove("DATABASE/DATABASE")
            os.rename("DATABASE/DATABASE1", "DATABASE/DATABASE")
            shutil.rmtree(os.path.abspath(os.path.dirname(__file__)) + '/DATABASE/' + self.valid.get_name()) #deletes the filename folder and directory recursively with name of profile
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
            self.export.export_details(self.name)
            '''
            self.database.import_friends(self.name)
            self.database.import_status(self.name)
            self.database.import_messages(self.name)
            self.database.import_friend_requests(self.name)
            self.database.import_friend_requests_sent(self.name)
            self.database.import_messages_sent(self.name)
            '''
            return 1
        return 0


class registryDatabase(object):
    def __init__(self):
        self.name = ''
        self.password = ''
        self.friends = []

    def set_name(self, name): #mutator
        self.name = name

    def set_password(self, password): #mutator
        self.password = password

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def set_friends(self, name, pwd):
        entry = name + ": " + pwd + "\n"
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE")
        while True:
            if f.readline() == entry:
                break
        while True:
            friend = f.readline()            
            if len(friend) != 0:
                if list(friend)[0] != "\t":
                    break
            if len(friend) == 0:
                break
            self.friends.append(friend.strip())
        f.close()

    def get_friends(self):
        return self.friends

    def import_friends(self, name): #importing friends list
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True: #scanning untill it reaches the friends list
            temp = f.readline()
            if temp == "Friends\n":
                break
        temp = f.readline()        
        self.friends = eval(temp.rstrip())
        f.close()

    def register(self):                         # For existing database without each account's formal setup from the creation class
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE", 'a+')        
        f.write(self.get_name() + ': ' + self.get_password() + '\n')
        if self.get_friends() != []:
            for x in self.get_friends():
                f.write("\t"+x+"\n")
        f.close()

    def registerFriends(self, friendsName):                  # Still experimental
		entry = self.get_name() + ": " + self.get_password() + "\n"        
		f = open("DATABASE/DATABASE", 'r')
		g = open("DATABASE/DATABASE1", 'w')

		try:
			while True:
				temp = f.readline()
				if temp == entry:
					g.write(temp)
					break
				g.write(temp)               # Traverse through DB until entry is found
		except Exception:
			raise IOError

		g.write("\t" + friendsName + "\n")
		for line in f:
			g.write(line)
        
		f.close()
		g.close()

		os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE")
		os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE1", os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE")

		f = open("DATABASE/DATABASE", 'r')
		g = open("DATABASE/DATABASE1", 'w')

		try:
			while True:
			    temp = f.readline()
			    if friendsName in temp and "\t" not in temp:
			        g.write(temp)
			        break
			    g.write(temp)               # Traverse through DB until entry is found
		except Exception:
			raise IOError

		g.write("\t" + self.get_name() + "\n")
		for line in f:
		    g.write(line)

		f.close()
		g.close()

		os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE")
		os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE1", os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE")

    def deleteFromRegistry(self, friendsName):
		entry = self.get_name() + ": " + self.get_password() + "\n"
		f = open("DATABASE/DATABASE", 'r')
		g = open("DATABASE/DATABASE1", 'w')

		try:
			while True:
				temp = f.readline()
				if temp == entry:
					g.write(temp)
					break
				g.write(temp)               # Traverse through DB until entry is found

		except Exception:
			raise IOError

		for line in f:
			if line == "\t" + friendsName + "\n":
				continue
			g.write(line)

		f.close()
		g.close()

		os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE")
		os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE1", os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE")

		f = open("DATABASE/DATABASE", 'r')
		g = open("DATABASE/DATABASE1", 'w')

		try:
		    while True:
		        temp = f.readline()
		        if friendsName in temp and "\t" not in temp:
		            g.write(temp)
		            break
		        g.write(temp)               # Traverse through DB until entry is found
		except Exception:
			raise IOError

		for line in f:
		    if line == "\t" + self.get_name() +"\n":
		        continue
		    g.write(line)

		f.close()
		g.close()

		os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE")
		os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE1", os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE")


class import_database(registryDatabase): #importing data from the profile's database

    def __init__(self):
        registryDatabase.__init__(self)
        self.displayname = ""
        self.firstname = ""
        self.lastname = ""
        self.details = []
        self.status = {}
        self.onoroff = ""
        self.DP = "GUIE/default.gif"
        self.wall = {}
        self.messages = {}
        self.messages_sent = {}
        self.friend_requests = []
        self.friend_requests_sent = []
        self.messages_copy = {}
        self.friend_requests_copy = []

        self.pool = []

    def get_display_name(self):
        return self.displayname

    def get_first_name(self):
        return self.firstname

    def get_last_name(self):
        return self.lastname

    def get_DP(self):
        return self.DP

    def get_onoroff(self):
        return self.onoroff

    def get_details(self):
        return self.details

    def get_status(self):
        return self.status

    def get_messages(self):
        return self.messages

    def get_messages_sent(self):
        return self.messages_sent

    def get_friend_requests(self):
        return self.friend_requests

    def get_friend_requests_sent(self):
        return self.friend_requests_sent

    def get_wall(self):
        return self.wall

    def get_messages_copy(self):
        return self.messages_copy

    def get_friend_requests_copy(self):
        return self.friend_requests_copy

    def get_pool(self):
        return self.pool

    def import_pool(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/DATABASE", "r")        
        for line in f:
            if "\t" in line:
                continue
            else:
                if line == "\n":
                    continue
                else:
                    temp = line.split(": ")
                    if temp[0] == name:
                        continue
                    self.pool.append(temp[0])       
        f.close()

    def import_all(self, name):
        try:            
            self.import_display_name(name)
            self.import_details(name)
            self.import_DP(name)
            self.import_friends(name)
            self.import_status(name)
            self.import_messages(name)
            self.import_messages_sent(name)
            self.import_friend_requests(name)
            self.import_friend_requests_sent(name)
            self.import_wall(name)
            self.import_pool(name)
        except:
            raise IOError

    def import_display_name(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        f.readline()
        a = f.readline().split("|")
        a[1] = a[1].rstrip()
        self.firstname = a[0]
        self.lastname = a[1]
        self.displayname = self.firstname + " " + self.lastname        
        f.close()

    def import_onoroff(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        for line in f:
            if line == 'Offline\n' or line == 'Online\n' or line == 'Offline Setup\n':
                break
        self.onoroff = line.rstrip()
        f.close()

    def import_basics(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        self.name = name     #username from the login username entry
        f.readline()
        f.readline()
        self.password = f.readline()
        f.close()

    def import_details(self, name):
        self.details = []
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        f.readline()    #details
        f.readline()    #name
        f.readline()    #password
        self.details.append(f.readline().rstrip())      #gender
        for line in f:
            if line == 'Offline\n' or line == 'Online\n' or line == 'Offline Setup\n':
                break
            self.details.append(eval(line.rstrip()))
        f.close()

    def import_DP(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True:
            temp = f.readline()
            if temp == "DP\n":
                break
        temp = f.readline()
        temp = temp[0:-1]
        self.DP = temp
        f.close()    

    def import_status(self, name): #importing status
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True: #scanning untill it reaches the status
            temp = f.readline()
            if temp == "Status\n":
                break
        temp = eval(f.readline().rstrip())
        self.status = collections.OrderedDict(sorted(temp.items()))
        f.close()

    def import_messages(self, name): #importing messages
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True: #scanning untill it reaches the messages
            temp = f.readline()
            if temp == "Messages Recieved\n":
                break
        messages = f.readline()
        f.close()
        messages = eval(messages)
        self.messages = {}
        for key in messages.iterkeys():
            a = []
            for counter in range(len(messages[key])):
                x = message_object()
                x.set_reciever(name)
                x.set_sender(key)
                temp = messages[key][counter].split(':')
                x.set_date(temp[0])
                x.set_text(temp[1])
                a.append(x)
            self.messages[key] = a

    def import_messages_sent(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True: #scanning untill it reaches the messages
            temp = f.readline()
            if temp == "Messages Sent\n":
                break
        messages = f.readline()
        f.close()
        messages = eval(messages)
        self.messages_sent = {}
        for key in messages.iterkeys():
            a = []
            for counter in range(len(messages[key])):
                x = message_object()
                x.set_reciever(name)
                x.set_sender(key)
                temp = messages[key][counter].split(':')
                x.set_date(temp[0])
                x.set_text(temp[1])
                a.append(x)
            self.messages_sent[key] = a

    def import_friend_requests(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True:
            temp = f.readline()
            if temp == "Friend Requests Recieved\n":
                break
        self.friend_requests = f.readline().rstrip()
        f.close()

    def import_friend_requests_sent(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True:
            temp = f.readline()
            if temp == "Friend Requests Sent\n":
                break
        self.friend_requests_sent = f.readline().rstrip()
        f.close()

    def import_wall(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True:
            temp = f.readline()
            if temp == "Wall\n":
                break
        self.wall = f.readline().rstrip()
        f.close()

    def import_messages_copy(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True:
            temp = f.readline()
            if temp == "Messages Copy\n":
                break
        self.messages_copy = eval(f.readline().rstrip())
        f.close()

    def import_friend_requests_copy(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        while True:
            temp = f.readline()
            if temp == "Friend Requests Recieved Copy\n":
                break
        self.friend_requests_copy = f.readline().rstrip()
        f.close()


class export_database(): #exporting data to the database by creating a temporary file, deleting the original file, then renaming the temporary file

    def export_onoroff(self, name, onoroff):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + "1", 'w')
        for x in f:
            if x == "Offline Setup\n" or x == "Offline\n" or x == "Online\n":
                g.write(onoroff+"\n")
            else:
                g.write(x)
        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)        

    def export_details(self, name, password, firstname=None, lastname=None, gender=None, birthday=None, jobs=None, education=None): #exporting username and password
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + "1", 'w')
        if gender != None:
            g.write(f.readline())       #Details 2013-20376
            g.write(firstname + '|' + lastname + '\n')    #DISPLAYNAME
            f.readline()                # Skip reading the name from f
            g.write(f.readline())       #Write the Password (from f's readline) to g
            g.write(gender + '\n')
            g.write(str(birthday) + '\n')
            g.write(str(jobs) + '\n')
            g.write(str(education) + '\n')
            f.readline()                #Skip the gender
            f.readline()
            f.readline()
            f.readline()
            for x in f:
                g.write(x)
        else:            
            for line in f:
                g.write(line)
        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)

    def export_DP(self, name, DPPath):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + "1", 'w')
        for x in range(10):
            g.write(f.readline())          
        
        g.write(str(DPPath)+"\n")
        f.readline()
        for line in f:
            g.write(line)

        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)

    def export_friends(self, name, friends): #exporting friends list
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + "1", 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Friends\n":
                break
        g.write(str(friends) + '\n')
        f.readline()
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        '''
        f = open("DATABASE/DATABASE")
        g = open("DATABASE/DATABASE" + '1', 'w')
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
        os.remove("DATABASE/DATABASE")
        os.rename("DATABASE/DATABASE" + '1', "DATABASE/DATABASE")
        '''

    def export_status(self, name, status, time): #exporting status
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + "1", 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Status\n":
                break
        temp = eval(f.readline())
        temp[time] = status
        g.write(str(temp) + '\n')
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)

    def export_messages(self, name, message, time, reciever):
        message = str(message)
        time = str(time)
        reciever = str(reciever)
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Messages Recieved\n":
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
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)

    def export_sent_messages(self, name, message, time, sender):
        message = str(message)
        time = str(time)
        sender = str(sender)
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Messages Sent\n":
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
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)

    def export_friend_request(self, name, friend_requests):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Friend Requests Recieved\n":
                break
        g.write(str(friend_requests) + '\n')
        f.readline()
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)

    def export_friend_request_sent(self, name, friend_requests_sent):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Friend Requests Sent\n":
                break
        g.write(str(friend_requests_sent) + '\n')
        f.readline()
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)

    def export_wall(self, name, wall):
        wall = str(wall)
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + '1', 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Wall\n":
                break
        g.write(wall + '\n')
        f.readline()
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name+ '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)

    def export_messages_copy(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + "1", "w")
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Messages Recieved\n":
                break
        x = f.readline()
        g.write(x)
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Messages Copy\n":
                break
        f.readline()
        g.write(x)
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name+ '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)

    def export_friend_requests_copy(self, name):
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name + "1", "w")
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Friend Requests Recieved\n":
                break
        x = f.readline()
        g.write(x)
        while True:
            temp = f.readline()
            g.write(temp)
            if temp == "Friend Requests Recieved Copy\n":
                break
        f.readline()
        g.write(x)
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)
        os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name+ '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + name + "/" + name)


class logout(object): #will reset the name and password of CC after returning to the main GUI

    def __init__(self):
        self.quit = CC()
        self.exporter = export_database()

    def exit(self, name, password):
        self.exporter.export_details(name)
        self.quit.set_name('')
        self.quit.set_password('')


class message_object():
    def __init__(self):
        self.sender = ''
        self.reciever = ''
        self.date = ''
        self.text = ''

    def get_sender(self):
        return self.sender

    def get_reciever(self):
        return self.reciever

    def get_date(self):
        return self.date

    def get_text(self):
        return self.text

    def set_sender(self, name):
        self.sender = name

    def set_reciever(self, name):
        self.reciever = name

    def set_date(self, date):
        self.date = date

    def set_text(self, message):
        self.text = message
