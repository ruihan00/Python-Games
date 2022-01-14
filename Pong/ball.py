from turtle import Turtle
import random

start_heading = [20, 30, 40, 50, 60, 70, 110, 130, 150, 170, 190, 210, 230, 250, 290, 310, 330]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.choice(start_heading))

    def move(self):
        self.forward(10)

    def wall_bounce(self):
        current_heading = self.heading()
        new_heading = 360 - current_heading
        self.setheading(new_heading)

    def paddle_bounce(self):
        current_heading = self.heading()
        new_heading = - 180 - current_heading
        self.setheading(new_heading)
        self.forward(20)
