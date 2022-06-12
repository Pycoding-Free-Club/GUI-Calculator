from tkinter import *
from math import *

window__width = 500
window__height = 756

win = Tk()
win.geometry(f"{window__width}x{window__height}")
win.title("공학계산기")
win.option_add("*Font","맑은고딕 25")
win.attributes('-alpha', 0.95)

BbuttonSize = (250, 84)
SbuttonSize = (125, 84)

expression = ""

def place_btn(isSmall, x, y, text, command):
    button = Button(win, text=text, background = "white", command=command)
    if isSmall == True:
        button.place(x=x, y=y, width=SbuttonSize[0], height=SbuttonSize[1])
    else:
        button.place(x=x, y=y, width=BbuttonSize[0], height=BbuttonSize[1])

def make_lambda(number):
    return lambda: add_number(number)

def add_number(value):
    global expression

    if value == "=":
        result = eval(expression)
        expression = str(result)
        change_text(result)

    else:
        expression += value
        change_text(expression)

def change_text(value):
    global label
    label.config(text=value)

texts = [ "sin", "cos", "tan", "%", "π", "√", "(", ")", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0", "=", "/" ]
btn_Pos = (0, 168)
column_and_row = (6, 4)

text_idx = 0
for i in range(column_and_row[0]):
    for j in range(column_and_row[1]):
        place_btn(True, btn_Pos[0]+(j*125), btn_Pos[1]+(i*84), texts[text_idx], make_lambda(texts[text_idx])) 
        text_idx += 1

place_btn(False, 0, 672, "AC", command=add_number)
place_btn(False, 250, 672, "Save", command=add_number)

label = Label(win, text="", fg="black", relief="solid")
label.place(x=0, y=0, width=500, height=168)

win.mainloop()
