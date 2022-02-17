from tkinter import *
import mysql.connector


def query_creation():
    mydb = mysql.connector.connect(buffered=True,#Used buffered because i am using fetchall and fetchall reqires its buffered  to be cleaned each time it iterates
    host = "localhost",
    user = "root",
    passwd = "pradeep",
    database ="attendence_book"
    )

    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXIXTS attendence_book")
    mydb.commit()

    my_cursor.execute("""CREATE TABLE IF NOT EXIXTS login(
        usn varchar(40),
        password varchar(40),
        role varchar(10),
        security_key varchar(40),
        primary key(usn)
        """)
    mydb.commit()
    
    my_cursor.execute("""CREATE TABLE IF NOT EXIXTS subject(
        subname varchar(40),   
        subcode varchar(40),
        primary key(subcode),
        """)
    mydb.commit()

    my_cursor.execute("""CREATE TABLE IF NOT EXIXTS admin_details(
        name varchar(40),
        aid varchar(40),
        phone bigint,
        email varchar(40)
        address varchar(40),
        primary key(aid),
        foreign key(aid) references login(usn) on delete cascade
        """)
    mydb.commit()

    my_cursor.execute("""CREATE TABLE IF NOT EXIXTS lecture_details(
        name varchar(40),
        ssid varchar(40),
        phone bigint,
        email varchar(40)
        address varchar(40),
        primary key(ssid),
        foreign key(ssid) references login(usn) on delete cascade
        """)
    mydb.commit()

    my_cursor.execute("""CREATE TABLE IF NOT EXIXTS student_details(
        name varchar(40),
        usn varchar(40),
        sem int,
        sec varchar(10),
        address varchar(40),
        email varchar(40)
        phone bigint,        
        primary key(usn),
        foreign key(usn) references login(usn) on delete cascade
        """)
    mydb.commit()

    my_cursor.execute("""CREATE TABLE IF NOT EXIXTS lecture_record(
        ssid varchar(40),
        subcode varchar(40),
        sem int,
        sec varchar(10),      
        attendence_table_name varchar(40),
        primary key(ssid,subcode,sem,sec),
        foreign key(ssid) references login(usn) on delete cascade,
        foreign key(subcode) references subject(subcode) on delete cascade
        """)
    mydb.commit()

   


    
                                    
    