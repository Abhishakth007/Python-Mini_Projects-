from turtle import *
import random
import time
from snake import Snake
from food_generator import *
from score_card_for_snake_game import *

screen = Screen()
screen.listen()
screen.setup(width=900, height=700)
screen.tracer(0)
screen.bgcolor('black')
screen.title("Snake Game")
snake_bro = Snake()
food = Food()
snake_bro.create_snake()
scorer = Scorer()
screen.onkey(key="Up", fun=snake_bro.move_up)
screen.onkey(key="Down", fun=snake_bro.move_down)
screen.onkey(key="Left", fun=snake_bro.move_left)
screen.onkey(key="Right", fun=snake_bro.move_right)
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake_bro.make_snake_move()
    if snake_bro.collision_detector():
        scorer.game_over_due_to_wall()
        game_on = False
    if snake_bro.collision_with_tail():
        scorer.game_over_due_to_tail()
        game_on = False
    if snake_bro.head.distance(food) <= 15:
        snake_bro.new_turtle_block()
        food.new_food()
        scorer.increase_score()

screen.exitonclick()
