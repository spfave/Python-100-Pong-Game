from turtle import Turtle


# Constants
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_START_POSITION = (350, 0)
MOVE_INCREMENT = 20

# Classes


class Paddle(Turtle):
    """ docstring """

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.color("white")
        self.goto(PADDLE_START_POSITION)

    def move_up(self):
        """ Move paddle up """
        self.forward(MOVE_INCREMENT)

    def move_down(self):
        """ Move paddle down """
        self.backward(MOVE_INCREMENT)
