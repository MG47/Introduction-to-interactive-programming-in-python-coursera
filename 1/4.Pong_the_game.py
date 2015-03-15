# Classic Arcade Game: Pong
# Mihir Ganu
# Date: March 14, 2015

import simplegui
import random


# initialize globals - pos and vel encode vertical info for paddles

#size of canvas
WIDTH = 600
HEIGHT = 400       

BALL_RADIUS = 20

PAD_WIDTH = 8
PAD_HEIGHT = 80

HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

LEFT = False
RIGHT = True


# Initializes ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists  
 
    ball_pos=[WIDTH/2,HEIGHT/2]
 

    if direction==RIGHT:
        ball_vel=[random.randrange(3,5), -random.randrange(1,3)]
    
    if direction==LEFT:
        ball_vel=[-random.randrange(3,5), -random.randrange(1,3)]

# Event handlers
def new_game():
    
    global ball_pos,paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    global score1, score2  
    global ball_pos 
    
    spawn_ball(random.choice([True,False]))
    
    paddle1_pos=HEIGHT/2+PAD_HEIGHT
    paddle2_pos=HEIGHT/2+PAD_HEIGHT
    
    paddle1_vel=0
    paddle2_vel=0
    
    score1=0
    score2=0
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global LEFT,RIGHT
        
    # draws mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")	#mide line
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    
    # draws paddles
    
    if paddle1_pos+paddle1_vel>=0 and paddle1_pos+paddle1_vel<=HEIGHT-PAD_HEIGHT:
        paddle1_pos+=paddle1_vel
        
    
    if paddle2_pos+paddle2_vel>=0 and paddle2_pos+paddle2_vel<=HEIGHT-PAD_HEIGHT:
        paddle2_pos+=paddle2_vel
    
    canvas.draw_line([0,paddle1_pos],[0,paddle1_pos+PAD_HEIGHT],2*PAD_WIDTH,"GREEN")	
    canvas.draw_line([WIDTH,paddle2_pos],[WIDTH,paddle2_pos+PAD_HEIGHT],2*PAD_WIDTH,"GREEN")   
  
    # Determines whether paddle and ball collide    
    
    if (ball_pos[0] - BALL_RADIUS - PAD_WIDTH <= 0):
        if (ball_pos[1] >= (paddle1_pos - BALL_RADIUS) and ball_pos[1] <= (paddle1_pos + PAD_HEIGHT + BALL_RADIUS)):	
            ball_vel[0] *=-1.1
            ball_vel[1] *= 1.1
                
        else:
            print "OUT11!"
            score2+=1
            spawn_ball(RIGHT)
    
    if (ball_pos[0] + BALL_RADIUS + PAD_WIDTH >= WIDTH):
        if (ball_pos[1] >= (paddle2_pos - BALL_RADIUS) and ball_pos[1] <= (paddle2_pos + PAD_HEIGHT + BALL_RADIUS)):
            ball_vel[0] *=-1.2
            ball_vel[1] *=1.1
    
        else:
            print "OUT22!"
            score1+=1
            spawn_ball(LEFT)
                    
    #Reflects of the top and bottom of canvas
    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT-BALL_RADIUS:   
        ball_vel[1] = -ball_vel[1]
  
    # Updates ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draws ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,3.5,"WHITE","WHITE")  
               
    # draws scores
    canvas.draw_text(str(score1),[WIDTH/4,HEIGHT/8],30,"Yellow")
    canvas.draw_text(str(score2),[3*WIDTH/4,HEIGHT/8],30,"Yellow")
    
    
#keyboard input handlers       
def keydown(key):
    global paddle1_vel, paddle2_vel
      
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 6
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -6   
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 6
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -6

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0  
    
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0   
    
    
#Restarts the game and resets scores
def restart():		
    new_game()
    
# Creates frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESTART",restart)

# Starts frame
new_game()
frame.start()
