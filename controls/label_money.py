from tkinter import Label

class LabelMoney(Label):
    def __init__(self):
        super().__init__(text="Gehalt: 00,00€", font=("", 32))
        self.place(x=0, y=50)

    def setMoney(self, money):
        self.configure(text = "Gehalt: " + "{0:.2f}".format(money) + "€")
