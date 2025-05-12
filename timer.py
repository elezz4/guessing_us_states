from functools import update_wrapper
from turtle import Turtle, Screen
import time

class Timer(Turtle):
    def __init__(self, screen, game_over):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.screen = screen
        self.game_over = game_over
        self.time = 10
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Remaining time: {self.time}", move=False, font=("Montserat", 17, "normal"))
        if self.time > 0:
            self.time -= 1
            self.screen.ontimer(self.update_score, 1000)
        else:
            self.game_over = True



