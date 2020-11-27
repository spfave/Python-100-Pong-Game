from math import sqrt


# Constants
# Window size and limit offset
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
OFFSET = 25

# Paddle size and start positions
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

PLAYER1_START_POSITION = (-350, 0)
PLAYER2_START_POSITION = (350, 0)

# Ball size
BALL_RADIUS = 10

# Variables
limit_horz = WINDOW_WIDTH/2
limit_vert = WINDOW_HEIGHT/2-OFFSET
limit_paddle_face = PLAYER2_START_POSITION[0]-PADDLE_WIDTH/2-BALL_RADIUS
limit_paddle_distance = PADDLE_HEIGHT/2
limit_paddle_position = WINDOW_HEIGHT/2-PADDLE_HEIGHT/2
