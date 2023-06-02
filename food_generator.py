from turtle import *
import random




class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(0.7)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        x_coordinates_for_food = random.randint(-280, 280)
        y_coordinates_for_food = random.randint(-280, 280)
        self.goto(x_coordinates_for_food, y_coordinates_for_food)
        self.speed("fastest")



