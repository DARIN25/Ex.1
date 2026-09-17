hidden = True
def setup():
    fullScreen()
    
def dog(x,y,s):
    head_dog(x,y,s)
    eye2_dog(x,y,s)
    eye_dog(x,y,s)
    eye1_dog(x,y,s)
    nose_dog(x,y,s)
    mouth_dog(x,y,s)
    ear_dog(x,y,s)
    ear1_dog(x,y,s)
    cheek_dog(x,y,s)
    
def head_dog(x,y,s):
    fill(210,160,90)
    ellipse(x,y,s*2,s*2)

def ear_dog(x,y,s):
    fill(60,30,10)
    ellipse(x-(s/2),y-(s/1.5),s/1.7,s/1.8)

def ear1_dog(x,y,s):
    fill(210,150,80)
    ellipse(x+(s/2),y-(s/1.5),s/1.7,s/1.8)

    
def eye_dog(x,y,s):
    fill(20)
    ellipse(x-(s/3),y-(s/5),s/3,s/3)
    ellipse(x+(s/3),y-(s/5),s/3,s/3)
    
def eye1_dog(x,y,s):
    fill(255)
    ellipse(x-(s/2.5),y-(s/8),s/10,s/10)
    ellipse(x-(s/4),y-(s/4),s/8,s/8)
    ellipse(x+(s/4),y-(s/8),s/10,s/10)
    ellipse(x+(s/2.5),y-(s/4),s/8,s/8)
   
def eye2_dog(x,y,s):
    fill(255)
    ellipse(x+s/3,y-(s/5),s/2.5,s/2.5)
    
def nose_dog(x,y,s):
    fill(20)
    ellipse(x,y+(s/10),s/6,s/8)

def mouth_dog(x,y,s):
    line(x,y+(s/6),x,y+(s/3))
    line(x,y+(s/3),x-(s/8),y+(s/2.5))
    line(x,y+(s/3),x+(s/8),y+(s/2.5))
    
def cheek_dog(x,y,s):
    fill(245,253,208)
    ellipse(x-(s/2),y+(s/6),s/5,s/10)
    ellipse(x+(s/2),y+(s/6),s/5,s/10)
    
def dog_card(x,y,s,h):
    stroke(0)
    fill(255)
    rect(x-(s/2),y-(s*1.5)/2,s,s*1.5,12)
    if h:
        dog(x,y,s/4)
    return "dog"

def setup():
    size(500,500)
    
def Panda(x,y,s):
    ear_Panda(x,y,s)
    ear1_Panda(x,y,s)
    head_Panda(x,y,s)
    eye_Panda(x,y,s)
    eye1_Panda(x,y,s)
    nose_Panda(x,y,s)
    mouth_Panda(x,y,s)
    
def ear_Panda(x,y,s):
    fill(100)
    ellipse(x-s/2,y-(s/1.5),s/1.5,s/1.5)
    ellipse(x+s/2,y-(s/1.5),s/1.5,s/1.5)
    
def ear1_Panda(x,y,s):
    fill(255,182,193)
    ellipse(x-s/2,y-(s/1.5),s/2,s/2)
    ellipse(x+s/2,y-(s/1.5),s/2,s/2)
    
def head_Panda(x,y,s):
    fill(255)
    ellipse(x,y,s*2,s*1.6)
    
def eye_Panda(x,y,s):
    fill(100)
    ellipse(x-(s/2.5),y-(s/5),s/2,s/2)
    ellipse(x+(s/2.5),y-(s/5),s/2,s/2)
    
def eye1_Panda(x,y,s):
    fill(255)
    ellipse(x-(s/2.8),y-(s/4),s/10,s/10)
    ellipse(x+(s/2.8),y-(s/4),s/10,s/10)
    
def nose_Panda(x,y,s):
    fill(100)
    ellipse(x,y+(s/20),s/8,s/10)
    
def mouth_Panda(x,y,s):
    fill(255,0,0)
    line(x,y+(s/10),x,y+(s/3))
    ellipse(x,y+(s/3),s/5,s/10)
    
