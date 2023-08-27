import turtle
import colorgram
from turtle import Turtle, Screen
import random

turtle.colormode(255)
"""
colors=colorgram.extract('colorart.jpg',20)
print(colors)
for i in range(len(colors)):
    colors[i]=(colors[i].rgb.r,colors[i].rgb.g,colors[i].rgb.b)
colors.pop(0)
colors.pop(0)
def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


color_list = [generate_random_color() for _ in range(30)]"""
color = [(184, 90, 3), (226, 237, 231), (216, 64, 81), (45, 108, 152), (248, 244, 246), (67, 127, 63), (234, 217, 105),
         (169, 187, 5), (58, 52, 45), (2, 29, 83), (155, 7, 126), (173, 190, 215), (151, 199, 194), (203, 160, 164),
         (200, 162, 144), (68, 162, 5), (147, 174, 190), (157, 203, 197)]

number_of_dots=100
my_turtle = Turtle()
my_turtle.penup()
my_turtle.speed(0)
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
for dot_count in range(1,number_of_dots+1):
    my_turtle.dot(20, random.choice(color))
    my_turtle.forward(50)
    if dot_count%10==0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)
screen = Screen()
screen.exitonclick()
