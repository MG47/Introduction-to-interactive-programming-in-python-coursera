
# Implementation of card game - Memory
# Mihir Ganu
# Date : Mar 27, 2015

# To play-> http://www.codeskulptor.org/#user39_qMGjnk76Ow_5.py

"""Memory is a card game in which the player deals out a set of cards face down.
In Memory, a turn (or a move) consists of the player flipping over two cards. If they match,
the player leaves them face up. If they don't match, the player flips the cards back face down. 
The goal of Memory is to end up with all of the cards flipped face up in the minimum number of
turns. For this game, a Memory deck consists 
of eight pairs of matching cards.
"""

import simplegui
import random

# Helper function to initialize globals
def new_game():
    pass  
    global st1,st2,numbers #variables to generate cards
    global exposed,turns, state,card1,card2
    st1=range(0,8)
    st2=range(0,8)
    numbers=st1+st2    
    random.shuffle(numbers)
    
    state=0
    exposed=[False for i in range(0,16)]  
    turns=0
    card1=card2=[0,0]
    label.set_text("Turns:"+str(turns))
    
    
# Defines event handlers and game logic
def mouseclick(pos):
    global turns,exposed,state,card1,card2
    for i in range(0,16):
        if pos[0]> i*50 and pos[0]< i*50+50:
            
            if exposed[i]==False:
                
                if state==0:
                    state=1
                    card1=[i,numbers[i]]
                
                elif state==1:
                    state=2
                    card2=[i,numbers[i]]
                    
                    turns+=1
                    label.set_text("Turns:"+str(turns))
                    
                else:
                    state=1  
                    if card1[1]!=card2[1]:
                        exposed[card1[0]]=False
                        exposed[card2[0]]=False
                 
                    card1[0]=i
                    card1[1]=numbers[i]
                    
                exposed[i]=True
                
# Cards are logically 50x100 pixels in size    
def draw(canvas):
    global numbers,exposed  
    
    for i in range(0,16):
        canvas.draw_line((50+i*50,0),(50+i*50,100),5,"RED")
        if exposed[i] is True:
            canvas.draw_text(str(numbers[i]),[20+50*i,50],20,"White")
        else:
            canvas.draw_polygon([(i*50+5,0),(i*50+5,100),(i*50+45,100),(i*50+45,0)],1,"Green","Green")
    
# Creates frame and adds a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# Registers event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# Starts the game
new_game()
frame.start()


# End of program
