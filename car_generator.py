import random
import car
import time

# create lanes so that cars do not overlap
lanes = [ ]
for y in range(-240, 270, 30):
    lanes.append(y)


def generate_ypos():
    return random.choice(lanes)


class CarGenerator():

    def __init__(self, cars):
        self.max_cars = cars
        self.cars = []
        self.generate_car(1)

    def generate_car(self, score):
        #generate cars as more frequent as level grows
        if score > 10:
            c = car.Car(320, generate_ypos())
            self.cars.append(c)
        elif random.randint(0, 11 - score) == 1:
            c = car.Car(320, generate_ypos())
            self.cars.append(c)

    def move_cars(self):
        for c in self.cars:
            c.move()

    def clear_cars(self):
        self.cars = []
