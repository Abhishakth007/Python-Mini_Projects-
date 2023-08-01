# ---------------------------- CONSTANTS ------------------------------- #
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
turn = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(str(my_timer))
    canvas.itemconfig(timer_countdown,text="00:00")
    canvas.itemconfig(work_to_do,text="TIMER")
    check_mark_label.config(text="")
    global turn
    turn =0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global turn
    turn += 1
    if turn % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        canvas.itemconfig(work_to_do, text=f"Long..Break..Time", font=(FONT_NAME, 20, "bold"), fill="white")
    elif turn % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        canvas.itemconfig(work_to_do, text=f"Short..Break..Time", font=(FONT_NAME, 20, "bold"), fill="white")


    else:
        count_down(WORK_MIN * 60)
        canvas.itemconfig(work_to_do, text=f"Work..Time", font=(FONT_NAME, 20, "bold"), fill="white")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global my_timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_countdown, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(10, count_down, count - 1)

    else:
        start_time()
        mark = " "
        for i in range(int(turn / 2)):
            mark += " ✔"
            check_mark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Pomodoro..")
window.config(bg=GREEN)
canvas = Canvas(width=400, height=423, bg=GREEN)

start_button = Button(text="start", font=(FONT_NAME, 10, "bold"))
start_button.config(command=start_time)
start_button.place(x=65, y=310)

reset_button = Button(text="reset", font=(FONT_NAME, 10, "bold"))
reset_button.config(command=reset_time)
reset_button.place(x=280, y=310)

check_mark_label = Label(font=(FONT_NAME, 10, "bold"))
check_mark_label.config(bg=GREEN)
check_mark_label.place(x=150, y=370)

picture = PhotoImage(file="tomato.png")
canvas.create_image(200, 220, image=picture)
timer_countdown = canvas.create_text(200, 230, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
work_to_do = canvas.create_text(200, 70, text="TIMER", font=(FONT_NAME, 50, "bold"), fill="white")
canvas.pack()

window.mainloop()
