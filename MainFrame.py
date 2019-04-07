from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from controls.button_start import ButtonStart
from controls.button_pause import ButtonPause
from controls.button_gehen import ButtonGehen
from controls.label_money import LabelMoney
from controls.label_work import LabelWork
from controls.label_infos import LabelInfos
import datetime
import os

class MainFrame(Tk):
    def __init__(self):
        super().__init__()
        self.title("Ollis kleine Zeiterfassung")
        self.geometry("500x200+%d+%d" % (self.winfo_screenwidth(), 0))
        self.resizable(0, 0)
        self.buttonStart = ButtonStart(command=self.onStartClick)
        self.buttonPause = ButtonPause(command=self.onPauseClick)
        self.buttonGehen = ButtonGehen(command=self.exportCsv)
        self.workLabel = LabelWork()
        self.labelMoney = LabelMoney()
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.labelInfos = LabelInfos()

        self.start = FALSE

        self.after(1000, self.updateTime)

        self.mainloop()

    def onStartClick(self):
        self.start = True
        self.labelInfos.setStartTime()
        if self.paused:
            aHours = datetime.datetime.now().hour
            aMinutes = datetime.datetime.now().minute
            aSeconds = datetime.datetime.now().second
            self.pauseTime = str(int(aHours) - int(self.hours)) + ":" + str(int(aMinutes) - int(self.minutes)) + ":" + str(int(aSeconds) - int(self.seconds))

    def onPauseClick(self):
        self.start = FALSE
        self.paused = True

    def exportCsv(self):
        startDay, startTime = self.labelInfos.getStartTime()
        sTime = startTime.split(":")
        eTime = datetime.datetime.today().strftime("%H:%M:%S").split(":")

        diff = str(int(eTime[0]) - int(sTime[0])) + ":" + str(int(eTime[1]) - int(sTime[1])) + ":" + str(int(eTime[2]) - int(sTime[2]))

        try:
            self.pauseTime
        except:
            self.pauseTime = "0"

        csvText = startDay + "," + startTime + "," + self.pauseTime + "," + datetime.datetime.today().strftime("%H:%M:%S") + "," + diff
        print(csvText)

        name = asksaveasfilename(filetypes =(("CSV", "*.csv"),),title="Stundendatei auswählen")

        print(name)

        if not os.path.exists(name):
            file = open(name, "w+")
            file.write("Tag,Beginn,Pause,Ende,Dauer\r\n")
        else:
            file = open(name, "a")

        file.write(csvText + "\r\n")
        file.flush()
        file.close()

    def updateTime(self):
        if(self.start):
            self.seconds = self.seconds + 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes = self.minutes + 1

            if self.minutes >= 60:
                self.minutes = 0
                self.hours = self.hours + 1

            if self.hours >= 99:
                messagebox.showwarning("Geh nach Hause!", "Geh nach Hause!")


            allMinutes = self.hours * 60 + self.minutes + self.seconds / 60
            money = allMinutes / 60 * 10

            self.labelMoney.setMoney(money)

            self.workLabel.setTime(self.hours, self.minutes, self.seconds)
        self.after(1000, self.updateTime)
