from turtle import *
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
abhi = Turtle()
side = 3
for i in range(8):
    random_color = random.randint(len(colours))
    abhi.color(colours[random_color])  # Set a different color for each shape
    for _ in range(side):
        angle = 360 / side
        abhi.fd(100)
        abhi.right(angle)
    side += 1

screen = Screen()
screen.exitonclick()
