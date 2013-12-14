import os ##for deleting and renaming files
class CC: ##profile management ##superclass
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
        self.name = raw_input()
    def ask_password(self): ##GUI imput of password
        self.password = raw_input()
    def create(self): ##creating the database and adding the username and password
        f = open(self.name, 'w')
        f.write(self.name + '\n')
        f.write(self.password)
        f.close()

class validation(CC): ##validation for logging in and deleting profiles
    def validation(self):
        self.name = raw_input()
        f = open(self.name)
        f.readline()
        self.password = raw_input()
        if self.password == f.readline():
            return 1
        return 0

class delete(CC): ##profile deletion
    def __init__(self):
        super(delete, CC)
        self.valid = validation()
    def delete(self):
        temp = self.valid.validation() ##will return 1 if valid and 0 if invalid
        if temp == 1:
            self.name = self.valid.get_name()
            os.delete(self.name) ##deleted the file with that name

class login(CC): ##logging in
    def __init__(self):
        super(login, CC)
        self.valid = validation()
        self.database = import_database()
    def login(self):
        temp = self.valid.validation()##will return 1 if valid and 0 if invalid
        if temp == 1:
            self.database.set_name(self.valid.get_name) ##see import_database
            self.database.set_password(self.valid.get_password)
            self.database.import_friends()
            self.database.import_status()
            self.database.import_messages()
        else:
            print "Username/Password is invalid"

class import_database: ##importing data from the profile's database
    def __init__(self):
        self.name = ''
        self.password = ''
        self.friends = []
        self.status = ''
        self.wall = {}
        self.messages = {}
        self.friend_requests = []
    def set_name(self, name): ##mutator
        self.name = name
    def set_password(self, password): ##mutator
        self.password = password
    def import_friends(self): ##importing friends list
        f = open(self.name)
        while True: ##scanning untill it reaches the newline before the friends list
            temp = f.readline()
            if temp == '' or temp == '\n':
                break
        temp = f.readline()
        self.friends.append(temp)
        f.close()
    def import_status(self): ##importing status
        f = open(self.name)
        counter = 0
        while counter < 2: ##scanning untill it reaches the newline before the status
            if f.readline() == '\n':
                counter += 1
        self.status = f.readline()
        f.close()
    def import_messages(self): ##importing messages
        friend = []
        f = open(self.name)
        counter = 0
        while counter < 3: ##scanning untill it reaches the newline before the messages
            if f.readline() == '\n':
                counter += 1
        counter = 0
        while True: ##scanning untill it reaches the newline after the messages
            temp = f.readline()
            if temp == '' or temp == '\n':
                break
            if ':' in temp: ##if the line is a message, it will be added to the list of messages from that friend
                temp = temp.split(':')
                temp_date = temp[0]
                temp_message = temp[1].split('\n')
                friend.append({temp_message[0]:temp_date})
                self.messages[temp_friend] = friend
                counter += 1
            else: ##if the line is a friend's name, it will be a key of the dictionary
                temp = temp.split('\n')
                self.messages[temp[0]] = ''
                temp_friend = temp[0]
    def get_messages(self): ##accessor
        return self.messages

class export_database(import_database): ##exporting data to the database by creating a temporary file, deleting the original file, then renaming the temporary file
    def export_details(self, name, password): ##exporting username and password
        f = open(self.name)
        g = open(self.name + "1", 'w')
        g.write(name)
        g.write(password)
        for line in f:
            g.write(line)
        os.remove(self.name)
        os.rename(self.name + '1', self.name)
        g.close()
    def export_friends(self, friends): ##exporting friends list
        f = open(self.name)
        g = open(self.name + "1", 'w')
        counter = 0
        while counter < 1:
            temp = f.readline()
            if temp == '\n':
                counter += 1
            g.write(temp)
        counter = 0
        while True:
            if friends[counter] == '':
                break
            g.write(friends[counter])
        for line in f:
            g.write(line)
        os.remove(self.name)
        os.rename(self.name + '1', self.name)
        g.close()
    def export_status(self, status): ##exporting status
        f = open(self.name)
        g = open(self.name + "1", 'w')
        counter = 0
        while counter < 2:
            temp = f.readline()
            if temp == '\n':
                counter += 1
            g.write(temp)
        g.write(status)
        for line in f:
            g.write(line)
        os.remove(self.name)
        os.rename(self.name + '1', self.name)
        g.close()

class logout: ##will reset the name and password of CC after returning to the main GUI
    def __init__(self):
        self.quit = CC()
    def exit(self):
        quit.set_name('')
        quit.set_password('')