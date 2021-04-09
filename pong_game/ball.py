from turtle import Turtle

SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move_speed = 0.1
        self.dir_y = SPEED
        self.dir_x = SPEED

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x + self.dir_x, new_y + self.dir_y)

    def bounce(self):
        self.dir_y *= -1

    def reflect(self):
        self.dir_x *= -1
        self.move_speed *= 0.75

    def restart(self):
        self.move_speed = 0.1
        self.dir_x *= -1
        self.goto(0, 0)
