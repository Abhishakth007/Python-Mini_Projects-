import random
import turtle
from turtle import *

COLORS = ['red', 'orange', 'black', 'purple', 'yellow','green','blue','pink','brown']
MOVE_INCREMENT = 5



class Cars:
    def __init__(self):
        self.all_obstacles = []
        self.obstacle_speed = 5

    def obstacle(self):
        obstacle_creating_chance = random.randint(0, 6)
        if obstacle_creating_chance == 5:
            abhi = Turtle()
            abhi.penup()
            abhi.color(random.choice(COLORS))
            abhi.shape('square')
            abhi.shapesize(stretch_wid=1, stretch_len=2)
            y = random.randint(-200, 200)
            abhi.goto(350, y)
            self.all_obstacles.append(abhi)

    def movement_of_obstacles(self):
        for i in range(len(self.all_obstacles)):
            self.all_obstacles[i].backward(self.obstacle_speed)

    def increase_speed(self):
        self.obstacle_speed+=2


