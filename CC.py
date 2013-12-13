class CC:
    def __init__(self):
        self.name = ''
        self.password = ''
    def set_name(self, name):
        self.name = name
    def set_password(self, password):
        self.password = password
    def get_name(self):
        return self.name
    def get_password(self):
        return self.password

class create(CC):
    def ask_name(self):
        self.name = raw_input("Username: ")
    def ask_password(self):
        self.password = raw_input("Password: ")
    def create(self):
        f = open(self.name, 'w')
        f.write(self.name + '\n')
        f.write(self.password)
        f.close()

class validation(CC):
        def validation(self):
            self.name = raw_input("Username: ")
            f = open(self.name)
            f.readline()
            self.password = raw_input("Password: ")
            if self.password == f.readline():
                return self.name
            return 0

class delete(CC):
    def delete(self):
        valid = validation()
        self.name = valid.validation()
        if self.name != 0:
            import os
            os.delete(self.name)

class login(CC):
    def login(self):
        valid = validation()
        self.name = valid.validation()
        if self.name != 0:
            return 1
        else:
            print "Username/Password is invalid"

class import_database:
    def __init__(self):
        self.name = ''
        self.password = ''
        self.friends = []
        self.status = ''
        self.wall = {}
        self.messages = {{}}
    def set_name(self):
        name = login()
        self.name = name.get_name()
    def set_password(self):
        password = login()
        self.password = password.get_password()
    def import_friends(self):
        f = open(self.name)
        while True:
            temp = f.readline()
            if temp == None:
                break
            self.friends.append(temp)
            temp = None
        f.close()
    def status(self):
        f = open(self.name)
        counter = 0
        while counter < 2:
            if f.readline() == '\n':
                counter += 1
        self.status = f.readline()
        f.close()

class export_database(import_database):
    def details(self):
        f = open(self.name, 'w')
        f.write(self.name, + "\n")
        f.write(self.password + "\n")
        f.close()
    def friends(self):
        f = open(self.name, 'a')
        counter = 0
        while True:
            if self.friends[counter] == None:
                break
            f.write(self.friends[counter] + "\n")
            counter += 1
        f.close()
class exit:
    def exit(self):
        control = CC()
        control.set_name('')
        control.set_password('')
