from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.score_number = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {0}", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question text",
            font=("arial", 14, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true = PhotoImage(file="images/true.png")
        self.true = Button(image=true, highlightthickness=0, fg="white" , bg=THEME_COLOR, command=self.true_button)
        self.true.grid(column=1, row=2)

        false = PhotoImage(file="images/false.png")
        self.false = Button(image=false, highlightthickness=0, fg="white" , bg=THEME_COLOR, command=self.false_button)
        self.false.grid(column=0, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
            text="You have reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))



    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question )
