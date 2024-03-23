from turtle import Turtle
ALIGNMENT = "center"
FONT_STYLE = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_STYLE)

    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT_STYLE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
