from turtle import Turtle


# Constants
TEXT_ALIGNMENT = "center"
TEXT_SIZE = 60
FONT_STYLE = ("Courier", TEXT_SIZE, "bold")  # font, font size, b
P1_SCORE_POSITION = (-100, 200)
P2_SCORE_POSITION = (100, 200)


# Constants
WINNING_TOTAL = 5


# Classes
class Score():
    """ Player score """

    def __init__(self):
        self.value = 0

    def scored(self):
        self.value += 1


class Scoreboard(Turtle):
    """ Game scoreboard """

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.p1_score = Score()
        self.p2_score = Score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(P1_SCORE_POSITION)
        self.write(f"{self.p1_score.value}",
                   align=TEXT_ALIGNMENT, font=FONT_STYLE)
        self.goto(P2_SCORE_POSITION)
        self.write(f"{self.p2_score.value}",
                   align=TEXT_ALIGNMENT, font=FONT_STYLE)

    def player_point(self, ball_xcor):
        if ball_xcor > 0:
            self.p1_score.scored()
        else:
            self.p2_score.scored()
        self.update_score()
