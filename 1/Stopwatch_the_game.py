#"Stopwatch: The Game"
# Mihir Ganu
# Date:March 10,2015


''' 
The stopwatch game:
Start the stopwatch with START Button
Click on STOP when the seconds are whole number( when tenths
of seconds is zero) to score.
To run-> http://www.codeskulptor.org/#user39_48z4TiUUj6_3.py
'''

import simplegui

#Global variables
time_ms=0
successful_stops=0
total_stops=0
stop_state=False

canvas_width,canvas_height=300,300


""" Helper function format that converts time
in tenths of seconds into formatted string A:BC.D"""
def format(t):
    tenths=int(t%10)
    seconds2=int((t//10)%10)
    seconds1=int((t//100)%6)
    minutes=int(t//600)
    return str(minutes)+":"+str(seconds1)+str(seconds2)+"."+str(tenths)
 
    


#  Event handler for timer with 0.1 sec interval
def timer_handler():
    global time_ms
    time_ms+=1 
    format(time_ms)

#  Event handler for score
def score():
    return "Score:"+str(successful_stops)+"/"+str(total_stops)
    
# Event handlers for buttons; "Start", "Stop", "Reset"
def start():
    """method to start the timer"""
    timer.start()  
    global stop_state
    stop_state=True
    
def stop():
    """method to stop the timer"""
    timer.stop()
    global total_stops,successful_stops,stop_state
       
    if  stop_state==True:
        total_stops+=1
        if time_ms%10==0:	#Check if seconds is whole number
            successful_stops+=1
    stop_state=False
    
def reset():
    """method to reset the timer"""
    global time_ms,total_stops,successful_stops
    timer.stop()
    time_ms=0
    total_stops=0
    successful_stops=0
    
# define draw handler
def draw_handler(canvas):
    """draws canvas"""
    canvas.draw_text("STOPWATCH",(125,150),34,"Red")
    canvas.draw_text(str(format(time_ms)),(180,200),40,"GREEN")
    canvas.draw_text(str(score()),(20,50),40,"BLUE")
    
# Creates frame
frame=simplegui.create_frame("STOPWATCH",400,400)

frame.add_label("STOPWATCH")
frame.add_button("START",start,100)
frame.add_button("STOP ",stop,100)
frame.add_button("RESET",reset,100)
frame.set_draw_handler(draw_handler)

#Creates timer
timer_interval=100	#100 milliseconds

timer=simplegui.create_timer(timer_interval,timer_handler)


# start frame 
frame.start()
