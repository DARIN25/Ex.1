def setup():
    size(500,500)
    
def num1(x,y,s):
    hu(x,y,s)
    hu1(x,y,s)
    h(x,y,s)
    eye(x,y,s)
    eye1(x,y,s)
    g(x,y,s)
    
def hu(x,y,s):
    fill(100)
    ellipse(x-s/2,y-(s/1.5),s/1.5,s/1.5)
    ellipse(x+s/2,y-(s/1.5),s/1.5,s/1.5)
    
def hu1(x,y,s):
    fill(255,182,193)
    ellipse(x-s/2,y-(s/1.5),s/2,s/2)
    ellipse(x+s/2,y-(s/1.5),s/2,s/2)
    
def h(x,y,s):
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
    
def g(x,y,s):
    fill(100)
    ellipse(x,y+(s/20),s/8,s/10)
    
    
    
def draw():
    background(255)
    num1(250,150,50)
