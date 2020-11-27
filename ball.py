from turtle import Turtle
from random import choice


# Constants
MOVE_INCREMENT = 10
YTRAJECTORY_START = [-MOVE_INCREMENT, MOVE_INCREMENT]


# Classes
class Ball(Turtle):
    """ Game ball """

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.set_trajectory()

    def move(self):
        """ Move ball along trajectory path """
        self.setx(self.xcor()+self.x_move)
        self.sety(self.ycor()+self.y_move)

    def bounce_wall(self):
        """ Bounce ball off wall """
        self.y_move *= -1

    def set_trajectory(self, trajectory=(MOVE_INCREMENT, MOVE_INCREMENT)):
        """ Set ball trajectory by setting movement increment in x and y direction 
            Default ball trajectory at start is up and to the right
        """
        self.x_move = trajectory[0]
        self.y_move = trajectory[1]
