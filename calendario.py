"""
import calendar
print(calendar.Calendar(2015))
"""
from tkinter import *
from tkinter import ttk
from datetime import datetime
"""
from datetime import datetime
currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
"""

class calendarButton(ttk.Frame):
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=30, width=51)
        self.pack_propagate(0)

        self.__btn = ttk.Button(self, text=args["text"])
        self.__btn.pack(fill=BOTH, expand=1)

class mesDisplay(ttk.Frame):
    __value = datetime.date.month


    def __init__(self,parent,**args):
        
        self.__labelframe = ttk.LabelFrame(self, text=self.__value)
        self.__labelframe.pack(fill=BOTH)

        left = ttk.Label(self.__labelframe, text="Aqui van los numeros")
        left.pack(fill=BOTH)


class mainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
        #self.configure(bg="#A9D0F5")

        __btnLastYear = calendarButton(self, text="<<").place(x=24, y=5)
        __btnLastMonth = calendarButton(self, text="<").place(x=83, y=5)
        __btnNextMonth = calendarButton(self, text=">").place(x=398, y=5)
        __btnNextYear = calendarButton(self, text=">>").place(x=457, y=5)

        mesDisplay(self).place(x=0,y=0)



    def start(self):
        self.mainloop()


if __name__ == "__main__":
    calend = mainApp()
    calend.start()
