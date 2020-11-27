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
        self.setx(self.xcor()+MOVE_INCREMENT)
        self.sety(self.ycor()+MOVE_INCREMENT)
        # self.forward(MOVE_INCREMENT)
