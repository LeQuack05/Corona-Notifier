from tkinter import *
from scraping_vals import *
from tkinter import ttk


def all_loc():
    loc1=loc.get()
    scrapper(loc1,1)

def Cr():
    loc1=loc.get()
    scrapper(loc1,2)


screen_main=Tk()
screen_main.geometry("200x100")
screen_main.title('Corona Tracker')
Label(text="Enter Country").place(x=5,y=10)
screen_main.iconbitmap('corona.ico')
loc=StringVar()

Country = ttk.Combobox(screen_main, width = 27, textvariable = loc)
Country['values'] = ('US','India','Canada','Brazil', 'Russia','Spain','Argentina','Colombia','France','Peru',"Mexico",'uk',"South-Africa",'Iran','Chile','Italy','Iraq','Bangladesh','Germany','Indonesia','Philippines','Turkey','Saudi-Arabia','Pakistan','Ukraine','Israel','Netherlands','Belgium','Poland','Czechia','Canada') 
Country.current(1)
Country.grid(column = 1, row = 10)
Country.place(x=5,y=30)

Button(text="Total Report",command=all_loc).place(x=5,y=60)
Button(text="Current Report",command=Cr).place(x=100,y=60)

screen_main.mainloop()