from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for segments in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[segments - 1].xcor()
            new_y = self.turtles[segments - 1].ycor()
            self.turtles[segments].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DIS)

    def reset_snake(self):
        for seg in self.turtles:
            seg.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)