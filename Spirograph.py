from turtle import *
import turtle
import random
abhi = Turtle()
abhi.pensize(4)
angle_of_tilt = 30
abhi.speed(50)

turtle.colormode(255)



def color_selector():
    random_intensity1 = random.randint(0, 255)
    random_intensity2 = random.randint(0, 255)
    random_intensity3 = random.randint(0, 255)
    abhi.pencolor((random_intensity1, random_intensity2, random_intensity3))


for i in range(100):
    abhi.setheading(angle_of_tilt)
    color_selector()
    abhi.circle(100)
    angle_of_tilt+=10




screen = Screen()
screen.exitonclick()
