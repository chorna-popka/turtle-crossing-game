from turtle import Turtle


class Actor(Turtle):

    def __init__(self, color):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.restart()

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def restart(self):
        self.goto(0, -280)

