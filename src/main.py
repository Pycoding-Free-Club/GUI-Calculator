# Import Modules
from tkinter import *
from math import *

from buttons import Buttons
from windows import Windows
from calculator import Calculator

# Create Window and Calculator
window = Windows()
calculator = Calculator()

# Place the buttons pretty
texts = [ "sin", "cos", "tan", "%", "π", "√", "!", "^", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "X", ".", "0", "=", "÷" ]
btn_Pos = (0, 168)
column_and_row = (6, 4)
buttons = []

text_idx = 0
for i in range(column_and_row[0]):
  for j in range(column_and_row[1]):
    buttons.append(
      Buttons(
        window.window,
        True,
        [
          btn_Pos[0]+(j*125),
          btn_Pos[1]+(i*84)
        ],
        texts[text_idx]
      )
    )

    text_idx += 1

buttons.append(Buttons(window.window, False, [0, 672], "Save"))
buttons.append(Buttons(window.window, False, [250, 672], "AC"))

# Start Calculator
window.window.mainloop();
