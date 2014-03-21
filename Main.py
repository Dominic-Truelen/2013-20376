from CC import import_database, export_database
from time import strftime
from collections import OrderedDict
import glob, os, threading, Queue, collections

class messages():
    def __init__(self, name):
        self.name = name
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
        self.exporter.export_messages_copy(self.name) #To remove the notifications

        print "Messages Recieved"
        if self.messages != {}: #If the messasges is not blank
            for x in self.messages.iterkeys(): #Iteration over the senders
                for counter in range(len(self.messages[x])): #Length of the messages per sender
                    print self.messages[x][counter].get_sender() #Name of sender
                    print '\t' + self.messages[x][counter].get_text() #Body of the message
                    print '\t\t' + self.messages[x][counter].get_date() #Date & time the message was sent

        print "Messages Sent"
        if self.messages_sent != {}:
            for x in self.messages_sent.iterkeys():
                for counter in range(len(self.messages_sent[x])):
                    print self.messages_sent[x][counter].get_sender()
                    print '\t' + self.messages_sent[x][counter].get_text()
                    print '\t\t' + self.messages_sent[x][counter].get_date()

    def send_message(self): #Sending messages
        reciever = str(raw_input("Send to: ")) #The reciever of the message

        if os.path.isdir(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + reciever) is False: #Searching for a file with the inputed name in the database
            print "User does not exist"
        elif reciever == self.name:
            print "You cannot send messages to yourself"
        else:
            message = str(raw_input("Message: "))
            time = strftime("%m/%d/%Y, %I.%M.%S%p") #Format for the time

            self.exporter.export_sent_messages(self.name, message, time, reciever) #Exporting sent message
            self.exporter.export_messages(reciever, message, time, self.name) #Exporting the recieved message

    def delete_message(self):
        sender = str(raw_input("Delete whose message: "))
        if os.path.isdir(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + sender) is False:
            print "User does not exist"
            return
        elif self.messages.has_key(sender) is False:
            print "User did not send a message"
            return

        date = str(raw_input("Date of the message:"))
        self.get_messages(self.name) #Importing messages of the user
        messages = self.messages[sender] #Getting the messages sent by a specific user

        counter = 0

        for item in messages: #For each message by that user
            if date == item.get_date(): #If the date inputed is equal to the date of the message
                messages.pop(counter) #That message would be removed

                f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name)
                g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name + '1', 'w')
                
                for line in f:
                    if sender and date not in line: #If the line is not the messages line in the file
                        g.write(line)
                    else:
                        a = [] #A temporary list
                        for x in range(len(messages)): #For each message minus the message to be deleted
                            a.append(messages[x].get_date() + ':' + messages[x].get_text()) #It would be appended to the temporary list
                        g.write(str({str(sender):a}) + '\n') #It would then be written to the file in dictionary form

                f.close()
                g.close()
                os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name)
                os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name)
                
                self.get_messages_sent(sender)
                messages = self.messages_sent[self.name]
                messages.pop(counter)

                f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + sender + "/" + sender)
                g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + sender + "/" + sender + '1', 'w')
                
                for line in f:
                    if self.name and date not in line:
                        g.write(line)
                    else:
                        a = []
                        for x in range(len(messages)):
                            a.append(messages[x].get_date() + ':' + messages[x].get_text())
                        g.write(str({str(sender):a}) + '\n')

                f.close()
                g.close()
                os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + sender + "/" + sender)
                os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + sender + "/" + sender + '1', os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + sender + "/" + sender)

                counter += 1 #Counter would be the number of times this has looped

        if counter == 0: #If the counter never iterated
            print "Message does not exist"

class post(object): #Getters and Setters for posts
	def __init__(self, name):
		self.name = name
		self.text = ''
		self.date = ''
		self.state = ''
		self.enabled = True
		self.tags = []
		self.comments = [] #List of comment()s instances, not just a list, but INSTANCES OF THE COMMENT cLASS
		self.exporter = export_database()

	def get_name(self):
		return self.name

	def get_text(self):
		return self.text

	def get_date(self):
		return self.date

	def get_state(self):
		return self.state

	def get_tags(self):
		return self.tags

	def get_comments(self):
		return self.comments

	def set_text(self, text):
		self.text = text

	def set_date(self, date):
		self.date = date

	def set_state(self, state):
		self.state = state

	def set_tags(self, tags):
		self.tags.append(tags)

	def set_comments(self, comments):
		self.comments.append(comments)

	def set_enabled(self, ans):
	    self.enabled = ans

