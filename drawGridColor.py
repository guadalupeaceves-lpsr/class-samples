import turtle


def drawLeftSquare(myTurtle):
	countOfSides = 0
	while countOfSides < 4:
	        myTurtle.left(90)
	        myTurtle.forward(15)
		countOfSides = countOfSides + 1


def drawRightSquare(myTurtle):
        countOfSides = 0
	myTurtle.left(90)
        while countOfSides < 4:
                myTurtle.forward(15)
                myTurtle.right(90)
                countOfSides = countOfSides + 1

def drawCompleteSquare(myTurtle):
	myTurtle.color("red")
	drawLeftSquare(myTurtle)
	myTurtle.color("blue")
	drawRightSquare(myTurtle)
	myTurtle.left(90)
	myTurtle.color("green")	
	drawLeftSquare(myTurtle)
	myTurtle.color("yellow")
	drawRightSquare(myTurtle)

def drawCompletePicture(myTurtle):
	countOfBigSquare2 = 0
	drawCompleteSquare(myTurtle)
	while countOfBigSquare2 < 4:
		myTurtle.penup()
		myTurtle.forward(11)
		myTurtle.left(90)
		myTurtle.forward(15)
		myTurtle.right(90)
		myTurtle.forward(15)
		myTurtle.left(90)
		myTurtle.pendown()
		drawCompleteSquare(myTurtle)
		countOfBigSquare2 = countOfBigSquare2 + 1

startTheCompleteProgramForPicture = turtle.Turtle()
drawCompletePicture(startTheCompleteProgramForPicture)
turtle.exitonclick()

