# shapeDrawer.py
# draws user-input shapes in random places on the screen
# with random sizes and colors

# bring in the packages of functions we need
import random
import turtle

# -------- functions start here ----------------
# this allows me to get the colors from a different webiste through
# different numbers, and allows me to change the color of a shape
turtle.colormode(255)

# every time that you type something in place of
# regular_triangle(myTurtle, x, y, side):
# instead of those variables going through the other code
# below it, the variables that you typed in place will go for them
# say that you write it like this: regular_triangle(you, we, I, no).
# nothing can replace reular_triangle for this to work, and will start the
# process of the whole code block below this
# you will go instead of myTurtle, we instead of x, I instead of y, and
# no instead of side.
def regular_triangle(myTurtle, x, y, side):
# this is setting recolornumber equal to random.randint(1,255), which means
# that redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
        redcolornumber = random.randint(1,255)
        greencolornumber = random.randint(1,255)
        bluecolornumber = random.randint(1,255)
# This is saying that the function, myTurtle(or in this case,
# whatever name the user decides the function to be), and 
# in the program pace, the "pen" will go up, which means
# that it will not draw anything on the page, but it will move.
        myTurtle.penup()
# here, instead of myTurtle, it would be you going through this, etc.
# This is saying that the color that will be put on the page will be
# the value of the variable redcolornumber, greencolornumber, and
# the number assigned to the variable bluecolornumber.
# This means that the first integer is for the red color quantity,
# the second integer for the green, and the third number
# for the blue. In a website online, you get to choose a 
# number depending on the amount of green, red, and blue.
# Or, you can say that any three number sequence is tied
# to a specific color.
        myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# The "pen" wll go to the value of the variable x, and the value of
# the variable y. X is horizontal, and y is vertical.
        myTurtle.goto(x,y)
# The "pen" will get down, which means that it will start 
# leaving visible colors on the myTurtle page. 
        myTurtle.pendown()
# This is setting side_count to the variable 0.
        side_count = 0
# This is saying that uuntil the value of the variable
# side_count is less than 3, it will continue to
# go through the block of code tied to it.
        while side_count < 3:
# This is setting recolornumber equal to random.randint(1,255), which means 
# that redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
                redcolornumber = random.randint(1,255)
                greencolornumber = random.randint(1,255)
                bluecolornumber = random.randint(1,255)
# here, instead of myTurtle, it would be you going through this, etc.
# This is saying that the color that will be put on the page will be
# the value of the variable redcolornumber, greencolornumber, and
# the number assigned to the variable bluecolornumber.
# This means that the first integer is for the red color quantity,
# the second integer for the green, and the third number
# for the blue. In a website online, you get to choose a 
# number depending on the amount of green, red, and blue.
# Or, you can say that any three number sequence is tied
# to a specific color.
                myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# This is saying that myTurtle will go forward by the value of the 
# variable side, which would be inputed later by the user.
                myTurtle.forward(side)
# This is saying that the angle in which myTurtle will go
# to the right would be 120.
                myTurtle.right(120)
# This will assign side_count to the value of the
# variable side_count plus 1.
                side_count = side_count + 1

# This is saying that every time that you set three variables in the format,
# regular_square(myTurtle, x, y, side)(the noes inside the parenthesis),
#  it will replace the variables here
# below with your own, and in the block of code that is set to it. 
# So, it's like you are removing those variables with your own.
def regular_square(myTurtle, x, y, side):
# Instead of myTurtle, it will be whatever name that the
# user set to the function, 'turtle.Turtle()', and that function, or pen,
# will go up. This means that you will not be able to see any color on
#  the home page when you run this whole code.
        myTurtle.penup()
# This is setting recolornumber equal to random.randint(1,255), which means that
# redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
        redcolornumber = random.randint(1,255)
        greencolornumber = random.randint(1,255)
        bluecolornumber = random.randint(1,255)
# This is saying that the color of the 'pen' would be the value of
# the variable redcolornumber, greencolornumber, and bluecolornumber.
# In an internet website, these thre numbers would equal to a
# specific color, so that specific color will
# show up on the home page when you run this whole code instead.
        myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# This is saying that 'myTurtle' will go to the coordinates x and y,
# or the values of the variable x and y.
        myTurtle.goto(x,y)
# This is saying that if you move the "pen" around, you woould be able
# to see where it actually moved. Or, you would be able to see color.
        myTurtle.pendown()
# This is assigning side_count_2 to 0, making it an integer variable.
        side_count2 = 0
