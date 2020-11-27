from turtle import Turtle


# Constants
MOVE_INCREMENT = 20


# Classes
class Ball(Turtle):
    """ Game ball """

    def __init__(self, initial_heading):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(initial_heading)

    def move(self):
        self.forward(MOVE_INCREMENT)
