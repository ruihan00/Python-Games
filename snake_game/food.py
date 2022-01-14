from turtle import Turtle
import random


def random_color():
    return random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color(random_color())
        self.speed("fastest")
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.color(random_color())
        self.goto(random_x, random_y)
