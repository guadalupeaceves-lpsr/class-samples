# this is a class-sample that you will have to move to your other directory

import turtle

def drawSide(myTurtle):
        ct = 0
        while ct < 4:
                drawVee(myTurtle)
                ct = ct + 1

def drawVee(myTurtle):
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.left(90)

shawn = turtle.Turtle()
drawSide(shawn)
count = 0

while count < 4:
        drawSide(shawn)
        shawn.right(90)
        count = count + 1

turtle.exitonclick()

