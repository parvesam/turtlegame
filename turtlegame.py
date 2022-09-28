import turtle           # allows us to use the turtles library
turtle.speed(1)
wn = turtle.Screen()           # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
#alex.forward(150)            # tell alex to move forward by 150 units
alex.right(45)               # turn by 90 degrees
alex.forward(100)           # complete the second side of a rectangle
alex.left(90)
alex.forward(100)
alex.left(45)
alex.forward(70)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(70)
wn.exitonclick()
