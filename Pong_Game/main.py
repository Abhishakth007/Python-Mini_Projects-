from turtle import *
from Paddle1 import *
from Paddle2 import *
from Pong_Ball import *
from Score_keeper import *
import time

screen = Screen()
screen.listen()
screen.tracer(0)
score_board = ScoreBoard()
score_board.middle_line()
screen.update()
screen.bgcolor('black')
screen.tracer(0)
paddle1 = PaddleOne()
paddle2 = PaddleTwo()
ball = Ball()

screen.onkey(key="Up", fun=paddle1.move_up)
screen.onkey(key="Down", fun=paddle1.move_down)
screen.onkey(key="w", fun=paddle2.move_up)
screen.onkey(key="s", fun=paddle2.move_down)

screen.setup(height=600, width=800)
screen.title("Pong")
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_movement_toward_paddle1()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_back()

    if ball.xcor() >= 380:
        ball.reset_ball()
        score_board.player2_score()

    if ball.xcor() <= -380:
        ball.reset_ball()
        score_board.player1_score()
    if ball.distance(paddle1) < 50 and ball.xcor() > 340:
        ball.paddle_bounce()

    if paddle2.distance(ball) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()

screen.exitonclick()