def Panda_Panda(x,y,s):
    ear(x,y,s)
    ear1(x,y,s)
    head(x,y,s)
    eye(x,y,s)
    eye1(x,y,s)
    nose(x,y,s)
    mouth(x,y,s)
    
def panda_card(x,y,s,h):
    stroke(0)
    fill(255)
    rect(x-s/2,y-(s*1.5)/2,s,s*1.5,12)
    if h:
        Panda(x,y,s/4)
    return "Panda"

def squid(x,y,s):
    head_squid(x,y,s)
    eye_squid(x,y,s)
    nose_squid(x,y,s)
    nose1_squid(x,y,s)
    mouth_squid(x,y,s)
    
def head_squid(x,y,s):
    fill(255,182,200)
    ellipse(x,y,s*2,s*1.6)
    
def eye_squid(x,y,s):
    fill(0)
    ellipse(x-(s/2.5),y-(s/5),s/10,s/10)
    ellipse(x+(s/2.5),y-(s/5),s/10,s/10)
    
def nose_squid(x,y,s):
    fill(255,182,200)
    ellipse(x,y+(s/10),s/2,s/2)
    
def nose1_squid(x,y,s):
    fill(0)
    line(x-(s/10),y,x+(s/10),y+(s/5))
    line(x+(s/10),y,x-(s/10),y+(s/5))
    
def mouth_squid(x,y,s):
    fill(255,182,200)
    ellipse(x-(s/1.6),y+(s/1.3),s/3,s/2)
    ellipse(x-(s/3.4),y+(s/1.2),s/3,s/2)
    ellipse(x+(s/1.6),y+(s/1.3),s/3,s/2)
    ellipse(x+(s/2.8),y+(s/1.2),s/3,s/2)
    ellipse(x+(s/30),y+(s/1.2),s/3,s/2)
    
def squid_card(x,y,s,h):
    stroke(0)
    fill(255)
    rect(x-(s/2),y-(s*1.5)/2,s,s*1.5,12)
    if h:
        squid(x,y,s/4)
    return "squid"

def cat(x, y, s):
    ear_cat(x, y, s)       
    ear1_cat(x, y, s)    
    head_cat(x, y, s)     
    nuad_maew(x, y, s)       
    eye_cat(x, y, s)     
    eye1_cat(x, y, s)     
    nose_cat(x, y, s)     
    mouth_cat(x, y, s)    
    cheek_cat(x, y, s)     

def head_cat(x, y, s):
    fill(180) 
    ellipse(x, y, s*1.8, s*1.4)

def ear_cat(x, y, s): # huu dan nork
    fill(180)
    triangle(x-(s*0.75), y-(s*0.2),     #L
             x-(s*0.35), y-(s*0.65), 
             x-(s*0.75), y-(s*0.85))
    triangle(x+(s*0.75), y-(s*0.2),     #R
             x+(s*0.35), y-(s*0.65), 
             x+(s*0.75), y-(s*0.85))

def ear1_cat(x, y, s): # huu dan nai
    fill(255, 182, 193)
    triangle(x-(s*0.67), y-(s*0.28),    #L
             x-(s*0.38), y-(s*0.6), 
             x-(s*0.70), y-(s*0.78))
    triangle(x+(s*0.67), y-(s*0.28),    #R
             x+(s*0.38), y-(s*0.6), 
             x+(s*0.70), y-(s*0.78))

def nuad_maew(x, y, s):
    line(x-(s*0.4), y+(s*0.08), x-(s*0.85), y+(s*0.02))  #L
    line(x-(s*0.4), y+(s*0.16), x-(s*0.85), y+(s*0.16))
    line(x-(s*0.4), y+(s*0.24), x-(s*0.85), y+(s*0.30))
    
    line(x+(s*0.4), y+(s*0.08), x+(s*0.85), y+(s*0.02))  #R
    line(x+(s*0.4), y+(s*0.16), x+(s*0.85), y+(s*0.16))
    line(x+(s*0.4), y+(s*0.24), x+(s*0.85), y+(s*0.30))