class comment(): #Getters and Setters for comments
	def __init__(self): 
		self.name = ''
		self.date = ''
		self.text = ''

	def get_name(self):
		return self.name

	def get_date(self):
		return self.date

	def get_text(self):
		return self.text

	def set_name(self, name):
		self.name = name

	def set_date(self, date):
		self.date = date

	def set_text(self, text):
		self.text = text

class edit_profile():
    def __init__(self, name):
        self.name = name
        self.profile = profile_object(self.name)
        self.importer = import_database()
        self.exporter = export_database()

    def get_details(self):
        self.importer.import_details(self.name)
        temp = self.importer.get_details()
        self.profile.set_gender(temp[0])
        self.profile.set_age(temp[1])
        self.profile.set_job(temp[2])
        self.profile.set_education(eval(temp[3]))

    def change_gender(self):
        gender = raw_input("Male or Female? ")
        gender = gender.lower()
        self.profile.set_gender(gender)
        self.exporter.export_details(self.name, self.profile.get_gender(), self.profile.get_age(), self.profile.get_job(), self.profile.get_education())

    def change_age(self):
        age = raw_input("Age: ")
        self.profile.set_age(age)
        self.exporter.export_details(self.name, self.profile.get_gender(), self.profile.get_age(), self.profile.get_job(), self.profile.get_education())

    def change_job(self):
        job = raw_input("Job: ")
        self.profile.set_job(job)
        self.exporter.export_details(self.name, self.profile.get_gender(), self.profile.get_age(), self.profile.get_job(), self.profile.get_education())

    def change_education(self): #MUST BE CHANGED FOR GUI VERSION
        while True:
            choice = raw_input("E - Elementary, H - High School, C - College, R - Return: ")
            choice = choice.lower()
            if choice == 'e':
                choice = 0
            elif choice == 'h':
                choice = 1
            elif choice == 'c':
                choice = 2
            elif choice == 'r':
                break
            else:
                print "Invalid input"
            while True:
                state = raw_input("A - Add, D - Delete, R - Return: ")
                state = state.lower()
                if state == 'a':
                    add = raw_input("Enter school: ")
                    temp = self.profile.get_education()
                    temp[choice].append(str(add))
                    self.profile.set_education(temp)
                    self.exporter.export_details(self.name, self.profile.get_gender(), self.profile.get_age(), self.profile.get_job(), self.profile.get_education())
                elif state == 'd':
                    for x in range(len(self.profile.get_education()[choice])):
                        print str(x) + ' ' + self.profile.get_education()[choice][x]
                    delete = input("Enter number of the school to be deleted: ")
                    if delete in range(len(self.profile.get_education()[choice])):
                        temp = self.profile.get_education()
                        temp[choice].pop(delete)
                        self.profile.set_education(temp)
                        self.exporter.export_details(self.name, self.profile.get_gender(), self.profile.get_age(), self.profile.get_job(), self.profile.get_education())
                    else:
                        print"Invalid input"
                elif state == 'r':
                    break
                else:
                    print"Invalid input"
                
    def print_gender(self):
        print self.profile.get_gender()

    def print_age(self):
        print self.profile.get_age()

    def print_job(self):
        print self.profile.get_job()

    def print_education(self):
        if self.profile.get_education()[0] != []:
            print "Elementary: " + str(self.profile.get_education()[0])

        if self.profile.get_education()[1] != []:
            print "High School: " + str(self.profile.get_education()[1])

        if self.profile.get_education()[2] != []:
            print "College: " + str(self.profile.get_education()[2])

