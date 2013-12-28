import os ##for deleting and renaming files
import glob
class CC(object): ##profile management ##superclass
    def __init__(self):
        self.name = ''
        self.password = ''
    def set_name(self, name): ##mutator
        self.name = name
    def set_password(self, password): ##mutator
        self.password = password
    def get_name(self): ##accessor
        return self.name
    def get_password(self): ##accessor
        return self.password

class create(CC): ##profile creation
    def ask_name(self): ##GUI imput of username
        while True:
            self.name = raw_input("Enter username: ")
            if glob.glob(self.name) == []:
                break
            print "Username is taken"
    def ask_password(self): ##GUI imput of password
        self.password = raw_input("Enter password: ")
    def create(self): ##creating the database and adding the username and password
        f = open(self.name, 'w')
        f.write("Details 2013-20376\n" + self.name + '\n' + self.password + '\n\n' + "Friends 2013-20376\n" + '[]\n\n' + "Status 2013-20376\n" + "\n" + "Messages Recieved 2013-20376\n" + '[]\n\n' + "Messages Sent 2013-20376\n" + '[]\n\n' + "Friend Requests Recieved 2013-20376\n" + "[]\n\n" + "Friend Requests Sent 2013-20376\n" + "[]\n\n" + "Wall 2013-20376\n" + '\n')
        f.close()

class validation(CC): ##validation for logging in and deleting profiles
    def validation(self):
        self.set_name(raw_input("Username: "))
        if glob.glob(self.get_name()) == []:
            return 0
        f = open(self.get_name())
        f.readline()
        f.readline()
        self.set_password(raw_input("Password: "))
        if (self.get_password() + '\n') == f.readline():
            return 1
        return 0

class delete(CC): ##profile deletion
    def __init__(self):
		super(delete, self).__init__()
		self.valid = validation()
    def delete(self):
        temp = self.valid.validation() ##will return 1 if valid and 0 if invalid
        if temp == 1:
            self.name = self.valid.get_name()
            os.remove(self.name) ##deletes the filename with name of profile
	else:
		print "There is no such profile to delete!"

class login(CC): ##logging in
    def __init__(self):
		super(login, self).__init__()
		self.valid = validation()
		self.database = import_database()
    def login(self):
        temp = self.valid.validation()##will return 1 if valid and 0 if invalid
        if temp == 1:
            self.name = self.valid.get_name()
            self.database.set_name(self.name) ##see import_database
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

class import_database(object): ##importing data from the profile's database
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
    def set_name(self, name): ##mutator
        self.name = name
    def set_password(self, password): ##mutator
        self.password = password
    def get_name(self):
        return self.name
    def get_password(self):
        return self.password
    def get_friends(self):
        return self.friends
    def get_status(self):
        return self.status
    def get_messages(self): ##accessor
        return self.messages
    def get_messages_sent(self):
        return self.messages_sent
    def get_friend_requests(self):
        return self.friend_requests
    def get_friend_requests_sent(self):
        return self.friend_requests_sent
    def import_friends(self, name): ##importing friends list
        f = open(name)
        while True: ##scanning untill it reaches the friends list
            temp = f.readline()
            if "Friends 2013-20376" in temp:
                break
        temp = f.readline()
        self.friends = []
        self.friends += eval(temp)
        f.close()
    def import_status(self, name): ##importing status
        f = open(name)
        while True: ##scanning untill it reaches the status
            temp = f.readline()
            if "Status 2013-20376" in temp:
                break
        self.status = f.readline()
        f.close()
    def import_messages(self, name): ##importing messages
        self.messages = {}
        friend = []
        f = open(name)
        while True: ##scanning untill it reaches the messages
            temp = f.readline()
            if "Messages Recieved 2013-20376" in temp:
                break
        while True: ##scanning untill it reaches the newline after the messages
            temp = f.readline()
            if temp == '\n':
                break
            if ':' in temp: ##if the line is a message, it will be added to the list of messages from that friend
                temp = temp.split(':')
                temp_date = temp[0]
                temp_message = temp[1]
                temp_message = temp_message.split('\n')
                temp_message = temp_message[0]
                friend.append({temp_date:temp_message})
                self.messages[temp_friend] = friend
            else: ##if the line is a friend's name, it will be a key of the dictionary
                temp = temp.split('\n')
                self.messages[temp[0]] = ''
                temp_friend = temp[0]
                friend = []
    def import_messages_sent(self, name):
        self.messages_sent = {}
        friend = []
        f = open(name)
        while True: ##scanning untill it reaches the messages
            temp = f.readline()
            if "Messages Sent 2013-20376" in temp:
                break
        while True: ##scanning untill it reaches the newline after the messages
            temp = f.readline()
            if temp == '\n':
                break
            if ':' in temp: ##if the line is a message, it will be added to the list of messages from that friend
                temp = temp.split(':')
                temp_date = temp[0]
                temp_message = temp[1]
                temp_message = temp_message.split('\n')
                temp_message = temp_message[0]
                friend.append({temp_date:temp_message})
                self.messages_sent[temp_friend] = friend
            else: ##if the line is a friend's name, it will be a key of the dictionary
                temp = temp.split('\n')
                self.messages_sent[temp[0]] = ''
                temp_friend = temp[0]
                friend = []
    def import_friend_requests(self, name):
        f = open(name)
        while True:
            temp = f.readline()
            if "Friend Requests Recieved 2013-20376" in temp:
                break
        temp = f.readline()
        self.friend_requests = temp
    def import_friend_requests_sent(self, name):
        f = open(name)
        while True:
            temp = f.readline()
            if "Friend Requests Sent 2013-20376" in temp:
                break
        temp = f.readline()
        temp = temp.split('\n')
        temp = temp[0]
        self.friend_requests_sent = temp

