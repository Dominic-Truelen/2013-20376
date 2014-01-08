from CC import import_database, export_database
from time import strftime
import glob
import os

class messages():
    def __init__(self):
        self.messages = []
        self.messages_sent = []
        self.importer = import_database()
        self.exporter = export_database()

    def get_messages(self, name): #Importing the messages
        temp = import_database()
        temp.import_messages(name)
        self.messages = temp.get_messages()
        temp.import_messages_sent(name)
        self.messages_sent = temp.get_messages_sent()

    def print_messages(self): #Displaying the messages
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
        print message #Printing the messages recieved
        friend_name = self.messages_sent.keys()
        friend_message = self.messages_sent.values()
        counter = 0
        while True:
            if counter + 1 > len(friend_name):
                break
            message_sent.append({str(friend_name[counter]):str(friend_message[counter])})
            counter += 1
        print message_sent #Printing the messages sent
        #sort the messages by name and by date before printing (incomplete)

    def send_message(self, name): #Sending messages
        reciever = raw_input("Send to: ")
        if glob.glob(reciever) == []: #Searching for a file with the inputed name in the directory
            print "User does not exist"
        elif reciever == name:
            print "You cannot send messages to yourself"
        else:
            message = raw_input("Message: ")
            time = strftime("%m/%d/%Y, %I.%M%p") #Format for the time
            self.exporter.export_sent_messages(name, message, time, reciever) #Exporting sent message
            self.exporter.export_messages(reciever, message, time, name) #Exporting the recieved message

class status():
    def __init__(self):
        self.name = ''
        self.status = ''
        self.importer = import_database()
        self.exporter = export_database()

    def get_status(self, name): #Importing the status
        self.importer.import_status(name)
        self.status = self.importer.get_status()

    def create_status(self): #Overwritting the status
        self.status = raw_input("Enter your status: ")

    def status_export(self, name): #Exporting the status
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

    def see_friends(self, name): #Displaying the friends of the active user
        self.importer.import_friends(name) #Imported the friends
        self.friends = self.importer.get_friends() #Accessed the friends
        counter = 0
        while True:
            if counter + 1 > len(self.friends):
                break
            print self.friends[counter]
            counter += 1

    def add_friend(self, name): #Adding new friends
        add_friend = str(raw_input("Add who? "))
        if glob.glob(add_friend) == []: #Serching for a file with the inputed name in the directory
            print "User does not exist"
        elif add_friend == name:
            print "You cannot send yourself a friend request"
        else:
            self.importer.import_friend_requests(name)
            self.friend_requests = eval(self.importer.get_friend_requests())
            if add_friend in self.friend_requests: #If the user has sent you a request
                print "This user has already sent you a friend request"
            else:
                self.importer.import_friend_requests_sent(name)
                self.friend_requests_sent = eval(self.importer.get_friend_requests_sent())
                if str(add_friend) in self.friend_requests_sent: #If you already sent the user a request
                    print "You already sent a friend request"
                else:
                    self.friend_requests_sent.append(str(add_friend)) #Append the friend to the list of your sent friend requests
                    self.exporter.export_friend_request_sent(name, self.friend_requests_sent) #Exporting the list of friend requests sent
                    self.importer.import_friend_requests(add_friend) #Import list of friend requests of the reciever
                    self.friend_requests = eval(self.importer.get_friend_requests())
                    self.friend_requests.append(str(name)) #Append yourself to the list of the reciever's friend requests
                    self.exporter.export_friend_request(add_friend, self.friend_requests) #Exporting the list of friend requests

    def see_friend_requests(self, name): #Displaying the friend requests recieved and sent
        self.importer.import_friend_requests(name)
        self.friend_requests = self.importer.get_friend_requests()
        self.importer.import_friend_requests_sent(name)
        self.friend_requests_sent = self.importer.get_friend_requests_sent()
        print self.friend_requests
        print self.friend_requests_sent

    def delete_friends(self, name):
        delete = raw_input("Delete who? ")
        if glob.glob(delete) == []:
            print "User does not exist"
        else:
            self.importer.import_friends(name)
            self.friends = eval(self.importer.get_friends())
            if delete not in self.friends:
                print "User is not your friend"
            else:
                self.friends.remove(delete)
                self.exporter.export_friends(name, self.friends)
                self.importer.import_friends(delete)
                friends = self.importer.get_friends()
                self.friends.remove(name)
                self.exporter.export_friends(delete, self.friends)

    def approve_request(self, name):
        friend = str(raw_input("Approve who? "))
        if glob.glob(friend) == []:
            print "This user does not exist"
        else:
            self.importer.import_friend_requests(name)
            self.friend_requests = self.importer.get_friend_requests()
            if friend not in self.friend_requests:
                print "The user did not send a friend request"
            else:
                self.friend_requests = eval(self.friend_requests)
                self.friend_requests.remove(friend)
                self.importer.import_friends(name)
                self.friends = self.importer.get_friends()
                self.friends.append(friend)
                self.exporter.export_friends(name, self.friends)
                self.exporter.export_friend_request(name, self.friend_requests)
                self.importer.import_friend_requests_sent(friend)
                self.friend_requests_sent = self.importer.get_friend_requests_sent()
                self.friend_requests_sent = eval(self.friend_requests_sent)
                self.friend_requests_sent.remove(name)
                self.importer.import_friends(friend)
                self.friends = self.importer.get_friends()
                self.friends.append(str(name))
                self.exporter.export_friends(friend, self.friends)
                self.exporter.export_friend_request_sent(friend, self.friend_requests_sent)