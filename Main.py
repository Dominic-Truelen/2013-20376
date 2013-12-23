from CC import import_database, export_database
from time import strftime
import glob, os
class messages(import_database):
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
        ##sort the messages by name and by date before printing
    def send_message(self, name):
        importer = import_database()
        export = export_database()
        reciever = raw_input("Send to: ")
        if glob.glob(reciever) == []:
            print "User does not exist"
        elif reciever == name:
            print "You cannot send messages to yourself"
        else:
            message = raw_input("Message: ")
            time = strftime("%m/%d/%Y, %I-%M%p")
            export.export_sent_messages(name, message, time, reciever)
            export.export_messages(reciever, message, time, name)

class status(import_database):
    def __init__(self):
        self.name = ''
        self.friends = []
        self.status = ''
        self.wall = {}
        self.export = export_database()
    def get_status(self, name):
        temp = import_database()
        temp.import_status(name)
        self.status = temp.get_status()
    def create_status(self):
        self.status = raw_input("Enter your status: ")
    def status_export(self, name):
        self.export.export_status(name, self.status)
    def print_status(self):
        print self.status

class friends(import_database):
    def __init__(self):
        self.name = ''
        self.friends = []
        self.friend_requests = []
        self.friend_requests_sent = []
        self.export_friends = export_database()
        self.import_friends = import_database()
    def see_friends(self, name):
        self.import_friends.import_friends(name)
        self.friends = self.import_friends.get_friends()
        counter = 0
        while True:
            if counter + 1 > len(self.friends):
                break
            print self.friends[counter]
            counter += 1
    def add_friend(self, name):
        add_friend = str(raw_input("Add who? "))
        if glob.glob(add_friend) == []:
            print "User does not exist"
        elif add_friend == name:
            print "You cannot send yourself a friend request"
        else:
            sender = name
            self.import_friends.import_friend_requests_sent(name)
            self.friend_requests_sent = eval(self.import_friends.get_friend_requests_sent())
            if str(add_friend) in self.friend_requests_sent:
                print "You already sent a friend request"
            else:
                self.friend_requests_sent.append(str(add_friend))
                f = open(name)
                g = open(name + '1', 'w')
                while True:
                    temp = f.readline()
                    g.write(temp)
                    if "Friend Requests Sent 2013-20376" in temp:
                        break
                g.write(str(self.friend_requests_sent) + '\n')
                f.readline()
                for line in f:
                    g.write(line)
                f.close()
                g.close()
                os.remove(name)
                os.rename(name + '1', name)
                self.import_friends.set_name(add_friend)
                self.friend_requests = eval(self.import_friends.get_friend_requests())
                self.friend_requests.append(str(sender))
                f = open(add_friend)
                g = open(add_friend + '1', 'w')
                while True:
                    temp = f.readline()
                    g.write(temp)
                    if "Friend Requests Recieved 2013-20376" in temp:
                        break
                g.write(str(self.friend_requests) + '\n')
                f.readline()
                for line in f:
                    g.write(line)
                f.close()
                g.close()
                os.remove(add_friend)
                os.rename(add_friend + '1', add_friend)
    def see_friend_requests(self, name):
        self.import_friends.import_friend_requests(name)
        self.import_friends.import_friend_requests_sent(name)
        self.friend_requests = self.import_friends.get_friend_requests()
        self.friend_requests_sent = self.import_friends.get_friend_requests_sent()
        print self.friend_requests
        print self.friend_requests_sent
    def friends_export(self):
        self.export_friends.export_friends(self, friends)
    def delete_friends(self, name):
        self.import_friends.import_friends(name)
        self.friends = self.import_friends.get_friends()
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
            f = open(name)
            g = open(name + '1', 'w')
            while True:
                temp = f.readline()
                g.write(temp)
                if "Friends 2013-20376" in temp:
                    break
            g.write(str(self.friends) + '\n')
            f.readline()
            for line in f:
                g.write(line)
            f.close()
            g.close()
            os.remove(name)
            os.rename(name + '1', name)
            self.import_friends.set_name(delete)
            friends = self.import_friends.get_friends()
            counter = 0
            while counter + 1 <= len(self.friends):
                if self.friends[counter] == name:
                    self.friends.remove(name)
                counter += 1
            f = open(delete)
            g = open(delete + '1', 'w')
            while True:
                temp = f.readline()
                g.write(temp)
                if "Friends 2013-20376" in temp:
                    break
            g.write(str(friends) + '\n')
            f.readline()
            for line in f:
                g.write(line)
            f.close()
            g.close()
            os.remove(delete)
            os.rename(delete + '1', delete)
    def approve_request(self, name):
        friend = str(raw_input("Approve who? "))
        self.import_friends.import_friends(name)
        self.import_friends.import_friend_requests(name)
        self.friend_requests = self.import_friends.get_friend_requests()
        self.friends = self.import_friends.get_friends()
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
            f = open(name)
            g = open(name + '1', 'w')
            while True:
                temp = f.readline()
                g.write(temp)
                if "Friends 2013-20376" in temp:
                    break
            self.friends.append(friend)
            g.write(str(self.friends))
            g.write('\n')
            f.readline()
            while True:
                temp = f.readline()
                g.write(temp)
                if "Friend Requests Recieved 2013-20376" in temp:
                    break
            g.write(str(self.friend_requests) + '\n')
            f.readline()
            for line in f:
                g.write(line)
            f.close()
            g.close()
            os.remove(name)
            os.rename(name + '1', name)
            self.import_friends.set_name(friend)
            self.import_friends.import_friends(friend)
            self.import_friends.import_friend_requests_sent(friend)
            self.friend_requests_sent = self.import_friends.get_friend_requests_sent()
            self.friends = self.import_friends.get_friends()
            f = open(friend)
            g = open(friend + '1', 'w')
            while True:
                temp = f.readline()
                g.write(temp)
                if "Friends 2013-20376" in temp:
                    break
            self.friends.append(name)
            g.write(str(self.friends))
            g.write('\n')
            f.readline()
            while True:
                temp = f.readline()
                g.write(temp)
                if "Friend Requests Sent 2013-20376" in temp:
                    break
            self.friend_requests_sent = eval(self.friend_requests_sent)
            counter = 0
            while counter + 1 <= len(self.friend_requests_sent):
                if self.friend_requests_sent[counter] == name:
                    self.friend_requests_sent.remove(name)
                counter += 1
            g.write(str(self.friend_requests_sent))
            g.write('\n')
            f.readline()
            for line in f:
                g.write(line)
            f.close()
            g.close()
            os.remove(friend)
            os.rename(friend + '1', friend)