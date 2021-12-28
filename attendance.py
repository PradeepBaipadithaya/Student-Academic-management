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
                    # print(record[0][2])
                    if record[0][2]==record[0][0]:
                        def submit():
                            if security_key_entry.get()=="" or new_passwd_entry.get()==""  or rewrite_passwd_entry.get()=="":
                                messagebox.showerror("Invalid","All fields are mandatory")

                            elif record[0][2]!=security_key_entry.get():
                                messagebox.showerror("Invalid","Security key has not reached")

                            elif new_passwd_entry.get()!=rewrite_passwd_entry.get():
                                messagebox.showerror("Invalid","Password entered is not correct")

                            else:
                                my_cursor = mydb.cursor()
                                querry_string ="UPDATE login SET password =%s WHERE usn =%s"
                                my_cursor.execute(querry_string,(new_passwd_entry.get(),usn_no))
                                mydb.commit()
                                messagebox.showinfo("Successful","Password has updated")

                                exit()
                                
                        global img
                        # print(record[0][2])
                        login_frame.destroy()
                        signup_frame = Frame(root,bg="white", height="500", width="1000")
                        signup_frame.pack(side=TOP, expand=YES)
                        img = ImageTk.PhotoImage(Image.open("SOC_Prog.png"))
                        pic_frame = Frame(signup_frame)
                        pic_label =Label(pic_frame,image=img)
                        pic_label.pack()
                        pic_frame.grid(row=0, column=0)


                        text_frame = Frame(signup_frame, bg="white")
                        password_label = Label(text_frame, text="Enter Password", font=('Lobster 30 bold'), bg="white", fg="blue",pady=30, anchor=NW)
                        password_label.grid(row=0, column=0)

                        security_key_label =Label(text_frame,text="Security Key :",font=("Ubuntu 20"), bg="white",pady=15)
                        security_key_label.grid(row=1, column=0)

                        new_passwd_label =Label(text_frame,text="New Password :",font=("Ubuntu 20"), bg="white",pady=15)
                        new_passwd_label.grid(row=2, column=0)

                        rewrite_passwd_label =Label(text_frame,text="Re Enter Password :",font=("Ubuntu 20"), bg="white", pady=15)
                        rewrite_passwd_label.grid(row=3, column=0)

                        security_key_entry = Entry(text_frame, width=20, font=("Ubuntu",20))
                        security_key_entry.grid(row=1, column=1,padx=10)

                        new_passwd_entry = Entry(text_frame, width=20, font=("Ubuntu",20))
                        new_passwd_entry.grid(row=2, column=1,padx=10)

                        rewrite_passwd_entry = Entry(text_frame,show="*", width=20,font=("Ubuntu",20))
                        rewrite_passwd_entry.grid(row=3, column=1,padx=10)

                        submit_button = Button(text_frame,text="Submit", bg="blue", fg="white",font=("Ubuntu 15"),command=submit)
                        submit_button.grid(row=5, column=1,padx=10)



                        text_frame.grid(row=0, column=1)
                       
                    else:

                        if record[0][1]=="L":


                            def fetchall():
                                fetchall_window = Toplevel()
                                fetchall_window.title("Score")
                                fetchall_window.geometry("800x600")
                                fetchall_frame = Frame(fetchall_window)
                                name_labels = Label(fetchall_frame,text="names of students",font=('Lobster 30 bold'),pady=30)
                                name_labels.grid(row=0, column=0)
                                fetchall_frame.pack()

                            def fetch_by_one():
                                attendence_window = Toplevel()
                                attendence_window.title("attendence")
                                attendence_window.geometry("800x600")

                                def take_attendence():
                                    pass
                                lecture_frame = Frame(attendence_window, height="800", width="1000")    
                                class_no = [
                                    "1 sem",
                                    "2 sem",
                                    "3 sem",
                                    "4 sem",
                                ]

                                section = [
                                    "A",
                                    "B"
                                ]


                                username_label = Label(lecture_frame,text="Name :", font=('Lobster 30 bold'),pady=30)
                                username_label.grid(row=1, column=0)

                                username_name_entry = Entry(lecture_frame, font=('Lobster 30 bold'))
                                username_name_entry.grid(row=1, column=1)

                                class_label = Label(lecture_frame,text="Enter class", font=('Lobster 30 bold'),pady=30)
                                class_label.grid(row=2, column=0)

                                class_cliked = StringVar()
                                class_cliked.set(class_no[0])

                                class_combo = ttk.Combobox(lecture_frame,value =class_no,font=('Lobster 14 bold'),width="20")
                                class_combo.current(0)
                                class_combo.bind("<<ComboboxSelected>>", selected)
                                class_combo.grid(row=2, column=1, columnspan=20)

                                section_label = Label(lecture_frame,text="Enter section :", font=('Lobster 30 bold'),pady=30)
                                section_label.grid(row=3, column=0)

                                section_clicked = StringVar()
                                section_clicked.set(section[0])

                                section_combo = ttk.Combobox(lecture_frame,value =section,font=('Lobster 14 bold'),width="20")
                                section_combo.current(0)
                                section_combo.bind("<<ComboboxSelected>>", selected)
                                section_combo.grid(row=3, column=1)

                                submit_username_button = Button(lecture_frame,text="submit", pady=10, command=take_attendence)
                                submit_username_button.grid(row=4,column=1)
                                lecture_frame.pack()
                                attendence_window.state("zoomed")

                            def take_attendance():
                                x,y = 0,0
                                take_attendence_window = Toplevel()
                                take_attendence_window.title("Take Attendence")
                                take_attendence_window.geometry("800x600")

                                student_name_label = Label(take_attendence_window,text="name")
                                student_name_label.grid(row=x,column=y)

                                student_name_entry = Entry(take_attendence_window,width=2)
                                student_name_entry.grid(row=x, column=y+1)


                            login_frame.destroy()
                            lecture_frame = Frame(root, height="800", width="1000")
                            lecture_frame.pack(side=TOP, expand=YES)
                            output_text ="Pradeep"
                            output_id = "pra123"

                            subcode_no =[
                                "18CS54",
                                "18CS44",
                                "18CS32"
                                

                            ]

                            class_no = [
                                    "1 sem",
                                    "2 sem",
                                    "3 sem",
                                    "4 sem",
                                ]

                            section = [
                                    "A",
                                    "B"
                                ]
                            def selected(event):
                                return
                            # img = ImageTk.PhotoImage(Image.open(f"Photos\\{usn_no}.png"))
                            # pic_frame = Frame(lecture_frame)
                            # pic_label =Label(pic_frame,image=img)
                            # pic_label.pack()
                            # pic_frame.grid(row=0, column=0)


                            text_frame = Frame(lecture_frame)
                            username_label = Label(text_frame,text="Name :", font=('Lobster 30 bold'),pady=30)
                            username_label.grid(row=0, column=0)

                            username_name_label = Label(text_frame,text=output_text, font=('Lobster 30 bold'), pady=30)
                            username_name_label.grid(row=0, column=1)

                            lecture_label = Label(text_frame,text="Employee ID:", font=('Lobster 30 bold'), pady=30)
                            lecture_label.grid(row=1, column=0)

                            lecture_id_label = Label(text_frame, text=output_id, font=('Lobster 30 bold'),pady=30)
                            lecture_id_label.grid(row=1, column=1)

                            funtionality_label = Label(text_frame,text="Funtionality", font=('Lobster 40 bold'),pady=30)
                            funtionality_label.grid(row=2, column=0)

                            class_label = Label(text_frame,text="Enter sem", font=('Lobster 30 bold'),pady=30)
                            class_label.grid(row=3, column=0)


                            class_cliked = StringVar()
                            class_cliked.set(class_no[0])

                            class_combo = ttk.Combobox(text_frame,value =class_no,font=('Lobster 14 bold'),width="20")
                            class_combo.current(0)
                            class_combo.bind("<<ComboboxSelected>>", selected)
                            class_combo.grid(row=3, column=1, columnspan=20)

                            section_label = Label(text_frame,text="Enter section :", font=('Lobster 30 bold'),pady=30)
                            section_label.grid(row=4, column=0)

                            section_clicked = StringVar()
                            section_clicked.set(section[0])

                            section_combo = ttk.Combobox(text_frame,value =section,font=('Lobster 14 bold'),width="20")
                            section_combo.current(0)
                            section_combo.bind("<<ComboboxSelected>>", selected)
                            section_combo.grid(row=4, column=1)

                            subcode_label = Label(text_frame,text="Enter subject code", font=('Lobster 30 bold'),pady=30)
                            subcode_label.grid(row=5, column=0)


                            subcode_cliked = StringVar()
                            subcode_cliked.set(class_no[0])

                            subcode_combo = ttk.Combobox(text_frame,value =subcode_no,font=('Lobster 14 bold'),width="20")
                            subcode_combo.current(0)
                            subcode_combo.bind("<<ComboboxSelected>>", selected)
                            subcode_combo.grid(row=5, column=1, columnspan=20)

                            text_frame.grid(row=1,column=0)                

                            button_frame = Frame(lecture_frame)
                            fetchall_button = Button(button_frame,text="Fetch all details",width="20",height ="3",bg="blue", command=fetchall)
                            fetchall_button.grid(row=6,column=0,padx=15)

                            fetch_by_one_button = Button(button_frame,text="Fetch by one",width="20",height ="3",bg="blue", command=fetch_by_one)
                            fetch_by_one_button.grid(row=6,column=1,padx=15)

                            take_attendance_button = Button(button_frame,text="Take attendance",width="20",height ="3",bg="blue", command=take_attendance)
                            take_attendance_button.grid(row=6,column=2,padx=15)
                            button_frame.grid(row=2, column=0)

                        elif record[0][1] =="M":
                                                
                            sem_no = list(range(1,9))

                            # section = [
                            #         "A",
                            #         "B"
                            #     ]
                            role =[
                                "Student",
                                "Lecture",
                                "Maintainer"
                            ]
                            subject_taken =[
                                "1",
                                "2",
                                "3"
                            ]
                            def add_records():
                                add_records_window = Toplevel()
                                add_records_window.title("Add records")
                                add_records_window.geometry("600x800")
                                add_records_window.configure(background='#EAF8F8')
                                

                                def submit():
                                
                                    if var.get()==1 :
                                        if Sname_entry.get() =="" or Susn_entry.get() =="" or Saddress_entry.get()=="" or Ssem_entry.get()=="" or Ssection_entry.get()=="" or Semail_entry.get()=="" or Sphone_entry.get()=="" or Ssecret_key_entry.get()=="":
                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =add_records_window) 
                                        else:
                                            try:
                                                query_string = "INSERT INTO login (usn,password,role,security_key) VALUES(%s, %s, %s, %s)"
                                                my_cursor.execute(query_string,(Susn_entry.get(),Ssecret_key_entry.get(),"S",Ssecret_key_entry.get()))

                                                mydb.commit()

                                                query_string = "INSERT INTO student_details (name, usn, sem, sec, address, email, phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                                                value=(Sname_entry.get(),Susn_entry.get(),Ssem_entry.get(),Ssection_entry.get(),Saddress_entry.get(),Semail_entry.get(),Sphone_entry.get())
                                                my_cursor.execute(query_string,value)

                                                

                                                mydb.commit()
                                                image_path ="C:\\Users\\pc\\Desktop\\Atten_all\\Photos"

                                                image = imagechoosen.save(f"{image_path}\\{Susn_entry.get()}.png")
                                                response =messagebox.showinfo("Added successfully","Record has been added to database",parent =add_records_window)
                                                add_records_window.destroy()
                                                
                                                    
                                            except:
                                                messagebox.showerror("Invalid","Record already exists",parent = add_records_window)
                                


                                    elif var.get()==2:
                                        # print(2)
                                        if Lname_entry.get() =="" or Lusn_entry.get() =="" or  Lphone_entry.get()=="" or Lemail_entry.get()=="" or Laddress_entry.get()==""  or Lsecret_key_entry.get()=="":
                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =add_records_window) 
                                        else:
                                            try:
                                                query_string = "INSERT INTO login (usn,password,role,security_key) VALUES(%s, %s, %s, %s)"
                                                my_cursor.execute(query_string,(Lusn_entry.get(),Lsecret_key_entry.get(),"L",Lsecret_key_entry.get()))

                                                mydb.commit()

                                                
                                                query_string = "INSERT INTO lecture_details (name, ssid, phone, email,address ) VALUES (%s, %s, %s, %s, %s)"
                                                value=(Lname_entry.get(),Lusn_entry.get(),Lphone_entry.get(),Lemail_entry.get(),Laddress_entry.get())
                                                my_cursor.execute(query_string,value)

                                                mydb.commit()
                                                image_path ="C:\\Users\\pc\\Desktop\\Atten_all\\Photos"

                                                image = imagechoosen.save(f"{image_path}\\{Lusn_entry.get()}.png")
                                                response =messagebox.showinfo("Added successfully","Record has been added to database",parent =add_records_window)
                                                add_records_window.destroy()
                                                
                                                    
                                            except:
                                                messagebox.showerror("Invalid","Record already exists",parent = add_records_window)
                                


                                    elif var.get()==3:
                                        if Mname_entry.get() =="" or Musn_entry.get() =="" or  Mphone_entry.get()=="" or Memail_entry.get()=="" or Maddress_entry.get()=="" or Msecret_key_entry.get()=="" :
                                            messagebox.showwarning("Invalid","All fields are mandatory",parent =add_records_window) 
                                        else:
                                            try:
                                                query_string = "INSERT INTO login (usn,password,role,security_key) VALUES(%s, %s, %s, %s)"
                                                my_cursor.execute(query_string,(Musn_entry.get(),Msecret_key_entry.get(),"M",Msecret_key_entry.get()))

                                                mydb.commit()

                                                
                                                query_string = "INSERT INTO admin_details (name, aid, phone, email,address ) VALUES (%s, %s, %s, %s, %s)"
                                                value=(Mname_entry.get(),Musn_entry.get(),Mphone_entry.get(),Memail_entry.get(),Maddress_entry.get())
                                                my_cursor.execute(query_string,value)

                                                mydb.commit()
                                                image_path ="C:\\Users\\pc\\Desktop\\Atten_all\\Photos"

                                                image = imagechoosen.save(f"{image_path}\\{Musn_entry.get()}.png")
                                                response =messagebox.showinfo("Added successfully","Record has been added to database",parent =add_records_window)
                                                add_records_window.destroy()
                                                
                                                    
                                            except:
                                                messagebox.showerror("Invalid","Record already exists",parent = add_records_window)
                                
                                    
                                def add_photo():
                                    global photo
                                    global imagechoosen
                                    pic_frame.filename = filedialog.askopenfilename(initialdir=r"C:\\Users\\pc\\Desktop\\Dbms\\USN_Photos",title = "Select Photo",filetypes=(("jpg file","*.jpg"),("All files","*.*")))

                                    imagechoosen =Image.open(pic_frame.filename)
                                    photo = ImageTk.PhotoImage(Image.open(pic_frame.filename))
                                    
                                    my_image_label = Label(pic_frame,image=photo).grid(row=0, column=0)
                                    

                                    
                                # def section_selected(event):
                                #     global section_click
                                #     section_click = section_cliked.get()
                                #     # return section_click
                                #     print(section_click)

                                # def class_selected(event):
                                #     global class_click
                                #     class_click = class_clicked.get()
                                #     # return class_click
                                #     print(class_click)



                                    

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
                                        # var.set("1")
                                        student_detais()
                                    elif (value==2):
                                        # var.set("2")
                                        
                                        lecture_details()
                                    elif (value==3):
                                        # var.set("3")
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
                                    Sname_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Sname_entry.grid(row=1, column=1)

                                    Susn_label = Label(text_frame,text="USN", font=('Lobster 15 bold'),pady=10,bg='white')
                                    Susn_label.grid(row=2, column=0)
                                    Susn_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Susn_entry.grid(row=2, column=1)

                                    Ssem_label = Label(text_frame,text="Sem", font=('Lobster 15 bold'),pady=10,bg='white')
                                    Ssem_label.grid(row=3, column=0)

                                    Ssem_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'))
                                    Ssem_entry.grid(row=3, column=1)

                                    # class_clicked = StringVar()
                                    # class_clicked.set(sem_no[0])

                                    # class_combo = ttk.Combobox(text_frame,value =sem_no,font=('Lobster 14 bold'),width="20")
                                    # class_combo.current(0)
                                    # class_combo.bind("<<ComboboxSelected>>", class_selected)
                                    # class_combo.grid(row=3, column=1, columnspan=20)

                                    

                                    Ssection_label = Label(text_frame,text="Section", font=('Lobster 15 bold'),pady=10,bg='white')
                                    Ssection_label.grid(row=4, column=0)

                                    Ssection_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'))
                                    Ssection_entry.grid(row=4, column=1)


                                    # section_cliked = StringVar()
                                    # section_cliked.set(section[0])

                                    # section_combo = ttk.Combobox(text_frame,value =section,font=('Lobster 14 bold'),width="20")
                                    # section_combo.current(0)
                                    # section_combo.bind("<<ComboboxSelected>>", section_selected)
                                    # section_combo.grid(row=4, column=1)

                                    Saddress_label = Label(text_frame,text="Address",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Saddress_label.grid(row=5, column=0)
                                    Saddress_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Saddress_entry.grid(row=5, column=1)

                                    Semail_label = Label(text_frame,text="Email",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Semail_label.grid(row=6, column=0)
                                    Semail_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Semail_entry.grid(row=6, column=1)


                                    Sphone_label = Label(text_frame,text="Phone",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Sphone_label.grid(row=7, column=0)
                                    Sphone_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Sphone_entry.grid(row=7, column=1)


                                    Ssecret_key_label = Label(text_frame,text="Secret key",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Ssecret_key_label.grid(row=8,column=0)
                                    Ssecret_key_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'))
                                    Ssecret_key_entry.grid(row=8, column=1)

                                    submit_button =Button(text_frame,text="Submit", command=submit, bg="light blue",width="25",height ="3")
                                    submit_button.grid(row=9, column=1)

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
                                    Lname_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Lname_entry.grid(row=1, column=1)

                                    usn_label = Label(text_frame,text="SSID", font=('Lobster 15 bold'),pady=10,bg='white')
                                    usn_label.grid(row=2, column=0)
                                    Lusn_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Lusn_entry.grid(row=2, column=1)
                                
                                    phone_label = Label(text_frame,text="Phone",font=('Lobster 15 bold'),pady=10,bg='white')
                                    phone_label.grid(row=3, column=0)
                                    Lphone_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Lphone_entry.grid(row=3, column=1)

                                    email_label = Label(text_frame,text="Email",font=('Lobster 15 bold'),pady=10,bg='white')
                                    email_label.grid(row=4, column=0)
                                    Lemail_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Lemail_entry.grid(row=4, column=1)
                                    
                                    address_label = Label(text_frame,text="Address",font=('Lobster 15 bold'),pady=10,bg='white')
                                    address_label.grid(row=5, column=0)
                                    Laddress_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Laddress_entry.grid(row=5, column=1)

                                    Lsecret_key_label = Label(text_frame,text="Secret key",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Lsecret_key_label.grid(row=6,column=0)
                                    Lsecret_key_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'))
                                    Lsecret_key_entry.grid(row=6, column=1)

                                    submit_button =Button(text_frame,text="Submit", command=submit, bg="light blue",width="25",height ="3")
                                    submit_button.grid(row=7, column=1)

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
                                    Mname_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Mname_entry.grid(row=1, column=1)

                                    usn_label = Label(text_frame,text="MID", font=('Lobster 15 bold'),pady=10,bg='white')
                                    usn_label.grid(row=2, column=0)
                                    Musn_entry = Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Musn_entry.grid(row=2, column=1)

                                    phone_label = Label(text_frame,text="Phone",font=('Lobster 15 bold'),pady=10,bg='white')
                                    phone_label.grid(row=3, column=0)
                                    Mphone_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Mphone_entry.grid(row=3, column=1)

                                    email_label = Label(text_frame,text="Email",font=('Lobster 15 bold'),pady=10,bg='white')
                                    email_label.grid(row=4, column=0)
                                    Memail_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Memail_entry.grid(row=4, column=1)
                                    
                                    address_label = Label(text_frame,text="Address",font=('Lobster 15 bold'),pady=10,bg='white')
                                    address_label.grid(row=5, column=0)
                                    Maddress_entry =Entry(text_frame, width="22",font=('Lobster 15 bold'))
                                    Maddress_entry.grid(row=5, column=1)

                                    Msecret_key_label = Label(text_frame,text="Secret key",font=('Lobster 15 bold'),pady=10,bg='white')
                                    Msecret_key_label.grid(row=6,column=0)
                                    Msecret_key_entry = Entry(text_frame,width="22",font=('Lobster 15 bold'))
                                    Msecret_key_entry.grid(row=6, column=1)

                                    submit_button =Button(text_frame,text="Submit", command=submit, bg="light blue",width="25",height ="3")
                                    submit_button.grid(row=7, column=1)

                                    text_frame.grid(row=1, column=0)

                                text_frame_header.grid(row=1, column=0)
                                student_detais()

                            def update_records():
                                def submit():
                                    try:
                                        entered_usn = usn_entry.get()
                                        querry_string = "SELECT role FROM login WHERE usn =%s"
                                        my_cursor.execute(querry_string,(entered_usn,))
                                        record = my_cursor.fetchall()
                                        if record[0][0]=="L":
                                            global Lupdate_image
                                            
                                            usn_frame.destroy()
                                            def update():
                                                if L_update_name_entry.get()=="" or L_update_name_entry.get()=="" or L_update_usn_entry.get()=="" or L_update_phone_entry.get()=="" or L_update_email_entry.get()=="" or L_update_address_entry.get()=="" :
                                                    messagebox.showwarning("Invalid","All fields are mandatory",parent =update_records_window)

                                                else:
                                                    querry_string = "UPDATE lecture_details SET name=%s, ssid= %s, phone=%s, email=%s, address=%s WHERE ssid =%s"
                                                    values = (L_update_name_entry.get(),L_update_usn_entry.get(),L_update_phone_entry.get(),L_update_email_entry.get(),L_update_address_entry.get(),L_update_usn_entry.get())

                                                    my_cursor.execute(querry_string,values)

                                                    mydb.commit()
                                                    messagebox.showinfo("Added successfully","Record has been added to database",parent =update_records_window)
                                                    update_records_window.destroy()

         
                                            querry_string = "SELECT name,ssid,phone,email,address FROM lecture_details WHERE ssid =%s"
                                            my_cursor.execute(querry_string,(entered_usn,))
                                            record = my_cursor.fetchall()

                                            update_frame = Frame(update_records_window)
                                            Lupdate_image = ImageTk.PhotoImage(Image.open(f"Photos\\{record[0][1]}.png"))
                                        
                                            pic_label =Label(update_frame,image=Lupdate_image)
                                            pic_label.grid(row=0, column=0)

                                            name_label = Label(update_frame,text="Name", font=('Lobster 15 bold'),pady=10,bg='white')
                                            name_label.grid(row=1, column=0)
                                            L_update_name_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            L_update_name_entry.insert(0,f"{record[0][0]}")
                                            L_update_name_entry.grid(row=1, column=1)

                                            usn_label = Label(update_frame,text="SSID", font=('Lobster 15 bold'),pady=10,bg='white')
                                            usn_label.grid(row=2, column=0)
                                            L_update_usn_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            L_update_usn_entry.insert(0,f"{record[0][1]}")
                                            L_update_usn_entry.grid(row=2, column=1)
                                
                                            phone_label = Label(update_frame,text="Phone",font=('Lobster 15 bold'),pady=10,bg='white')
                                            phone_label.grid(row=3, column=0)
                                            L_update_phone_entry =Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            L_update_phone_entry.insert(0,f"{record[0][2]}")
                                            L_update_phone_entry.grid(row=3, column=1)

                                            email_label = Label(update_frame,text="Email",font=('Lobster 15 bold'),pady=10,bg='white')
                                            email_label.grid(row=4, column=0)
                                            L_update_email_entry =Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            L_update_email_entry.insert(0,f"{record[0][3]}")
                                            L_update_email_entry.grid(row=4, column=1)
                                    
                                            address_label = Label(update_frame,text="Address",font=('Lobster 15 bold'),pady=10,bg='white')
                                            address_label.grid(row=5, column=0)
                                            L_update_address_entry =Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            L_update_address_entry.insert(0,f"{record[0][4]}")
                                            L_update_address_entry.grid(row=5, column=1)

                                            update_button =Button(update_frame,text="Update",   command=update, bg="light blue",width="25",height ="3")
                                            update_button.grid(row=6, column=1)
                                            update_frame.grid(row=0,column=0)

                                        elif record[0][0]=="M":
                                            global Mupdate_image
                                            
                                            usn_frame.destroy()
                                            def update():
                                                if M_update_name_entry.get()=="" or M_update_name_entry.get()=="" or M_update_usn_entry.get()=="" or M_update_phone_entry.get()=="" or M_update_email_entry.get()=="" or M_update_address_entry.get()=="" :
                                                    messagebox.showwarning("Invalid","All fields are mandatory",parent =update_records_window)

                                                else:
                                                    querry_string = "UPDATE admin_details SET name=%s, aid= %s, phone=%s, email=%s, address=%s WHERE aid =%s"
                                                    values = (M_update_name_entry.get(),M_update_usn_entry.get(),M_update_phone_entry.get(),M_update_email_entry.get(),M_update_address_entry.get(),M_update_usn_entry.get())

                                                    my_cursor.execute(querry_string,values)

                                                    mydb.commit()
                                                    messagebox.showinfo("Added successfully","Record has been added to database",parent =update_records_window)
                                                    update_records_window.destroy()

         
                                            querry_string = "SELECT name,aid,phone,email,address FROM admin_details WHERE aid =%s"
                                            my_cursor.execute(querry_string,(entered_usn,))
                                            record = my_cursor.fetchall()

                                            update_frame = Frame(update_records_window)
                                            Mupdate_image = ImageTk.PhotoImage(Image.open(f"Photos\\{record[0][1]}.png"))
                                        
                                            pic_label =Label(update_frame,image=Mupdate_image)
                                            pic_label.grid(row=0, column=0)

                                            name_label = Label(update_frame,text="Name", font=('Lobster 15 bold'),pady=10,bg='white')
                                            name_label.grid(row=1, column=0)
                                            M_update_name_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            M_update_name_entry.insert(0,f"{record[0][0]}")
                                            M_update_name_entry.grid(row=1, column=1)

                                            usn_label = Label(update_frame,text="AID", font=('Lobster 15 bold'),pady=10,bg='white')
                                            usn_label.grid(row=2, column=0)
                                            M_update_usn_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            M_update_usn_entry.insert(0,f"{record[0][1]}")
                                            M_update_usn_entry.grid(row=2, column=1)
                                
                                            phone_label = Label(update_frame,text="Phone",font=('Lobster 15 bold'),pady=10,bg='white')
                                            phone_label.grid(row=3, column=0)
                                            M_update_phone_entry =Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            M_update_phone_entry.insert(0,f"{record[0][2]}")
                                            M_update_phone_entry.grid(row=3, column=1)

                                            email_label = Label(update_frame,text="Email",font=('Lobster 15 bold'),pady=10,bg='white')
                                            email_label.grid(row=4, column=0)
                                            M_update_email_entry =Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            M_update_email_entry.insert(0,f"{record[0][3]}")
                                            M_update_email_entry.grid(row=4, column=1)
                                    
                                            address_label = Label(update_frame,text="Address",font=('Lobster 15 bold'),pady=10,bg='white')
                                            address_label.grid(row=5, column=0)
                                            M_update_address_entry =Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            M_update_address_entry.insert(0,f"{record[0][4]}")
                                            M_update_address_entry.grid(row=5, column=1)

                                            update_button =Button(update_frame,text="Update",   command=update, bg="light blue",width="25",height ="3")
                                            update_button.grid(row=6, column=1)
                                            update_frame.grid(row=0,column=0)

                                        if record[0][0]=="S":
                                            global Supdate_image
                                            
                                            usn_frame.destroy()
                                            def update():
                                                if S_update_name_entry.get()=="" or S_update_name_entry.get()=="" or S_update_usn_entry.get()=="" or S_update_sem_entry.get()=="" or S_update_section_entry.get()=="" or S_update_phone_entry.get()=="" or S_update_email_entry.get()=="" or S_update_address_entry.get()=="" :
                                                    messagebox.showwarning("Invalid","All fields are mandatory",parent =update_records_window)

                                                else:
                                                    querry_string = "UPDATE student_details SET name=%s, usn= %s, sem = %s, sec=%s, phone=%s, email=%s, address=%s WHERE usn =%s"
                                                    values = (S_update_name_entry.get(),S_update_usn_entry.get(),S_update_sem_entry.get(),S_update_section_entry.get(),S_update_phone_entry.get(),S_update_email_entry.get(),S_update_address_entry.get(),S_update_usn_entry.get())

                                                    my_cursor.execute(querry_string,values)

                                                    mydb.commit()
                                                    messagebox.showinfo("Added successfully","Record has been added to database",parent =update_records_window)
                                                    update_records_window.destroy()

         
                                            querry_string = "SELECT name,usn,sem,sec,phone,email,address FROM student_details WHERE usn =%s"
                                            my_cursor.execute(querry_string,(entered_usn,))
                                            record = my_cursor.fetchall()

                                            update_frame = Frame(update_records_window)
                                            Supdate_image = ImageTk.PhotoImage(Image.open(f"Photos\\{record[0][1]}.png"))
                                        
                                            pic_label =Label(update_frame,image=Supdate_image)
                                            pic_label.grid(row=0, column=0)

                                            name_label = Label(update_frame,text="Name", font=('Lobster 15 bold'),pady=10,bg='white')
                                            name_label.grid(row=1, column=0)
                                            S_update_name_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            S_update_name_entry.insert(0,f"{record[0][0]}")
                                            S_update_name_entry.grid(row=1, column=1)

                                            usn_label = Label(update_frame,text="SSID", font=('Lobster 15 bold'),pady=10,bg='white')
                                            usn_label.grid(row=2, column=0)
                                            S_update_usn_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            S_update_usn_entry.insert(0,f"{record[0][1]}")
                                            S_update_usn_entry.grid(row=2, column=1)

                                            sem_label = Label(update_frame,text="Sem", font=('Lobster 15 bold'),pady=10,bg='white')
                                            sem_label.grid(row=3, column=0)
                                            S_update_sem_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            S_update_sem_entry.insert(0,f"{record[0][2]}")
                                            S_update_sem_entry.grid(row=3, column=1)

                                            section_label = Label(update_frame,text="Section", font=('Lobster 15 bold'),pady=10,bg='white')
                                            section_label.grid(row=4, column=0)
                                            S_update_section_entry = Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            S_update_section_entry.insert(0,f"{record[0][3]}")
                                            S_update_section_entry.grid(row=4, column=1)
                                
                                            phone_label = Label(update_frame,text="Phone",font=('Lobster 15 bold'),pady=10,bg='white')
                                            phone_label.grid(row=5, column=0)
                                            S_update_phone_entry =Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            S_update_phone_entry.insert(0,f"{record[0][4]}")
                                            S_update_phone_entry.grid(row=5, column=1)

                                            email_label = Label(update_frame,text="Email",font=('Lobster 15 bold'),pady=10,bg='white')
                                            email_label.grid(row=6, column=0)
                                            S_update_email_entry =Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            S_update_email_entry.insert(0,f"{record[0][5]}")
                                            S_update_email_entry.grid(row=6, column=1)
                                    
                                            address_label = Label(update_frame,text="Address",font=('Lobster 15 bold'),pady=10,bg='white')
                                            address_label.grid(row=7, column=0)
                                            S_update_address_entry =Entry(update_frame, width="22",font=('Lobster 15 bold'))
                                            S_update_address_entry.insert(0,f"{record[0][6]}")
                                            S_update_address_entry.grid(row=7, column=1)

                                            update_button =Button(update_frame,text="Update",   command=update, bg="light blue",width="25",height ="3")
                                            update_button.grid(row=8, column=1)
                                            update_frame.grid(row=0,column=0)
                                    except:
                                        messagebox.showerror("Invalid","Entered USN or SSID not exists!")



                                

                                update_records_window = Toplevel()
                                update_records_window.title("Update records")
                                update_records_window.geometry("600x800")
                                update_records_window.configure(background='#EAF8F8')
                                

                                usn_frame = Frame(update_records_window)
                                usn_label = Label(usn_frame,text="Enter USN or SSID", font=('Lobster 15 bold'),pady=10,bg='white',padx=10)
                                usn_label.grid(row=0, column=0)
                                usn_entry = Entry(usn_frame, width="17",font=('Lobster 20 bold'))
                                usn_entry.grid(row=0, column=1,padx=10)

                                

                                submit_button =Button(usn_frame,text="Submit", command=submit, bg="light blue",width="25",height ="3")
                                submit_button.grid(row=1, column=1)
                                usn_frame.pack()
                                
                            def add_subjects():
                                def submit():
                                    return

                                add_subjects_window = Toplevel()
                                add_subjects_window.title("Update records")
                                add_subjects_window.geometry("700x600")
                                add_subjects_window.configure(background='#EAF8F8')

                                usn_frame = Frame(add_subjects_window,width="600", height="500")
                                usn_frame.pack(side=RIGHT,expand=YES)
                                usn_label = Label(usn_frame,text="Enter USN or SSID", font=('Lobster 15 bold'),pady=10,bg='white',padx=10)
                                usn_label.grid(row=0, column=0)
                                usn_entry = Entry(usn_frame, width="17",font=('Lobster 20 bold'))
                                usn_entry.grid(row=0, column=1,padx=10)

                                sem_label = Label(usn_frame,text="Sem", font=('Lobster 15 bold'),pady=10,bg='white')
                                sem_label.grid(row=1, column=0)

                                def selected(self):
                                    return
                                sem_cliked = StringVar()
                                sem_cliked.set(sem_no[0])

                                sem_combo = ttk.Combobox(usn_frame,value =sem_no,font=('Lobster 14 bold'),width="20")
                                sem_combo.current(0)
                                sem_combo.bind("<<ComboboxSelected>>", selected)
                                sem_combo.grid(row=1, column=1, columnspan=20)

                                section_label = Label(usn_frame,text="Section", font=('Lobster 15 bold'),pady=10,bg='white')
                                section_label.grid(row=2, column=0)

                                sec_clicked = StringVar()
                                sec_clicked.set(section[0])

                                sec_combo = ttk.Combobox(usn_frame,value =section,font=('Lobster 14 bold'),width="20")
                                sec_combo.current(0)
                                sec_combo.bind("<<ComboboxSelected>>", selected)
                                sec_combo.grid(row=2, column=1) 

                                subcode_label = Label(usn_frame,text="Subcode", font=('Lobster 15 bold'),pady=10,bg='white')
                                subcode_label.grid(row=3, column=0) 

                                subcode_entry = Entry(usn_frame, width="17",font=('Lobster 20 bold'))
                                subcode_entry.grid(row=3, column=1) 

                                submit_button =Button(usn_frame,text="Submit", command=submit, bg="light blue",width="25",height ="3")
                                submit_button.grid(row=4, column=1)

                            

                            login_frame.destroy()
                            querry_string = "SELECT name,aid FROM admin_details WHERE aid =%s"
                            my_cursor.execute(querry_string,(usn_no,))
                            record = my_cursor.fetchall()

                            maintainer_frame = Frame(root, height="800", width="1000")
                            maintainer_frame.pack(side=TOP, expand=YES)

                            img = ImageTk.PhotoImage(Image.open(f"Photos\\{usn_no}.png"))
                            pic_frame = Frame(maintainer_frame)
                            pic_label =Label(pic_frame,image=img)
                            pic_label.pack()
                            pic_frame.grid(row=0, column=0)

                            text_frame = Frame(maintainer_frame)
                            M_username_label = Label(text_frame,text="Name :", font=('Lobster 30 bold'),pady=30)
                            M_username_label.grid(row=0, column=0)

                            M_username_name_label = Label(text_frame,text=f"{record[0][0]}", font=('Lobster 30 bold'), pady=30)
                            M_username_name_label.grid(row=0, column=1)

                            maintainer_label = Label(text_frame,text="Admin id :", font=('Lobster 30 bold'), pady=30)
                            maintainer_label.grid(row=1, column=0)

                            maintainer_id_label = Label(text_frame, text=f"{record[0][1]}", font=('Lobster 30 bold'),pady=30)
                            maintainer_id_label.grid(row=1, column=1)

                            funtionality_label = Label(text_frame,text="Funtionality", font=('Lobster 40 bold'),pady=30)
                            funtionality_label.grid(row=2, column=0)

                            text_frame.grid(row=1, column=0)

                            button_frame = Frame(maintainer_frame)

                            add_records_button = Button(button_frame,text="Add records",width="20",height ="3",bg="blue", command=add_records)
                            add_records_button.grid(row=3,column=0,pady=30,padx=15)

                            update_records_button = Button(button_frame,text="Update records",width="20",height ="3",bg="blue", command=update_records)
                            update_records_button.grid(row=3,column=1,pady=30,padx=15)

                            add_subject_button = Button(button_frame,text="Add subjects",width="20",height ="3",bg="blue", command=add_subjects)
                            add_subject_button.grid(row=3,column=2,pady=30,padx=15)
                            button_frame.grid(row=2, column=0)

                        elif record[0][1]== "S":

                            def view_attendence():
                                def submit():
                                    return
                                view_attendece_window = Toplevel()
                                view_attendece_window.title("Add records")
                                view_attendece_window.geometry("600x800")
                                view_attendece_window.configure(background='#EAF8F8')

                                usn_frame = Frame(view_attendece_window)
                                subcode_label = Label(usn_frame,text="Enter Subject Code", font=('Lobster 15 bold'),pady=10,bg='white',padx=10)
                                subcode_label.grid(row=0, column=0)
                                subcode_entry = Entry(usn_frame, width="17",font=('Lobster 20 bold'))
                                subcode_entry.grid(row=0, column=1,padx=10)

                                

                                submit_button =Button(usn_frame,text="Submit", command=submit, bg="light blue",width="25",height ="3")
                                submit_button.grid(row=1, column=1)
                                usn_frame.pack()



                            login_frame.destroy()
                            student_frame = Frame(root, height="800", width="1000")
                            student_frame.pack(side=TOP, expand=YES)

                            text_frame = Frame(student_frame)
                            L_username_label = Label(text_frame,text="Name :", font=('Lobster 30 bold'),pady=30)
                            L_username_label.grid(row=0, column=0)

                            L_username_name_label = Label(text_frame,text="Pradeep", font=('Lobster 30 bold'), pady=30)
                            L_username_name_label.grid(row=0, column=1)

                            usn_label = Label(text_frame,text="USN :", font=('Lobster 30 bold'), pady=30)
                            usn_label.grid(row=1, column=0)

                            usn_id_label = Label(text_frame, text="948", font=('Lobster 30 bold'),pady=30)
                            usn_id_label.grid(row=1, column=1)

                            funtionality_label = Label(text_frame,text="Funtionality", font=('Lobster 40 bold'),pady=30)
                            funtionality_label.grid(row=2, column=0)

                            text_frame.grid(row=1, column=0)

                            button_frame = Frame(student_frame)

                            view_attendece_button = Button(button_frame,text="View attendece",width="20",height ="3",bg="blue", command=view_attendence)
                            view_attendece_button.grid(row=3,column=0,pady=30,padx=15)

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
    login_label = Label(text_frame, text="Log In", font=('Lobster 30 bold'), bg="white", fg="blue",pady=30, anchor=NW)
    login_label.grid(row=0, column=0)
    username_label =Label(text_frame,text="Username :",font=("Ubuntu 20"), bg="white",pady=15)
    username_label.grid(row=1, column=0)

    password_label =Label(text_frame,text="Password :",font=("Ubuntu 20"), bg="white", pady=15)
    password_label.grid(row=3, column=0)

    username_entry = Entry(text_frame, width=20, font=("Ubuntu",20))
    username_entry.grid(row=1, column=1,padx=10)

    password_entry = Entry(text_frame,show="*", width=20,font=("Ubuntu",20))
    password_entry.grid(row=3, column=1,padx=10)

    submit_button = Button(text_frame,text="Submit", bg="blue", fg="white",font=("Ubuntu 15"),command=submit)
    submit_button.grid(row=5, column=1,padx=10)

        # sign_up_button = Button(text_frame,text="Sign up",bg="blue", fg="white",font=("Ubuntu 15"),command=sign_up)
        # sign_up_button.grid(row=5, column=0,padx=10)
    text_frame.grid(row=0, column= 1)


show_login_frame()
root.state("zoomed")

root.mainloop()

