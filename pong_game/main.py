from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

# Create the screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


# draw half way line
line = Turtle()
line.speed("fastest")
line.penup()
line.color("white")
line.pensize(width=4)
line.hideturtle()
line.goto(0, 260)
line.setheading(270)
for _ in range(0, 20):
    line.fd(20)
    line.pendown()
    line.fd(16)
    line.penup()

# Create use paddle and have it controlled by up and down arrows

r_paddle = Paddle((350, 0))
# Create second paddle and have it move up and down
l_paddle = Paddle((-360, 0))

# Create ball and have it move in a diagonal the direction
ball = Ball()


scoreboard = Scoreboard()

screen.listen()

# Controls

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "q")
screen.onkey(l_paddle.down, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Collision with walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce()

    # Collision with paddle
    if ball.distance(r_paddle) < 65 and 320 < ball.xcor() < 340:
        ball.reflect()
    if ball.distance(l_paddle) < 65 and -330 > ball.xcor() > -350:
        ball.reflect()

    # Detect ball in goal
    # player a wins a point
    if ball.xcor() > 390:
        scoreboard.update_score("l_paddle")
        time.sleep(1)
        ball.restart()
    elif ball.xcor() < -400:
        scoreboard.update_score("r_paddle")
        time.sleep(1)
        ball.restart()















screen.exitonclick()