hidden = True
def setup():
    size(800,800)
    
def dog(x,y,s):
    head(x,y,s)
    eye2(x,y,s)
    eye(x,y,s)
    eye1(x,y,s)
    nose(x,y,s)
    mouth(x,y,s)
    ear(x,y,s)
    ear1(x,y,s)
    cheek(x,y,s)
    
def head(x,y,s):
    fill(210,160,90)
    ellipse(x,y,s*2,s*2)

def ear(x,y,s):
    fill(60,30,10)
    ellipse(x-(s/2),y-(s/1.5),s/1.7,s/1.8)

def ear1(x,y,s):
    fill(210,150,80)
    ellipse(x+(s/2),y-(s/1.5),s/1.7,s/1.8)

    
def eye(x,y,s):
    fill(20)
    ellipse(x-(s/3),y-(s/5),s/3,s/3)
    ellipse(x+(s/3),y-(s/5),s/3,s/3)
    
def eye1(x,y,s):
    fill(255)
    ellipse(x-(s/2.5),y-(s/8),s/10,s/10)
    ellipse(x-(s/4),y-(s/4),s/8,s/8)
    ellipse(x+(s/4),y-(s/8),s/10,s/10)
    ellipse(x+(s/2.5),y-(s/4),s/8,s/8)
   
def eye2(x,y,s):
    fill(255)
    ellipse(x+s/3,y-(s/5),s/2.5,s/2.5)
    
def nose(x,y,s):
    fill(20)
    ellipse(x,y+(s/10),s/6,s/8)

def mouth(x,y,s):
    line(x,y+(s/6),x,y+(s/3))
    line(x,y+(s/3),x-(s/8),y+(s/2.5))
    line(x,y+(s/3),x+(s/8),y+(s/2.5))
    
def cheek(x,y,s):
    fill(245,253,208)
    ellipse(x-(s/2),y+(s/6),s/5,s/10)
    ellipse(x+(s/2),y+(s/6),s/5,s/10)
    
def dog_card(x,y,s,h):
    fill(255)
    rect(x-(s/2),y-(s*1.5)/2,s,s*1.5)
    if h:
        dog(x,y,s/3)
    return "dog"
    
def draw():
    background(255)
    dog_card(width/2,height/2,200,hidden)
