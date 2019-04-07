from tkinter import Button

class ButtonStart(Button):
    def __init__(self, command):
        super().__init__(text="Kommen", command=command)
        self.place(width=166, height=50, x=0, y=150)
