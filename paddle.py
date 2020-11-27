from turtle import Turtle


# Constants
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
MOVE_INCREMENT = 20


# Classes
class Paddle(Turtle):
    """ Pong game paddle """

    def __init__(self, start_coords):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)  # starting size = 20, 20
        self.color("white")
        self.goto(start_coords)

    def move_up(self):
        """ Move paddle up """
        self.sety(self.ycor()+MOVE_INCREMENT)

    def move_down(self):
        """ Move paddle down """
        self.sety(self.ycor()-MOVE_INCREMENT)
