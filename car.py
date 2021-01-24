from turtle import Turtle
from random import randint


def get_color():
    """Generates random color"""
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Car(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(get_color())
        self.speed("fastest")
        self.penup()
        self.shapesize(1, 2)
        self.velocity = 10
        self.goto(x, y)

    def move(self):
        self.goto(self.xcor() - self.velocity, self.ycor())


    def speed_up(self):
        self.velocity += 5

