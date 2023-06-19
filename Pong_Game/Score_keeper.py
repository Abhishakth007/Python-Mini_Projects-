from turtle import *


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.hideturtle()
        self.paddle1_score = 0
        self.paddle2_score = 0
        self.score_updater()

    def score_updater(self):
        self.clear()
        self.goto(-200, 270)
        self.write(arg=f'Player_1 : {self.paddle2_score}', align='left', font=("algerian", 15, 'bold'))
        self.goto(200, 270)
        self.write(arg=f'Player_2 : {self.paddle1_score}', align='right', font=("algerian", 15, 'bold'))

    def player1_score(self):
        self.paddle1_score+=1
        self.score_updater()
        self.middle_line()

    def player2_score(self):
        self.paddle2_score+=1
        self.score_updater()
        self.middle_line()

    def middle_line(self):
        self.color('blue')
        self.penup()
        self.goto(0, -300)
        self.pensize(2)
        self.setheading(90)
        for i in range(16):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)
