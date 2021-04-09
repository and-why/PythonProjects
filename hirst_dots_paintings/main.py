# import colorgram
#
# colors = colorgram.extract("image.jpeg", 30)
#
# new_colors = []
#
# for color in colors:
#     # r = color.rgb[0]
#     # g = color.rgb[1]
#     # b = color.rgb[2]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors.append((r, g, b))

color_list = [(177, 47, 69), (25, 106, 155), (33, 135, 69), (219, 163, 92), (9, 62, 132), (207, 74, 98), (223, 84, 53),
              (103, 164, 206), (160, 89, 40), (124, 194, 174), (43, 162, 106), (229, 240, 235), (178, 159, 56),
              (5, 98, 50), (232, 204, 64), (131, 37, 48), (239, 204, 2), (54, 54, 54), (170, 208, 204), (4, 58, 116),
              (227, 231, 236), (75, 42, 50), (235, 229, 231), (188, 148, 156), (218, 178, 172), (191, 21, 20),
              (111, 115, 159), (10, 74, 38), (93, 65, 27)]

from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)

damian = Turtle()


def draw_art(dots_x, dots_y, gap, dot_size):
    """Draw art - choose a number of dots in height, a number of dots width and distance between the dots"""
    damian.hideturtle()
    damian.speed(0)
    damian.penup()
    start_y = ((dots_y * gap) / 2) * -1
    start_x = ((dots_x * gap) / 2) * -1
    damian.goto(start_x, start_y)
    y_pos = start_y
    for _ in range(dots_y):
        damian.goto(start_x, y_pos)
        for dots in range(dots_x):
            color = random.choice(color_list)
            damian.dot(dot_size, color)
            damian.fd(gap)
        y_pos += gap

draw_art(10, 10, 50, 20)



screen.exitonclick()