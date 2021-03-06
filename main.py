from spy_details import spy, Spy, ChatMessage, friends #imporing classes to use pre-defined variables
from steganography.steganography import Steganography #used to send and receive messages between spies
from datetime import datetime #used to provide datestamp

from termcolor import*
import colorama
colorama.init()

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Last rat standing', 'I stop when I am Done.']

print "Hello! Let's get started"

existing = raw_input("Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? ")


def add_status(): #function created to add status, def is the keyword to define a function

    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message) #append() will add the new status
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message) #displays status in 1 My name is Bond, James Bond format to help us select
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages ")) #stores the selection


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message #function will return the value stored in this variable when called


def add_friend(): #to add new friend

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= 4:
        friends.append(new_friend)
        print  new_friend.name + " of age: " \
              + str(new_friend.age) + " and rating of: " + str(new_friend.rating) + " added as your friend!"
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends) #retuens the number of friends we have


def select_a_friend(): #selects the friend from the list
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position #returns the position in the list


def send_message(): #

    friend_choice = select_a_friend()

    src ="input.jpg" #original path
    dest = "output.jpg" #output path
    text = raw_input("What do you want to say? ") #our messagey
    Steganography.encode(src, dest, text) #encode is inbuilt in steganography to hide the message

    new_chat = ChatMessage(text,True) #this has our message

    friends[friend_choice].chats.append(new_chat) #adds the message for the friend selected

    print "Your secret message image is ready!"


def read_message():

    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path) #decode is inbuilt in steganography to decode the hidden message

    new_chat = ChatMessage(secret_text, False)
    friends[sender].chats.append(new_chat)

    if secret_text == 'BRB':
        print "BE RIGHT BACK!!!"
    elif secret_text == 'SAVE ME':
        print "DON'T WORRY! BACK UP TEAM WILL REACH SOON"
    elif secret_text == 'SOS':
        print "SAVE OUR SOULS"
    elif len(secret_text) == 0:
        print "Nothing recieved, send again."
    else:
        print secret_text


def read_chat_history(): #this function will helps us see the messages send along with the date and time

    read_for = select_a_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:

            cprint('[%s]' % chat.time.strftime("%d %B %Y"), 'blue') #strftime function is used for the timestamp associated with each chat
            cprint('%s' % 'you said:', 'red')
            print '%s' % chat.message

        else:
            cprint('[%s]' % chat.time.strftime("%d %B %Y"), 'blue')
            cprint('%s said :' % friends[read_for].name, 'red')
            print '%s' % chat.message


def start_chat(spy): #this is the main function which will give us menu of choices to select , and call different functions created before

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing.upper() == "Y":
    spy_enter = raw_input("Enter password. ") #password protected
    if spy_enter == "vesper": #this is the password,
        print "Welcome"
        start_chat(spy)
    else:
        print "Invalid Password. Please restart and try again."

else: #if we want to enter as a different user

    spy = Spy('','',0,0.0)

    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'