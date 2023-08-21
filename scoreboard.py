from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Player L Score {self.l_score}", align="center",
                   font=("Courier", 20, "normal"))
        self.goto(200, 250)
        self.write(f"Player R Score {self.r_score}", align="center",
                   font=("Courier", 20, "normal"))

    def l_score_update(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_score_update(self):
        self.r_score += 1
        self.update_scoreboard()
