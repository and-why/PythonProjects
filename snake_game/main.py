from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()

screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.colormode(255)
screen.title("Snake Game")
screen.tracer(0)
segments = []


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(snake.head_up, "Up")
screen.onkey(snake.head_right, "Right")
screen.onkey(snake.head_left, "Left")
screen.onkey(snake.head_down, "Down")


def end_game():
    snake.stop()
    scoreboard.game_over()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            end_game()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or\
            snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        end_game()























screen.exitonclick()