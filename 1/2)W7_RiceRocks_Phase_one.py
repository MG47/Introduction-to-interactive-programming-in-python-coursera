# RiceRocks- Modified version of classic arcade game - Asteroids
# Mihir Ganu
# Date : Apr 11, 2015

""" Phase one of the code - Please refer full version of the code
to play the game
"""

"""
The 2D space game RiceRocks is inspired by the classic 
arcade game Asteroids (1979). In the game, the player
controls a spaceship via four buttons: two buttons('left' and 'right' key)
that rotate the spaceship clockwise or counterclockwise 
(independent of its current velocity), a thrust button('up' key)
that accelerates the ship in its forward direction and 
a fire button('spacebar') that shoots missiles. Large asteroids spawn
randomly on the screen with random velocities. The player's
goal is to destroy these asteroids before they strike the
player's ship. 

Happy Gaming!
"""

import simplegui
import math
import random

# Globals variables for user interface
WIDTH = 800
HEIGHT = 600

score = 0
lives = 0

time = 0.5

#global variable for game elements
global rock_angle_vel, rock_pos , rock_vel, missile_pos,missile_vel
#global lives,score

lives=0
score=0

rock_angle_vel=(random.random()*2-1)/10
rock_pos=[0,0]
rock_vel=[0,0]
rock_pos[0]=random.randint(0,WIDTH)
rock_pos[1]=random.randint(0,HEIGHT)
rock_vel[0]=(random.random()*2-1)*2
rock_vel[1]=(random.random()*2-1)*2                                    

missile_pos=[-400,-400]    
missile_vel=[-10,-10]
    
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# Art assets credits: Kim Lathrop

# Debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# Nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# Splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# Ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# Missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# Asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# Animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# Sounds
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# Helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):		#to draw the ship
        if self.thrust:			#when thrust is on
            canvas.draw_image(self.image, [self.image_center[0]+self.image_size[0],self.image_center[1]], self.image_size, self.pos, self.image_size,self.angle)
        else:					#when thrust is on
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size,self.angle)
            
    def update(self):			#update the ship's position
  
    #Ship position and rotation
    
        vector=angle_to_vector(self.angle)  
  
        self.angle+=self.angle_vel
        
        self.vel[0]*=0.95		#friction
        self.vel[1]*=0.95
        
        self.pos[0]=(self.pos[0]+self.vel[0])%WIDTH
        self.pos[1]=(self.pos[1]+self.vel[1])%HEIGHT
        
    #Effect of thrust
        if self.thrust:
            self.vel[0]+=0.25*vector[0]
            self.vel[1]+=0.25*vector[1]     
            ship_thrust_sound.play()
            
        else:
            ship_thrust_sound.rewind()
         
    # Missiles        
    def launch_missile(self):		
        global missile_pos,missile_vel,missile
        vector=angle_to_vector(self.angle)  
        missile_pos[0]=self.pos[0]+40*vector[0]
        missile_pos[1]=self.pos[1]+40*vector[1]
        
        missile_vel[0]=self.vel[0]+5*vector[0]
        missile_vel[1]=self.vel[1]+5*vector[1]
                
        missile = Sprite(missile_pos,missile_vel,self.angle, 0, missile_image, missile_info, missile_sound)

        
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image,self.image_center,self.image_size,self.pos, self.image_size, self.angle)
        
    def update(self):
        self.angle+=self.angle_vel
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
           
def draw(canvas):
    global time
    global lives,score
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # Scores and lives
    canvas.draw_text("Lives: "+str(lives), (100, 55), 25, 'Red')    
    canvas.draw_text("Score: "+str(score),(600, 55), 25, 'Green')      
    
    # draw ship and sprites
    my_ship.draw(canvas)
    random_asteroid.draw(canvas)
    missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    random_asteroid.update()
    missile.update()
    
    
def keyup_handler(key_press):
    
    if key_press== simplegui.KEY_MAP['up']:
        my_ship.thrust=not my_ship.thrust
        
    elif key_press == simplegui.KEY_MAP['space']:
         my_ship.launch_missile()
   
    elif key_press == simplegui.KEY_MAP['left']:
        my_ship.angle_vel+=0.07
    
    elif key_press == simplegui.KEY_MAP['right']:
        my_ship.angle_vel-=0.07

def keydown_handler(key_press):
    
    if key_press== simplegui.KEY_MAP['up']:
        my_ship.thrust=not my_ship.thrust
            
    elif key_press == simplegui.KEY_MAP['space']:
        my_ship.launch_missile()
            
    elif key_press == simplegui.KEY_MAP['left']:
        my_ship.angle_vel-=0.07
    
    elif key_press == simplegui.KEY_MAP['right']:
        my_ship.angle_vel+=0.07
        
        
# Timer handler that spawns a rock    
def rock_spawner():
    global rock_angle_vel,rock_pos,rock_vel,random_asteroid
    
    rock_pos[0]=random.randint(0,WIDTH)
    rock_pos[1]=random.randint(0,HEIGHT)
  
    rock_vel[0]=(random.random()*2-1)*2
    rock_vel[1]=(random.random()*2-1)*2
     
    rock_angle_vel=(random.random()*2-1)/10
    random_asteroid = Sprite(rock_pos, rock_vel, 0, rock_angle_vel, asteroid_image, asteroid_info)
        
# Initialize frame
frame = simplegui.create_frame("RiceRocks", WIDTH, HEIGHT)

# Initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
missile = Sprite(missile_pos,missile_vel, 0, 0, missile_image, missile_info, missile_sound)
random_asteroid = Sprite(rock_pos,rock_vel, 0, rock_angle_vel, asteroid_image, asteroid_info)

# Keyboard handlers
frame.set_keyup_handler(keyup_handler)
frame.set_keydown_handler(keydown_handler)

# Register handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000.0, rock_spawner)

# Start the game
timer.start()
frame.start()
