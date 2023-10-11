from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f'Score: {self.score} High Score: {self.highscore}', font=("Courier", 23, "normal"), align="Center")


    def score_add(self):
        self.score += 1
        self.update_score()

