from tkinter import *
from tkinter import ttk
from datetime *
import calendar

anioActual = datetime.now().year
dictMes = {"1":"Enero","2":"Febrero","3":"Marzo","4":"Abril","5":"Mayo","6":"Junio","7":"Julio","8":"Agosto","9":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}
unMes = timedelta(days=31)
unAnio = timedelta(days=356)
mesActual = dictMes[str(datetime.now().month)]

calendarioMensual = calendar.month(datetime.now().year,datetime.now().month)

class calendarButton(ttk.Frame):
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=30, width=51)
        self.pack_propagate(0)

        self.__btn = ttk.Button(self, text=args["text"])
        self.__btn.pack(fill=BOTH, expand=1)



        def sumaMeses(self,**args):
            sumaMes = mesActual + unMes
            otroMes = sumaMes.month

            return mesDict[str(otroMes)]

        def restaMeses(self,**args):
            restaMes = mesActual - unMes
            otroMes = restaMes.month

            mesDict[str(otroMes)]


class mesDisplay(ttk.Frame):


    __value = mesActual, anioActual

    def __init__(self, parent, **args):

        ttk.Frame.__init__(self,parent)
        self.__labelframe = ttk.LabelFrame(self, text=self.__value)
        self.__labelframe.pack(fill=BOTH)

        s = ttk.Style()
        s.configure("my.TLabel",font=("Arial",24,"bold"))
        self.__lbl = ttk.Label(self.__labelframe, text=str(calendarioMensual),style="my.TLabel")
        self.__lbl.pack(fill=BOTH)


class mainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
        # self.configure(bg="#A9D0F5")

        __btnLastYear = calendarButton(self, text="<<").place(x=24, y=5)
        #__btnLastMonth = calendarButton(self, text="<",command=restaMeses).place(x=83, y=5)
        #__btnNextMonth = calendarButton(self, text=">",command=sumaMeses).place(x=398, y=5)
        __btnLastMonth = calendarButton(self, text="<").place(x=83, y=5)
        __btnNextMonth = calendarButton(self, text=">").place(x=398, y=5)
        __btnNextYear = calendarButton(self, text=">>").place(x=457, y=5)

        self.__display = mesDisplay(self)
        self.__display.place(x=202, y=5)

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    calend = mainApp()
    calend.start()