from turtle import Turtle, Screen
import random

move = [0, 90, 180, 270]


timy = Turtle()
timy.shape("turtle")
timy.color("blue")
timy.speed(5)
timy.pensize(10)

a = 100
# Setting the colormode to use RGB values
Turtle.colormode(255)

while a:
    timy.forward(30)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    timy.color(r, g, b)
    # Set a random heading for the turtle
    timy.setheading(random.choice(move))
    a -= 1  