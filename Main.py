from CC import import_database, export_database
from time import strftime
import glob, os
class messages():
    def __init__(self):
        self.messages = []
        self.messages_sent = []
        self.importer = import_database()
        self.exporter = export_database()
    def get_messages(self, name):
        temp = import_database()
        temp.import_messages(name)
        self.messages = temp.get_messages()
        temp.import_messages_sent(name)
        self.messages_sent = temp.get_messages_sent()
    def print_messages(self):
        message = []
        message_sent = []
        friend_name = self.messages.keys()
        friend_message = self.messages.values()
        counter = 0
        while True:
            if counter + 1 > len(friend_name):
                break
            message.append({str(friend_name[counter]):str(friend_message[counter])})
            counter += 1
        print message
        friend_name = self.messages_sent.keys()
        friend_message = self.messages_sent.values()
        counter = 0
        while True:
            if counter + 1 > len(friend_name):
                break
            message_sent.append({str(friend_name[counter]):str(friend_message[counter])})
            counter += 1
        print message_sent
        #sort the messages by name and by date before printing (incomplete)
    def send_message(self, name):
        reciever = raw_input("Send to: ")
        if glob.glob(reciever) == []:
            print "User does not exist"
        elif reciever == name:
            print "You cannot send messages to yourself"
        else:
            message = raw_input("Message: ")
            time = strftime("%m/%d/%Y, %I.%M%p")
            self.exporter.export_sent_messages(name, message, time, reciever)
            self.exporter.export_messages(reciever, message, time, name)

class status():
    def __init__(self):
        self.name = ''
        self.status = ''
        self.importer = import_database()
        self.exporter = export_database()
    def get_status(self, name):
        self.importer.import_status(name)
        self.status = self.importer.get_status()
    def create_status(self):
        self.status = raw_input("Enter your status: ")
    def status_export(self, name):
        self.exporter.export_status(name, self.status)
    def print_status(self):
        print self.status

class friends():
    def __init__(self):
        self.name = ''
        self.friends = []
        self.friend_requests = []
        self.friend_requests_sent = []
        self.exporter = export_database()
        self.importer = import_database()
    def see_friends(self, name):
        self.importer.import_friends(name)
        self.friends = self.importer.get_friends()
        counter = 0
        while True:
            if counter + 1 > len(self.friends):
                break
            print self.friends[counter]
            counter += 1
    def add_friend(self, name):
        add_friend = str(raw_input("Add who? "))
        self.friend_requests
        if glob.glob(add_friend) == []:
            print "User does not exist"
        elif add_friend == name:
            print "You cannot send yourself a friend request"
        else:
            self.importer.import_friend_requests(name)
            self.friend_requests = eval(self.importer.get_friend_requests())
            if add_friend in self.friend_requests:
                print "This user has already sent you a friend request"
            else:
                self.importer.import_friend_requests_sent(name)
                self.friend_requests_sent = eval(self.importer.get_friend_requests_sent())
                if str(add_friend) in self.friend_requests_sent:
                    print "You already sent a friend request"
                else:
                    self.friend_requests_sent.append(str(add_friend))
                    self.exporter.export_friend_request_sent(name, add_friend, self.friend_requests_sent)
                    self.importer.set_name(add_friend)
                    self.friend_requests = eval(self.importer.get_friend_requests())
                    self.friend_requests.append(str(name))
                    self.exporter.export_friend_request(name, add_friend, self.friend_requests)
    def see_friend_requests(self, name):
        self.importer.import_friend_requests(name)
        self.friend_requests = self.importer.get_friend_requests()
        self.importer.import_friend_requests_sent(name)
        self.friend_requests_sent = self.importer.get_friend_requests_sent()
        print self.friend_requests
        print self.friend_requests_sent
    def friends_export(self):
        self.exporter.export_friends(self, friends)
    def delete_friends(self, name):
        self.importer.import_friends(name)
        self.friends = self.importer.get_friends()
        delete = raw_input("Delete who? ")
        if glob.glob(delete) == []:
            print "User does not exist"
        elif delete not in self.friends:
            print "User is not your friend"
        else:
            counter = 0
            while counter + 1 <= len(self.friends):
                if self.friends[counter] == delete:
                    self.friends.remove(delete)
                counter += 1
            self.exporter.export_friends(name, self.friends)
            self.importer.import_friends(delete)
            friends = self.importer.get_friends()
            counter = 0
            while counter + 1 <= len(self.friends):
                if self.friends[counter] == name:
                    self.friends.remove(name)
                counter += 1
            self.exporter.export_friends(delete, self.friends)
    def approve_request(self, name):
        friend = str(raw_input("Approve who? "))
        self.importer.import_friends(name)
        self.importer.import_friend_requests(name)
        self.friend_requests = self.importer.get_friend_requests()
        self.friends = self.importer.get_friends()
        if glob.glob(friend) == []:
            print "This user does not exist"
        elif friend not in self.friend_requests:
            print "The user did not send a friend request"
        else:
            self.friend_requests = eval(self.friend_requests)
            counter = 0
            while counter + 1 <= len(self.friend_requests):
                if self.friend_requests[counter] == friend:
                    self.friend_requests.remove(friend)
                counter += 1
            self.friends.append(friend)
            self.exporter.export_friends(name, self.friends)
            self.exporter.export_friend_request(name, friend, self.friend_requests)
            self.importer.import_friends(friend)
            self.importer.import_friend_requests_sent(friend)
            self.friend_requests_sent = self.importer.get_friend_requests_sent()
            self.friends = self.importer.get_friends()
            self.friend_requests_sent = eval(self.friend_requests_sent)
            counter = 0
            while counter + 1 <= len(self.friend_requests_sent):
                if self.friend_requests_sent[counter] == name:
                    self.friend_requests_sent.remove(name)
                counter += 1
            self.friends.append(name)
            self.exporter.export_friends(friend, self.friends)
            self.exporter.export_friend_request_sent(name, friend, self.friend_requests_sent)