import turtle
from Tkinter import *
import random

# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()
def regular_triangle(myTurtle):
	numberoftimesloop = 3
	randside = random.randint(15, 50)
	while numberoftimesloop > 0:
		myTurtle.pendown()
		myTurtle.forward(randside)
		myTurtle.left(120)	

# make some simple buttons

fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
penup = Button(frame, text='penup', command=lambda: shawn.penup())
pendown = Button(frame, text='pendown', command=lambda: shawn.pendown())
exitonclick = Button(frame, text="exit", command=quit)
regtriangle = Button(frame, text='triangle', command=lambda: regular_triangle(shawn))

# put it all together
regtriangle.pack(side=RIGHT)
exitonclick.pack(side=RIGHT)
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
turtle.exitonclick()
