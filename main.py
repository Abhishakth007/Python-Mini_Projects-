import random
from turtle import *
from Turtle_Movement import *
from Obstacles import *
import time
from random import *
from random import *
from Score_Board import *

screen = Screen()
screen.bgcolor('white')
screen.setup(width=700, height=600)
screen.tracer(0)
movement = Movement()

screen.listen()
screen.onkey(key='Up', fun=movement.move_turtle)
screen.onkey(key='Down', fun=movement.move_back)
cars = Cars()
score = Score()
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.obstacle()
    cars.movement_of_obstacles()
    for i in cars.all_obstacles:
        if i.distance(movement) < 27:
            game_on = False
            movement.end_game()

    if movement.winning_line():
        movement.goto_start()
        cars.increase_speed()
        score.level_up()

screen.exitonclick()
