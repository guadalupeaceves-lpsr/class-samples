import turtle
import random
number = 0
numbertwo = 0
shape = turtle.Turtle()
turtle.colormode(255)

while number < 4:
	redcolornumber = random.randint(1,255)
        bluecolornumber = random.randint(1,255)
        greencolornumber = random.randint(1,255)
        shape.color(redcolornumber,bluecolornumber,greencolornumber)
        shape.forward(100)
        shape.right(90)
        number = number + 1


while numbertwo < 100:
        redcolornumber = random.randint(1,255)
        bluecolornumber = random.randint(1,255)
        greencolornumber = random.randint(1,255)
        shape.color(redcolornumber,bluecolornumber,greencolornumber)
        angle = random.randint(1,1000)
        length = random.randint(1,50)
        shape.forward(length)
        shape.left(angle)
        numbertwo  =  numbertwo + 1

turtle.exitonclick()