class profile_object(): #Getters and setters for profiles
    def __init__(self, name):
        self.name = name
        #self.profile_picture =
        self.gender = ''
        self.age = 0
        self.job = ''
        self.education = [[],[],[]]

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_job(self):
        return self.job

    def get_education(self):
        return self.education

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age

    def set_job(self, job):
        self.job = job

    def set_education(self, education):
        self.education = education

class statusGUI(post):
	def __init__(self, name):
		post.__init__(self, name)
		self.state = 'Status'
		self.status = {}
		self.importer = import_database()

	def get_status(self): #Importing the status
		self.importer.import_status(self.name)
		self.status = dict(self.importer.get_status())

	def create_status(self): #Overwriting the status
		status = str(raw_input("Enter your status: "))
		date = strftime("%m/%d/%Y, %I.%M.%S%p")
		self.exporter.export_status(self.name, status, date)

	def print_status(self):
		print self.status

	def delete_status(self):
		date = str(raw_input("Date of status: "))
		self.get_status()
		if self.status.has_key(date) is False:
			return
		self.status.pop(date)
		f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name)
		g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name + '1', 'w')
		while True:
			temp = f.readline()
			g.write(temp)
			if "Status" in temp:
				break
		g.write(str(self.status) + '\n')
		f.readline()
		for line in f:
			g.write(line)
		f.close()
		g.close()
		os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name)
		os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name + "1", os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name)

	def delete_status_gui(self, date):
		self.get_status()
		self.status.pop(date)
		f = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name)
		g = open(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name + '1', 'w')
		while True:
			temp = f.readline()
			g.write(temp)
			if "Status" in temp:
				break
		g.write(str(self.status) + '\n')
		f.readline()
		for line in f:
		    g.write(line)
		f.close()
		g.close()
		os.remove(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name)
		os.rename(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name + "1", os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + self.name + "/" + self.name)


