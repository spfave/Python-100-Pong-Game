from game_parameters import limit_vert, limit_paddle_face, limit_paddle_distance


# Functions
def detect_wall_collision(ball_yposition):
    """ Evaluate if the ball hit the top or bottom wall """
    return abs(ball_yposition) > limit_vert  # or ball_yposition < -limit_vert


def detect_paddle_collision(ball, player1_paddle, player2_paddle):
    """ Evaluate if the ball hit the front side of the paddle """

    # check collision with player 1 paddle
    if ball.distance(player1_paddle) <= limit_paddle_distance and ball.xcor() <= -limit_paddle_face:
        return True
    # check collision with player 2 paddle
    elif ball.distance(player2_paddle) <= limit_paddle_distance and ball.xcor() >= limit_paddle_face:
        return True
    else:
        return False
