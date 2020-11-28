import time
import game_parameters as gp
import game_engine as ge
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Main --------------------------------------------------------------
# Game setup
screen = gp.game_screen()

player1_paddle = Paddle(start_coords=gp.PLAYER1_START_POSITION)
player2_paddle = Paddle(start_coords=gp.PLAYER2_START_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=player1_paddle.move_up)
screen.onkey(key="s", fun=player1_paddle.move_down)
screen.onkey(key="Up",   fun=player2_paddle.move_up)
screen.onkey(key="Down", fun=player2_paddle.move_down)

# Run game
game_running = True
while game_running:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    if ge.detect_wall_collision(ball.ycor()):
        ball.bounce_wall()

    if ge.detect_paddle_collision(ball, player1_paddle, player2_paddle):
        ball.bounce_paddle()

    if ge.detect_missed_ball(ball.xcor()):
        scoreboard.player_score(ball.xcor())
        if scoreboard.check_winner():
            game_running = False
        ball.reset()

screen.exitonclick()
