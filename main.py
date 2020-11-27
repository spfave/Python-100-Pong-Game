from turtle import Screen
import time
import game_parameters as gp
import game_engine as ge
from paddle import Paddle
from ball import Ball


# Functions
def game_screen():
    """ Create game screen """
    screen = Screen()
    screen.setup(width=gp.WINDOW_WIDTH, height=gp.WINDOW_HEIGHT)
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.tracer(0)

    return screen


# Main --------------------------------------------------------------
# Game setup
screen = game_screen()

player1_paddle = Paddle(start_coords=gp.PLAYER1_START_POSITION)
player2_paddle = Paddle(start_coords=gp.PLAYER2_START_POSITION)
ball = Ball(45)

screen.listen()
screen.onkey(key="Up", fun=player1_paddle.move_up)
screen.onkey(key="Down", fun=player1_paddle.move_down)
screen.onkey(key="w", fun=player2_paddle.move_up)
screen.onkey(key="s", fun=player2_paddle.move_down)

screen.update()

# Run game
game_running = True
while game_running:
    ball.move()

    ge.detect_wall_collision(ball.ycor())

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
