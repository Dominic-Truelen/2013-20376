from CC import import_database, export_database
from time import strftime
from collections import OrderedDict
import glob
import os
import threading
import Queue

class messages():
    def __init__(self):
        self.messages = {}
        self.messages_sent = {}
        self.importer = import_database()
        self.exporter = export_database()

    def get_messages(self, name): #Importing the messages
        self.importer.import_messages(name)
        self.messages = self.importer.get_messages()

    def get_messages_sent(self, name):
        self.importer.import_messages_sent(name)
        self.messages_sent = self.importer.get_messages_sent()

    def print_messages(self): #Displaying the messages
        print self.messages #Printing the messages recieved
        print self.messages_sent #Printing the messages sent
        #sort the messages by name and by date before printing (incomplete)

    def send_message(self, name): #Sending messages
        reciever = str(raw_input("Send to: "))
        if os.path.isdir(os.getcwd() + "/" + name) is False: #Searching for a file with the inputed name in the database
            print "User does not exist"
        elif reciever == name:
            print "You cannot send messages to yourself"
        else:
            message = str(raw_input("Message: "))
            time = strftime("%m/%d/%Y, %I.%M.%S%p") #Format for the time
            self.exporter.export_sent_messages(name, message, time, reciever) #Exporting sent message
            self.exporter.export_messages(reciever, message, time, name) #Exporting the recieved message

    def delete_message(self, name):
        sender = str(raw_input("Delete whose message: "))
        if os.path.isdir(os.getcwd() + "/" + sender) is False:
            print "User does not exist"
            return
        elif self.messages.has_key is False:
            print "User did not send a message"
            return
        date = str(raw_input("Date of the message:"))
        self.importer.import_messages(name)
        self.messages = eval(self.importer.get_messages())
        messages = self.messages[sender]
        counter = 0
        for item in messages:
            if date in item:
                messages.pop(counter)
                f = open(os.getcwd() + "/" + name + "/" + name)
                g = open(os.getcwd() + "/" + name + "/" + name + '1', 'w')
                for line in f:
                    if sender and date not in line:
                        g.write(line)
                    else:
                        g.write(str({str(sender):messages}) + '\n')
                f.close()
                g.close()
                os.remove(os.getcwd() + "/" + name + "/" + name)
                os.rename(os.getcwd() + "/" + name + "/" + name + '1', os.getcwd() + "/" + name + "/" + name)
            counter += 1
        if counter == 0:
            print "Message does not exist"

class status():
    def __init__(self):
        self.name = ''
        self.status = {}
        self.importer = import_database()
        self.exporter = export_database()

    def get_status(self, name): #Importing the status
        self.importer.import_status(name)
        self.status = eval(self.importer.get_status())

    def create_status(self, name): #Overwritting the status
        status = str(raw_input("Enter your status: "))
        time = strftime("%m/%d/%Y, %I.%M.%S%p")
        self.exporter.export_status(name, status, time)

    def print_status(self):
        print self.status

    def delete_status(self, name):
        time = str(raw_input("Date of status: "))
        self.get_status(name)
        if self.status.has_key(time) is False:
            return
        self.status.pop(time)
        f = open(os.getcwd() + "/" + name + "/" + name)
        g = open(os.getcwd() + "/" + name + "/" + name + '1', 'w')
        while True:
            temp = f.readline()
            g.write(temp)
            if "Status 2013-20376" in temp:
                break
        g.write(str(self.status) + '\n')
        f.readline()
        for line in f:
            g.write(line)
        f.close()
        g.close()
        os.remove(os.getcwd() + "/" + name + "/" + name)
        os.rename(os.getcwd() + "/" + name + "/" + name + "1", os.getcwd() + "/" + name + "/" + name)

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
        for counter in range(len(self.friends)):
            print self.friends[counter]

    def add_friend(self, name): #Adding new friends
        add_friend = str(raw_input("Add who? "))
        if os.path.isdir(os.getcwd() + "/" + name) is False: #Serching for a file with the inputed name in the database
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
        if os.path.isdir(os.getcwd() + "/" + name) is False:
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
        if os.path.isdir(os.getcwd() + "/" + name) is False:
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

class wall():
    def __init__(self):
        self.importer = import_database()
        self.exporter = export_database()
        self.wall = {}
        self.queue = Queue.Queue()
        self.out_queue = Queue.Queue()

    def friend_request(self):
        self.importer.import_wall()
        self.wall = self.importer.get_wall()
        thread_friend_request = thread_friend_request(self.wall)
        thread_friend_request.start()

    def status(self, name):
        self.importer.import_wall(name)
        self.wall = eval(self.importer.get_wall())
        self.importer.import_friends(name)
        friends = self.importer.get_friends()
        for i in friends:
            thread = thread_status(self.queue, self.out_queue)
            thread.setDaemon(True)
            thread.start()
        for item in friends:
            self.queue.put(item)
        wall = {}
        for i in friends:
            temp = self.out_queue.get()
            wall.update(temp)
        self.queue.all_tasks_done
        self.queue.join()
        self.wall.update(wall)
        self.exporter.export_wall(name, wall)

    def print_wall(self, name):
        self.importer.import_wall(name)
        self.wall = eval(self.importer.get_wall())
        print OrderedDict(sorted(self.wall.items(), key=lambda t: t[0]))


#class thread_friend_request():
#	def run(self):
class thread_status(threading.Thread):
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.importer = import_database()
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        name = self.queue.get()
        status = {}
        self.importer.import_status(name)
        status = eval(self.importer.get_status())
        self.out_queue.put({name:status})
        self.queue.task_done()