def eye_cat(x, y, s): # ta dam
    fill(0)
    ellipse(x-(s*0.32), y-(s*0.08), s*0.25, s*0.28) #L
    ellipse(x+(s*0.32), y-(s*0.08), s*0.25, s*0.28) #R

def eye1_cat(x, y, s): # ta kow
    fill(255)
    ellipse(x-(s*0.36), y-(s*0.13), s*0.1, s*0.1)
    ellipse(x+(s*0.28), y-(s*0.13), s*0.1, s*0.1)

def nose_cat(x, y, s): 
    fill(255, 120, 150)
    ellipse(x, y+(s*0.06), s*0.12, s*0.08)

def mouth_cat(x, y, s): 
    line(x, y+(s/9), x , y+(s/4))
    line(x, y+(s/4), x-(s/9), y+(s/3))
    line(x, y+(s/4), x+(s/9), y+(s/3))

def cheek_cat(x, y, s): 
    noStroke()
    fill(255, 182, 193, 180)
    ellipse(x-(s*0.48), y+(s*0.1), s*0.2, s*0.12)
    ellipse(x+(s*0.48), y+(s*0.1), s*0.2, s*0.12)

def cat_card(x, y, s, h):
    stroke(0)
    fill(255) # si card
    rect(x-(s/2), y-(s*1.5)/2, s, s*1.5,12) # 12 kob
    
    if h:
        cat(x, y, s / 3)
    return "cat"

def chicken(x,y,s):
    ngon_kai(x,y,s)     
    head(x,y,s)    
    niang_kai(x,y,s)   
    pak_kai(x,y,s)          
    eye_kai(x,y,s)       
    eye1_kai(x,y,s)     
    cheek_kai(x,y,s)     

def ngon_kai(x,y,s): 
    fill(235,60,60)
    ellipse(x-(s*0.18), y-(s*0.65), s*0.22, s*0.32)
    ellipse(x, y-(s*0.72), s*0.26, s*\0.38)
    ellipse(x+(s*0.18), y-(s*0.65), s*0.22, s*0.32)

def head(x,y,s):
    fill(255,245,180) 
    ellipse(x,y,s*1.6,s*1.4)

def niang_kai(x,y,s): 
    fill(235,60,60)
    ellipse(x-(s*0.07), y+(s*0.27), s*0.14, s*0.20)
    ellipse(x+(s*0.07), y+(s*0.27), s*0.14, s*0.20)

def pak_kai(x,y,s): 
    fill(255,140,0)
    triangle(x-(s*0.12), y+(s*0.06), 
             x+(s*0.12), y+(s*0.06), 
             x, y+(s*0.22))

def eye_kai(x,y,s): # ta dam baew
    stroke(0)
    fill(40)
    ellipse(x-(s*0.3), y-(s*0.08), s*0.23, s*0.26)
    ellipse(x+(s*0.3), y-(s*0.08), s*0.23, s*0.26)

def eye1_kai(x,y,s):
    fill(255)
    ellipse(x-(s*0.34), y-(s*0.13), s*0.09, s*0.09)
    ellipse(x+(s*0.26), y-(s*0.13), s*0.09, s*0.09)

def cheek_kai(x,y,s): # kaem
    noStroke()
    fill(255, 182, 193, 180)
    ellipse(x-(s*0.48), y+(s*0.1), s*0.2, s*0.12)
    ellipse(x+(s*0.48), y+(s*0.1), s*0.2, s*0.12)

def chicken_card(x,y,s,h):
    stroke(0)
    fill(255) # si card
    rect(x-(s/2), y-(s*1.5)/2, s, s*1.5,12) # 12 kob
    
    if h:
        chicken(x, y, s/3)
    return "chicken"

def cow(x, y, s):
    khao_wua(x, y, s)    
    ear_cow(x, y, s)
    ear1_cow(x, y, s)      
    head_cow(x, y, s)      
    spot_cow(x, y, s)     
    snout_cow(x, y, s)    
    nose_cow(x, y, s)      
    eye2_cow(x, y, s)     
    eye_cow(x, y, s)       
    eye1_cow(x, y, s)      
    cheek_cow(x, y, s)    

