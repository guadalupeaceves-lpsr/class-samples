# shapeDrawer.py
# draws user-input shapes in random places on the screen
# with random sizes and colors
 
# bring in the packages of functions we need
import random
import turtle
 
# -------- functions start here ----------------

def regular_triangle(myTurtle, x, y, side):
        myTurtle.penup()
	color = ['blue','red','yellow','green']
	color = color.random(color)
	myTurtle.color(color)
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        while side_count < 3:
                myTurtle.forward(side)
                myTurtle.right(120)
                side_count = side_count + 1
 
def regular_square(myTurtle, x, y, side):
	myTurtle.penup()
	color = ['blue','red','yellow','green']
	color = color.random()
	myTurtle.color(color)
	myTurtle.goto(x,y)
	myTurtle.pendown()
        side_count2 = 0
	while side_count2 < 4:
		myTurtle.forward(side)
		myTurtle.left(90)
		side_count2 = side_count2 + 1
 
def regular_pentagon(myTurtle, x, y, side):
	myTurtle.penup()
	color = ['blue','red','yellow','green']
	color = color.random()
	myTurtle.color(color)
	myTurtle.goto(x,y)
	myTurtle.pendown()
        side_count3 = 0
	while side_count3 < 5:
		myTurtle.forward(side)
		myTurtle.left(72)
		side_count3 = side_count3 + 1
 
def regular_hexagon(myTurtle, x, y, side):
	myTurtle.penup()
	color = ['blue','red','yellow','green']
	color = color.random()	
	myTurtle.color(color)
	myTurtle.goto(x,y)
	myTurtle.pendown()
        side_count4 = 0
	while side_count4 < 6:
		myTurtle.forward(side)
		myTurtle.left(60)
		side_count4 = side_count4 + 1
 
def regular_octagon(myTurtle, x, y, side):
	myTurtle.penup()
	color = ['blue','red','yellow','green']
	color = color.random()
	myTurtle.color(color)
	myTurtle.goto(x,y)
        myTurtle.pendown()

        side_count5 = 0
        while side_count5 < 8:
                redcolornumber = random.randint(1,255)
                greencolornumber = random.randint(1,255)
                bluecolornumber = random.randint(1,255)
                myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
                myTurtle.forward(side)
                myTurtle.left(45)
                side_count5 = side_count5 + 1

def circle(myTurtle, x, y, radius):
        myTurtle.penup()
        redcolornumber = random.randint(1,255)
        greencolornumber = random.randint(1,255)
        bluecolornumber = random.randint(1,255)
        myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
        myTurtle.goto(x,y)
        myTurtle.pendown()
        myTurtle.circle(radius)

	
 
# -------- execution starts here ----------------
 
print("Welcome to the random shape drawer!")
print("You choose the shapes, and we choose the position, color, and size.")
 
squirt = turtle.Turtle()
 
shape = ""
while shape != "exit":
        print("Enter a shape - your choices are triangle, square, pentagon, hexagon, octagon, and circle.")
        print("If you're done making shapes, just type 'exit'.")
        shape = raw_input()
 
        randx = random.randint(-200,200)
        randy = random.randint(-200,200)
        randside = random.randint(5,100)
 
        if shape == 'triangle':
                regular_triangle(squirt, randx, randy, randside)
        elif shape == 'square':
                regular_square(squirt, randx, randy, randside)
        elif shape == 'pentagon':
                regular_pentagon(squirt, randx, randy, randside)
        elif shape == 'hexagon':
                regular_hexagon(squirt, randx, randy, randside)
        elif shape == 'octagon':
                regular_octagon(squirt, randx, randy, randside)
        elif shape == 'circle':
                circle(squirt, randx, randy, randside)

