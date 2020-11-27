from turtle import Screen
from game_parameters import WINDOW_WIDTH, WINDOW_HEIGHT
from paddle import Paddle


# Functions
def game_screen():
    """ Create game screen """
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.tracer(0, 1)

    return screen


# Main --------------------------------------------------------------
# Game setup
screen = game_screen()

player1_paddle = Paddle()

screen.listen()
screen.onkey(key="Up", fun=player1_paddle.move_up)
screen.onkey(key="Down", fun=player1_paddle.move_down)

screen.update()

# Run game
game_running = True
while game_running:
    screen.update()

screen.exitonclick()
