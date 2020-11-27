from game_parameters import limit_vert


# Functions
def detect_wall_collision(ball_yposition):
    """ Evaluates if the ball has hit the top or bottom walls """
    if ball_yposition > limit_vert or ball_yposition < -limit_vert:
        print("ball bounce")
