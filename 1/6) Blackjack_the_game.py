# Implementation of the card game - Blackjack
# Mihir Ganu
# Date : Apr 4, 2015

# To play -> http://www.codeskulptor.org/#user39_fB18wavgMr_6.py

"""
Blackjack is a simple, popular card game that is played in many casinos.
Cards in Blackjack have the following values:an ace may be valued 
as either 1 or 11 (player's choice), face cards (kings, queens and jacks) 
are valued at 10 and the value of the remaining cards corresponds to their
number. During a round of Blackjack, the players plays 
against a dealer with the goal of building a hand (a collection of 
cards) whose cards have a total value that is higher than the value of the 
dealer's hand, but not over 21.  (A round of Blackjack is also sometimes referred
to as a hand.)

The game logic for our simplified version of Blackjack is as follows.
The player and the dealer are each dealt two cards initially with one
of the dealer's cards being dealt faced down (his hole card). 
The player may then ask for the dealer to repeatedly "hit" his hand 
by dealing him another card. If, at any point, the value of the player's 
hand exceeds 21, the player is "busted" and loses 
immediately. At any point prior to busting, the player 
may "stand" and the dealer will then hit his hand until the
value of his hand is 17 or more. (For the dealer, aces count as 11 unless
it causes the dealer's hand to bust). If the dealer busts, the player wins.
Otherwise, the player and dealer then compare the values of their hands and 
the hand with the higher value wins. The dealer wins ties in this version."""

import simplegui
import random

# Load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# Initializes useful global variables
in_play = False
outcome = ""
win = 0
loss =0

# Global variables for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# Card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], 
                           pos[1] + CARD_CENTER[1]], 
                          CARD_SIZE)
        
    def drawDown(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0] + 1, 
                           pos[1] + CARD_BACK_CENTER[1] + 1], CARD_BACK_SIZE)
        
# Hand class

class Hand:
    def __init__(self):
        self.hand=[]	# Creates Hand object

    def __str__(self):
        string=""
        for i in range(len(self.hand)):
            string+=str(self.hand[i])
        return string	# returns a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)				# adds a card object to a hand

    def get_value(self):
        value=0
        for card in self.hand:
            value+= VALUES[card.get_rank()]
            if card.get_rank() =='A':  # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
                if value +10 < 22:
                    value+=10            
        return value
    
    def draw(self, canvas, pos):
        for card in self.hand:
            pos[0] = pos[0] + CARD_SIZE[0] + 20
            card.draw(canvas, pos)
            
# Deck class 
class Deck:
    def __init__(self):
        self.deck=[]	# creates a Deck object
        for suit_no in range(0, len(SUITS)):
            for rank_no in range(0, len(RANKS)):
                self.deck.append(Card(SUITS[suit_no], RANKS[rank_no]))
                
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        string=""			# return a string representing the deck
        for i in range(len(self.deck)):
            string+=str(self.deck[i])
        return string	# returns a string representation of a hand
        

#Define event handlers for buttons
def deal():
    global outcome, in_play, new_deck, dealer, player, win, loss
    
    outcome=""

    if in_play == True:
        in_play=False
        deal()
    
    else:
        new_deck=Deck()
        new_deck.shuffle()
    
        dealer=Hand() 
        player=Hand()
    
        dealer.add_card(new_deck.deal_card())
        dealer.add_card(new_deck.deal_card())
    
        player.add_card(new_deck.deal_card())
        player.add_card(new_deck.deal_card())
        in_play = True
  
def hit():
    global outcome, in_play, new_deck, dealer, player, score, win, loss
    #if not busted
    if in_play==True:
        player.add_card(new_deck.deal_card())   # if the hand is in play, hit the player
        outcome="Hit or stand?"   
        if player.get_value() > 21:
            loss+=1  
            outcome="Busted!!"
            in_play=False
                                            
    
def stand():   
    global outcome, in_play, new_deck, dealer, player, score, win, loss

    if in_play==True:
        while dealer.get_value()< 17:
            dealer.add_card(new_deck.deal_card())	
     
        if dealer.get_value() > 21:
            win += 1
            outcome="You win!"
            in_play = False
          
        elif player.get_value() > dealer.get_value():
            win += 1
            outcome="You win!"
            in_play = False

        else:
            loss += 1
            outcome="You lose!"
            in_play = False
                     
# Draw handler    
def draw(canvas):
    canvas.draw_text("BlackJack", (175, 75), 70, 'Black')    
    canvas.draw_text("Dealer", (45, 200), 25, 'Black')    
    canvas.draw_text("You", (45, 420), 25, 'Black')    
    canvas.draw_text("Wins:" + str(win), (45, 575), 30, 'Black')
    canvas.draw_text("Losses: " + str(loss), (415, 575), 30, 'Black')
    canvas.draw_text(outcome, (215, 575), 30, 'Black')
        
    
    player.draw(canvas, [35,350])
    dealer.draw(canvas, [35,150])    
  
    if in_play==True:
        dealer.hand[0].drawDown(canvas, [124,150])    
    else:        
        dealer.draw(canvas, [35,150])
            
# Initialization frame
frame = simplegui.create_frame("Blackjack", 580, 600)
frame.set_canvas_background("Green")

#Creates buttons and canvas callbacks
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# Starts the game
deal()
frame.start()
