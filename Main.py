from CC import import_database, export_database
from datetime import datetime
import glob, os

class messages(import_database):
    def get_messages(self):
        temp = import_database()
        self.messages = temp.get_messages()
    def print_messages(self):
        friend_name = []
        friend_message = []
        friend_name = self.messages.keys()
        ## missing stuff

class status(import_database):
    def __init__(self):
        super(status, import_database)
        self.export = export_database()
    def create_status(self):
        self.status = raw_input()
    def status_export(self):
        self.export.export_status(self.status)

class friends(import_database):
    def __init__(self):
        super(friends, import_database)
        self.export_friends = export_database()
    def see_friends(self):
        counter = 0
        while True:
            if friends[counter] == '':
                break
            print friends[counter]
    def add_friend(self):
        add_friend = raw_input()
        if glob.glob(add_friend) == []:
            print "User does not exist"
        else:
            self.friend_requests.append(add_friend)
            f = open(add_friend)
            g = open(add_friend + '1')
            counter = 0
            while counter < 4:
                temp = f.readline()
                g.write(temp)
                if temp == '\n':
                    counter += 1
            g.write(self.friend_requests)
            for line in f:
                g.write(line)
            os.remove(add_friend)
            os.rename(add_friend + '1', add_friend)
    def friends_export(self):
        self.export_friends.export_friends(self, friends)





