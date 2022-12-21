import math
import turtle
count = 0
while count <= 10:
    turtle.bgcolor("black")
    turtle.shape("turtle")
    turtle.speed(0)
    turtle.fillcolor("brown")
    phi = 137.508 * (math.pi/180.0)

    for i in range (160 + 40):
        r = 4 * math.sqrt(i)
        theta = i * phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        turtle.penup()
        turtle.goto(x,y)
        turtle.setheading(i * 137.508)
        turtle.pendown()
        if i < 160:
            turtle.stamp()
        else:
            turtle.fillcolor("yellow")
            turtle.begin_fill()
            turtle.right(75)
            turtle.forward(140)
            turtle.left(60)
            turtle.forward(140)
            turtle.left(125)
            turtle.forward(140)
            turtle.left(60)
            turtle.forward(140)
            turtle.end_fill()        
    turtle.hideturtle()
    count += 1
