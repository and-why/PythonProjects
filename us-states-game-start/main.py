import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# GET STATE LOCATIONS
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

states_guessed = []
game_is_on = True

while len(states_guessed) < 50:

    answer_state = (screen.textinput(title=f"Guess the state. {len(states_guessed)}/50", prompt="What's another State's name?")).title()

    if answer_state == "Exit":
        states_to_learn = []
        for state in states:
            if state not in states_guessed:
                states_to_learn.append(state)
            new_data = pandas.DataFrame(states_to_learn)
            new_data.to_csv("states-to-learn.csv")
        break
    for state_check in states:
        if answer_state == state_check:
            states_guessed.append(state_check)
            x_cor = int(data[data.state == state_check].x)
            y_cor = int(data[data.state == state_check].y)
            location = turtle.Turtle()
            location.penup()
            location.hideturtle()
            location.goto(x_cor, y_cor)
            location.write(state_check, move=False, align="left", font=("Helvetica", 8, "normal"))



