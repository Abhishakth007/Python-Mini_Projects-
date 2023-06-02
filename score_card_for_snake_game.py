from turtle import *


class Scorer(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(0, 315)
        self.write(f"Score = {self.score}", align="center", font=("Algerian", 15, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE = {self.score}", align="center", font=("Algerian", 15, "bold"))

    def game_over_due_to_wall(self):
        self.goto(0, 0)
        self.write(f"GAME OVER..YOU HIT A WALL", align="center", font=("Algerian", 15, "bold"))

    def game_over_due_to_tail(self):
        self.goto(0, 0)
        self.write(f"GAME OVER..YOU HIT YOUR TAIL", align="center", font=("Algerian", 15, "bold"))

    # def high_score_checker(self):
    #     self.color("blue")
    #     self.penup()
    #     self.hideturtle()
    #     self.goto(200, 315)
    #     self.write(f"High_Score = {self.high_score}", align="center", font=("Arial", 15, "normal"))
    #     if self.score > self.high_score:
    #         self.high_score += 1
    #         self.clear()
    #         self.write(f"High_Score = {self.high_score}", align="center", font=("Arial", 15, "normal"))
