# imported all tkinter classes
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

# Made a pop-up window with appropriate title
screen = Tk()
screen.config(padx=100, pady=50, bg=YELLOW)
screen.title("Pomodoro Clock")

# build a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Pomodoro Label
timer_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME,50))
timer_label.grid(row=0,column=1)

# Start Button
start_button = Button(text="Start",highlightthickness=0)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(row=2, column=2)

# Check marks
check_marks = Label(text="✅",fg=GREEN,bg=YELLOW)
check_marks.grid(row=3,column=1)
# Photo
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

screen.mainloop()