def khao_wua(x, y, s): 
    fill(240, 200, 120)
    ellipse(x - (s * 0.38), y - (s * 0.52), s * 0.24, s * 0.38)
    ellipse(x + (s * 0.38), y - (s * 0.52), s * 0.2, s * 0.38)

def ear_cow(x, y, s): # huu dan nork
    stroke(0)
    fill(255)
    ellipse(x - (s * 0.65), y - (s * 0.22), s * 0.45, s * 0.25)
    ellipse(x + (s * 0.65), y - (s * 0.22), s * 0.45, s * 0.25)

def ear1_cow(x, y, s): # huu dan nai
    stroke(0)
    fill(255, 182, 193)
    ellipse(x - (s * 0.65), y - (s * 0.22), s * 0.28, s * 0.15)
    ellipse(x + (s * 0.65), y - (s * 0.22), s * 0.28, s * 0.15)

def head_cow(x, y, s): # hua wua
    stroke(0)
    fill(255)
    ellipse(x, y, s * 1.6, s * 1.4)

def spot_cow(x, y, s): # lai wua
    noStroke()
    fill(40)
    ellipse(x - (s * 0.38), y - (s * 0.2), s * 0.45, s * 0.45)

def snout_cow(x, y, s): # pak yuen
    stroke(0)
    fill(255, 190, 200)
    ellipse(x, y + (s * 0.18), s * 0.75, s * 0.42)

def nose_cow(x, y, s): # ru jamuk
    stroke(0)
    fill(40)
    ellipse(x - (s * 0.12), y + (s * 0.14), s * 0.08, s * 0.12)
    ellipse(x + (s * 0.12), y + (s * 0.14), s * 0.08, s * 0.12)


def eye2_cow(x, y, s): # ta kow
    stroke(0)
    fill(255)
    ellipse(x - (s * 0.3), y - (s * 0.08), s * 0.3, s * 0.33)
    ellipse(x + (s * 0.3), y - (s * 0.08), s * 0.3, s * 0.33)

def eye_cow(x, y, s): # ta dam baew
    stroke(0)
    fill(40)
    ellipse(x - (s * 0.3), y - (s * 0.08), s * 0.23, s * 0.26)
    ellipse(x + (s * 0.3), y - (s * 0.08), s * 0.23, s * 0.26)

def eye1_cow(x, y, s): # pra kai ta
    noStroke()
    fill(255)
    ellipse(x - (s * 0.34), y - (s * 0.13), s * 0.09, s * 0.09)
    ellipse(x + (s * 0.26), y - (s * 0.13), s * 0.09, s * 0.09)

def cheek_cow(x, y, s): # kaem
    noStroke()
    fill(255, 182, 193, 180)
    ellipse(x - (s * 0.48), y + (s * 0.05), s * 0.2, s * 0.12)
    ellipse(x + (s * 0.48), y + (s * 0.05), s * 0.2, s * 0.12)

def cow_card(x, y, s, h):
    stroke(0)
    fill(255) # si card
    rect(x - (s / 2), y - (s * 1.5) / 2, s, s * 1.5, 12) # 12 kob
    
    if h:
        cow(x, y, s / 3)
    return "cow"

def rabbit(x,y,s):
    ear_rabbit(x,y,s)
    ear1_rabbit(x,y,s)
    head_rabbit(x,y,s)
    eye_rabbit(x,y,s)
    eye1_rabbit(x,y,s)
    nose_rabbit(x,y,s)
    mouth_rabbit(x,y,s)
    cheek_rabbit(x,y,s)

def head_rabbit(x,y,s):
    fill(255)
    ellipse(x, y, s*1.8, s*1.5)

def ear_rabbit(x, y, s): #huu dan nork
    fill(255)
    ellipse(x-(s/3), y-(s/1.1), s/2.5,s*1.3)
    ellipse(x+(s/3), y-(s/1.1), s/2.5,s*1.3)

