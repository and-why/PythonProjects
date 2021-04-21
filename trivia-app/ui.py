from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ("Helvetica", 20, "italic")
FONT2 = ("Helvetica", 14, "normal")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = self.quiz.score
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20)
        self.canvas = Canvas(bg=THEME_COLOR, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.rectangle = self.canvas.create_rectangle(0, 0, 300, 250, fill="white", outline=THEME_COLOR)
        self.question_text = self.canvas.create_text(140, 100, width=260, text="Text items", font=FONT,
                                                     fill=THEME_COLOR,
                                                     justify="center")
        self.score_label = Label(text="Score: 0", fg="white", font=FONT2, bg=THEME_COLOR,
                                 justify="center", pady=20)
        self.score_label.grid(column=1, row=0)
        self.true = PhotoImage(file="images/true.png")
        self.false = PhotoImage(file="images/false.png")
        self.button_true = Button(image=self.true, highlightthickness=0, bg=THEME_COLOR, border=0,
                                  command=self.true_selected)
        self.button_false = Button(image=self.false, highlightthickness=0, bg=THEME_COLOR, border=0,
                                   command=self.false_selected)
        self.button_true.grid(column=0, row=2, pady=20)
        self.button_false.grid(column=1, row=2, pady=20)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.itemconfig(self.rectangle, fill="white")
        else:
            self.canvas.itemconfig(self.question_text,
                               text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def true_selected(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_selected(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.itemconfig(self.rectangle, fill="green")
        else:
            self.canvas.itemconfig(self.rectangle, fill="red")
        self.window.after(500, self.get_next_question)