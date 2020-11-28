from turtle import Turtle


# Constants
TEXT_ALIGNMENT = "center"
FONT_STYLE = ("Courier", 80, "bold")  # font, font size, b
P1_SCORE_POSITION = (-100, 200)
P2_SCORE_POSITION = (100, 200)


# Variables
# scoreboard_position = (0, WINDOWHEIGHT/2-TEXT_SIZE*2)


# Classes
class Score():
    """ Player score """

    def __init__(self):
        self.value = 0

    def increase_score(self):
        self.value += 1


class Scoreboard(Turtle):
    """ Game scoreboard """

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.pl_score = Score()
        self.p2_score = Score()

    def write_score(self):
        self.clear()
        self.goto(P1_SCORE_POSITION)
        self.write("f{self.p1_score.value}",
                   align=TEXT_ALIGNMENT, font=FONT_STYLE)
        self.goto(P1_SCORE_POSITION)
        self.write("f{self.p2_score.value}",
                   align=TEXT_ALIGNMENT, font=FONT_STYLE)