def ear1_rabbit(x, y, s): #huu dan nai
    fill(255, 182, 193)
    ellipse(x-(s/3), y-(s/1.1), s/5,s)
    ellipse(x+(s/3), y-(s/1.1), s/5,s)

def eye_rabbit(x, y, s): #ta dam
    fill(40)
    ellipse(x-(s/3), y-(s/6), s/4,s/4)
    ellipse(x+(s/3), y-(s/6), s/4,s/4)

def eye1_rabbit(x, y, s): #ta dan nai
    fill(255)
    ellipse(x-(s/2.8), y-(s/4), s/10, s/10)
    ellipse(x+(s/3.3), y-(s/4), s/10, s/10)

def nose_rabbit(x, y, s):
    fill(255, 120, 150)
    ellipse(x, y+(s/10), s/8, s/12) 

def mouth_rabbit(x, y, s):
    noFill()
    line(x, y+(s/7), x , y+(s/4))
    line(x, y+(s/4), x-(s/10), y+(s/3))
    line(x, y+(s/4), x+(s/10), y+(s/3))

def cheek_rabbit(x, y, s):
    fill(255, 182, 193)
    ellipse(x-(s/2), y+(s/8), s/4, s/6)
    ellipse(x+(s/2), y+(s/8), s/4, s/6)

def rabbit_card(x, y, s, h):
    stroke(0)
    fill(255) #si card
    rect(x-(s/2), y-(s * 1.5)/ 2, s, s * 1.5,12) # 12 kob
    
    if h:
        rabbit(x, y, s / 3)
    return "rabbit"

def bear(x, y, s):
    bear_ears(x, y, s)
    bear_head(x, y, s)
    bear_muzzle(x, y, s)
    bear_nose(x, y, s)
    bear_eyes(x, y, s)

def bear_ears(x, y, s):
    fill(130, 85, 50)
    ellipse(x - s * 0.7, y - s * 0.7, s * 0.6, s * 0.6)
    ellipse(x + s * 0.7, y - s * 0.7, s * 0.6, s * 0.6)
    
    fill(185, 135, 95)
    ellipse(x - s * 0.7, y - s * 0.7, s * 0.35, s * 0.35)
    ellipse(x + s * 0.7, y - s * 0.7, s * 0.35, s * 0.35)

def bear_head(x, y, s):
    fill(150, 100, 60)
    ellipse(x, y, s * 1.8, s * 1.6)

def bear_muzzle(x, y, s):
    fill(215, 175, 135)
    ellipse(x, y + s * 0.25, s * 0.8, s * 0.6)

def bear_nose(x, y, s):
    fill(35, 25, 20)
    ellipse(x, y + s * 0.12, s * 0.3, s * 0.2)
    line(x, y + s * 0.22, x, y + s * 0.38)
    line(x, y + s * 0.38, x - s * 0.15, y + s * 0.45)
    line(x, y + s * 0.38, x + s * 0.15, y + s * 0.45)

def bear_eyes(x, y, s):
    fill(25)
    ellipse(x - s * 0.4, y - s * 0.1, s * 0.18, s * 0.18)
    ellipse(x + s * 0.4, y - s * 0.1, s * 0.18, s * 0.18)
    fill(255)
    ellipse(x - s * 0.42, y - s * 0.12, s * 0.06, s * 0.06)
    ellipse(x + s * 0.38, y - s * 0.12, s * 0.06, s * 0.06)

def bear_card(x, y, s, h):
    fill(255)
    rect(x - (s / 2), y - (s * 1.5) / 2, s, s * 1.5, 12)
    if h:
        bear(x, y, s / 3)
    return "bear"

def fish(x, y, s):
    cx = x + s * 0.22
    cy = y + s * 0.05
    
    fish_tail_fin(cx, cy, s)
    fish_dorsal_fin(cx, cy, s)
    fish_body(cx, cy, s)
    fish_eye(cx, cy, s)


def fish_tail_fin(x, y, s):
    fill(235, 100, 70)
    triangle(x - s * 0.7, y, x - s * 1.3, y - s * 0.6, x - s * 1.3, y + s * 0.6)

