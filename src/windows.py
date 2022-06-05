from tkinter import *

class Windows:
  def __init__(self) -> None:
    self.window_options = {
      "width": 500,
      "height": 756,
      "title": "Scientific Calculator",
      "font": ["*Font", "맑은고딕 25"],
      "alpha": 0.95,
    }

    self.window = Tk()
    self.setup()

  def setup(self):
    self.window.geometry(
      f"""{self.window_options.get("width")}x{self.window_options.get("height")}"""
    )
    self.window.title(self.window_options.get("title"))
    self.window.option_add(self.window_options.get("font")[0], self.window_options.get("font")[1])
    self.window.attributes("-alpha", self.window_options.get("alpha"))
