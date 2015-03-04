# Implementation of Rock-paer-scissors-lizard-spock
# Rock-paper-scissors-lizard-Spock

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

#converts names to numbers for easier implementation
def name_to_number(name):
    if name=='rock':
        return 0    
    elif name=='Spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4
    else:
        return "error"


# converts numbers back to names
def number_to_name(number):
    
    if number==0:
        return 'rock'    
    elif number==1:
        return 'Spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    elif number==4:
        return 'scissors'
    else:
        return "error"
    
# The main function
def rpsls(player_choice): 
    
    print 
    
    # prints out the message for the player's choice
    print "player's choice is:",player_choice
        
    # converts the player's choice to player_number using the function name_to_number()
    number=name_to_number(player_choice)

    # computes random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,5,1)
    
    # converts comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_number)
    
    # prints out the message for computer's choice
    print "Computer's choice is:",comp_choice
    
    
    # computes difference of comp_number and player_number modulo five
    difference= (number-comp_number) % 5
    
    
    # determines winner, print winner message
    if difference==0:
        print "Its tie"
    elif difference<=1 or difference <=2:
        print "Player wins!"
    else:
        print "Computer wins!"
    
    
# Testing the code    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