def fish_dorsal_fin(x, y, s):
    fill(235, 100, 70)
    triangle(x - s * 0.3, y - s * 0.45, x + s * 0.1, y - s * 0.45, x - s * 0.1, y - s * 0.9)

def fish_body(x, y, s):
    fill(250, 130, 85)
    ellipse(x, y, s * 1.7, s * 1.0)

def fish_eye(x, y, s):
    fill(255)
    ellipse(x + s * 0.45, y - s * 0.15, s * 0.28, s * 0.28)
    fill(20)
    ellipse(x + s * 0.48, y - s * 0.15, s * 0.14, s * 0.14)
    fill(255)
    ellipse(x + s * 0.50, y - s * 0.18, s * 0.05, s * 0.05)



def fish_card(x, y, s, h):
    fill(255)
    rect(x - (s / 2), y - (s * 1.5) / 2, s, s * 1.5, 12)
    if h:
        fish(x, y, s / 3)
    return "fish"

def turtle(x, y, s):
    turtle_feet(x, y, s)
    turtle_tail(x, y, s)
    turtle_shell(x, y, s)
    turtle_head(x, y, s)
    turtle_eyes(x, y, s)

def turtle_feet(x, y, s):
    fill(95, 145, 80)
    ellipse(x - s * 0.7, y - s * 0.5, s * 0.5, s * 0.35)
    ellipse(x + s * 0.7, y - s * 0.5, s * 0.5, s * 0.35)
    ellipse(x - s * 0.6, y + s * 0.5, s * 0.45, s * 0.35)
    ellipse(x + s * 0.6, y + s * 0.5, s * 0.45, s * 0.35)

def turtle_tail(x, y, s):
    fill(95, 145, 80)
    triangle(x - s * 0.15, y + s * 0.8, x + s * 0.15, y + s * 0.8, x, y + s * 1.1)

def turtle_shell(x, y, s):
    fill(60, 110, 50)
    ellipse(x, y, s * 1.6, s * 1.8)

def turtle_head(x, y, s):
    fill(110, 165, 95)
    ellipse(x, y - s * 0.85, s * 0.6, s * 0.7)

def turtle_eyes(x, y, s):
    fill(255)
    ellipse(x - s * 0.18, y - s * 0.95, s * 0.18, s * 0.18)
    ellipse(x + s * 0.18, y - s * 0.95, s * 0.18, s * 0.18)
    fill(20)
    ellipse(x - s * 0.18, y - s * 0.95, s * 0.08, s * 0.08)
    ellipse(x + s * 0.18, y - s * 0.95, s * 0.08, s * 0.08)

def turtle_card(x, y, s, h):
    fill(255)
    rect(x - (s / 2), y - (s * 1.5) / 2, s, s * 1.5, 12)
    if h:
        turtle(x, y, s / 3)
    return "turtle"


def draw():
    background(255)
    total_card = len(cards)
    
    i=140
    panda_card(i,height/2.3,100,hidden)
    dog_card(i*2,height/2.3,100,hidden)
    squid_card(i*3,height/2.3,100,hidden)
    cat_card(i*4,height/2.3, 100, hidden)
    chicken_card(i*5,height/2.3, 100, hidden)
    cow_card(i*6,height/2.3, 100, hidden)
    rabbit_card(i*7,height/2.3,100,hidden)
    bear_card(i*8, height / 2.3, 100, hidden)
    fish_card(i*9, height/2.3, 100, hidden)
    turtle_card(i*10, height / 2.3, 100, hidden)
    
    panda_card(i,height/1.5,100,hidden)
    dog_card(i*2,height/1.5,100,hidden)
    squid_card(i*3,height/1.5,100,hidden)
    cat_card(i*4,height/1.5, 100, hidden)
    chicken_card(i*5,height/1.5, 100, hidden)
    cow_card(i*6,height/1.5, 100, hidden)
    rabbit_card(i*7,height/1.5,100,hidden)
    bear_card(i*8, height / 1.5, 100, hidden)
    fish_card(i*9, height/1.5, 100, hidden)
    turtle_card(i*10, height / 1.5, 100, hidden)
