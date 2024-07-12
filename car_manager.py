from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # to create random cars and append it to the list:
    def create_car(self):
        random_choice = random.randint(0, 6)
        if random_choice == 1:
            new_cars = Turtle('square')
            new_cars.penup()
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.color(random.choice(COLORS))
            x_cor = 300
            y_cor = random.randint(-240, 250)
            new_cars.goto(x_cor, y_cor)
            self.all_cars.append(new_cars)

    # to move the cars from left to right when the screen refresh in the main.py it will move accordingly:
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
