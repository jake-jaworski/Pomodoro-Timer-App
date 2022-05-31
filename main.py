from tkinter import *
from PIL import ImageTk, Image
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BROWN = "#F4E8DC"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global repetitions
    repetitions = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global repetitions
    repetitions += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break)
    if repetitions % 2 == 0:
        countdown(short_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    minute = math.floor(count / 60)
    second = int(count % 60)
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check = ""
        for i in range(math.floor(repetitions / 2)):
            check += "✅"
        checkmark_label.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(bg=BROWN)


canvas = Canvas(width=350, height=300, highlightthickness=0, bg=BROWN)
tomato = ImageTk.PhotoImage(Image.open("tomato.gif"))
canvas.create_image(175, 100, image=tomato)
timer_text = canvas.create_text(173, 175, text="00:00", font=(FONT_NAME, 36, "bold"), fill="white")


start = Button(text="Start", highlightthickness=0, command=start_timer)
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)

timer_label = Label(text="Timer", font=(FONT_NAME, 72, "bold"), fg=GREEN, highlightthickness=0, bg=BROWN)
checkmark_label = Label(font=(FONT_NAME, 24, "bold"), fg=GREEN, highlightthickness=0, bg=BROWN)


canvas.grid(column=1, row=1)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)
timer_label.grid(column=1, row=0)
checkmark_label.grid(column=1, row=3)

window.mainloop()
