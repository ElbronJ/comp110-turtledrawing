"""
Module: draw_polygon

Program to draw a regular polygon based on user's input.
"""

import turtle

# create a turtle and set the pen color
duzzy = turtle.Turtle()
duzzy.pencolor("red")
#ask user the number of sides of the polygon and the length
number_sides = int(input("Please enter the amount of sides"))
length_of_each_side = int(input("Please enter the length of each side"))
#draw polygon
for i in range(number_sides):
    duzzy.forward(length_of_each_side)
    duzzy.left(360/number_sides)



# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()
