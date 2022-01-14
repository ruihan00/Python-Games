from turtle import Turtle

PADDLE_POSITIONS = [(-400, 0), (400, 0)]


class Paddle(Turtle):
    def __init__(self, num):
        super().__init__()
        self.create(num)

    def create(self, num):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.goto(PADDLE_POSITIONS[num - 1])
        self.speed("fastest")

    def move_up(self):
        if self.ycor() < 220:
            self.forward(50)
        else:
            pass

    def move_down(self):
        if self.ycor() > -220:
            self.back(50)
        else:
            pass

