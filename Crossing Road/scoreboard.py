from turtle import Turtle

FONT = ("courier", 14, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.setup()
        self.create()

    def create(self):
        self.hideturtle()
        self.color("black")
        self.penup()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.setup()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def setup(self):
        y = -260
        x = -300
        for _ in range(15):
            y += 40
            self.penup()
            self.goto(x, y)
            for _ in range(30):
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)
        self.goto(-220, 270)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! You reached level {self.level}", False, "center", FONT)

