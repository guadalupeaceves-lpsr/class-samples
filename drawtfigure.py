import turtle
import random

def drawTee(myTurtle):
	count = 0
	while count < 4:
		myTurtle.penup()
		drawFourTees(myTurtle)
		count = count + 1

def drawFourTees(myTurtle):
	parts = 0
	myTurtle.goto(x,y)
	myTurtle.pendown()
	otherpart = 0
	myTurtle.forward(100)	
	while otherpart < 4:
		myTurtle.right(90)
		myTurtle.forward(35)
		myTurtle.backward(35)
		otherpart = otherpart + 1
	parts = parts + 1
	myTurtle.right(90)		

x = random.randint(-10,10)
y = random.randint(-10,10)
snowflakemaker = turtle.Turtle()
drawTee(snowflakemaker)


# make your turtle down gere and pass it to the appropriate places

