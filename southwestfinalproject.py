'''
Program:    Southwest Pilot Flight Program 
Developer:  Sam Brown, Izaak Dittrich, & Viviance Nguyen
Date:       April 21, 2022
Purpose:    This application allows Southwest pilots to clock-in their flight, along with including hour 
            totals and corresponding wage based on hours inputed hours.
'''

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
        photo = PhotoImage(file='/Users/viviancenguyen/Downloads/help_linhtrang/labelxx.png')
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
        tkr.Label(main_frame, text="Month", bg='blue', fg='white', font='times 20 bold').grid(row=3, column=0, pady=10, sticky=W)


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
        month = Entry(main_frame, width=34, bg="white", textvariable=month).grid(row=3, column=1)
        monthSel = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December']
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


        def screen2():
            new_window = Toplevel(root)
            new_window.geometry('900x600')
            new_window.configure(bg='blue')
            new_window.title('Flight Hour and Wage Calculator!')
            photoLabel_frame = tkr.Frame(new_window)
            photoLabel_frame.pack()
            # Pass the path to the photo in your local computer here.
            #photo2 = PhotoImage(file='/Users/viviancenguyen/Downloads/help_linhtrang/labelxx.png')
            tkr.Label(photoLabel_frame, image=photo).grid(row=1, column=1)
            frame = tkr.Frame(new_window, bg='blue')
            frame.pack()

            Label(frame, text="Pilot ID", bg='blue', fg='white', font='times 16 bold').grid(row=2, column=1, pady = 15, padx =20, sticky=W)
            Label(frame, text="Calculate Below Using 24 Hour Time", bg='blue', fg='orange', font='times 16 bold').grid(row=3, column=1, pady = 15, padx =20, sticky=W)
            Label(frame, text="Time In (Hour)", bg='blue', fg='white', font='times 16 bold').grid(row=4, column=1,pady = 15,padx =20,sticky=W)                                                                                        
            Label(frame, text="Time In (Minute)", bg='blue', fg='white', font='times 16 bold').grid(row=5, column=1,pady = 15,padx =20,sticky=W)                                                                                          
            Label(frame, text="Time Out (Hour)", bg='blue', fg='white', font='times 16 bold').grid(row=6, column=1,pady = 15, padx =20,sticky=W)                                                                                            
            Label(frame, text="Time Out (Minute)", bg='blue', fg='white', font='times 16 bold').grid(row=7, column=1,pady = 15, padx =20,sticky=W)                                                                                               
            Label(frame, text="Total Hours", bg='blue', fg='white', font='times 16 bold').grid(row=8, column=1,pady = 15,padx =20,sticky=W)                                                                                     
            Label(frame, text="Total Minutes", bg='blue', fg='white', font='times 16 bold').grid(row=9, column=1,pady = 15,padx =20,sticky=W)


            time_inHVar = StringVar()
            Entry(frame, textvariable=time_inHVar, justify=RIGHT).grid(row=4, column=2, padx= 20)
            time_inMVar = StringVar()
            Entry(frame, textvariable=time_inMVar, justify=RIGHT).grid(row=5, column=2, padx=20)
            time_outHVar = StringVar()
            Entry(frame, textvariable=time_outHVar, justify=RIGHT).grid(row=6, column=2,padx =20)
            time_outMVar = StringVar()
            Entry(frame, textvariable=time_outMVar, justify=RIGHT).grid(row=7, column=2,padx =20)
            total_hoursVar = StringVar()
            Label(frame, textvariable=total_hoursVar,width=21).grid(row=8, column=2)
            total_minVar = StringVar()
            Label(frame, textvariable=total_minVar,width=21).grid(row=9, column=2)

            Entry(frame, justify=RIGHT).grid(row=2, column=4)

            Label(frame, text="Total Hours", bg='blue', fg='white', font='times 16 bold').grid(row=2, column=3,pady = 15, padx =15, sticky=E)                                                                                                
            Label(frame, text="Domestic Hours", bg='blue', fg='white', font='times 16 bold').grid(row=3, column=3,pady = 15, padx =15,sticky=E)                                                                                    
            Label(frame, text="International Hours", bg='blue', fg='white', font='times 16 bold').grid(row=4,column=3,pady = 15, padx =15,sticky=E)
            Label(frame, text="Total Wage", bg='blue', fg='white', font='times 16 bold').grid(row=5, column=3,pady = 15,padx =15,sticky=E)                                                                                  
            Entry(frame, justify=RIGHT).grid(row=2, column=2)

            total_hours2Var = StringVar()
            Entry(frame, textvariable=total_hours2Var, justify=RIGHT).grid(row=2, column=4)
            domestic_hoursVar = StringVar()
            Entry(frame, textvariable=domestic_hoursVar, justify=RIGHT).grid(row=3, column=4)
            international_hoursVar = StringVar()
            Entry(frame, textvariable=international_hoursVar, justify=RIGHT).grid(row=4, column=4)
            total_wageVar = StringVar()
            Label(frame, textvariable=total_wageVar,width=21).grid(row=5, column=4, sticky=E)

            # to help label the outputs
            total_hoursVar.set("Total Hours")
            total_minVar.set("Total Minuets")
            total_wageVar.set("Currency")

            # This helps to remain the app opened until the user close it

            def computetotalhours():
                Total_hours = int(time_outHVar.get()) - int(time_inHVar.get())
                Total_min = int(time_inMVar.get()) - int(time_outMVar.get())

                total_hoursVar.set(format(abs(Total_hours)))
                total_minVar.set(format(abs(Total_min)))

            def getwage(domestic, international):
                total_wage = domestic + international
                print({total_wage})
                return total_wage

            def computewage():
                total_wage = getwage(
                    float(domestic_hoursVar.get()) * 1075,
                    float(international_hoursVar.get()) * 1275)

                total_wageVar.set("${:,.2f}".format(total_wage))
                
            Button(frame, text="Compute Total Time", command=computetotalhours,fg= 'black',bg='blue',highlightbackground='orange',font='times 12 bold').grid(row=10, column=2, padx =30)
            Button(frame, text="Compute Total Wage", command=computewage,fg= 'black',bg='blue',highlightbackground='orange',font='times 12 bold').grid(row=6, column=4, padx= 30)
            Button(frame, text="Get More Information",fg= 'black',bg='blue',highlightbackground='red',font='times 12 bold').grid(row=10, column=1, padx= 30)
            Button(frame, text="Need Help?",fg= 'black',bg='blue',highlightbackground='red',font='times 12 bold').grid(row=6, column=3, padx= 30)


        tkr.Button(main_frame, text="Go Back", fg='black', bg='blue', highlightbackground='orange',
                font='times 18 bold').grid(row=4, column=1, pady=28, sticky=W)
        tkr.Button(main_frame, text="Clock In", command=lambda: [validation(), screen2()], fg='black', bg='blue',
                highlightbackground='orange', font='times 18 bold').grid(row=4, column=1, pady=28, sticky=E)
        tkr.Button(main_frame, text="Need help?", bg='blue', fg='black', highlightbackground='blue',
                font='times 15 bold').grid(row=5, column=2, pady=40, padx=15, sticky=E)

        root.mainloop()


if __name__ == '__main__':
    App()