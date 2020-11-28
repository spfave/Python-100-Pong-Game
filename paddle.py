from turtle import Turtle
from game_parameters import limit_paddle_position


# Constants
MOVE_INCREMENT = 20


# Classes
class Paddle(Turtle):
    """ Pong game paddle """

    def __init__(self, start_coords):
        super().__init__()
        self.penup()
        self.shape("square")
        # Stretch starting size = 20, 20
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(start_coords)

    def move_up(self):
        """ Move paddle up """
        if self.ycor() < limit_paddle_position:
            self.sety(self.ycor()+MOVE_INCREMENT)

    def move_down(self):
        """ Move paddle down """
        if self.ycor() > -limit_paddle_position:
            self.sety(self.ycor()-MOVE_INCREMENT)
