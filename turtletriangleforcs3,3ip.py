import turtle

drawing = turtle.Turtle()
x = 0
y = 0
z = 0
a = 0

drawing.color("gray")
while x < 4:
	drawing.forward(200)	
	drawing.left(90)
	x = x + 1

drawing.penup()
drawing.left(90)
drawing.forward(100)
drawing.right(90)

drawing.pendown()
drawing.color("black")
drawing.forward(40)
drawing.shape("circle")
drawing.stamp()

drawing.forward(120)
drawing.stamp()
drawing.forward(40)

drawing.left(90)
drawing.penup()
drawing.forward(100)
drawing.pendown()
drawing.color("blue")
drawing.color("orange")
drawing.left(245)

while y < 50:
	drawing.forward(39)
	drawing.penup()
	drawing.backward(39)
	drawing.pendown()
	drawing.left(2)
	y = y + 1

drawing.left(195)
drawing.color("blue")
drawing.shape("turtle")
drawing.stamp()
drawing.left(270)
drawing.penup()
drawing.forward(200)
drawing.color("orange")
drawing.left(295)

while z < 50:
        drawing.forward(39)
        drawing.penup()
	drawing.backward(39)
        drawing.pendown()
	drawing.left(2)
        z = z + 1

drawing.left(55)
drawing.pendown()
drawing.color("blue")
drawing.shape("turtle")
drawing.stamp()
drawing.penup()
drawing.forward(200)
drawing.left(90)

drawing.forward(90)
drawing.left(270)
drawing.pendown()
drawing.color("gray")
drawing.forward(12)
drawing.penup()
drawing.backward(12)

drawing.left(90)
drawing.forward(20)
drawing.left(270)
drawing.pendown()
drawing.forward(12)

drawing.left(270)
drawing.forward(9)

