from turtle import Turtle
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
limit_horz = WINDOW_WIDTH/2-OFFSET
limit_vert = WINDOW_HEIGHT/2-OFFSET
limit_paddle_face = PLAYER2_START_POSITION[0]-PADDLE_WIDTH/2-BALL_RADIUS
limit_paddle_distance = sqrt(
    (PADDLE_HEIGHT/2)**2 + (PADDLE_WIDTH/2+BALL_RADIUS)**2)
limit_paddle_position = WINDOW_HEIGHT/2-PADDLE_HEIGHT/2


# Functions
def draw_centerline():
    t = Turtle()
    t.penup()
    t.pensize(width=7)
    t.hideturtle()
    t.color("white")

    dash_length = 20
    boundary_vert = int(WINDOW_HEIGHT/2-dash_length/2)
    t.goto(0, -boundary_vert)
    for _ in range(-boundary_vert, boundary_vert+1, dash_length):
        t.pendown()
        t.goto(t.position()+(0, dash_length))
        t.penup()
        t.goto(t.position()+(0, dash_length))
