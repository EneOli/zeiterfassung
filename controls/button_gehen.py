from tkinter import Button

class ButtonGehen(Button):
    def __init__(self, command):
        super().__init__(text="Gehen", command=command)
        self.place(width=166, height=50, x=332, y=150)
