"""
Module: draw_pentagon

Program to draw a pentagon using turtles.
"""

import turtle

# create a turtle, have user input turtle color and size
sat = turtle.Turtle()
color_input = input('Please choose a color for the turtle')
turtle_size = int(input("Please indicate how far the turtle should go")) 
sat.color(color_input)
#draw the pentagon
for i in range(5):
    sat.forward(turtle_size)
    sat.left(72)
    
# draw the pentagon
# sat.forward(50)
# sat.left(72)
# sat.forward(50)
# sat.left(72)
# sat.forward(50)
# sat.left(72)
# sat.forward(50)
# sat.left(72)
# sat.forward(50)
# sat.left(72)

# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()