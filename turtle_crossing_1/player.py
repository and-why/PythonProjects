from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 5
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(0, -280)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def level_complete(self):
        self.goto(0, -280)