class export_database(import_database): ##exporting data to the database by creating a temporary file, deleting the original file, then renaming the temporary file
    def export_details(self, name, password): ##exporting username and password
        f = open(name, 'r+')
        g = open(name + "1", 'w+')
        g.write('Details 2013-2076' + '\n' + name + '\n' + password + '\n')
        for line in f:
            g.write(line + '\n')
        os.remove(name)
        os.rename(name + '1', name)
        g.close()
    def export_friends(self, name, friends): ##exporting friends list
        f = open(name + 'r')
        g = open(name + "1", 'w')
        while True:
            temp = f.readline()
            g.write(temp + '\n')
            if 'Friends 2013-20376' in temp:
                break
        g.write(friends + '\n')
        f.readline()
        for line in f:
            g.write(line + '\n')
        os.remove(name)
        os.rename(name + '1', name)
        g.close()
    def export_status(self, name, status): ##exporting status
        f = open(name)
        g = open(name + "1", 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if "Status 2013-20376" in temp:
                break
        g.write(status)
        f.readline()
        for line in f:
            g.write(line + '\n')
        f.close()
        g.close()
        os.remove(name)
        os.rename(name + '1', name)
        g.close()
    def export_messages(self, name, message, time, sender):
        f = open(name)
        g = open(name + '1', 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if "Messages Recieved 2013-20376" in temp:
                break
        while True:
            temp = f.readline()
            if temp == '\n':
                g.write(sender + '\n' + time + ':' + message + '\n\n')
                break
            if temp == sender + '\n':
                g.write(temp)
                while True:
                    temp = f.readline()
                    if temp == '\n' or temp == '':
                        g.write(time + ':' + message + '\n\n')
                        break
                    g.write(temp)
                break
            g.write(temp)
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(name)
        os.rename(name + '1', name)
    def export_sent_messages(self, name, message, time, reciever):
        f = open(name)
        g = open(name + '1', 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if "Messages Sent 2013-20376" in temp:
                break
        counter = 0
        while True:
            temp = f.readline()
            if temp == '\n':
                g.write(reciever + '\n' + time + ':' + message + '\n\n')
                break
            if temp == reciever + '\n':
                g.write(temp)
                while True:
                    temp = f.readline()
                    if temp == '\n' or temp == '':
                        g.write(time + ':' + message + '\n\n')
                        break
                    g.write(temp)
                break
            g.write(temp)
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(name)
        os.rename(name + '1', name)

class logout(object): ##will reset the name and password of CC after returning to the main GUI
    def __init__(self):
        self.quit = CC()
    def exit(self):
        self.quit.set_name('')
        self.quit.set_password('')