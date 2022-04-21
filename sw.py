import tkinter
from tkinter import *
import tkinter as tkr
from time import strftime
import datetime
import timeit
from tkinter import messagebox
from turtle import width
class App():
    def __init__(self):
        self.create_app()
    # create_app -> goback
    # create_login
    # if goback : -> call create_login
    def create_app(self):
        root = tkr.Tk()
        root.geometry('900x600')
        root.configure(bg='blue')
        root.title('Southwest Clock-in')
        photoLabel_frame = tkr.Frame(root)
        photoLabel_frame.pack()
        # Pass the path to the photo in your local computer here.
        photo = PhotoImage(file='')
        tkr.Label(photoLabel_frame, image=photo).grid(row=1, column=1)
        def time():
            x = datetime.datetime.now().strftime(("%d/%m/%Y \n%H:%M:%S %p"))
            clock.config(text=x, bg='blue', fg='white', font='times 20 bold')
            clock.after(1000, time)
        time_frame = tkr.Frame(root, bg='blue')
        time_frame.pack()
        clock = tkr.Label(time_frame, pady=30, padx=30)
        time()
        clock.grid(row=0, column=0)
        # create a label widget
        main_frame = tkr.Frame(root, bg='blue')
        main_frame.pack()
        tkr.Label(main_frame, text="Team", bg='blue', fg='white', font='times 20 bold').grid(row=0, column=0, sticky=W)
        tkr.Label(main_frame, text="Name", bg='blue', fg='white', font='times 20 bold').grid(row=1, column=0, pady=10,sticky=W)                                                                                    
        tkr.Label(main_frame, text="ID", bg='blue', fg='white', font='times 20 bold').grid(row=2, column=0, pady=10,sticky=W)                                                                                       
        tkr.Label(main_frame, text="Month", bg='blue', fg='white', font='times 20 bold').grid(row=3, column=0, pady=10,sticky=W)
                                                                                           
        # team number drop list
        options = [
            "Northwest",
            "Northeast",
            "Southwest",
            "Southeast",
            "Centeal North",
            "Central South"]
        clicked = IntVar()
        clicked.set("Select your team number")
        optionMenu = tkr.OptionMenu(main_frame, clicked, *options)
        optionMenu.config(width="30")
        optionMenu.grid(row=0, column=1)
        # name droplist
        pilot = [
            "John Rosenberry",
             "Viviance Nguyen",
             "Izaak Ditrich",
             "Patrick Bauer",
             'Sam Brown'

         ]
        clicked = StringVar()
        clicked.set("Chose your name")
        pilot = tkr.OptionMenu(main_frame, clicked, *pilot)
        pilot.config(width="30")
        pilot.grid(row=1, column=1)
        # entry widgets, used to take entry from user
        month = tkr.StringVar
        month= Entry(main_frame, width=34, bg="white", textvariable=month).grid (row=3, column=1)
        monthSel = ['January','February','March','April','May','June','July','August','September','October','November','December']
        clicked = StringVar()
        clicked.set("Select your month")
        monthSel = tkr.OptionMenu(main_frame, clicked, *monthSel)
        monthSel.config(width="30")
        monthSel.grid(row=3, column=1)
        # tkr.Entry(main_frame, id_numb)
        id = tkr.StringVar()
        id_numb = Entry(main_frame, width=34, bg="white", textvariable=id)
        id_numb.grid(row=2, column=1)
        def validation():
            id = id_numb.get()
            if len(id) == 0:
                msg = 'Field can\'t be empty'
            else:
                try:
                    if len(id) == 4:
                        msg = 'Clock-In Operation Successfully'
                    else:
                        msg = 'Try Again With 4 Digit'
                except:
                    msg = 'Enter Number Only'
            messagebox.showinfo('info', msg)

         # validation()

        def screen2():
            root = tkr.Tk()
            root.geometry('900x600')
            root.configure(bg='blue')
            root.title('Flight Hour and Wage Calculator!')
            photoLabel_frame = tkr.Frame(root)
            photoLabel_frame.pack()
        # Pass the path to the photo in your local computer here.
            photo = PhotoImage(file='')
            tkr.Label(photoLabel_frame, image=photo).grid(row=1, column=1)
            frame = tkr.Frame(root, bg='blue')
            frame.pack()
            Label(frame, text = "Pilot ID", bg='blue', fg='white', font='Courier 25 bold').grid(row = 2, column = 1, sticky = W)
            Label(frame, text = "Time In (Hour)", bg='blue', fg='white', font='Courier 25 bold').grid(row = 3, column = 1, sticky = W)
            Label(frame, text = "Time In (Minute)", bg='blue', fg='white', font='Courier 25 bold').grid(row = 4, column = 1, sticky = W)
            Label(frame, text = "Time Out (Hour)", bg='blue', fg='white', font='Courier 25 bold').grid(row = 5, column = 1, sticky = W)
            Label(frame, text = "Time Out (Minute)", bg='blue', fg='white', font='Courier 25 bold').grid(row = 6, column = 1, sticky = W)
            Label(frame, text = "Total Hours", bg='blue', fg='white', font='Courier 25 bold').grid(row = 7, column = 1, sticky = W)
            Label(frame, text = "Total Minute", bg='blue', fg='white', font='Courier 25 bold').grid(row = 8, column = 1, sticky = W)

            self.time_inHVar = StringVar()
            Entry(frame, textvariable = self.time_inHVar, justify = RIGHT).grid(row = 3, column = 2)
            self.time_inMVar = StringVar()
            Entry(frame, textvariable = self.time_inMVar, justify = RIGHT).grid(row = 4, column = 2)
            self.time_outHVar = StringVar()
            Entry(frame, textvariable = self.time_outHVar, justify = RIGHT).grid(row = 5, column = 2)
            self.time_outMVar = StringVar()
            Entry(frame, textvariable = self.time_outMVar, justify = RIGHT).grid(row = 6, column = 2)
            self.total_hoursVar = StringVar()
            Label(frame, textvariable = self.total_hoursVar).grid(row = 7, column = 2, sticky = E)
            self.total_minVar = StringVar()
            Label(frame, textvariable = self.total_minVar).grid(row = 8, column = 2, sticky = E)
            Entry(frame, justify = RIGHT).grid(row = 2, column = 4)
        
        
            Label(frame, text = "Total Hours", bg='blue', fg='white', font='Courier 25 bold').grid(row = 2, column = 3, sticky = W)
            Label(frame, text = "Domestic Hours", bg='blue', fg='white', font='Courier 25 bold').grid(row = 3, column = 3, sticky = W)
            Label(frame, text = "International Hours", bg='blue', fg='white', font='Courier 25 bold').grid(row = 4, column = 3, sticky = W)
            Label(frame, text = "Total Wage", bg='blue', fg='white', font='Courier 25 bold').grid(row = 5, column = 3, sticky = W)
            Entry(frame, justify = RIGHT).grid(row = 2, column = 2)

            self.total_hours2Var = StringVar()
            Entry(frame, textvariable = self.total_hours2Var, justify = RIGHT).grid(row = 2, column = 4)
            self.domestic_hoursVar = StringVar()
            Entry(frame, textvariable = self.domestic_hoursVar, justify = RIGHT).grid(row = 3, column = 4)
            self.international_hoursVar = StringVar()
            Entry(frame, textvariable = self.international_hoursVar, justify = RIGHT).grid(row = 4, column = 4)
            self.total_wageVar = StringVar()
            Label(frame, textvariable = self.total_wageVar).grid(row = 5, column = 4, sticky = E)
            Button(frame, text = "Compute Total Hours", command = self.computetotalhours).grid(row = 9, column = 2, sticky = E)
            Button(frame, text = "Compute Total Wage", command = self.computewage).grid(row = 6, column = 4, sticky = E)

        # button widget
        
        # This helps to remain the app opened until the user close it
            root.mainloop()
    def getflighthours(self,time_out, time_in):
        Total_hours = time_out - time_in 
        return Total_hours

    def getflightmin(self,min_in,min_out):
        Total_min = min_out - min_in
        return Total_min
  
    def computetotalhours(self):
        Total_hours = self.getflighthours(
            int(self.time_outHVar.get()),  
            int(self.time_inHVar.get()))
        
        Total_min = self.getflightmin(
                int(self.time_inMVar.get()),
                int(self.time_outMVar.get())
        )
    
        self.total_hoursVar.set(format(Total_hours))
        self.total_minVar.set(format(Total_min, ".1f"))

    def getwage(self, domestic, international):
            total_wage = domestic + international 
            print({total_wage})
            return total_wage

    def computewage(self):
        total_wage = self.getwage(
            float(self.domestic_hoursVar.get()) *43,
            float(self.international_hoursVar.get())*56)

        self.total_wageVar.set(format(total_wage, "10.2f"))
if __name__ == '__main__':
    App()