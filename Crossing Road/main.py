from turtle import Screen
import time
from player import Player
from car_manager import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
car = Cars()

player = Player()

screen.onkeypress(fun=player.move, key="Up")


def start_level():
    level_end = False

    while not level_end:
        car.move()
        car.manager()
        time.sleep(0.05)
        screen.update()
        for _ in car.car_list:
            if player.distance(_) < 20:
                return False
        if player.ycor() > 280:
            car.increase_speed()
            scoreboard.increase_level()
            player.refresh()
            return True



game_end = False

while not game_end:
    if not start_level():
        game_end = True

scoreboard.game_over()

screen.exitonclick()
