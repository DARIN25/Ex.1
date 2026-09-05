hidden = True
def setup():
    size(800,800)
    
def squid(x,y,s):
    head(x,y,s)
    eye(x,y,s)
    nose(x,y,s)
    nose1(x,y,s)
    mouth(x,y,s)
    
def head(x,y,s):
    fill(255,182,200)
    ellipse(x,y,s*2,s*1.6)
    
def eye(x,y,s):
    fill(0)
    ellipse(x-(s/2.5),y-(s/5),s/10,s/10)
    ellipse(x+(s/2.5),y-(s/5),s/10,s/10)
    
def nose(x,y,s):
    fill(255,182,200)
    ellipse(x,y+(s/10),s/2,s/2)
    
def nose1(x,y,s):
    fill(0)
    line(x-(s/10),y,x+(s/10),y+(s/5))
    line(x+(s/10),y,x-(s/10),y+(s/5))
    
def mouth(x,y,s):
    fill(255,182,200)
    ellipse(x-(s/1.6),y+(s/1.3),s/3,s/2)
    ellipse(x-(s/3.4),y+(s/1.2),s/3,s/2)
    ellipse(x+(s/1.6),y+(s/1.3),s/3,s/2)
    ellipse(x+(s/2.8),y+(s/1.2),s/3,s/2)
    ellipse(x+(s/30),y+(s/1.2),s/3,s/2)
    
def squid_crad(x,y,s,h):
    fill(255)
    rect(x-(s/2),y-(s*1.5)/2,s,s*1.5)
    if h:
        squid(x,y,s/3)
    return "squid"
    
def draw():
    background(255)
    squid_crad(width/2,height/2,200,hidden)
