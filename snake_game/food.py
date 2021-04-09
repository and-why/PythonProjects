from turtle import Turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random_color())
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = 2 * (random.randint(-28, 28)//2)
        random_y = 2 * (random.randint(-28, 28)//2)
        self.color(random_color())
        self.goto(random_x * 10, random_y * 10)