# This is saying that until the value of the variable side_count is less 
# than 4,it will continue to go thrugh the code tied to this while statement.
        while side_count2 < 4:
# this is setting recolornumber equal to random.randint(1,255), which means 
# that redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
                redcolornumber = random.randint(1,255)
                greencolornumber = random.randint(1,255)
                bluecolornumber = random.randint(1,255)
# This is saying that the color of myTurtle will turn to the
# value of the variables redcolornumber, greencolornumber, and
# bluecolornumber, which would be a specific color in a website online. All
# of the values would be numbers.
                myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# This would say that 'myTurtle' would go forward to whatever
# was set to the value of the variable side.
                myTurtle.forward(side)
# This is saying that 'myTurtle' would go left about an angle of 90 degrees.
# Or, at least where it would be pointing to would change to that direction.
                myTurtle.left(90)
# This is assigning side_count2 to the value of the
# variable side_count2 plus 1. Every time this while statement
# runs, the value of the variable side_count2 increases. Tehrefore, the amount
# of times that this loop runs is not infinite.
                side_count2 = side_count2 + 1

# The variable regular_pentagon, when in front of four variables in a parenthesis,
# will allow those variables to replace those below this comment in the 
# parenthesis accordingly. Those other variables will go in place of
# myTurtle, x, y, and side through this whole block of code tied to 
# the def statement, which means that the whole code is tied to
# regular_pentagon.
def regular_pentagon(myTurtle, x, y, side):
# This is saying that the function, myTurtle(or in this case,
# whatever name the user decides the function to be), and 
# in the program pace, the "pen" will go up, which means
# that it will not draw anything on the page, but it will move.
        myTurtle.penup()
# this is setting recolornumber equal to random.randint(1,255), which means that
# redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
        redcolornumber = random.randint(1,255)
        greencolornumber = random.randint(1,255)
        bluecolornumber = random.randint(1,255)
# This is saying that the color of myTurtle will turn to the
# value of the variables redcolornumber, greencolornumber, and
# bluecolornumber, which would be a specific color in a website online. All
# of the values would be numbers.
        myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# In the turtle home page, the shape that shows where you are located at and
# in which diretion you are pointing in will go to the coordinates x and y, which
# means that it will go to the value of the variable x as the x-coordinate,
# and the value of  the variable y as the y-coordinate.
        myTurtle.goto(x,y)
# This is saying that the shape that indicates as to where you are located and
# the direction where you are pointiong towards will be visible, and
# if you make it go forwards, and it is set to a visible color, that 
# color will be visible, and will leave a trail towards wherever the
# shape was set to go to.
        myTurtle.pendown()
# This will assign side_count3 to 0, making it an integer variable.
        side_count3 = 0
# This is saying that unless side_count3 < 5 is not a True statement, the
# code set to the while statement( or underneath it) will keep on going.
# The loop would continue.
        while side_count3 < 5:
# this is setting recolornumber equal to random.randint(1,255), which means 
# that redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
                redcolornumber = random.randint(1,255)
                greencolornumber = random.randint(1,255)
                bluecolornumber = random.randint(1,255)
# This is saying that the color of myTurtle will turn to the
# value of the variables redcolornumber, greencolornumber, and
# bluecolornumber, which would be a specific color in a website online. All
# of the values would be numbers.
                myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# This is saying that 'myTurtle' will go forward- depending on the direction 
# the shape points towards- by the value of the variable side.
                myTurtle.forward(side)
# This is saying that 'myTurtle' will go to the left by the angle 72.
                myTurtle.left(72)
# This is saying that the value of the variable side_count3 will
# change to the previous value of the variable side_coount3 plus 1.
                side_count3 = side_count3 + 1

# This is saying that if you have four variables in parenthesis, and regular_hexagon
# is in front of it, you are able to go through the whole block of code tied
# to the def statement. Those four variables will replace myTurtle, x, y, side
# accordingly, or inchronological order.
def regular_hexagon(myTurtle, x, y, side):
# This is saying that the function, myTurtle(or in this case,
# whatever name the user decides the function to be), and 
# in the program pace, the "pen" will go up, which means
# that it will not draw anything on the page, but it will move.
        myTurtle.penup()
# this is setting recolornumber equal to random.randint(1,255), which means that
# redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
        redcolornumber = random.randint(1,255)
        greencolornumber = random.randint(1,255)
        bluecolornumber = random.randint(1,255)
# This is saying that the color of myTurtle will turn to the
# value of the variables redcolornumber, greencolornumber, and
# bluecolornumber, which would be a specific color in a website online. All
# of the values would be numbers.
        myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# This is saying that the 'shape' of your most current location will go
