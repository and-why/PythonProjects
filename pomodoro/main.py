from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECONDS = 60

reps = 0
check_text = ""
global_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global check_text
    window.after_cancel(global_timer)
    button_start.config(state="normal")
    timer_label.config(text="Timer", fg=GREEN)
    reps = 0
    canvas.itemconfig(time_label, text="00:00")
    check_text = "︎"
    check_label.config(text=check_text)


# ---------------------------- TIMER MECHANISM ------------------------------- # 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_timer():
    button_start.config(state="disabled")
    global reps
    global check_text
    reps += 1

    if reps % 8 == 0:
        check_text = "︎"
        check_label.config(text=check_text)
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * SECONDS)
        window.attributes('-topmost', 1)
    elif reps % 2 == 0:
        check_text += "✔︎"
        check_label.config(text=check_text)
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * SECONDS)
        window.attributes('-topmost', 1)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * SECONDS)
        window.attributes('-topmost', 0)


def count_down(countdown):
    if countdown > 0:
        global global_timer
        minutes, secs = divmod(countdown, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        canvas.itemconfig(time_label, text=timer)
        global_timer = window.after(1000, count_down, countdown - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_tomato)
canvas.grid(column=1, row=1)
time_label = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 48, "normal"))
timer_label.grid(column=1, row=0)

# check marks for which loop we're on
check_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 32, "normal"))
check_label.grid(column=1, row=3)

# button for start
button_start = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 32, "normal"), command=start_timer)
button_start.grid(column=0, row=2)
# button for reset
button_reset = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 32, "normal"), command=reset_timer)
button_reset.grid(column=2, row=2)


window.mainloop()