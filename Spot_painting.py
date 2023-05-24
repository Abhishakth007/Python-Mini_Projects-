# import colorgram
# list_of_rgb_tuples = []
# colors = colorgram.extract('image.jpg',40)
# for i in colors:
#     red = i.rgb.r
#     green = i.rgb.g
#     blue = i.rgb.b
#     rbg_tuple = (red,green,blue)
#     list_of_rgb_tuples.append(rbg_tuple)
#     print(list_of_rgb_tuples)

from turtle import *
import turtle
import random
import turtle

colors_list = [(254, 253, 250), (235, 246, 250), (251, 241, 246), (245, 252, 249), (243, 235, 74), (211, 158, 93),
               (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31), (219, 129, 166), (161, 79, 35),
               (129, 185, 146), (9, 32, 76), (222, 62, 105), (235, 73, 42), (180, 45, 94), (30, 136, 81),
               (236, 164, 193), (78, 12, 63), (12, 54, 33), (234, 227, 7), (26, 165, 209), (16, 43, 132), (58, 166, 96),
               (134, 214, 229), (10, 101, 63), (133, 34, 20), (91, 27, 11), (159, 211, 188), (7, 90, 104), (252, 5, 63),
               (233, 172, 161), (105, 88, 9), (72, 129, 193), (178, 187, 217)]
screen = Screen()
turtle.colormode(255)
abhi = Turtle()
turtle.setworldcoordinates(1, 1, 225, 225)
abhi.speed(100)


def reallocation_of_position():
    abhi.left(90)
    abhi.fd(15)
    abhi.left(90)
    abhi.fd(225)
    abhi.right(180)


for j in range(15):
    for i in range(15):
        random_tuple = random.choice(colors_list)
        abhi.dot(21, random_tuple)
        abhi.penup()
        abhi.fd(15)
    reallocation_of_position()

screen.exitonclick()
