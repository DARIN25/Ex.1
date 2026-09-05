def setup():
    size(500,500)
    
def Panda(x,y,s):
    ear(x,y,s)
    ear1(x,y,s)
    head(x,y,s)
    eye(x,y,s)
    eye1(x,y,s)
    nose(x,y,s)
    mouth(x,y,s)
    
def ear(x,y,s):
    fill(100)
    ellipse(x-s/2,y-(s/1.5),s/1.5,s/1.5)
    ellipse(x+s/2,y-(s/1.5),s/1.5,s/1.5)
    
def ear1(x,y,s):
    fill(255,182,193)
    ellipse(x-s/2,y-(s/1.5),s/2,s/2)
    ellipse(x+s/2,y-(s/1.5),s/2,s/2)
    
def head(x,y,s):
    fill(255)
    ellipse(x,y,s*2,s*1.6)
    
def eye(x,y,s):
    fill(100)
    ellipse(x-(s/2.5),y-(s/5),s/2,s/2)
    ellipse(x+(s/2.5),y-(s/5),s/2,s/2)
    
def eye1(x,y,s):
    fill(255)
    ellipse(x-(s/2.8),y-(s/4),s/10,s/10)
    ellipse(x+(s/2.8),y-(s/4),s/10,s/10)
    
def nose(x,y,s):
    fill(100)
    ellipse(x,y+(s/20),s/8,s/10)
    
def mouth(x,y,s):
    fill(255,0,0)
    line(x,y+(s/10),x,y+(s/3))
    ellipse(x,y+(s/3),s/5,s/10)
         
def draw():
    background(255)
    Panda(250,150,100)
