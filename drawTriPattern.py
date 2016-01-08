import turtle

import random

# creating the triangles 
def drawSimpleTriangle(myTurtle):
	sidecountTri = 0
	while sidecountTri < 3:
		sidecountTri = sidecountTri + 1
		myTurtle.right(120)
		myTurtle.forward(10)

# creates the row of triangles
def drawTriangleRow(myTurtle):
	numberofTriInRow = 0
	while numberofTriInRow < 4:
		drawSimpleTriangle(myTurtle)
		myTurtle.penup()
		myTurtle.backward(45)
		myTurtle.pendown()
		numberofTriInRow = numberofTriInRow + 1

# creats the whole thing
def drawTriangleMultiplesTogetherPart1(myTurtle):
	numberoftimes = 0
	while numberoftimes < 3:
		myTurtle.penup()
		myTurtle.goto(x,y)
		myTurtle.pendown()
		drawTriangleRow(myTurtle)
		numberoftimes = numberoftimes + 1
		myTurtle.right(340)

def drawTriangleMultiplesTogetherPart2(myTurtle):
        numberoftimes = 0
        while numberoftimes < 3:
                myTurtle.penup()
                myTurtle.goto(x,y)
                myTurtle.pendown()
                drawTriangleRow(myTurtle)
                numberoftimes = numberoftimes + 1
                myTurtle.right(340)

def drawTrianglesMess(myTurtle):
	drawTriangleMultiplesTogetherPart1(myTurtle)
	myTurtle.penup()
	myTurtle.left(120)
	drawTriangleMultiplesTogetherPart2(myTurtle)

x = random.randint(-10,10)
y = random.randint(-10,10)
triangleMessCreator = turtle.Turtle()
drawTrianglesMess(triangleMessCreator)

turtle.exitonclick()