# to the coordinates x and y, or in this case, the value of the variable x
# as the x-coordinate, and the value of the variable y as the
# y-coordinate.
        myTurtle.goto(x,y)
# This is allowing everything to be visible now.
        myTurtle.pendown()
# This is assigning side_count4 to 0.
        side_count4 = 0
# This is saying that until the value of the variable side_count4 is equal to 6,
# the whole lock of code tied to this while statement will run.
        while side_count4 < 6:
# this is setting redcolornumber equal to random.randint(1,255), which means that
# redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time the whole code runs(not only this), the values of these integer variables
# will not be the same.
                redcolornumber = random.randint(1,255)
                greencolornumber = random.randint(1,255)
                bluecolornumber = random.randint(1,255)
# this is saying that the variable, myTurtle, will change color. It will change color
# depending of the numbers assigned to the variables in the parenthesis. The first
# variable represents red, the second green, and the third blue. In a website online,
# these three numbers would represent a specific color, and on the turtle webpage, that
# specific clor would show up if the shape of the current location moved.
                myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# This is sayiing that the shape of myTurtle will go forward depending
# on the number assigned to the integer variable called side.
                myTurtle.forward(side)
# Thsi is saying that, depending on the direction that the shape is pointing to, 
# it will go to the left of about an angle of 60 degrees.
                myTurtle.left(60)
# This is assigning side_count4 to the value of the variable, side_count4's past value plus 1.
                side_count4 = side_count4 + 1

def regular_octagon(myTurtle, x, y, side):
# This is saying that the function, myTurtle(or in this case,
# whatever name the user decides the function to be), and 
# in the program pace, the "pen" will go up, which means
# that it will not draw anything on the page, but it will move.
        myTurtle.penup()
# this is setting recolornumber equal to random.randint(1,255), which means that
# redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
        redcolornumber = random.randint(1,255)
        greencolornumber = random.randint(1,255)
        bluecolornumber = random.randint(1,255)
# This is saying that the color of myTurtle will turn to the
# value of the variables redcolornumber, greencolornumber, and
# bluecolornumber, which would be a specific color in a website online. All
# of the values would be numbers.
        myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
        myTurtle.goto(x,y)
        myTurtle.pendown()
# This is assigning side_count5 to 0.
	side_count5 = 0
# This is saying that until the value of the variable side_count5 is not more or equal to 8, 
# the loop will not terminate.
	while side_count5 < 8:
# this is setting recolornumber equal to random.randint(1,255), which means that
# redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
		redcolornumber = random.randint(1,255)
		greencolornumber = random.randint(1,255)
		bluecolornumber = random.randint(1,255)
# This is saying that the color of myTurtle will turn to the
# value of the variables redcolornumber, greencolornumber, and
# bluecolornumber, which would be a specific color in a website online. All
# of the values would be numbers.
        	myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# This is saying that 'myTurtle' will go forward by the value of the variable side.
        	myTurtle.forward(side)
# This is saying that 'myTurtle' will go to the left by the angle 45.
        	myTurtle.left(45)
# This is assigning side_count5 to the previous value of the variable side_count5 plus 1.
        	side_count5 = side_count5 + 1

# This is saying that every time that you type circle in front of four variable in a parenthesis,
# those four variables will go through the code assigned to circle, and below the def statement.
def circle(myTurtle, x, y, radius):
# This is saying that the shape that indicates where you are located currently will disappear, and
# it will not leave any trace if it moves around. So, it will not be visible on the screen.
        myTurtle.penup()
# this is setting recolornumber equal to random.randint(1,255), which means that
# redcolornumber will be equal to a number in between 1 and 255.
# the same applies for greencolornumber, and bluecolornumber.
# Every time this whole code runs, the values of these integer variables
# will not be the same.
        redcolornumber = random.randint(1,255)
        greencolornumber = random.randint(1,255)
        bluecolornumber = random.randint(1,255)
# This is saying that myTurtle will change to the color on
# a website online, whose color number set is the same as
# the value of the variable redcolornumber, the value of the variable
# greencolornumber, and the value of the variable bluecolornumber,
# all in that order.
        myTurtle.color(redcolornumber,greencolornumber,bluecolornumber)
# This is saying that if the whole turtle screen was a graph,
# 'myTurtle' would go to the value of the variable x as its
# x-coordinate, and to the value of the variable y, as its 
# y-coordinate.
        myTurtle.goto(x,y)
