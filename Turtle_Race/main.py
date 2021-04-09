from turtle import Turtle, Screen
import random



colors = ["red", "blue", "yellow", "green", "purple", "orange"]

is_playing = True


def play_game(user_bank):
    screen = Screen()
    screen.setup(width=500, height=400)

    is_race_on = False

    turtles = []

    pos_y = -100
    color_index = 0

    for turtle_index in range(0, 6):
        odds_move = random.randint(5, 15)
        odds_money = round(20/odds_move, 2)
        new_turtle = Turtle("turtle")
        new_turtle.color(colors[color_index])
        new_turtle.penup()
        new_turtle.goto(-230, pos_y)
        pos_y += 50
        color_index += 1
        turtles.append((new_turtle, odds_money, odds_move))

    bet_prompt = f"Who is going to win? Odds:\n" \
             f"Red: {turtles[0][1]}\n" \
             f"Blue: {turtles[1][1]}\n" \
             f"Yellow: {turtles[2][1]}\n" \
             f"Green: {turtles[3][1]}\n" \
             f"Purple: {turtles[4][1]}\n" \
             f"Orange: {turtles[5][1]}\n"

    money_prompt = f"You currently have ${user_bank}, How much would you like to bet?"

    user_bet_horse = screen.textinput(title="Make your bet", prompt=bet_prompt).lower()
    user_bet_money = int(screen.numinput(title="How much?", prompt=money_prompt))

    if user_bet_horse:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle[0].xcor() > 230:
                is_race_on = False
                win_color = turtle[0].fillcolor()
                odds_money = turtle[1]
                odds_move = turtle[2]
                if win_color == user_bet_horse:
                    user_bank += (user_bet_money * odds_money)
                    win_prompt = f"You won ${user_bet_money * (20 - odds_money)}! The {win_color} turtle with odds of" \
                                 f" {odds_money} won!\nWould you like to place another bet? Yes or No\n"
                    if screen.textinput(title="YOU WON :)", prompt=win_prompt).lower() == "yes":
                        screen.clear()
                        play_game(user_bank)
                    else:
                        screen.bye()
                else:
                    user_bank -= user_bet_money
                    lose_prompt = f"You lost ${user_bet_money}! The {win_color} turtle with odds of {odds_money} won!" \
                                  f"\n(press enter to continue)\nWould you like to place another bet? Yes or No\n"
                    if screen.textinput(title="YOU LOST :(", prompt=lose_prompt).lower() == "yes":
                        screen.clear()
                        play_game(user_bank)
                    else:
                        screen.bye()

            distance = random.randint(0, odds_move)
            turtle[0].fd(distance)


user_brings = int(input("How much money are you bringing to the races?: \n$"))

play_game(user_brings)










screen.exitonclick()
