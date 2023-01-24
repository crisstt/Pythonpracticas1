import turtle
import math

def xt(t):
    return 16*math.sin(t)**3

def yt(t):
    return 13*math.cos(t)-5*\
           math.cos(2*t)-2*\
           math.cos(3*t)-\
           math.cos(4*t)

t= turtle.Turtle()
t.speed(500)
turtle.bgcolor('black')

for i in range (2550):
    if i < 890:
        t.goto((xt(i)*20, yt(i)*20))
        t.pencolor('sky blue')
        t.goto(0,0)
    elif i > 890 and i < 1500:
        t.goto((xt(i)*20, yt(i)*20))
        t.pencolor('red')
        t.goto(0,0)
    else:
        t.goto((xt(i)*20, yt(i)*20))
        t.pencolor('dark green')
        t.goto(0,0)
