# Import statement is used to use pre-defined variables from there files
from spy_details import spy, Spy, ChatMessage, friends

# Steganography module is being imported
from steganography.steganography import Steganography

# Termcolor module is used to import colors
from termcolor import *
import colorama
colorama.init()

# Let us provide a list of status to our very own spy
STATUS_MESSAGES = ['My name is Apoorav', 'hey there! i am one of the best spy.', 'I am watching you! ']

# A simple print command in python helps to display string at console .

cprint ("Hello! Let\'s get started", 'green')

# Choice must be provided to spy by asking if they want to start with existing user or create a new spy
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)


# let's define all the necessary function

# a status message must be added.

def add_status(current_status_message):
    # None is used to set value of status message to null.
    updated_status_message = None

    if spy.current_status_message != None:
        print "Your current status message is %s \n" % (spy.current_status_message)

    else:
        print 'Currently You don\'t have any status message!\n'
    # user must select if they want to update from older status or they want to add a new one
    default = raw_input("Do you want to choose from the older status  (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("Which status message would you like to set? ")

        # len method is used to check if length of status message is not null
        # .append adds  the new status message to status list
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            # String formatting is done by using %d for integer and %S for strings

            print '%d. %s' % (item_position, message)
            # i_p + 1 updates %d to +1 for second status in status list
            item_position = item_position + 1

        # selected status is converted to int as python takes input as a string.
        # Conversion is done by using INT(input)
        message_selection = int(raw_input("\n Choose your status update from above list!! "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]


    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % updated_status_message
    else:
        print 'You current don\'t have a status update'
    # return statement is used to assign va;ue of output to some variable
    return updated_status_message


# Let's define a function to add friend!!
def add_friend():
    new_friend = Spy('', '', 0, 0.0)

    # Raw input allows to take input from user and new_friend.name is a variable where variable is stored.
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    # Variable has been updated
    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    # spy friend should meet the requirements for which we apply condition using IF keyword
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:

        # .append adds friend to new_friend
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        # \ is used before 't which is used for escaping character
        # Another better way of doing this is "Sorry! Invalid entry. We can\'t add spy with the details you provided"

        print 'Sorry! Invalid entry. We can\'t add spy with the details you just provided. .'
    return len(friends)


# def keyword is used to create a function and select_a_friend is function name
def select_a_friend():
    item_number = 0

    for friend in friends:
        # % d , %s , % .2f are referred to as placeholders when python tries to print a string it replaces
        # %d with item number + 1
        # %s with friend name
        # % .2f with friend rating
        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend.name, friend.age, friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose one of your friend")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


# let's send our friend a message
def send_message():
    # spy must select a friend to whom he want to send message
    # for this we  call the select_a_fiend function to  gain the index of the friend to whom we want to send message
    friend_choice = select_a_friend()

    # original_image is a variable used to input and store original image on which text is to be encoded
    original_image = raw_input("What is the name of the image?")

    # output path is a variable that stores the path of output image which will carry secret text
    output_path = "output.jpg"

    # spy must enter a text which is stored in a variable text
    text = raw_input("What do you want to say? ")

    #  encoding of message is done by using encode() function from Steganography module
    Steganography.encode(original_image, output_path, text)

    new_chat = Chat_message(text, True)
    if len(text) > 0:
        friends[friend_choice].chats.append(new_chat)
        print "Your secret message image is ready !"
    else:
        print "No secret message entered ! please try again "
        send_message()

# let us create a function to read message
def read_message():
    # Here we again call the select_a_fiend function to  gain the index of the friend whose  message is to be read
    sender = select_a_friend()

     # output path is variable which input and stores image that needs to be decoded
    output_path = raw_input("What is the name of the file?")

    # Message  decoding is by decode() function from steganography module and is stored in a variable called secret_text
    secret_text = Steganography.decode(output_path)
    new_chat = Chat_message(secret_text, False)

   # .append adds the chat to new chat variable
    friends[sender].chats.append(new_chat)

    if secret_text in ['BRB']:
        print "BE RIGHT BACK!!!"
    elif secret_text in ['HELP']:
        print "BACKU UP TEAM WILL REACH SOON"
    elif secret_text in ['SOS']:
        print "SAVE OUR SHIP"
    else:
        print secret_text
        print "your secret message has been saved!!!"



# lets create a function to read our chats
def read_chat_history():
    # here again we call the function select_a_friend to select a friend whose chat we want to read

    read_for = select_a_friend()

    # her we check if chat was send by any active user or by some other user
    for chat in friends[read_for].chats:
        if chat.sent_by_me:

            # strftime function is used to format the timestamp associated with each chat
            cprint('[%s]' % chat.time.strftime("%d %B %Y"), 'blue')
            cprint('%s' % 'you said:', 'red')
            print '%s' %chat.message


        else:
            cprint('[%s]' % chat.time.strftime("%d %B %Y"), 'blue')
            cprint('%s said :' % friends[read_for].name, 'red')
            print '%s' % chat.message


    # now lets create a start chat function


def start_chat(spy):
    current_status_message = None

    spy.name = spy.salutation + " " + spy.name

    # and keyword is used in python. python funda is that it should read like english
    if spy.age > 12 and spy.age < 50:

        # String Concatenation using + symbol .Here str is used before spy.age to convert age data type to string
        # because a string can be added to a string only
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(

            spy.rating) + " we are glad to have you with us."

        # while loop is used to repeat statements inside it until they are true
        # here we are creating a menu choice for our spy

        show_menu = True

        while show_menu:
            menu_choices = " What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n "
            menu_choice = raw_input(menu_choices)

            # Nested if
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)

                # elif keyword is used to handle multiple cases as we have a long list of menu
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % number_of_friends
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


# continue with existing user / details
if existing == "Y":

    start_chat(spy)

else:

    spy = Spy('', '', 0, 0.0)
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    # len function is used to check if length of name is greater than zero
    if len(spy.name) > 0:

        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        # int is used before spy.rating to int type as python takes input as a string
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        # float is used before spy.rating to float type as python takes input as a string
        spy.rating = float(spy.rating)

        # start_chat function is being called
        start_chat(spy)

    else:
        print ' Please add a valid spy name .'