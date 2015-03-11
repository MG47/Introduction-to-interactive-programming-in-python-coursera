#"Guess the Number" game
# Mihir Ganu
# Date:March 10,2015


''' The game is simple: The first 
player thinks of a secret number in some known
range while the second player attempts to guess
the number
To run -> http://www.codeskulptor.org/#user39_h1KTnwrwEe_12.py
'''


'''
Game Strategy:
 Any secret number in the
 range [low, high) can always be found in at
 most n guesses where n is the smallest integer 
 such that 2 ** n >= high - low + 1.
 For numbers in the range 0-100 the maximum limit is 7
 For numbers in the range 0-1000 the maximum limit is 10
 The best strategy is binary search
'''

import simplegui
import random
import math

#global variables
global secret_number	# Randomly generated secret number
global max_guesses		# Number of maximum guesse
global mode				# Range of input 

#Functions to initialize the secret number

def new_game_100():
    '''For Numbers in the range (0,100)'''
    print "Let's play GUESS THE NUMBER!!\n"
    print "Guess a number between 0-100"
    global mode
    mode=100
    global max_guesses
    max_guesses=7
    global secret_number
    secret_number=random.randrange(0,100)
    max_guesses=7
  # print secret_number


def new_game_1000():
    '''For Numbers in the range (0,1000)'''
    print "Let's play GUESS THE NUMBER!!"
    print "Guess a number between 0-1000"
    global max_guesses
    global mode
    mode=1000
    max_guesses=10
    global secret_number
    secret_number=random.randrange(0,1000)
    max_guesses=10
  # print secret_number

    
#create handler for the input
def input_guess(guess):
    global max_guesses
    max_guesses-=1
    
    if max_guesses>=0:
        print "Your guess is:",int(guess) 
        print "Number of remaining guesses:",max_guesses
        if int(guess)<secret_number:
            print "The secret number is Higher\n"
        elif int(guess)>secret_number:
            print "The secret number is Lower\n"
        else:
            print "Correct!"
            print "You win!\n"
    else:
        print "Maximum guess limit reached!"
        print "The secret_number is",secret_number
        print "You lose!\n\n"
        
        if mode==100:
            new_game_100()
        else:
            new_game_1000()
            
# create frame
frame=simplegui.create_frame("Play",300,300)
frame.add_button("Range:0-100",new_game_100)
frame.add_button("Range:0-1000",new_game_1000)
frame.add_input("Enter your guess:",input_guess,100)

#start game
frame.start()

#Initialize secret_number
new_game_100()
