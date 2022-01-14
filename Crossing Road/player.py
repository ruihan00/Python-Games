from turtle import Turtle

MOVE_DISTANCE = 15
STARTING_POS = (0, -250)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POS)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POS)
