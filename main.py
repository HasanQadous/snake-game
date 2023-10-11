from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Lo3bat AL Zobor AL Taweeeel")
screen.tracer(0)

snake = Snake()

food = Food()

score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.score_add()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset_snake()

    for seg in snake.turtles[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset_snake()


















screen.exitonclick()