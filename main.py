from spy_details import spy_name, spy_salutation, spy_rating, spy_age


STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

print 'Let\'s get started'
question = "Continue as " + spy_salutation + " " + spy_name + "(Y/N)?"
existing = raw_input(question)


def add_status(current_status_message):

    updated_status_message = None

    if current_status_message != None:
      print 'Your current status message is %s \n' % (current_status_message)
    else:
      print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
          new_status_message = raw_input("What status message do you want to set?")

          if len(new_status_message) > 0:
              updated_status_message = new_status_message
              STATUS_MESSAGES.append(updated_status_message)
    elif default.upper() == "Y":
          item_position = 1
          for message in STATUS_MESSAGES:
              print '%d. %s' % (item_position, message)
              item_position = item_position + 1
          message_selection = raw_input("\nChoose from the above messages ")
          if len(STATUS_MESSAGES) >= message_selection:
             updated_status_message = STATUS_MESSAGES[message_selection - 1]
    else:
          print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You did not update your status message'

    return updated_status_message



def start_chat(spy_name,spy_age, spy_rating):
  show_menu = True
  current_status_message = None

  while show_menu:
    menu_choices = "What do you want to do? \n1. Add a status update \n2. Close Application"
    menu_choice = raw_input(menu_choices)

    if menu_choice == '1':
      current_status_message = add_status(current_status_message)

    elif menu_choice == '2':
      show_menu = False



if (existing == "Y"):
    print 'ok'
    start_chat(spy_name,spy_age,spy_rating)
#Continue with the default user/details imported from the spy_details file.
else:
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy_name) > 0:
        print 'Welcome ' + spy_name + '. Glad to have you back with us.'
        spy_salutation = raw_input("Should I call you Mister or Miss?: ")
        spy_name = spy_salutation + " " + spy_name
        print "Alright " + " " + spy_name + ". I'd like to know a little bit more about you before we proceed..."
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_age = int(raw_input("What is your age?"))
        if spy_age > 12 and spy_age < 50:
            spy_rating = float(raw_input("What is your spy rating?"))
            if spy_rating > 4.5:
                print 'Great ace!'
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'
        else:
            print 'Sorry you are not of the correct age to be a spy'
        spy_is_online = True

        print "Authentication complete. Welcome %s of age: %d and rating %.2f Proud to have you onboard" % (
        spy_name, spy_age, spy_rating)

        start_chat(spy_name, spy_age, spy_rating)
    else:
        print "A spy needs to have a valid name. Try again please."