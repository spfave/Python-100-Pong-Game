from turtle import Screen
from game_parameters import WINDOWWIDTH, WINDOWHEIGHT


# Functions
def game_screen():
    """ Create game screen """
    screen = Screen()
    screen.setup(width=WINDOWWIDTH, height=WINDOWHEIGHT)
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.tracer(0, 1)

    screen.exitonclick()
    return screen


# Main
screen = game_screen()
