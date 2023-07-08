from turtle import *
SPECIFICATIONS = ("Algerian", 25, "bold")


class Movement(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.shapesize(stretch_len=1.25, stretch_wid=1.25)
        self.setheading(90)
        self.penup()
        self.goto(0, -250)

    def move_turtle(self):
        self.forward(10)

    def move_back(self):
        self.backward(10)

    def goto_start(self):
        self.goto(0,-250)

    def winning_line(self):
        if self.ycor() >= 250:
            return True
        else:
            return False

    def end_game(self):
        self.goto(0,0)
        self.color('red')
        self.write(f"GAME_OVER", align='center', font=SPECIFICATIONS)



