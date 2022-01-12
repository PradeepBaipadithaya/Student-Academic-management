from tkinter import *
from tkcalendar import Calendar
from datetime import date
 
# Create Object
root = Tk()
 
# Set geometry
root.geometry("400x400")
 
t_year = int(date.today().strftime('%Y'))
t_month = int(date.today().strftime('%m'))
t_day = int(date.today().strftime('%d'))

# Add Calendar
cal = Calendar(root, selectmode = 'day',
               year = t_year, month = t_month,
               day = t_day)
 
cal.pack(pady = 20)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
Button(root, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
date = Label(root, text = "")
date.pack(pady = 20)
 
# Execute Tkinter
root.mainloop()