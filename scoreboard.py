from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.current_score()

    def current_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.current_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
