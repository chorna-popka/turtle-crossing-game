from turtle import Turtle

FONT = ("Chalkboard", 17, "normal")
ALIGN = "center"


class Score(Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.color("#e87800")
        self.up()
        self.ht()
        self.goto(xpos, ypos)
        self.speed("fastest")
        self.score = 1
        self.delay = 0.1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level {self.score}", False, ALIGN, FONT)

    def add_score(self, points):
        self.score += points
        self.delay *= 0.9
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.color("#ff0000")
        self.write(f"GAME OVER", False, ALIGN, FONT)
