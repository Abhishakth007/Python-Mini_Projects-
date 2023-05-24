from turtle import *
import random
import turtle

turtle.colormode(255)
abhi = Turtle()
directions = [0, 90, 180, 270]
abhi.speed(50)
abhi.pensize(8)


def random_direction(choice):
    abhi.setheading(choice)
    abhi.fd(35)


def color_selector():
    random_intensity1 = random.randint(0, 255)
    random_intensity2 = random.randint(0, 255)
    random_intensity3 = random.randint(0, 255)
    abhi.pencolor((random_intensity1, random_intensity2, random_intensity3))


for i in range(500):
    direction_choice = random.choice(directions)
    random_direction(direction_choice)
    color_selector()

screen = Screen()
screen.exitonclick()
