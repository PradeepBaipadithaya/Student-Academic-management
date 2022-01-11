from os import _exit
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
import PIL
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import mysql.connector



root =Tk()
root.title("Login Page")
root.configure(background='#EAF8F8')

def add_stud():
    
                                    
    selected = table_combo.get()
    num = num_combo.get()
    print(selected)
    print(num)

    add_student_frame1 = Frame(root)
    add_table_labels = Label(add_student_frame1,text="Selected attendence table :",font=('Lobster 30 bold'),pady=30)
    add_table_labels.grid(row=0, column=0)

    table_selected_labels = Label(add_student_frame1,text=selected,font=('Lobster 30 bold'),pady=30)
    table_selected_labels.grid(row=0, column=1)

    no_student_labels = Label(add_student_frame1,text="Select number of student",font=('Lobster 30 bold'),pady=30)
    no_student_labels.grid(row=1, column=0)

    no_student_labels = Label(add_student_frame1,text=num,font=('Lobster 30 bold'),pady=30)
    no_student_labels.grid(row=1, column=1)


    add_student_frame1.grid(row=0, column=0)
                    
                                    
mydb = mysql.connector.connect(buffered=True,#Used buffered because i am using fetchall and fetchall reqires its buffered  to be cleaned each time it iterates
    host = "localhost",
    user = "root",
    passwd = "pradeep",
    database ="attendence_book"
)

my_cursor = mydb.cursor()
                                    

                               
add_student_window = Toplevel()
add_student_window.title("Score")
add_student_window.geometry("800x600")
add_student_frame = Frame(add_student_window)
global num_student_entry
                                

querry_string="SELECT attendence_table_name FROM lecture_record WHERE ssid = %s"
my_cursor.execute(querry_string,('15cs101',))
records = my_cursor.fetchall()
data =['15cs101','sdaas']
num = list(range(1,101))
                                
for record in records:
    data = data + list(record)

table_labels = Label(add_student_frame,text="Select attendence table")
table_labels.grid(row=0, column=0)

# print(data)
table_cliked = StringVar()
table_cliked.set(data[0])
table_combo = ttk.Combobox(add_student_frame,value =data,font=('Lobster 14 bold'),width="20")
table_combo.current(0)
table_combo.grid(row=0, column=1, columnspan=20)

num_student_labels = Label(add_student_frame,text="Select number of student",font=('Lobster 30 bold'),pady=30)
num_student_labels.grid(row=1, column=0)

num_cliked = StringVar()
                                # num_cliked.set(num[1])
num_combo = ttk.Combobox(add_student_frame,value =num,font=('Lobster 14 bold'),width="20")
num_combo.current(0)
num_combo.grid(row=1, column=1, columnspan=20)

                                
submit_button = Button(add_student_frame,text="submit", pady=10, command=add_stud)
submit_button.grid(row=4,column=1)


add_student_frame.pack()


root.mainloop()


