import random

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
#
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    
def rpsls(guess):
    guess = name_to_number(guess)
    computer_guess = random.randrange(4)
    print "you choose" +" " + number_to_name(guess)
    print "computer choose" + " " + number_to_name(computer_guess)
    
    if (guess - computer_guess > 0):
        if (guess - computer_guess < 3):
            print "You Win!"
        else:
            print "Computer Win"
    elif (guess - computer_guess == 0):
        print "You and the Computer tie" 
    else:
        if (computer_guess - guess < 3):
            print "Computer Win"
        else:
            print "You Win"

rpsls("scissors")
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
