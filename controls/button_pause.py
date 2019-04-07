from tkinter import Button

class ButtonPause(Button):
    def __init__(self, command):
        super().__init__(text="Pause", command=command)
        self.place(width=166, height=50, x=166, y=150)
