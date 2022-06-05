from tkinter import *

class Buttons:
  def __init__(self, window, is_small, pos, text) -> None:
    self.window = window
    self.is_small = is_small
    self.small_button_size = (125, 84)
    self.big_button_size = (250, 84)
    self.button_options = {
      "width": self.small_button_size[0] if self.is_small == True else self.big_button_size[0],
      "height": self.small_button_size[1] if self.is_small == True else self.big_button_size[1],
      "pos_x": pos[0],
      "pos_y": pos[1],
      "text": text,
    }
    self.button = Button(self.window, text=self.button_options.get("text"), background="white")
    self.button.place(x=self.button_options.get("pos_x"), y=self.button_options.get("pos_y"), width=self.button_options.get("width"), height=self.button_options.get("height"))
