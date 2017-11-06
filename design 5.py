import turtle
from random import randint
from myshape import *

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)
bob.width(10)
turtle.tracer(0)
turtle.bgcolor(0,0,0)

for times in range(50):
    x=randint(-500,500)
    y=randint(-800,800)
    n=randint(4,10)
    red=(0,255)
    blue=(0,255)
    green=(0,255)
    bob.color(139-times,times,139-times)
    polygon(bob,100,60-times)
    bob.right(10)
for times in range(50):
    x=randint(-500,500)
    y=randint(-800,800)
    n=randint(4,10)
    red=(0,255)
    blue=(0,255)
    green=(0,255)
    bob.color(150-times,times,100-times)
    star(bob,600-times)
    bob.left(130)
move(bob,25,70)
for times in range(89):
    bob.color(222-times,times,times)
    bob.begin_fill()
    star(bob,350)
    bob.forward(130)
    bob.left(135)
    bob.color(250-times,255-times,250-times)
    bob.forward(13)
    bob.right(12)






