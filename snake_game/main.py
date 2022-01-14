import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.colormode(255)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def start_game():

    scoreboard.clear()

    scoreboard.refresh()
    end_game = False
    while not end_game:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 18:
            food.refresh()
            scoreboard.score += 1
            scoreboard.refresh()
            snake.extend()

        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            end_game = True
            scoreboard.gameover()
            snake.clear()
            scoreboard.clear()
            food.clear()

        for segment in snake.all_segment[1:-1]:
            if snake.head.distance(segment) < 10:
                end_game = True
                scoreboard.gameover()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(start_game, "f")
screen.exitonclick()
