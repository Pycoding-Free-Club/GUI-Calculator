# Import Modules
from tkinter import *
from math import *

# Configure windows and etc...
win__width = 500
win__height = 756

win = Tk()
win.geometry(f"{win__width}x{win__height}")
win.title("공학계산기")
win.option_add("*Font","맑은고딕 25")
win.attributes('-alpha', 0.95)

BbuttonSize = (250, 84)
SbuttonSize = (125, 84)

# Define the function which are help calculating and etc...
def place_btn(isSmall, x, y, text, handler):
    button = Button(win, text=text, background = "white", command=handler)
    if isSmall == True:
        button.place(x=x, y=y, width=SbuttonSize[0], height=SbuttonSize[1])
    else:
        button.place(x=x, y=y, width=BbuttonSize[0], height=BbuttonSize[1])

def get_number(number):
    print(f"Button is clicked! And value of that is...{number}")

texts = [ "sin", "cos", "tan", "%", "π", "√", "!", "^", "7", "8","9","+","4","5","6","-","1","2","3", "X", ".", "0", "=", "÷" ]
btn_Pos = (0, 168)
column_and_row = (6, 4)

text_idx = 0
for i in range(column_and_row[0]):
    for j in range(column_and_row[1]):
        place_btn(True, btn_Pos[0]+(j*125), btn_Pos[1]+(i*84), texts[text_idx], command=get_number)
        text_idx += 1

place_btn(False, 0, 672, "AC", command=get_number)
place_btn(False, 250, 672, "Save", command=get_number)

win.mainloop()
