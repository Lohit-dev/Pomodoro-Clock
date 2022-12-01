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
screen.config(padx=100,pady=50,bg = YELLOW)
screen.title("Pomodoro Clock")

# build a canvas
canvas = Canvas(width=592, height=592,bg=YELLOW,highlightthickness=0)

# store the tomato image in a variable
tomato_photo = PhotoImage(file="pomodoro_img.png")
canvas.create_image(296, 296, image=tomato_photo)
canvas.create_text(320, 350,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.pack()

screen.mainloop()
