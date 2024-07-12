from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.Level = 1
        self.score()

    def score(self):
        self.write(f"Level = {self.Level}", align='left', font=FONT)

    def level_up(self):
        self.clear()
        self.Level += 1
        self.score()

    def game_end(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
