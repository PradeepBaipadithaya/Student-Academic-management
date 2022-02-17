from os import _exit
import re
from tkinter import *
from tkinter.font import Font
from turtle import right
from PIL import ImageTk,Image
import PIL
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import mysql.connector
from tkcalendar import Calendar
from datetime import date
import time

root =Tk()
root.title("Student Attendence Management")
root.configure(background='#EAF8F8')
root.iconbitmap("logo.ico")
Font_tuple = (("Comic Sans MS", 30, "bold"),("Island Moments",20,""))
mydb = mysql.connector.connect(buffered=True,#Used buffered because i am using fetchall and fetchall reqires its buffered  to be cleaned each time it iterates
    host = "localhost",
    user = "root",
    passwd = "pradeep",
    database ="attendence_book"
)

my_cursor = mydb.cursor()


def submit():
        if username_entry.get() == "" and password_entry.get() == "" :
            messagebox.showerror("Invalid","Please enter Username and Password")
        elif username_entry.get()=="":
            messagebox.showerror("Invalid","Please enter username")
        elif password_entry.get()=="":
            messagebox.showerror("Invalid","Please enter password")
        else:
            try:
                global login_frame
                usn_no = username_entry.get()
                password = password_entry.get()
                my_cursor = mydb.cursor()
                querry_string ="SELECT password,role,security_key FROM login WHERE usn = %s"
                my_cursor.execute(querry_string,(usn_no,))#Variables should be given with tuple
                record = my_cursor.fetchall()# gives tuple inside list
                if record[0][0]==password:
                    if record[0][2]==record[0][0]:
                        def submit():
                            if security_key_entry.get()=="" or new_passwd_entry.get()==""  or rewrite_passwd_entry.get()=="":
                                messagebox.showerror("Invalid","All fields are mandatory")

                            elif record[0][2]!=security_key_entry.get():
                                messagebox.showerror("Invalid","Security keyis not correct")

                            elif new_passwd_entry.get()!=rewrite_passwd_entry.get():
                                messagebox.showerror("Invalid","Password entered is not correct")

                            else:
                                my_cursor = mydb.cursor()
                                querry_string ="UPDATE login SET password =%s, security_key =NULL WHERE usn =%s"
                                my_cursor.execute(querry_string,(new_passwd_entry.get(),usn_no))
                                mydb.commit()
                                messagebox.showinfo("Successful","Password has updated")
                                exit()

                                
                                
                        global img
                        login_frame.destroy()
                        signup_frame = Frame(root,bg="white", height="500", width="1000")
                        signup_frame.pack(side=TOP, expand=YES)
                        img = ImageTk.PhotoImage(Image.open("SOC_Prog.png"))
                        pic_frame = Frame(signup_frame)
                        pic_label =Label(pic_frame,image=img)
                        pic_label.pack()
                        pic_frame.grid(row=0, column=0)


                        text_frame = Frame(signup_frame, bg="white")
                        password_label = Label(text_frame, text="Enter Password", font=Font_tuple[0], bg="white", fg="blue",pady=30, anchor=NW)
                        password_label.grid(row=0, column=0)

                        security_key_label =Label(text_frame,text="Security Key :",font=("'Lobster 25 "), bg="white", pady=15)
                        security_key_label.grid(row=1, column=0)

                        new_passwd_label =Label(text_frame,text="New Password :",font=("'Lobster 25 "), bg="white", pady=15)
                        new_passwd_label.grid(row=2, column=0)

                        rewrite_passwd_label =Label(text_frame,text="Re Enter Password :",font=("'Lobster 25 "), bg="white", pady=15)
                        rewrite_passwd_label.grid(row=3, column=0)

                        security_key_entry = Entry(text_frame, width=17,font=("Lobster 23 "),highlightthickness=2, highlightcolor = '#8fe0ce', cursor="hand2")
                        security_key_entry.grid(row=1, column=1,padx=10)

                        new_passwd_entry = Entry(text_frame, width=17,font=("Lobster 23 "),highlightthickness=2, highlightcolor = '#8fe0ce', cursor="hand2")
                        new_passwd_entry.grid(row=2, column=1,padx=10)

                        rewrite_passwd_entry = Entry(text_frame,show="*", width=17,font=("Lobster 23 "),highlightthickness=2, highlightcolor = '#8fe0ce', cursor="hand2")
                        rewrite_passwd_entry.grid(row=3, column=1,padx=10)

                        submit_button = Button(text_frame,text="Submit",font=("Lobster 17 bold "), bg="#1A73E8",fg ="#F9F2FA",highlightthickness=2, highlightcolor = 'red', cursor="hand2",command=submit)
                        submit_button.grid(row=5, column=1,padx=20,pady=25,ipadx=20,ipady=3)



                        text_frame.grid(row=0, column=1)

                       
                    else:

                        if record[0][1]=="L":
                            def add_student():                                                             
                                def add_stud():
                                    selected = table_combo.get()
                                    num = int(num_combo.get())
                                    def add_student():                                        
                                        value =[]
                                        try:
                                            count =0
                                            for entry_detail in entry_details:
                                                if entry_detail.get()=="":
                                                    count+=1
                                                
                                                else:
                                                    my_cursor.execute(f"ALTER TABLE {selected} ADD {entry_detail.get()} ENUM('p','a')")
                                                    entry_detail.delete(0,END)
                                            
                                                    mydb.commit()
                                            if count!=0:
                                                messagebox.showwarning("Invalid","Entered record are updated into database",parent =add_student_window)
                                            else:
                                                messagebox.showinfo("Added successfully","Record has been added to database",parent =add_student_window)
                                                add_student_window.destroy()
                                        except:
                                            messagebox.showwarning("Invalid","One or more record is/are already present",parent =add_student_window)

                                    add_student_frame.destroy()
                                    add_full_student_frame =Frame(add_student_window,bg="white")
                                    add_full_student_frame.pack(side=TOP,expand=YES)
                                    add_student_frame1 = Frame(add_full_student_frame,bg="white")
                                    add_student_frame2 = Frame(add_full_student_frame,bg="white")
                                    add_student_frame3 = Frame(add_full_student_frame,bg="white")

                                    value_label =Label(add_student_frame1,text="Enter Student Roll No.",font=("'Lobster 25 "), bg="white", pady=15)
                                    value_label.grid(row=0,column=0)

                                    i=0
                                    for i in range(0,num):
                                        name_labels = Label(add_student_frame2,text=f"Student {i+1}) ", font=('Lobster 15 bold'),pady=10,bg='white')
                                        name_labels.grid(row=i+3,column=0)

                                    entry_details=[]
                                    for iterator in range(0,num):
                                        my_entry = Entry(add_student_frame2, width="22", font=('Lobster 15 bold'),bg='white',highlightthickness=2,cursor="hand2")
                                        
                                        my_entry.grid(row=iterator+3, column=1)
                                        entry_details.append(my_entry)

                                    add_student_button =Button(add_student_frame3,text="Add Students",   command=add_student,font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                    add_student_button.grid(row=1, column=1,padx=20,pady=25,ipadx=15,ipady=5)

                                    add_student_frame1.grid(row=0, column=0)
                                    add_student_frame2.grid(row=1, column=0)
                                    add_student_frame3.grid(row=2, column=0)
  
                                add_student_window = Toplevel()
                                add_student_window.title("Add Student")
                                add_student_window.geometry("800x750")
                                add_student_window.iconbitmap("logo.ico")
                                add_student_window.configure(background='#EAF8F8')
                                add_student_frame = Frame(add_student_window,bg="white")
                                global num_student_entry
                                

                                querry_string="SELECT attendence_table_name FROM lecture_record WHERE ssid = %s"
                                my_cursor.execute(querry_string,(usn_no,))
                                records = my_cursor.fetchall()
                                data =[]
                                num = list(range(1,11))
                                
                                for record in records:
                                    data = data + list(record)

                                table_labels = Label(add_student_frame,text="Select attendence table",font=("'Lobster 25 "), bg="white", pady=15)
                                table_labels.grid(row=0, column=0)

                                
                                table_cliked = StringVar()
                                # table_cliked.set(data[0])

                                table_combo = ttk.Combobox(add_student_frame,value =data,font=('Lobster 14 bold'),width="20")
                                table_combo.current(0)
                                table_combo.grid(row=0, column=1, columnspan=20)

                                num_student_labels = Label(add_student_frame,text="Select number of student",font=("'Lobster 25 "), bg="white", pady=15)
                                num_student_labels.grid(row=1, column=0)

                                # num_cliked = StringVar()
                                # num_cliked.set(num[1])

                                num_combo = ttk.Combobox(add_student_frame,value =num,font=('Lobster 14 bold'),width="20")
                                num_combo.current(0)
                                num_combo.grid(row=1, column=1, columnspan=20)

                                

                                submit_button = Button(add_student_frame,text="submit",font=("Lobster 17 bold "), command=add_stud, bg="#1A73E8",fg ="#F9F2FA", cursor="hand2")
                                submit_button.grid(row=4,column=1,padx=20,pady=25,ipadx=20,ipady=3)


                                add_student_frame.pack(side=TOP,expand=YES)

                            def attn_records():
                                def view_attendence():
                                    selected=table_combo.get()
                                    view_attendence_frame.destroy()

                                    complete_frame = Frame(attendence_window,bg="#EAF8F8")
                                    complete_frame.pack(side=TOP,expand=YES)
                                    view_attendece_frame1 = Frame(complete_frame,bg="#EAF8F8")
                                    view_attendece_frame2 = Frame(complete_frame,bg="white")

                                    table_label = Label(view_attendece_frame1,text="Attendence table: ",font=('Lobster 15'),bg="#EAF8F8")
                                    table_label.grid(row=0, column=0)
                                    table_name_label = Label(view_attendece_frame1,text=f"{selected}",font=('Lobster 15'),bg="#EAF8F8")
                                    table_name_label.grid(row=0, column=1)

                                    my_tree = ttk.Treeview(view_attendece_frame2)
                                    my_tree['columns'] = ("USN","Total Class","Total Present","Pecentage")

                                    my_tree.column("#0",width=0,stretch=NO)
                                    # my_tree.column("Name",anchor=W,width=120)
                                    my_tree.column("USN",anchor=CENTER,width=120)
                                    my_tree.column("Total Class",anchor=CENTER,width=120)
                                    my_tree.column("Total Present",anchor=CENTER,width=120)
                                    my_tree.column("Pecentage",anchor=CENTER,width=120)

                                    my_tree.heading("#0",text="", anchor=W)
                                    # my_tree.heading("Name",text="Name", anchor=W)
                                    my_tree.heading("USN",text="USN", anchor=CENTER)
                                    my_tree.heading("Total Class",text="Total Class", anchor=CENTER)
                                    my_tree.heading("Total Present",text="Total Present", anchor=CENTER)
                                    my_tree.heading("Pecentage",text="Pecentage", anchor=CENTER)

                                    
                                    
                                    my_cursor.execute(f"SHOW COLUMNS FROM {selected}")
                                    # print(selected)
                                    record1 = my_cursor.fetchall()

                                    i=0
                                    usn_=[]
                            
                                    for records in record1:
                                        usn_.append(record1[i][0])
                                        i+=1

                                    
                                    usn_list =usn_[2:]
                                    # print(usn_)
                                    querry_list=[]
                                    result_list=[]
                                    i=0
                                    for usn in usn_list:
                                        result_list.append(usn)
                                        my_cursor.execute(f"SELECT COUNT(*) FROM {selected}")
                                        record2 =my_cursor.fetchall()
                                        # print(record2)
                                        # total_attendence_list =list(record2[0][0])
                                        result_list.append(record2[0][0])

                                        my_cursor.execute(f"SELECT COUNT(*) FROM {selected} WHERE {usn} ='p'")
                                        record3 =my_cursor.fetchall()
                                        # print(record2)
                                        # total_attendence_list =list(record3[0][0])
                                        result_list.append(record3[0][0])
                                        num = (record3[0][0]/record2[0][0])*100

                                        percentage =  '%.2f' % num
                                        result_list.append(percentage)
                                        result_tuple = tuple(result_list)
                                        # print(result_tuple)
                                        querry_list.insert(i,result_tuple)
                                        result_list.clear()

                                        i+=1
                                    
                                    j=0
                                    for query in querry_list:
                                        my_tree.insert(parent='',index='end',iid=j,text="",values=query)
                                        j+=1
                                    my_tree.pack()
                                    # print(querry_list)
                                    view_attendece_frame1.grid(row=0, column=0)
                                    view_attendece_frame2.grid(row=1, column=0)

                                attendence_window = Toplevel()
                                attendence_window.title("Attendence Record")
                                attendence_window.geometry("800x600")
                                attendence_window.iconbitmap("logo.ico")
                                attendence_window.config(background='#EAF8F8')
                                global view_attendence_frame

                                querry_string="SELECT attendence_table_name FROM lecture_record WHERE ssid = %s"
                                my_cursor.execute(querry_string,(usn_no,))
                                records = my_cursor.fetchall()
                                data=[]

                                for record in records:
                                    data = data + list(record)
                                

                                view_attendence_frame = Frame(attendence_window,bg="white")
                                view_attendence_frame.pack(side=TOP, expand=YES)
                                
                                table_labels = Label(view_attendence_frame,text="Select attendence table",font=("'Lobster 25 "), bg="white", pady=15)
                                table_labels.grid(row=0, column=0)

                                table_cliked = StringVar()

                                table_combo = ttk.Combobox(view_attendence_frame,value =data,font=('Lobster 14 bold'),width="20")
                                table_combo.current(0)
                                table_combo.grid(row=0, column=1, columnspan=20)

                                submit_button = Button(view_attendence_frame,text="View attendence",  command=view_attendence, font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                submit_button.grid(row=4,column=1,padx=20,pady=25,ipadx=15,ipady=4)

                                




                            def take_attn():

                                def take_attendence():
                                    selected = table_combo.get()
                                    def sel_cal():
                                        def ok():
                                            cal_entry.delete(0,END)
                                            cal_entry.insert(0,cal.get_date())
                                            cal_window.destroy()
                                        cal_window =Toplevel()
                                        cal_window.title("Calender")
                                        cal_window.geometry("400x300")
                                        cal_window.iconbitmap("logo.ico")
                                        cal_window.configure(background='#EAF8F8')

                                        t_year = int(date.today().strftime('%Y'))
                                        t_month = int(date.today().strftime('%m'))
                                        t_day = int(date.today().strftime('%d'))

                                        cal = Calendar(cal_window, selectmode = 'day',year = t_year, month= t_month,day = t_day)
                                        cal.pack(pady = 20)

                                        ok_button = Button(cal_window,text="Select",command=ok,font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                        ok_button.pack()
                                    # def sel_time():
                                    #     time_entry.delete(0,END)
                                    #     t_time = time.strftime("%H:%M:%S")
                                    #     time_entry.insert(0,t_time)

                                    def save_att():
                                        i=0
                                        value =[]
                                        try:
                                            for entry_detail in entry_details:
                                                    
                                                    if entry_detail.get()=="":
                                                        i+=1
                                                    else:                                           
                                                        value.insert(i,entry_detail.get())
                                                        i+=1
                                                
                                            value.insert(0,cal_entry.get())
                                            value.insert(1,time_combo.get())

                                            tuple_value = tuple(value)
                                            my_cursor.execute(f"INSERT INTO {selected} VALUES {tuple_value}")

                                            mydb.commit()
                                            # print(value)
                                            messagebox.showinfo("Added successfully","Attendence has been added to database",parent =take_attendence_window)
                                            take_attendence_window.destroy()

                                        except mysql.connector.errors.IntegrityError:
                                            messagebox.showwarning("Invalid","Attendance is already taken",parent =take_attendence_window)

                                        except mysql.connector.errors.DataError:
                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =take_attendence_window)

                                        except mysql.connector.errors.DatabaseError:
                                            messagebox.showwarning("Invalid","Attendance should be of for 'p' or 'a'",parent =take_attendence_window)



                                                
                                            

                                    take_attendence_frame.destroy()
                                    global cal_entry
                                    global time_entry
                                    time =[
                                        "9-10",
                                        "10-11",
                                        "11-12",
                                        "12-1",
                                        "2-3",
                                        "3-4"
                                    ]
                                    take_attendence_full_frame = Frame(take_attendence_window,bg ="white")
                                    take_attendence_full_frame.pack(side=TOP,expand=YES)
                                    take_attendence_frame1 = Frame(take_attendence_full_frame,bg ="white")
                                    cal_label =Label(take_attendence_frame1,text="Select date : ",font=("'Lobster 25 "), bg="white", pady=15)

                                    cal_label.grid(row=0,column=0)
                                    cal_entry =Entry(take_attendence_frame1, width="15",font=('Lobster 20 bold'),highlightthickness=2)
                                    cal_entry.grid(row=0, column=1)

                                    cal_button = Button(take_attendence_frame1,text="Select", command=sel_cal, font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                    cal_button.grid(row=0, column=2,padx=20,pady=25,ipadx=15,ipady=4)

                                    time_label = Label(take_attendence_frame1,text="Select Time :",font=("'Lobster 25 "), bg="white", pady=15)
                                    time_label.grid(row=1,column=0)

          
                                    time_combo = ttk.Combobox(take_attendence_frame1,value =time,font=("Lobster 20 "))
                                    time_combo.current(0)
                                    time_combo.grid(row=1, column=1, columnspan=20)

                                    take_attendence_frame2 = Frame(take_attendence_full_frame,bg="white")
                                    name_label =Label(take_attendence_frame2,text="USN",font=("'Lobster 25 "), bg="white", pady=15)

                                    name_label.grid(row=0,column=0)

                                    P_or_A_label =Label(take_attendence_frame2,text="P/A",font=("'Lobster 25 "), bg="white", pady=15)

                                    P_or_A_label.grid(row=0,column=1,sticky=E,ipadx=20)
                 
                                    my_cursor.execute(f"SHOW COLUMNS FROM {selected}")
                                    # print(selected)
                                    record = my_cursor.fetchall()
                                    # print(record)
                                    i=0
                                    usn_=[]
                            
                                    for records in record:
                                        usn_.append(record[i][0])
                                        i+=1

                                    # print(usn_)
                                    usn_list =usn_[2:]
                                    i=0

                                    for usn in usn_list:
                                        i+=1
                                        attn_usn_label = Label(take_attendence_frame2,text=f"{usn}",font=('Lobster 15 bold'),bg="white")
                                        attn_usn_label.grid(row=i,column=0,sticky=W)

                                    entry_details =[]

                                    for i in range(1,len(usn_list)+1):
                                        my_entry = Entry(take_attendence_frame2, width="10",font=('Lobster 15 bold'),bg="white",highlightthickness=2)
                                        my_entry.grid(row=i, column=1,sticky=E)
                                        entry_details.append(my_entry)

                                        
                                    take_attendence_frame3 = Frame(take_attendence_full_frame,bg="white")
                                    save_button = Button(take_attendence_frame3,text="Save",command=save_att, font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                    save_button.grid(row=0, column=2,padx=20,pady=25,ipadx=15,ipady=4)



                                    take_attendence_frame1.grid(row=0,column=0)

                                    take_attendence_frame2.grid(row=1,column=0)
                                    take_attendence_frame3.grid(row=2,column=0)
                                    # return
                                # x,y = 0,0
                                take_attendence_window = Toplevel()
                                take_attendence_window.title("Take Attendence")
                                take_attendence_window.geometry("800x600")
                                take_attendence_window.iconbitmap("logo.ico")
                                take_attendence_window.configure(background='#EAF8F8')

                                querry_string="SELECT attendence_table_name FROM lecture_record WHERE ssid = %s"
                                my_cursor.execute(querry_string,(usn_no,))
                                records = my_cursor.fetchall()
                                data=[]

                                for record in records:
                                    data = data + list(record)
                                

                                take_attendence_frame = Frame(take_attendence_window,bg="White")
                                take_attendence_frame.pack(side=TOP,expand=YES)
                                table_labels = Label(take_attendence_frame,text="Select attendence table  ",font=("'Lobster 25 "), bg="white", pady=15)
                                table_labels.grid(row=0, column=0)

                                table_cliked = StringVar()

                                table_combo = ttk.Combobox(take_attendence_frame,value =data,font=("Lobster 15 "))
                                table_combo.current(0)
                                table_combo.grid(row=0, column=1, columnspan=20)

                                submit_button = Button(take_attendence_frame,text="Take attendence", command=take_attendence,font=("Lobster 17 bold "),bg="#1A73E8",fg ="#F9F2FA", cursor="hand2")
                                submit_button.grid(row=4,column=1,padx=20,pady=25,ipadx=20,ipady=3)

                            login_frame.destroy()
                            querry_string = "SELECT name,ssid FROM lecture_details WHERE ssid =%s"
                            my_cursor.execute(querry_string,(usn_no,))
                            record = my_cursor.fetchall()

                            lecture_frame = Frame(root, height="800", width="1000",bg ="white")
                            lecture_frame.pack(side=TOP, expand=YES)

                            img = ImageTk.PhotoImage(Image.open(f"Photos\\{usn_no}.png"))
                            pic_frame = Frame(lecture_frame)
                            pic_label =Label(pic_frame,image=img,bg="white")
                            pic_label.pack()
                            pic_frame.grid(row=0, column=0)

                            text_frame = Frame(lecture_frame,bg="white")
                            L_username_label = Label(text_frame,text=f"Name : {record[0][0]}",font=("Lobster 25"), bg="white",pady=15)
                            L_username_label.grid(row=0, column=0,sticky=W)

                            lecture_label = Label(text_frame,text=f"Lecture id : {record[0][1]}", font=("Lobster 25 "), bg="white",pady=15)
                            lecture_label.grid(row=1, column=0,sticky=W)

                            funtionality_label = Label(text_frame,text="    Funtionality", font=('Lobster 30 '),bg="white",pady=20)
                            funtionality_label.grid(row=2, column=0,sticky=W)

                            text_frame.grid(row=1, column=0)

                            button_frame = Frame(lecture_frame,bg="white")

                            add_student_button = Button(button_frame,text="Add student",font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2", command=add_student)
                            add_student_button.grid(row=3,column=0,padx=20,pady=25,ipadx=50,ipady=8)

                            attn_records_button = Button(button_frame,text="Attendence Record",font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2", command=attn_records)
                            attn_records_button.grid(row=3,column=1,padx=20,pady=25,ipadx=15,ipady=8)

                            take_attn_button = Button(button_frame,text="Take Attendence",font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2", command=take_attn)
                            take_attn_button.grid(row=3,column=2,padx=20,pady=25,ipadx=15,ipady=8)

                            button_frame.grid(row=2, column=0)
                           

                        elif record[0][1] =="A":
                                                

                            def add_records():
                                add_records_window = Toplevel()
                                add_records_window.title("Add records")
                                add_records_window.geometry("600x800")
                                add_records_window.iconbitmap("logo.ico")
                                add_records_window.configure(background='#EAF8F8')
                                

                                def submit():
                                
                                    if var.get()==1 :
                                        if Sname_entry.get() =="" or Susn_entry.get() =="" or Saddress_entry.get()=="" or Ssem_entry.get()=="" or Ssection_entry.get()=="" or Semail_entry.get()=="" or Sphone_entry.get()=="" or Ssecret_key_entry.get()=="":
                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =add_records_window) 
                                        else:
                                            try:
                                                query_string = "INSERT IGNORE INTO login (usn,password,role,security_key) VALUES(%s, %s, %s, %s)"
                                                my_cursor.execute(query_string,(Susn_entry.get(),Ssecret_key_entry.get(),"S",Ssecret_key_entry.get()))

                                                

                                                query_string = "INSERT INTO student_details (name, usn, sem, sec, address, email, phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                                                value=(Sname_entry.get(),Susn_entry.get(),Ssem_entry.get(),Ssection_entry.get(),Saddress_entry.get(),Semail_entry.get(),Sphone_entry.get())
                                                my_cursor.execute(query_string,value)

                                                

                                                mydb.commit()
                                                image_path ="Photos"

                                                image = imagechoosen1.save(f"{image_path}\\{Susn_entry.get()}.png")
                                                response =messagebox.showinfo("Added successfully","Record has been added to database",parent =add_records_window)
                                                add_records_window.destroy()
                                                
                                                    
                                            except mysql.connector.errors.IntegrityError:
                                                messagebox.showerror("Invalid","Record already exists",parent = add_records_window)
                                            except mysql.connector.errors.DatabaseError:
                                                messagebox.showerror("Invalid","Class and phone number should be of integer type",parent = add_records_window)
                                                
                                            
                                


                                    elif var.get()==2:
                                        # print(2)
                                        if Lname_entry.get() =="" or Lusn_entry.get() =="" or  Lphone_entry.get()=="" or Lemail_entry.get()=="" or Laddress_entry.get()==""  or Lsecret_key_entry.get()=="":
                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =add_records_window) 
                                        else:
                                            try:
                                                query_string = "INSERT IGNORE INTO login (usn,password,role,security_key) VALUES(%s, %s, %s, %s)"
                                                my_cursor.execute(query_string,(Lusn_entry.get(),Lsecret_key_entry.get(),"L",Lsecret_key_entry.get()))

                                                mydb.commit()

                                                
                                                query_string = "INSERT INTO lecture_details (name, ssid, phone, email,address ) VALUES (%s, %s, %s, %s, %s)"
                                                value=(Lname_entry.get(),Lusn_entry.get(),Lphone_entry.get(),Lemail_entry.get(),Laddress_entry.get())
                                                my_cursor.execute(query_string,value)

                                                mydb.commit()
                                                image_path ="Photos"

                                                image = imagechoosen1.save(f"{image_path}\\{Lusn_entry.get()}.png")
                                                response =messagebox.showinfo("Added successfully","Record has been added to database",parent =add_records_window)
                                                add_records_window.destroy()
                                                
                                            except mysql.connector.errors.IntegrityError:
                                                messagebox.showerror("Invalid","Record already exists",parent = add_records_window)
                                            except mysql.connector.errors.DatabaseError:
                                                messagebox.showerror("Invalid","Class and phone number should be of integer type",parent = add_records_window)
                                                
                                


                                    elif var.get()==3:
                                        if Mname_entry.get() =="" or Musn_entry.get() =="" or  Mphone_entry.get()=="" or Memail_entry.get()=="" or Maddress_entry.get()=="" or Msecret_key_entry.get()=="" :
                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =add_records_window) 
                                        else:
                                            try:
                                                query_string = "INSERT IGNORE INTO login (usn,password,role,security_key) VALUES(%s, %s, %s, %s)"
                                                my_cursor.execute(query_string,(Musn_entry.get(),Msecret_key_entry.get(),"A",Msecret_key_entry.get()))

                                                mydb.commit()

                                                
                                                query_string = "INSERT INTO admin_details (name, aid, phone, email,address ) VALUES (%s, %s, %s, %s, %s)"
                                                value=(Mname_entry.get(),Musn_entry.get(),Mphone_entry.get(),Memail_entry.get(),Maddress_entry.get())
                                                my_cursor.execute(query_string,value)

                                                mydb.commit()
                                                image_path ="Photos"

                                                image = imagechoosen1.save(f"{image_path}\\{Musn_entry.get()}.png")
                                                response =messagebox.showinfo("Added successfully","Record has been added to database",parent =add_records_window)
                                                add_records_window.destroy()
                                                
                                            except mysql.connector.errors.IntegrityError:
                                                messagebox.showerror("Invalid","Record already exists",parent = add_records_window)
                                            except mysql.connector.errors.DatabaseError:
                                                messagebox.showerror("Invalid","Class and phone number should be of integer type",parent = add_records_window)
                                                
                                    
                                def add_photo():
                                    global photo
                                    global imagechoosen1
                                    pic_frame.filename = filedialog.askopenfilename(initialdir=r"C:\\Users\\user\\Pictures\\Usn_Photos",title = "Select Photo",filetypes=(("png file","*.png"),("All files","*.*")))

                                    imagechoosen =Image.open(pic_frame.filename)
                                    newsize=(200,250)
                                    imagechoosen1 = imagechoosen.resize(newsize)
                                    photo = ImageTk.PhotoImage(imagechoosen1)
                                    
                                    my_image_label = Label(pic_frame,image=photo).grid(row=0, column=0)
                                    

                                    
                                

                                add_details_frame = Frame(add_records_window, height="800", width="1000", bg="white")
                                add_details_frame.pack(side=TOP, expand=YES)

                                pic_frame = Frame(add_details_frame,height="250", width="200", bg="light blue")
                                add_photo_button = Button(pic_frame,text="Add Photo",command=add_photo, font=('Lobster 15 bold'))
                                add_photo_button.place(relx=0.5, rely=0.5, anchor=CENTER)
                                pic_frame.grid(row=0, column=0)

                                text_frame_header = Frame(add_details_frame,height="500", width="600", bg="white")

                                radio_frame = Frame(text_frame_header,bg="white")
                                def clicked(value):
                                    if(value==1):
                                        student_detais()
                                    elif (value==2):                                        
                                        lecture_details()
                                    elif (value==3):
                                        maintainer_details()
                                        
                                var = IntVar()
                                var.set("1")

                                student_radio_button = Radiobutton(radio_frame, text="Student",font=('Lobster 15 bold'),padx=10,variable=var, value=1,bg='white',pady=15,command=lambda:clicked(var.get())).grid(row=0, column=1)
                                lecture_radio_button = Radiobutton(radio_frame, text="Lecture", variable=var, value=2,font=('Lobster 15 bold'),padx=10,bg='white',pady=15,command=lambda:clicked(var.get())).grid(row=0, column=2)
                                maintainer_radio_button = Radiobutton(radio_frame, text="Maintainer", variable=var, value=3,font=('Lobster 15 bold'),padx=10,bg='white',pady=15,command=lambda:clicked(var.get())).grid(row=0, column=3)

                                radio_frame.grid(row=0,column=0)

                                def student_detais():
                                    global Sname_entry
                                    global Susn_entry
                                    global Ssem_entry
                                    global Ssection_entry
                                    global Saddress_entry
                                    global Semail_entry
                                    global Sphone_entry
                                    global Ssecret_key_entry

                                    global text_frame

                                    text_frame = Frame(text_frame_header,bg="white")
                                    Sname_label = Label(text_frame,text="Name", font=('Lobster 15 bold'),pady=10,bg='white')
                                    Sname_label.grid(row=1, column=0)
                                    Sname_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Sname_entry.grid(row=1, column=1)

                                    Susn_label = Label(text_frame,text="Roll No", font=('Lobster 15 bold'),pady=10,bg='white')
                                    Susn_label.grid(row=2, column=0)
                                    Susn_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Susn_entry.grid(row=2, column=1)

                                    Ssem_label = Label(text_frame,text="Class", font=('Lobster 15 bold'),pady=10,bg='white')
                                    Ssem_label.grid(row=3, column=0)

                                    Ssem_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Ssem_entry.grid(row=3, column=1)
                                    
                                    Ssection_label = Label(text_frame,text="Section", font=('Lobster 15 bold'),pady=10,bg='white')
                                    Ssection_label.grid(row=4, column=0)

                                    Ssection_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Ssection_entry.grid(row=4, column=1)


                                    Saddress_label = Label(text_frame,text="Address",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Saddress_label.grid(row=5, column=0)
                                    Saddress_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Saddress_entry.grid(row=5, column=1)

                                    Semail_label = Label(text_frame,text="Email",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Semail_label.grid(row=6, column=0)
                                    Semail_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Semail_entry.grid(row=6, column=1)


                                    Sphone_label = Label(text_frame,text="Phone",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Sphone_label.grid(row=7, column=0)
                                    Sphone_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Sphone_entry.grid(row=7, column=1)


                                    Ssecret_key_label = Label(text_frame,text="Secret key",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Ssecret_key_label.grid(row=8,column=0)
                                    Ssecret_key_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Ssecret_key_entry.grid(row=8, column=1)

                                    submit_button =Button(text_frame,text="Submit", command=submit, font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                    submit_button.grid(row=9, column=1,padx=20,pady=25,ipadx=15,ipady=4)

                                    text_frame.grid(row=1, column=0)


                                def lecture_details():
                                    global Lname_entry
                                    global Lusn_entry
                                    global Lphone_entry
                                    global Lemail_entry
                                    global Laddress_entry
                                    global text_frame
                                    global Lsecret_key_entry

                                    text_frame.destroy()
                                    text_frame = Frame(text_frame_header,bg="white")
                                    name_label = Label(text_frame,text="Name", font=('Lobster 15 bold'),pady=10,bg='white')
                                    name_label.grid(row=1, column=0)
                                    Lname_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Lname_entry.grid(row=1, column=1)

                                    usn_label = Label(text_frame,text="SSID", font=('Lobster 15 bold'),pady=10,bg='white')
                                    usn_label.grid(row=2, column=0)
                                    Lusn_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Lusn_entry.grid(row=2, column=1)
                                
                                    phone_label = Label(text_frame,text="Phone",font=('Lobster 15 bold'),pady=10,bg='white')
                                    phone_label.grid(row=3, column=0)
                                    Lphone_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Lphone_entry.grid(row=3, column=1)

                                    email_label = Label(text_frame,text="Email",font=('Lobster 15 bold'),pady=10,bg='white')
                                    email_label.grid(row=4, column=0)
                                    Lemail_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Lemail_entry.grid(row=4, column=1)
                                    
                                    address_label = Label(text_frame,text="Address",font=('Lobster 15 bold'),pady=10,bg='white')
                                    address_label.grid(row=5, column=0)
                                    Laddress_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Laddress_entry.grid(row=5, column=1)

                                    Lsecret_key_label = Label(text_frame,text="Secret key",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Lsecret_key_label.grid(row=6,column=0)
                                    Lsecret_key_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Lsecret_key_entry.grid(row=6, column=1)

                                    submit_button =Button(text_frame,text="Submit", command=submit, font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                    submit_button.grid(row=7, column=1,padx=20,pady=25,ipadx=15,ipady=4)

                                    text_frame.grid(row=1, column=0)

                                def maintainer_details():
                                    global Mname_entry
                                    global Musn_entry
                                    global Mphone_entry
                                    global Memail_entry
                                    global Maddress_entry
                                    global text_frame
                                    global Msecret_key_entry

                                    text_frame.destroy()
                                    text_frame = Frame(text_frame_header,bg="white")

                                    name_label = Label(text_frame,text="Name", font=('Lobster 15 bold'),pady=10,bg='white')
                                    name_label.grid(row=1, column=0)
                                    Mname_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Mname_entry.grid(row=1, column=1)

                                    usn_label = Label(text_frame,text="AID", font=('Lobster 15 bold'),pady=10,bg='white')
                                    usn_label.grid(row=2, column=0)
                                    Musn_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Musn_entry.grid(row=2, column=1)

                                    phone_label = Label(text_frame,text="Phone",font=('Lobster 15 bold'),pady=10,bg='white')
                                    phone_label.grid(row=3, column=0)
                                    Mphone_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Mphone_entry.grid(row=3, column=1)

                                    email_label = Label(text_frame,text="Email",font=('Lobster 15 bold'),pady=10,bg='white')
                                    email_label.grid(row=4, column=0)
                                    Memail_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Memail_entry.grid(row=4, column=1)
                                    
                                    address_label = Label(text_frame,text="Address",font=('Lobster 15 bold'),pady=10,bg='white')
                                    address_label.grid(row=5, column=0)
                                    Maddress_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Maddress_entry.grid(row=5, column=1)

                                    Msecret_key_label = Label(text_frame,text="Secret key",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Msecret_key_label.grid(row=6,column=0)
                                    Msecret_key_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'),highlightthickness=2, cursor="hand2")
                                    Msecret_key_entry.grid(row=6, column=1)

                                    submit_button =Button(text_frame,text="Submit", command=submit, font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                    submit_button.grid(row=7, column=1,padx=20,pady=25,ipadx=15,ipady=4)

                                    text_frame.grid(row=1, column=0)

                                text_frame_header.grid(row=1, column=0)
                                student_detais()

                            def alter_records():
                                def delete_record():
                                    entered_usn = reg_entry.get()
                                    if entered_usn=="":
                                        messagebox.showerror("Invalid","All fields are mandatory",parent =update_records_window)
                                    else:
                                        try: 
                                            query ="SELECT * FROM login WHERE usn=%s"  
                                            my_cursor.execute(query,(entered_usn,))
                                            if my_cursor.fetchall()==[]:
                                                messagebox.showerror("Invalid","Entered USN or SSID not exists!",parent =update_records_window)
                                            else:
                                                querry_string = "DELETE FROM login WHERE usn =%s"
                                                my_cursor.execute(querry_string,(entered_usn,))
                                                mydb.commit()
                                                
                                                messagebox.showinfo("Deleted successfully","Record has been deleted from database",parent =update_records_window)
                                                update_records_window.destroy()
                                        except:
                                            messagebox.showerror("Invalid","Entered USN or SSID not exists!",parent =update_records_window)


                                def update_record():
                                    entered_usn = reg_entry.get()
                                    if entered_usn=="":
                                        messagebox.showerror("Invalid","All fields are mandatory",parent =update_records_window)
                                    else:
                                        try:
                                            
                                            querry_string = "SELECT role FROM login WHERE usn =%s"
                                            my_cursor.execute(querry_string,(entered_usn,))
                                            record = my_cursor.fetchall()

                                            if record[0][0]=="L":
                                                global Lupdate_image
                                                
                                                usn_frame.destroy()
                                                def update():
                                                    
                                                    value=[]
                                                    i=0
                                                    for entry_detail in L_entry_details:
                                                        i+=1
                                                        if entry_detail.get()=="":
                                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =update_records_window)
                                                        else:
                                                            if i==2:
                                                                ssid =entry_detail.get()
                                                                value.append(entry_detail.get())
                                                            # print(entry_detail.get())
                                                            else:
                                                                value.append(entry_detail.get())
                                                    
                                                    value.append(ssid)
                                                    # print(value)
                                                    querry_string = "UPDATE lecture_details SET name=%s, ssid= %s, phone=%s, email=%s, address=%s WHERE ssid =%s"

                                                    my_cursor.execute(querry_string,tuple(value))

                                                    mydb.commit()
                                                    messagebox.showinfo("Update successfully","Record has been updated to database",parent =update_records_window)
                                                    update_records_window.destroy()

                                                querry_string = "SELECT name,ssid,phone,email,address FROM lecture_details WHERE ssid =%s"
                                                my_cursor.execute(querry_string,(entered_usn,))
                                                record = my_cursor.fetchall()
                                                update_entire_frame = Frame(update_records_window,bg ="white")
                                                update_entire_frame.pack(side=TOP, expand=YES)

                                                update_frame = Frame(update_entire_frame,bg ="white")
                                                photo_frame = Frame(update_entire_frame,bg ="white")
                                                Lupdate_image = ImageTk.PhotoImage(Image.open(f"Photos\\{record[0][1]}.png"))
                                            
                                                pic_label =Label(photo_frame,image=Lupdate_image,bg="white")
                                                pic_label.pack(side=TOP, expand=YES)

                                                lecture_details_labels =["Name","SSID","Phone","Email","Address"]

                                                i=1
                                                for label_details in lecture_details_labels:
                                                    my_label = Label(update_frame,text=f"{label_details}", font=('Lobster 15 bold'),pady=10,bg='white')
                                                    my_label.grid(row=i, column=0)
                                                    i+=1

                                                L_entry_details =[]
                                                for iterator in range(1,6):
                                                    my_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'),bg="white")
                                                    my_entry.insert(0,f"{record[0][iterator-1]}")
                                                    my_entry.grid(row=iterator, column=1)
                                                    L_entry_details.append(my_entry)

                                            
                                                update_button =Button(update_frame,text="Update",command=update,font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                                update_button.grid(row=6, column=1)
                                                photo_frame.grid(row=0,column=0)
                                                update_frame.grid(row=1,column=0)

                                            elif record[0][0]=="A":
                                                global Mupdate_image
                                                
                                                usn_frame.destroy()
                                                def update():
                                                    value=[]
                                                    i=0
                                                    for entry_detail in A_entry_details:
                                                        i+=1
                                                        if entry_detail.get()=="":
                                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =update_records_window)
                                                        else:
                                                            if i==2:
                                                                aid =entry_detail.get()
                                                                value.append(entry_detail.get())
                                                            # print(entry_detail.get())
                                                            else:
                                                                value.append(entry_detail.get())
                                                    
                                                    value.append(aid)
                                                    # print(value)
                                                
                                                    querry_string = "UPDATE admin_details SET name=%s, aid= %s, phone=%s, email=%s, address=%s WHERE aid =%s"
                                                    my_cursor.execute(querry_string,tuple(value))
                                                                                            
                                                    mydb.commit()
                                                    messagebox.showinfo("Update successfully","Record has been updated to database",parent =update_records_window)
                                                    update_records_window.destroy()

            
                                                querry_string = "SELECT name,aid,phone,email,address FROM admin_details WHERE aid =%s"
                                                my_cursor.execute(querry_string,(entered_usn,))
                                                record = my_cursor.fetchall()

                                                update_entire_frame = Frame(update_records_window,bg ="white")
                                                update_entire_frame.pack(side=TOP, expand=YES)

                                                update_frame = Frame(update_entire_frame,bg ="white")
                                                photo_frame = Frame(update_entire_frame,bg ="white")
                                                Mupdate_image = ImageTk.PhotoImage(Image.open(f"Photos\\{record[0][1]}.png"))
                                            
                                                pic_label =Label(photo_frame,image=Mupdate_image,bg="white")
                                                pic_label.pack(side=TOP, expand=YES)

                                                admin_details_labels =["Name","AID","Phone","Email","Address"]

                                                i=1
                                                for label_details in admin_details_labels:
                                                    my_label = Label(update_frame,text=f"{label_details}", font=('Lobster 15 bold'),pady=10,bg='white')
                                                    my_label.grid(row=i, column=0)
                                                    i+=1

                                                A_entry_details =[]
                                                for iterator in range(1,6):
                                                    my_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'),bg="white")
                                                    my_entry.insert(0,f"{record[0][iterator-1]}")
                                                    my_entry.grid(row=iterator, column=1)
                                                    A_entry_details.append(my_entry)

                                                
                                                update_button =Button(update_frame,text="Update",   command=update,font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                                update_button.grid(row=6, column=1)
                                                photo_frame.grid(row=0,column=0)
                                                update_frame.grid(row=1,column=0)

                                            if record[0][0]=="S":
                                                global Supdate_image
                                                
                                                usn_frame.destroy()
                                                def update():
                                                    value=[]
                                                    i=0
                                                    for entry_detail in S_entry_details:
                                                        i+=1
                                                        if entry_detail.get()=="":
                                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =update_records_window)
                                                        else:
                                                            if i==2:
                                                                usn =entry_detail.get()
                                                                value.append(entry_detail.get())
                                                            # print(entry_detail.get())
                                                            else:
                                                                value.append(entry_detail.get())
                                                    
                                                    value.append(usn)
                                                    # print(value)
                                                
                                                    querry_string = "UPDATE student_details SET name=%s, usn= %s, sem = %s, sec=%s, phone=%s, email=%s, address=%s WHERE usn =%s"
                                                        
                                                    my_cursor.execute(querry_string,tuple(value))

                                                    mydb.commit()
                                                    messagebox.showinfo("update successfully","Record has been updated to database",parent =update_records_window)
                                                    update_records_window.destroy()

            
                                                querry_string = "SELECT name,usn,sem,sec,phone,email,address FROM student_details WHERE usn =%s"
                                                my_cursor.execute(querry_string,(entered_usn,))
                                                record = my_cursor.fetchall()
                                                update_entire_frame = Frame(update_records_window,bg ="white")
                                                update_entire_frame.pack(side=TOP, expand=YES)

                                                update_frame = Frame(update_entire_frame,bg ="white")
                                                photo_frame = Frame(update_entire_frame,bg ="white")
                                                Supdate_image = ImageTk.PhotoImage(Image.open(f"Photos\\{record[0][1]}.png"))
                                            
                                                pic_label =Label(photo_frame,image=Supdate_image,bg="white")
                                                pic_label.pack(side=TOP, expand=YES)
                                                
                                                student_details_labels =["Name","USN","Sem","Section","Phone","Email","Address"]

                                                i=1
                                                for label_details in student_details_labels:
                                                    my_label = Label(update_frame,text=f"{label_details}", font=('Lobster 15 bold'),pady=10,bg='white')
                                                    my_label.grid(row=i, column=0)
                                                    i+=1

                                                S_entry_details =[]

                                                for iterator in range(1,8):
                                                    my_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'),bg="white")
                                                    my_entry.insert(0,f"{record[0][iterator-1]}")
                                                    my_entry.grid(row=iterator, column=1)
                                                    S_entry_details.append(my_entry)


                                                
                                                update_button =Button(update_frame,text="Update",   command=update,font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                                update_button.grid(row=8, column=1)
                                                photo_frame.grid(row=0,column=0)
                                                update_frame.grid(row=1,column=0)
                                        except:
                                            messagebox.showerror("Invalid","Entered USN or SSID not exists!",parent =update_records_window)
                                            



                                

                                update_records_window = Toplevel()
                                update_records_window.title("Alter records")
                                update_records_window.geometry("600x750")
                                update_records_window.iconbitmap("logo.ico")
                                update_records_window.configure(background='#EAF8F8')
                                

                                usn_frame = Frame(update_records_window,bg = "white")
                                
                                usn_label = Label(usn_frame,text="Enter Reg. ID", font=('Lobster 15 bold'),pady=10,bg='white',padx=10)
                                usn_label.grid(row=0, column=0)
                                reg_entry = Entry(usn_frame, width="17",font=('Lobster 20 bold'),highlightthickness=2,  cursor="hand2")
                                reg_entry.grid(row=0, column=1,padx=10)

                                

                                delete_button =Button(usn_frame,text="Delete", command=delete_record,font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                delete_button.grid(row=1, column=0,padx=20,pady=25,ipadx=15,ipady=4,sticky=E)
                                update_button =Button(usn_frame,text="Update", command=update_record,font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                update_button.grid(row=1, column=1,padx=20,pady=25,ipadx=15,ipady=4)
                                usn_frame.pack(side=TOP, expand=YES)
                                
                            def assign_lecture():
                                def submit():
                                    if ssid_entry.get()=="" or sem_entry.get()=="" or section_entry.get()=="" or subcode_entry.get()=="" :
                                        messagebox.showwarning("Invalid","All fields are mandatory",parent =add_subjects_window) 
                                    
                                    else:
                                        try:
                                            ssid = ssid_entry.get()
                                            querry_string ="SELECT role FROM login WHERE usn = %s"
                                            my_cursor.execute(querry_string,(ssid,))#Variables should be given with tuple
                                            
                                            record = my_cursor.fetchall()
                                            
                                            try:
                                                if record[0][0]!="L":
                                                    messagebox.showwarning("Invalid","Given SSID is not found to be of lecture",parent =add_subjects_window)
                                                else:
                                                    table_value = str(subcode_entry.get())+"_"+str(sem_entry.get())+"_"+str(section_entry.get())
                                                    query_string ="INSERT INTO lecture_record values(%s,%s,%s,%s,%s)"
                                                    value = (ssid_entry.get(),subcode_entry.get(),sem_entry.get(),section_entry.get(),table_value)
                                                    my_cursor.execute(query_string,value)

                                                    my_cursor.execute(f"""CREATE TABLE {table_value} (
                                                        Date varchar(20),
                                                        Time varchar(20),
                                                        primary key(Date,Time)
                                                    )
                                                    """)

                                                    mydb.commit()
                                                    messagebox.showinfo("Added successfully","Record has been added to database",parent =add_subjects_window)
                                                    add_subjects_window.destroy()

                                            except mysql.connector.errors.IntegrityError:
                                                messagebox.showerror("Invalid","Record is already present in database or Subject is not found",parent =add_subjects_window)

                                            except mysql.connector.errors.DatabaseError:
                                                messagebox.showwarning("Invalid","Class should be integer ",parent =add_subjects_window)
                                            
                                                
                                        except:
                                            messagebox.showwarning("Invalid","Given SSID is not found ",parent =add_subjects_window)



                                add_subjects_window = Toplevel()
                                add_subjects_window.title("Assign Lecture")
                                add_subjects_window.geometry("700x600")
                                add_subjects_window.iconbitmap("logo.ico")
                                add_subjects_window.configure(background='#EAF8F8')

                                ssid_frame = Frame(add_subjects_window,width="600", height="500",bg ="white")
                                ssid_frame.pack(side=TOP,expand=YES)
                                ssid_label = Label(ssid_frame,text="Enter SSID", font=('Lobster 15 bold'),pady=10,bg='white',padx=10)
                                ssid_label.grid(row=0, column=0)
                                ssid_entry = Entry(ssid_frame, width="17",font=('Lobster 20 bold'),bg="white")
                                ssid_entry.grid(row=0, column=1,padx=10)

                                sem_label = Label(ssid_frame,text="Class", font=('Lobster 15 bold'),pady=10,bg='white')
                                sem_label.grid(row=1, column=0)

                                sem_entry = Entry(ssid_frame, width="17",font=('Lobster 20 bold'),bg="white")
                                sem_entry.grid(row=1, column=1,padx=10)

                            
                                section_label = Label(ssid_frame,text="Section", font=('Lobster 15 bold'),pady=10,bg='white')
                                section_label.grid(row=2, column=0)
                                section_entry = Entry(ssid_frame, width="17",font=('Lobster 20 bold'),bg ="white")
                                section_entry.grid(row=2, column=1,padx=10)
                                
                                subcode_label = Label(ssid_frame,text="Subcode", font=('Lobster 15 bold'),pady=10,bg='white')
                                subcode_label.grid(row=3, column=0) 

                                subcode_entry = Entry(ssid_frame, width="17",font=('Lobster 20 bold'),bg="white")
                                subcode_entry.grid(row=3, column=1) 

                                submit_button =Button(ssid_frame,text="Submit", command=submit,font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2")
                                submit_button.grid(row=4, column=1,padx=20,pady=25,ipadx=15,ipady=4)

                            

                            login_frame.destroy()
                            querry_string = "SELECT name,aid FROM admin_details WHERE aid =%s"
                            my_cursor.execute(querry_string,(usn_no,))
                            record = my_cursor.fetchall()

                            maintainer_frame = Frame(root,bg="white",height="800", width="1000")
                            maintainer_frame.pack(side=TOP, expand=YES)

                            img = ImageTk.PhotoImage(Image.open(f"Photos\\{usn_no}.png"))
                            pic_frame = Frame(maintainer_frame)
                            pic_label =Label(pic_frame,image=img)
                            pic_label.pack()
                            pic_frame.grid(row=0, column=0)

                            text_frame = Frame(maintainer_frame,bg="white")
                            M_username_label = Label(text_frame,text=f"Name : {record[0][0]}", font=("Lobster 25 "), bg="white",pady=15)
                            M_username_label.grid(row=0, column=0,sticky=W)

                            # M_username_name_label = Label(text_frame,text=f"{record[0][0]}",font=("Lobster 25 bold"), bg="white",pady=15)
                            # M_username_name_label.grid(row=0, column=1,sticky=W)

                            maintainer_label = Label(text_frame,text=f"Admin id : {record[0][1]}",font=("Lobster 25"), bg="white",pady=15)
                            maintainer_label.grid(row=1, column=0,sticky=W)

                            # maintainer_id_label = Label(text_frame, text=f"{record[0][1]}",font=("Lobster 25  bold"), bg="white",pady=15)
                            # maintainer_id_label.grid(row=1, column=1,sticky=W)

                            funtionality_label = Label(text_frame,text="      Funtionality", font=('Lobster 30 '),bg="white",pady=20)
                            funtionality_label.grid(row=2, column=0,sticky=W)

                            text_frame.grid(row=1, column=0)

                            button_frame = Frame(maintainer_frame,bg="white")

                            add_records_button = Button(button_frame,text="Add records",font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2", command=add_records)
                            add_records_button.grid(row=3,column=0,padx=20,pady=25,ipadx=15,ipady=8)

                            update_records_button = Button(button_frame,text="Alter records",font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2",command=alter_records)
                            update_records_button.grid(row=3,column=1,padx=20,pady=25,ipadx=15,ipady=8)

                            add_subject_button = Button(button_frame,text="Assign Lecture",font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2", command=assign_lecture)
                            add_subject_button.grid(row=3,column=2,padx=20,pady=25,ipadx=15,ipady=8)
                            button_frame.grid(row=2, column=0)

                        elif record[0][1]== "S":

                            def view_attendence():
                                
                                view_attendence_window =Toplevel()
                                view_attendence_window.title("Attendence Record")
                                view_attendence_window.geometry("800x600")
                                view_attendence_window.iconbitmap("logo.ico")
                                view_attendence_window.configure(background='#EAF8F8')

                                student_frame1 = Frame(view_attendence_window,bg="#EAF8F8")
                                attendence_label = Label(student_frame1,text=f"Attendence Report", font=("Lobster 25 "), bg='#EAF8F8',pady=15)
                                attendence_label.grid(row=0, column=0,sticky=W)

                                my_tree = ttk.Treeview(student_frame1)
                                my_tree['columns'] = ("Subject Name","Total Class","Total Present","Pecentage")

                                my_tree.column("#0",width=0,stretch=NO)
                                    # my_tree.column("Name",anchor=W,width=120)
                                my_tree.column("Subject Name",anchor=CENTER,width=120)
                                my_tree.column("Total Class",anchor=CENTER,width=120)
                                my_tree.column("Total Present",anchor=CENTER,width=120)
                                my_tree.column("Pecentage",anchor=CENTER,width=120)

                                my_tree.heading("#0",text="", anchor=W)
                                    # my_tree.heading("Name",text="Name", anchor=W)
                                my_tree.heading("Subject Name",text="Subject Name", anchor=CENTER)
                                my_tree.heading("Total Class",text="Total Class", anchor=CENTER)
                                my_tree.heading("Total Present",text="Total Present", anchor=CENTER)
                                my_tree.heading("Pecentage",text="Pecentage", anchor=CENTER)

                                    

                                query="SELECT sem,sec FROM student_details WHERE usn =%s"
                                my_cursor.execute(query,(usn_no,))
                                record = my_cursor.fetchall()
                                sem = record[0][0]
                                sec = record[0][1]
                                query2="SELECT subcode,attendence_table_name FROM lecture_record WHERE sem =%s AND sec =%s"
                                my_cursor.execute(query2,(sem,sec))
                                record1 = my_cursor.fetchall()
                                subject =[]
                                subject_table =[]
                                #  list(record1[0][0])
                                for item in record1:                                   
                                        subject.append(item[0])                                    
                                        subject_table.append(item[1])

                                querry_list=[]
                                result_list=[]
                                i=0;
                                # print(subject_table)

                                for selected in subject_table:
                                    result_list.append(subject[i])
                                    my_cursor.execute(f"SELECT COUNT(*) FROM {selected}")
                                    record2 =my_cursor.fetchall()
                              
                                    result_list.append(record2[0][0])

                                    my_cursor.execute(f"SELECT COUNT(*) FROM {selected} WHERE {usn_no} ='p'")
                                    record3 =my_cursor.fetchall()
                                    # print(record2)
                            
                                    result_list.append(record3[0][0])

                                    num = (record3[0][0]/record2[0][0])*100
                                    percentage =  '%.2f' % num
                                    result_list.append(percentage)
                                    
                                    result_tuple = tuple(result_list)
                                    # print(result_tuple)
                                    querry_list.insert(i,result_tuple)
                                    result_list.clear()

                                    i+=1
                                j=0
                                for query in querry_list:
                                    my_tree.insert(parent='',index='end',iid=j,text="",values=query)
                                    j+=1
                                my_tree.grid(row=1,column=0) 

                                
                                student_frame1.pack(side=TOP,expand=YES)



                            login_frame.destroy()
                            querry_string = "SELECT name,usn FROM student_details WHERE usn =%s"
                            my_cursor.execute(querry_string,(usn_no,))
                            record = my_cursor.fetchall()

                            student_frame = Frame(root, height="800", width="1000",bg="white")
                            student_frame.pack(side=TOP, expand=YES)

                            img = ImageTk.PhotoImage(Image.open(f"Photos\\{usn_no}.png"))
                            pic_frame = Frame(student_frame)
                            pic_label =Label(pic_frame,image=img)
                            pic_label.pack()
                            pic_frame.grid(row=0, column=0)

                            text_frame = Frame(student_frame,bg="white")
                            L_username_label = Label(text_frame,text=f"Name : {record[0][0]}                    ", font=("Lobster 25 "), bg="white",pady=15)
                            L_username_label.grid(row=0, column=0,sticky=W)

                            usn_label = Label(text_frame,text=f"USN : {record[0][1]}", font=("Lobster 25 "), bg="white",pady=15)
                            usn_label.grid(row=1, column=0,sticky=W)

                            funtionality_label = Label(text_frame,text="Funtionality", font=('Lobster 30 '),bg="white",pady=20)
                            funtionality_label.grid(row=2, column=0,sticky=W)

                            text_frame.grid(row=1, column=0)

                            button_frame = Frame(student_frame,bg="white")

                            view_attendece_button = Button(button_frame,text="View attendece",font=("Lobster 15 bold "), bg="#1A73E8",fg ="white", cursor="hand2", command=view_attendence)
                            view_attendece_button.grid(row=3,column=0,padx=20,pady=25,ipadx=15,ipady=8)

                            button_frame.grid(row=2, column=0)

                else:
                    messagebox.showerror("Invalid","password not exists")
            except:
                messagebox.showerror("Invalid","Username not exists")



def show_login_frame():
    global username_entry
    global password_entry
    global img
    global login_frame
    global text_frame
        
    login_frame = Frame(root,bg="white", height="500", width="1000")
    login_frame.pack(side=TOP, expand=YES)
    img = ImageTk.PhotoImage(Image.open("Home_Prog.png"))
    pic_frame = Frame(login_frame)
    pic_label =Label(pic_frame,image=img)
    pic_label.pack()
    pic_frame.grid(row=0, column=0)


    text_frame = Frame(login_frame, bg="white")
    login_label = Label(text_frame, text="Log In", font=Font_tuple[0], bg="white", fg="#1dbcdd",pady=30, anchor=NW)
    login_label.grid(row=0, column=0)
    username_label =Label(text_frame,text="Username :",font=("Lobster 25 "), bg="white",pady=15)
    username_label.grid(row=1, column=0)
    

    password_label =Label(text_frame,text="Password :",font=("'Lobster 25 "), bg="white", pady=15)
    password_label.grid(row=3, column=0)

    username_entry = Entry(text_frame, width=17, font=("Lobster 23 "),highlightthickness=2, highlightcolor = '#8fe0ce', cursor="hand2")
    username_entry.grid(row=1, column=1,padx=10)

    password_entry = Entry(text_frame,show="*", width=17,font=("Lobster 23 "),highlightthickness=2, highlightcolor = '#8fe0ce', cursor="hand2")
    password_entry.grid(row=3, column=1,padx=10)

    submit_button = Button(text_frame,text="Submit",font=("Lobster 17 bold "), bg="#1A73E8",fg ="#F9F2FA",highlightthickness=2, highlightcolor = 'red', cursor="hand2",command=submit)
    submit_button.grid(row=5, column=1,padx=20,pady=25,ipadx=20,ipady=3)

        # sign_up_button = Button(text_frame,text="Sign up",bg="blue", fg="white",font=("Ubuntu 15"),command=sign_up)
        # sign_up_button.grid(row=5, column=0,padx=10)
    text_frame.grid(row=0, column= 1)


show_login_frame()
root.state("zoomed")

root.mainloop()

