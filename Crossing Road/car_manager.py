from turtle import Turtle
import random

COLORS = ["red", "green", "orange", "blue", "purple"]
STARTING_DISTANCE = 5
MOVE_INCREMENT = 5
START_X = 300
START_Y = [-200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240]


class Cars:
    def __init__(self):
        self.car_list = []
        self.create()
        self.create()
        self.speed = STARTING_DISTANCE
        self.increment = MOVE_INCREMENT

    def create(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        self.car_list.append(car)
        car.goto(START_X, random.choice(START_Y))

    def manager(self):
        if self.car_list[-1].xcor() < 280:
            self.create()
        if self.car_list[-1].ycor() == self.car_list[-2].ycor():
            self.car_list[-1].goto(START_X, random.choice(START_Y))
        for cars in self.car_list:
            if cars.xcor() < -350:
                self.car_list.remove(cars)

    def move(self):
        for car in self.car_list:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed = self.speed + self.increment
