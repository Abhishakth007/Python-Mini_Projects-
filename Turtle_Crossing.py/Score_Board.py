from turtle import *

SPECIFICATIONS = ("Algerian", 15, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.goto(-320, 260)
        self.color('blue')

        self.hideturtle()
        self.write(f"Level ={self.current_level}", align='left', font=SPECIFICATIONS)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level ={self.current_level}", align='left', font=SPECIFICATIONS)

    def level_up(self):
        self.current_level += 1
        self.update_score()



