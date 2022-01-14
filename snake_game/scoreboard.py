from turtle import Turtle

FONT = ("courier", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.goto(0, 275)
        self.write(f"Score: {self.score}", False, "center", FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over.", False, "center", FONT)
