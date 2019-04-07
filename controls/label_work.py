from tkinter import Label

class LabelWork(Label):
    def __init__(self):
        super().__init__(text="Arbeitszeit: 00:00:00", font=("", 32))
        self.place(x=0, y=0)

    def setTime(self, hours, minutes, seconds):
        if(hours < 10):
            hours = "0" + str(hours)
        if(minutes < 10):
            minutes = "0" + str(minutes)
        if(seconds < 10):
            seconds = "0" + str(seconds)

        self.configure(text = "Arbeitszeit: " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
