from turtle import Turtle

FONT = ("courier", 14, "normal")
starting_position = [(-60, 270), (60, 270)]


def setup():
    score = Turtle()
    score.setheading(270)
    score.color("white")
    score.penup()
    score.goto(0, 300)
    score.hideturtle()
    for times in range(60):
        score.pendown()
        score.forward(5)
        score.penup()
        score.forward(5)


class Scoreboard(Turtle):
    def __init__(self, num):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.create(num)
        setup()

    def create(self, num):
        self.goto(starting_position[num - 1])
        self.write(f"Score: {self.score}", False, "center", FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", FONT)

    def game_over(self, winner):
        self.goto(0, -10)
        self.write(f"{winner} Wins!", False, "center", FONT)
