# Implementation of rock-paper-scissors-lizard-Spock using
# Math's modulo operator.
# http://en.wikipedia.org/wiki/Rock-paper-scissors-lizard-Spock

import random


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "not a valid name:", name
        number = None

    return number


def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "not a valid number:", number
        name = None

    return name
    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    print "Player chooses", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice

    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    
    # If difference is either 1 or 2, Computer wins.
    # Player wins if difference is either 3 or 4.
    # Needless to say, it is a tie if difference is 0.
    if difference == 0:
        print "Player and computer tie!"
    elif ((difference == 1) or (difference == 2)):
        print "Computer wins!"
    elif ((difference == 3) or (difference == 4)):
        print "Player wins!"
    else:
        print "Unexpected result of no winner nor a tie!"

        
# test 
def main():
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")
    
if __name__ == "__main__":
    main()

