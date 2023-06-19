from turtle import *


class PaddleTwo(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('blue')
        self.goto(x=-370, y=0)

    def move_up(self):
        new_y = self.ycor()+20
        self.goto(x=-370,y=new_y)

    def move_down(self):
        new_y = self.ycor()-20
        self.goto(x=-370,y=new_y)



