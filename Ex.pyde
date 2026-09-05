def setup():
    size(500,500)
    
x = 50

def draw_balloon(x, y):
    ellipse(x, y, 100, 100)
    line(x, y+50, x, y+200)

def draw():
    background(255)
    global x
    draw_balloon(x, mouseY)
    x = x + 1
    if x > width:
        x = 100