class friends():
    def __init__(self, name, database):
        self.name = name
        self.friends = []
        self.friend_requests = []
        self.friend_requests_sent = []
        self.exporter = export_database()
        self.importer = database

    def see_friends(self): #Displaying the friends of the active user
        self.importer.import_friends(self.name) #Imported the friends
        self.friends = self.importer.get_friends() #Accessed the friends
        for counter in range(len(self.friends)):
            print self.friends[counter]

    def add_friend(self): #Adding new friends
        add_friend = str(raw_input("Add who? "))
        if os.path.isdir(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + add_friend) is False: #Serching for a file with the inputed name in the database
            print "User does not exist"
        elif add_friend == self.name:
            print "You cannot send yourself a friend request"
        else:
            self.importer.import_friend_requests(self.name)
            self.friend_requests = eval(self.importer.get_friend_requests())
            if add_friend in self.friend_requests: #If the user has sent you a request
                print "This user has already sent you a friend request"
            else:
                self.importer.import_friend_requests_sent(self.name)
                self.friend_requests_sent = eval(self.importer.get_friend_requests_sent())
                if str(add_friend) in self.friend_requests_sent: #If you already sent the user a request
                    print "You already sent a friend request"
                else:
                    self.friend_requests_sent.append(str(add_friend)) #Append the friend to the list of your sent friend requests
                    self.exporter.export_friend_request_sent(self.name, self.friend_requests_sent) #Exporting the list of friend requests sent
                    self.importer.import_friend_requests(add_friend) #Import list of friend requests of the reciever
                    self.friend_requests = eval(self.importer.get_friend_requests())
                    self.friend_requests.append(str(self.name)) #Append yourself to the list of the reciever's friend requests
                    self.exporter.export_friend_request(add_friend, self.friend_requests) #Exporting the list of friend requests

    def add_friend_gui(self, toBeAdded):       
        self.importer.import_friend_requests(self.name)
        self.friend_requests = eval(self.importer.get_friend_requests())
       
        self.importer.import_friend_requests_sent(self.name)
        self.friend_requests_sent = eval(self.importer.get_friend_requests_sent())                
        self.friend_requests_sent.append(str(toBeAdded)) #Append the friend to the list of your sent friend requests
        self.exporter.export_friend_request_sent(self.name, self.friend_requests_sent) #Exporting the list of friend requests sent
        
        self.importer.import_friend_requests(toBeAdded) #Import list of friend requests of the reciever
        self.friend_requests = eval(self.importer.get_friend_requests())
        self.friend_requests.append(str(self.name)) #Append yourself to the list of the reciever's friend requests
        self.exporter.export_friend_request(toBeAdded, self.friend_requests) #Exporting the list of friend requests    

    def see_friend_requests(self): #Displaying the friend requests recieved and sent
        self.importer.import_friend_requests(self.name)
        self.friend_requests = self.importer.get_friend_requests()

        print self.friend_requests

        self.importer.import_friend_requests_sent(self.name)
        self.friend_requests_sent = self.importer.get_friend_requests_sent()

        print self.friend_requests_sent

        self.exporter.export_friend_requests_copy(self.name) #For the notifications

    def delete_friends(self):
        delete = raw_input("Delete who? ")
        if os.path.isdir(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + delete) is False:
            print "User does not exist"
        else:
            self.importer.import_friends(self.name)
            self.friends = self.importer.get_friends()
            if delete not in self.friends:
                print "User is not your friend"
            else:
                self.friends.remove(delete)
                self.exporter.export_friends(self.name, self.friends)
                self.importer.import_friends(delete)
                friends = self.importer.get_friends()
                friends.remove(self.name)
                self.exporter.export_friends(delete, friends)

    def delete_friends_gui(self, toBeDeleted):       
		self.importer.import_friends(self.name)
		self.friends = self.importer.get_friends()		
		self.friends.remove(toBeDeleted)
		self.exporter.export_friends(self.name, self.friends)
		
		self.importer.import_friends(toBeDeleted)
		friends = self.importer.get_friends()
		friends.remove(self.name)
		self.exporter.export_friends(toBeDeleted, friends)

    def cancel_friend_request_gui(self, toBeCancelled):
        
        self.importer.import_friend_requests(toBeCancelled)
        self.friend_requests = eval(self.importer.get_friend_requests())
        self.friend_requests.remove(str(self.name))
        self.exporter.export_friend_request(toBeCancelled, self.friend_requests)
        
        self.importer.import_friend_requests_sent(self.name)
        self.friend_requests_sent = eval(self.importer.get_friend_requests_sent())
        self.friend_requests_sent.remove(str(toBeCancelled))
        self.exporter.export_friend_request_sent(self.name, self.friend_requests_sent)

    def approve_request(self):
        friend = str(raw_input("Approve who? "))
        if os.path.isdir(os.path.abspath(os.path.dirname(__file__)) + "/DATABASE/" + friend) is False:
            print "This user does not exist"
        else:
            self.importer.import_friend_requests(self.name)
            self.friend_requests = self.importer.get_friend_requests()
            if friend not in self.friend_requests:
                print "The user did not send a friend request"
            else:
                self.friend_requests = eval(self.friend_requests)
                self.friend_requests.remove(friend)
                self.importer.import_friends(self.name)
                self.friends = self.importer.get_friends()
                self.friends.append(friend)
                self.exporter.export_friends(self.name, self.friends)
                self.exporter.export_friend_request(self.name, self.friend_requests)
                self.importer.import_friend_requests_sent(friend)
                self.friend_requests_sent = self.importer.get_friend_requests_sent()
                self.friend_requests_sent = eval(self.friend_requests_sent)
                self.friend_requests_sent.remove(self.name)
                self.importer.import_friends(friend)
                self.friends = self.importer.get_friends()
                self.friends.append(str(self.name))
                self.exporter.export_friends(friend, self.friends)
                self.exporter.export_friend_request_sent(friend, self.friend_requests_sent)

    def approve_request_gui(self, toBeApproved):
        self.importer.import_friend_requests(self.name)
        self.friend_requests = self.importer.get_friend_requests()
        
        self.friend_requests = eval(self.friend_requests)
        self.friend_requests.remove(toBeApproved)
        self.importer.import_friends(self.name)
        self.friends = self.importer.get_friends()
        self.friends.append(toBeApproved)
        self.exporter.export_friends(self.name, self.friends)
        self.exporter.export_friend_request(self.name, self.friend_requests)
        self.importer.import_friend_requests_sent(toBeApproved)
        self.friend_requests_sent = self.importer.get_friend_requests_sent()
        self.friend_requests_sent = eval(self.friend_requests_sent)
        self.friend_requests_sent.remove(self.name)
        self.importer.import_friends(toBeApproved)
        self.friends = self.importer.get_friends()
        self.friends.append(str(self.name))
        self.exporter.export_friends(toBeApproved, self.friends)
        self.exporter.export_friend_request_sent(toBeApproved, self.friend_requests_sent)

    def disapprove_request_gui(self, toBeDisapproved):
        self.importer.import_friend_requests(self.name)
        self.friend_requests = eval(self.importer.get_friend_requests())
        self.friend_requests.remove(str(toBeDisapproved))
        self.exporter.export_friend_request(self.name, self.friend_requests)

        self.importer.import_friend_requests_sent(toBeDisapproved)
        self.friend_requests_sent = eval(self.importer.get_friend_requests_sent())
        self.friend_requests_sent.remove(str(self.name))
        self.exporter.export_friend_request_sent(toBeDisapproved, self.friend_requests_sent)

