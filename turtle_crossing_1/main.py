import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

car_manager = CarManager()


# Controls
screen.onkey(player.move, "Up")
screen.listen()
count = 0



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1
    # generate cars on y and have them move left to right

    car_manager.build_car()
    car_manager.move_cars()

# turtle hits the top and level increases, turtle goes to start and cars move faster for next level
    if player.ycor() > 280:
        player.level_complete()
        scoreboard.update_level()
        car_manager.increase_speed()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            for _ in range(0, 15):
                screen.bgcolor("pink")
                time.sleep(0.05)
                screen.bgcolor("white")
                time.sleep(0.05)
            game_is_on = False


screen.exitonclick()
