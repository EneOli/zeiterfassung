from tkinter import Label
import datetime

class LabelInfos(Label):
    def __init__(self):
        self.set = False
        self.startDay = datetime.date.today().strftime("%d.%m.%y")
        super().__init__(text="Arbeitsbeginn: " + str(self.startDay), font=("", 20))
        self.place(x=0, y=100)

    def setStartTime(self):
        if not self.set:
            self.startTime = datetime.datetime.today().strftime("%H:%M:%S")
            self.configure(text="Arbeitsbeginn: " + str(self.startDay) + " "+ str(self.startTime))
            self.set = True

    def getStartTime(self):
        return self.startDay, self.startTime

