from CC import creation, login, deletion, logout
from Main import messages, status, friends, wall, post, edit_profile, notifications
import os

while True:
    choice = raw_input("What do you want to do? (C - Create, L - Login, D - Delete, Q - Quit) ")
    choice = choice.lower()
    if choice == 'c':
        c = creation()
        c.ask_name()
        c.ask_password()
        c.create()
    elif choice == 'l':
        l = login()
        if l.login() == 1:
            name = str(l.get_name())
            pr = edit_profile(name)
            m = messages(name)
            p = post(name)
            s = status(name)
            f = friends(name)
            w = wall(name)
            n = notifications(name)
            log = logout()
            while True:
                choice = raw_input("What do you want to do? (P - Profile, M - Messages, S - Status, F - Friends, W - Wall, N - Notifications L - Logout) ")
                choice = choice.lower()
                if choice == 'p':
                    while True:
                        pr.get_details()
                        print "Gender"
                        pr.print_gender()
                        print "Age"
                        pr.print_age()
                        print "Job"
                        pr.print_job()
                        print "Education"
                        pr.print_education()
                        choice = raw_input("What do you want to do? (G - Change Gender, A - Change Age, J - Change Job, E - Change Education, R - Return)")
                        choice = choice.lower()
                        if choice == 'g':
                            pr.change_gender()
                        elif choice == 'a':
                            pr.change_age()
                        elif choice == 'j':
                            pr.change_job()
                        elif choice == 'e':
                            pr.change_education()
                        elif choice == 'r':
                            break
                        else:
                            print"Invalid input"
                elif choice == 'm':
                    while True:
                        m.get_messages(name)
                        m.get_messages_sent(name)
                        m.print_messages()
                        choice = raw_input("What do you want to do? (S - Send Message, D - Delete Message, R - Return) ")
                        choice = choice.lower()
                        if choice == 's':
                            m.send_message()
                        elif choice == 'd':
                            m.delete_message()
                        elif choice =='r':
                            break
                        else:
                            print "Invalid input"
                elif choice == 's':
                    while True:
                        s.get_status()
                        s.print_status()
                        choice = raw_input("What do you want to do? (C - Create Status, D - Delete Status, R - Return) ")
                        choice = choice.lower()
                        if choice == 'c':
                            s.create_status()
                        elif choice == 'd':
                            s.delete_status()
                        elif choice == 'r':
                            break
                        else:
                            print "Invalid input"
                elif choice == 'f':
                    while True:
                        print "Friends:"
                        f.see_friends()
                        print "Friend Requests (Recieved, Sent):"
                        f.see_friend_requests()
                        choice = raw_input("What do you want to do? (A - Add Friend, D - Delete Friend, F - Approve Friend Request, R - Return) ")
                        choice = choice.lower()
                        if choice == 'a':
                            f.add_friend()
                        elif choice == 'd':
                            f.delete_friends()
                        elif choice == 'f':
                            f.approve_request()
                        elif choice == 'r':
                            break
                        else:
                            print "Invalid input"
                elif choice == 'w':
                    w.status()
                    w.print_wall()
                elif choice == 'n':
                    while True:
                        choice = raw_input("What do you want to do? (M - Messages, F - Friends R - Return)")
                        choice = choice.lower()
                        if choice == 'm':
                            while True:
                                n.messages()
                                choice = raw_input("What do you want to do? (M - Messages, C - Counter, R - Return)")
                                choice = choice.lower()
                                if choice == 'm':
                                    n.print_messages_new()
                                elif choice == 'c':
                                    n.messages_counter()
                                elif choice == 'r':
                                    break
                                else:
                                    print "Invalid input"
                        elif choice == 'f':
                            while True:
                                n.friend_requests()
                                choice = raw_input("What do you want to do? (F - Friends, C - Counter, R - Return)")
                                choice = choice.lower()
                                if choice == 'f':
                                    n.print_friend_requests_new()
                                elif choice == 'c':
                                    n.friend_requests_counter()
                                elif choice == 'r':
                                    break
                                else:
                                    print "Invalid input"
                        elif choice == 'r':
                            break
                        else:
                            print "Invalid input"
                elif choice == 'l':
                    log.exit(l.get_name(), l.get_password())
                    break
                else:
                    print "Invalid input"
        else:
            print "Username/Password is invalid"
    elif choice == 'd':
        d = deletion()
        d.delete()
    elif choice == 'q':
        break
    else:
        print "Invalid input"
#os.remove('CC.pyc')
#os.remove('Main.pyc')