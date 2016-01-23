import turtle

def drawOneCube(myTurtle):
	sidesOf_dark_Rhombus = 0
	myTurtle.left(30)
	myTurtle.fillcolor("darkblue")
	myTurtle.begin_fill()
	while sidesOf_dark_Rhombus < 2:
		myTurtle.forward(20)
		myTurtle.right(60)
		myTurtle.forward(20)
		myTurtle.right(120)
		sidesOf_dark_Rhombus = sidesOf_dark_Rhombus + 1
	myTurtle.end_fill()
	sidesOf_light_Rhombus = 0
	myTurtle.right(120)
	myTurtle.fillcolor("lightblue")
	myTurtle.begin_fill()
	while sidesOf_light_Rhombus < 2:
		myTurtle.forward(20)
		myTurtle.left(60)
		myTurtle.forward(20)
		myTurtle.left(120)
		sidesOf_light_Rhombus = sidesOf_light_Rhombus + 1
	myTurtle.end_fill()
	myTurtle.right(270)
	myTurtle.penup()
	myTurtle.forward(35)
	myTurtle.right(90)
	myTurtle.pendown()
	sidesOf_medium_Rhombus = 0
	myTurtle.fillcolor("blue")
	myTurtle.begin_fill()
	while sidesOf_medium_Rhombus < 2:
		myTurtle.forward(20)
		myTurtle.right(60)
		myTurtle.forward(20)
		myTurtle.right(120)
		sidesOf_medium_Rhombus = sidesOf_medium_Rhombus + 1
	myTurtle.end_fill()

def drawOneRowOfCubes(myTurtle):
	numberOfCubes = 0
	while numberOfCubes < 6:
		drawOneCube(myTurtle)
		myTurtle.left(120)
		myTurtle.right(30)
		numberOfCubes = numberOfCubes + 1

def drawRowOne(myTurtle, x, y):
	myTurtle.penup()
	myTurtle.goto(x, y)
	myTurtle.pendown()

def drawRowTwo(myTurtle, x, y):
	myTurtle.penup()
	myTurtle.goto(x, y)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.right(60)
	myTurtle.forward(20)

def drawRowThree(myTurtle, x, y):
	myTurtle.penup()
	drawRowTwo(myTurtle, x, y)
	myTurtle.left(60)
	myTurtle.forward(20)
	myTurtle.right(60)
	myTurtle.forward(20)

def drawRowFour(myTurtle, x, y):
	myTurtle.penup()
	drawRowThree(myTurtle, x, y)
	myTurtle.left(60)
	myTurtle.forward(20)
	myTurtle.right(60)
	myTurtle.forward(20)
	myTurtle.left(150)
	myTurtle.pendown()

def drawWholePicture(myTurtle, x, y):
	drawRowOne(myTurtle, x, y)
	drawOneRowOfCubes(myTurtle)	
	drawRowTwo(myTurtle, x, y)
	myTurtle.left(150)
	myTurtle.pendown()
	drawOneRowOfCubes(myTurtle)
	drawRowThree(myTurtle, x, y)
	myTurtle.left(150)
	myTurtle.pendown()
	drawOneRowOfCubes(myTurtle)
	drawRowFour(myTurtle, x, y)
	drawOneRowOfCubes(myTurtle)

thePictureCreator = turtle.Turtle()
xcoordinate = -150
ycoordinate = 150
drawWholePicture(thePictureCreator, xcoordinate, ycoordinate)
turtle.exitonclick()
