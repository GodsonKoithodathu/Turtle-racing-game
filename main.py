import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setting the screen for the game:
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initializing objects from their respective classes:
turtle = Player()
car = CarManager()
score = Scoreboard()

# making the screen listen to the keys pressed to move the turtle:
screen.listen()
screen.onkey(fun=turtle.up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    # to check whether the car hits the turtle if yes then to stop the game:
    for cars in car.all_cars:
        if cars.distance(turtle) < 20:
            score.game_end()
            game_is_on = False

    # to check whether the turtle has reached the finish line if yes then level up and increase the speed of cars:
    if turtle.ycor() == 280:
        turtle.turtle_start()
        car.increase_speed()
        score.level_up()

screen.exitonclick()
