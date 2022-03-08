from turtle import Turtle, Screen

from matplotlib.style import use

# screen.listen()

# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.back(10)
# def turn_clockwise():
#     tim.right(10)    
# def turn_anticlockwise():
#     tim.left(10)
# def clear():
#     tim.penup()
#     tim.clear()
#     tim.home()
#     tim.pendown()
# screen.onkey(move_forward, "w") 
# screen.onkey(turn_anticlockwise, "a") 
# screen.onkey(move_backward, "s") 
# screen.onkey(turn_clockwise, "d") 
# screen.onkey(clear, "c") 

import random

screen = Screen()

screen.setup(height=400, width=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_index = [100, 60, 20, -20, -60, -100]
turtle_list = []

for turtle in range(0,6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[turtle])
    tim.goto(x=-230, y=y_index[turtle])
    turtle_list.append(tim)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for run in turtle_list:
        if run.xcor() > 230:
            is_race_on = False
            win_color = run.pencolor()
            if win_color == user_bet:
                print(f"You have won! The {win_color} won the bet.")
            else:
                print(f"You have lost! The {win_color} won the bet.")
        rand_distance = random.randint(0, 10)
        run.forward(rand_distance)















screen.exitonclick()

