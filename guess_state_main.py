import turtle
import pandas as pd
from timer import Timer

screen = turtle.Screen()

print("Welcome to the guessing game!")
image = "blank_states_img.gif"
file = "50_states.csv"
data = pd.read_csv(file)

screen.addshape(image)
screen.setup(width = 700, height = 600)
turtle.shape(image)

writer = turtle.Turtle() #object that write name of guessed state
writer.hideturtle()
writer.penup()

game_over = False
score = 0

timer = Timer(screen, game_over) #timerclass

states = data["state"].to_list() #column of states become list

while not game_over:
    guess = screen.textinput(title=f"SCORE: {score}/50", prompt="Guess the state: ")
    guess = guess.strip().title()

    if guess is None:
        break

    elif guess not in states:
        break

    elif guess in states:
        new_row = data[data.state == guess].iloc[0]
        writer.goto(new_row.x, new_row.y)
        writer.write(new_row.state)
        score += 1

screen.exitonclick()
screen.mainloop()

