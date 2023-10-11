import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)


