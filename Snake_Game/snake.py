from turtle import *
import random
import time

CURRENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for positions in CURRENT_POSITIONS:
            segment = Turtle()
            segment.penup()

            segment.shape('square')
            segment.color('blue')
            segment.goto(positions)
            segment.showturtle()
            self.all_segments.append(segment)

    def make_snake_move(self):
        for index in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[index - 1].xcor()
            new_y = self.all_segments[index - 1].ycor()
            self.all_segments[index].goto(new_x, new_y)

        self.head.forward(10)

    def move_up(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            pass

        else:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            pass
        else:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() == 180 or self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() == 180 or self.head.heading() == 0:
            pass
        else:
            self.head.setheading(0)

    def collision_detector(self):
        if self.head.xcor() <= -435 or self.head.xcor() >= 435:
            return True
        elif self.head.ycor() >= 335 or self.head.ycor() <= -335:
            return True

    def new_turtle_block(self, ):
        abhi = Turtle()
        abhi.penup()
        abhi.shape('square')
        abhi.color('blue')
        abhi.goto(self.all_segments[len(self.all_segments) - 1].xcor(),
                  self.all_segments[len(self.all_segments) - 1].ycor())
        self.all_segments.append(abhi)

    def collision_with_tail(self):
        for seg in self.all_segments:
            if seg == self.head:
                pass
            elif self.head.distance(seg) < 0.5:
                return True
