from tkinter import *
import pandas
import random

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Helvetica", 40, "italic")
WORD_FONT = ("Helvetica", 60, "bold")

# -------------- WORD DATABASE --------------#

try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = words.to_dict(orient="records")

correct_translations = []
current_card = {}


def show_english_word():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)
    button_wrong['state'] = 'normal'
    button_correct['state'] = 'normal'


def new_french_word():
    global current_card
    current_card = random.choice(word_dict)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    window.after(3000, show_english_word)
    button_wrong['state'] = 'disabled'
    button_correct['state'] = 'disabled'


def get_english_word(english_translation):
    canvas.create_image(400, 263, image=card_back)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=english_translation)


def correct_answer():
    global word_dict
    global current_card
    new_french_word()
    correct_translations.append(current_card)
    word_dict.remove(current_card)
    words_to_learn = pandas.DataFrame.from_dict(word_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)



def incorrect_answer():
    new_french_word()


# ------------------- UI -------------------#

window = Tk()
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

# Canvas
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, fill="black", text="Title", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, fill="black", text="Word", font=WORD_FONT)

# Buttons
image_correct = PhotoImage(file="images/right.png")
image_wrong = PhotoImage(file="images/wrong.png")
button_correct = Button(image=image_correct, bd=0, highlightthickness=0, bg=BACKGROUND_COLOR, command=correct_answer)
button_correct.grid(column=0, row=1)
button_wrong = Button(image=image_wrong, bd=0, highlightthickness=0, bg=BACKGROUND_COLOR, command=incorrect_answer)
button_wrong.grid(column=1, row=1)

new_french_word()

window.mainloop()
