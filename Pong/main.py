from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(900, 600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

player1 = Paddle(1)
player2 = Paddle(2)
screen.update()

scoreboard1 = Scoreboard(1)
scoreboard2 = Scoreboard(2)

end_game = False

def start_round():
    ball = Ball()
    screen.onkey(fun=player1.move_up, key="w")
    screen.onkey(fun=player1.move_down, key="s")
    screen.onkey(fun=player2.move_up, key="Up")
    screen.onkey(fun=player2.move_down, key="Down")

    round_continue = True
    while round_continue:
        screen.update()
        time.sleep(0.01)
        print(ball.heading())
        if ball.ycor() > 285 or ball.ycor() < -285:
            ball.wall_bounce()

        ball.move()
        if ball.xcor() > 390 or ball.xcor() < -390:
            if player1.distance(ball) < 60:
                ball.paddle_bounce()
            elif player2.distance(ball) < 60:
                ball.paddle_bounce()

        if ball.xcor() > 440:
            scoreboard1.increase_score()
            round_continue = False
            ball.reset()

        elif ball.xcor() < -440:
            scoreboard2.increase_score()
            round_continue = False
            ball.reset()

while not end_game:
    if scoreboard1.score >= 10 or scoreboard2.score >= 10:
        end_game = True
    else:
        start_round()

if scoreboard1.score >= 10:
    winner = "Player 1"
    scoreboard1.game_over(winner)

elif scoreboard2.score >= 10:
    winner = "Player 2"
    scoreboard2.game_over(winner)


screen.exitonclick()
