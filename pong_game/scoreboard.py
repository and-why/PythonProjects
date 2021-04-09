from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.write_scores()

    def write_scores(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"{self.score_l}  {self.score_r}", align="center", move=False, font=("Courier", 40, "normal"))

    def update_score(self, player):
        if player == "r_paddle":
            self.score_r += 1
            self.write_scores()
        else:
            self.score_l += 1
            self.write_scores()