class wall():
    def __init__(self, name):
        self.importer = import_database()
        self.exporter = export_database()
        self.wall = {}
        self.queue = Queue.Queue()
        self.out_queue = Queue.Queue()
        self.name = name

    def friend_request(self):
        self.importer.import_wall()
        self.wall = self.importer.get_wall()
        thread_friend_request = thread_friend_request(self.wall)
        thread_friend_request.start()

    def status(self):
        self.importer.import_wall(self.name)
        self.wall = eval(self.importer.get_wall())
        self.importer.import_friends(self.name)
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
        self.queue.join()
        self.wall.update(wall)
        self.exporter.export_wall(self.name, wall)

    def print_wall(self):
        self.importer.import_wall(self.name)
        self.wall = eval(self.importer.get_wall())
        sortedWall = OrderedDict(sorted(self.wall.items(), key=lambda t: t[0]))
        for x,y in sortedWall.iteritems():
            print x, y

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

class notifications():
    def __init__(self, name):
        self.name = name
        self.importer = import_database()
        self.exporter = export_database()
        self.messages_new = {}
        self.friend_requests_new = []
        self.posts_new = {}

    def messages(self):
        self.importer.import_messages(self.name)
        x = self.importer.get_messages()

        self.importer.import_messages_copy(self.name)
        y = self.importer.get_messages_copy()

        self.messages_new = {} #Reset the messages

        for key in x:
            if key not in y: #If in x but not in y
                self.messages_new[key] = x[key]
            else:
                for counter in range(len(x[key])):
                    x[key][counter] = x[key][counter].get_date() + ':' + x[key][counter].get_text()
                
                self.messages_new[key] = list(set(x[key]) - set(y[key]))

                if self.messages_new[key] == []: #If all the messages from that user has been removed, remove the user itself
                    del self.messages_new[key]

    def messages_counter(self):
        print len(self.messages_new)

    def print_messages_new(self): #Just like printing the messages in the original messages()
        if self.messages_new != {}:
            for x in self.messages_new.iterkeys():
                for counter in range(len(self.messages_new[x])):
                    print self.messages_new[x][counter].get_sender()
                    print '\t' + self.messages_new[x][counter].get_text()
                    print '\t\t' + self.messages_new[x][counter].get_date()

        self.exporter.export_messages_copy(self.name)

    def friend_requests(self):
        self.importer.import_friend_requests(self.name)
        friends = eval(self.importer.get_friend_requests())

        self.importer.import_friend_requests_copy(self.name)
        temp = eval(self.importer.get_friend_requests_copy())

        for x in temp:
            if x in friends:
                friends.remove(x)
            elif x not in friends:
                friends.append(x)

        self.friend_requests_new = friends

    def friend_requests_counter(self):
        print len(self.friend_requests_new)

    def print_friend_requests_new(self):
        print self.friend_requests_new
        self.exporter.export_friend_requests_copy(self.name)
        
    def notifications(self):
        print len(friend_requests_new) + len(posts_new)