from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)