# This is saying that 'myTurtle''s pen will go down, whic means that if
# there is a shape as the indicator as to where you are at, and where
# you are pointing towards to, you could see whatever it does. As in,
# the color would be visible.
        myTurtle.pendown()
# This is saying that 'myTurtle' would create a variable with
# a radius of the value of the variables radius.
        myTurtle.circle(radius) 

# This is saying that every time someone types in splat right in front of four variables
# in parenthesis, that the rest of the code tied to def will run for those variables.
# So, if you replace x with yeah, the variable yeah will go in place
# of the variable x.
def splat(myTurtle, x, y, side):
# This will assign asterisk to 0.
	asterisk = 0
# This is saying that the function assigned to turtle will not
# leave anything visible anymore if you make the shape change location.
	myTurtle.penup()
# This is saying that you will move to the value of the variable x as the
# x-coordinate, and the value of the variable y as
# the y-coordinate.
	myTurtle.goto(x,y)
# This is saying that untl the value of the vriable asterisk goes over 6,
# the rest of the code tied to the while statement will keep on running.
	while asterisk < 6:
# This will assign redcolornumber to a number from 1-255. The same
# goes for greencolornumber, and bluecolornumber.
		redcolornumber = random.randint(1,255)
		greencolornumber = random.randint(1,255)
		bluecolornumber = random.randint(1,255)
# This is saying that the variable ted to the turtle function's shape will now be
# visible, and if you make it go forward, the color of the shape will leave an imprint
# of the direction that it went through.
		myTurtle.pendown()
# This is saying that the color of the shape and the color that it will leave behind
# on the home page will be determined by the values of the variables 
# redcolornumber, greencolornumber, and bluecolornumber. In a 
# website online, those three numbers are assigned to a specifi color.
# The value of the variable redcolornumber determines how much red the color will have,
# and the same goe for greencolronumber(green) and bluecolornumber(blue).
# Those three numbers, when together in the red, green, blue sequence, determine
# how much of that pigment it will have, and makes a color.
		myTurtle.color(redcolornumber, greencolornumber, bluecolornumber)
# This is saying that the shape that determines where you are currently located at will
# go forwards by the value of the variable side, and that if it is set to
# a specific color, that color will show where the shape has moved through, or which
# path it has taken to to get to where it is.
		myTurtle.forward(side)
# This is saying that the shape showing where you are currently on the page will go, to
# the left, 60 degrees.
		myTurtle.left(60)
# This is saying that the shape will disappear, and if you ask the function to make a
#line, it will not be able to do a visible one.
		myTurtle.penup()
# This is saying that the shape that shows where your current location in
# the home page will go backwards to the value of the variable side.
		myTurtle.backward(side)
# This is assigning asterisk to the value of its previous self plus one.
		asterisk = asterisk + 1

# This is saying that whenever smiley is in front of four variables in parenthesis, the
#
def smiley(myTurtle, x, y, side):
# This is saying that the shape will not be visible, and it will go
# (even though you will not be able to see) to the value of the
# variable x as the x-coordinate, and to the value of the variable y as the y-coordinate.
	myTurtle.penup()
	myTurtle.goto(x,y)
# This is saying that the shape will now be set to a specific color. That 
# specific color will be determined by the values of the variables redcolornumber, 
# greencolornumber, and bluecolornumber. Online, there is a website that
#  determines what color is set to those numbers
	myTurtle.color(redcolornumber, greencolornumber, bluecolornumber)
	redcolornumber = random.randint(1,255)
	greencolornumber = random.randint(1,255)
	bluecolornumber = random.randint(1,255)
	numberoflength = 0
	while numberoflength < 2:
		myTurtle.pendown()
        	redcolornumber = random.randint(1,255)
        	greencolornumber = random.randint(1,255)
        	bluecolornumber = random.randint(1,255)
		myTurtle.forward(side)
		myTurtle.penup()
	while numberoflength > 0 :
		myTurtle.pendown()
		myTurtle.color(redcolornumber, greencolornumber, bluecolornumber)
		myTurtle.goto(x, y)
		

# -------- execution starts here ----------------
 
print("Welcome to the random shape drawer!")
print("You choose the shapes, and we choose the position, color, and size.")
 
squirt = turtle.Turtle()
 
shape = ""
while shape != "exit":
        print("Enter a shape - your choices are triangle, square, pentagon, hexagon, octagon, circle, asterisk, and a smiley face.")
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
	elif shape == 'asterisk':
		splat(squirt, randx, randy, randside)
	elif shape == 'smiley face':
		smiley(squirt, randx, randy, randside)
