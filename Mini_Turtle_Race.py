from turtle import *
import turtle
import random

game_on = False
screen = Screen()
screen.setup(width=700, height=500)
user_choice = turtle.textinput("Welcome to turtle race", "Who do you think will win the race").lower()
colors_list = ["red", 'blue', 'green', 'yellow', 'brown', 'purple']
y_coordinates = [-30, -60, 0, 30, 60, 90]
participants = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors_list[turtle_index])
    new_turtle.setpos(x=-330, y=y_coordinates[turtle_index])
    participants.append(new_turtle)
if user_choice:
    game_on = True
while game_on:
    for turtles in participants:
        random_dist = random.randint(0, 10)
        turtles.fd(random_dist)
        if turtles.xcor() >= 230:
            game_on = False
            winner = turtles.pencolor()
            if winner == user_choice:
                print(f'Hurray !! You won it . The winner is {winner}.')
            else:
                print(f"Oops !! You are to slow.The winner is {winner}.")

screen.exitonclick()
