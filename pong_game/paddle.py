from turtle import Turtle

SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)

    def up(self):
        print(self.xcor())
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + SPEED)

    def down(self):
        print(self.xcor())
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - SPEED)

    # def auto_move_paddle(self):
    #     global direction
    #     new_x = self.xcor()
    #     new_y = self.ycor()
    #     self.goto(new_x, new_y + direction)
    #     if self.ycor() == 250:
    #         direction = -10
    #     if self.ycor() == -240:
    #         direction = 10
