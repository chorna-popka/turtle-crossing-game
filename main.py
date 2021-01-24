from turtle import Screen
from score import Score
from actor import Actor
from car_generator import CarGenerator


import time

# some config
width = 600
height = 600
turtle_color = "#3b3742"

screen = Screen()
screen.setup(width=width, height=height)
screen.colormode(255)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)
game_over = False


#objects
score = Score(0, 270)
actor = Actor(turtle_color)
car_gen = CarGenerator(40)

#controls
screen.listen()
screen.onkey(fun=actor.up, key="Up")

while not game_over:

    time.sleep(score.delay)
    screen.update()
    car_gen.generate_car(score.score)
    car_gen.move_cars()

    for car in car_gen.cars:
        if car.distance(actor) < 20:
            game_over = True
            score.game_over()

    if actor.distance(score) <= 10:
        score.add_score(1)
        actor.restart()

    #crash
    # if actor.distance(actor) < 10:
    #     game_over = True
    #     score.game_over()



screen.exitonclick()