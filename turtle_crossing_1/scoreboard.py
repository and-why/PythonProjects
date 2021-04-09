from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-290, 270)
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)
