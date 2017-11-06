def square(t,distance):
    for times in range(8):
        t.forward(distance)
        t.left(90)
        
def triangle(t,distance):
    for times in range(3):
        t.forward(distance)
        t.left(120)

def pentagon(t,distance,side):
    angle=360/5
    for times in range(side):
        t.forward(distance)
        t.left(angle)
        
def polygon(t,distance,side):
    angle=360/side
    t.begin_fill()
    for times in range (side):
        t.forward(distance)
        t.left(angle)
        t.end_fill()
def star (t,distance):

    for times in range(8):
        t.forward(distance)
        t.left(135)
        
def move (t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

