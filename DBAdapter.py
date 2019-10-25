
import sqlite3 as sq
from sqlite3 import Error
from tkinter import messagebox

def connect():
    conn = None
    try:
        conn = sq.connect("db.sqlite3")
        conn.commit()
    except Error as e :
        messagebox.showinfo("Error",str(e)+" during connect")

    return conn

def create_table(conn,t_name) :
    try :
        sql = "create table if not exists "+t_name+" (" \
                                                         "month varchar(10) primary key," \
                                                         "consumption integer," \
                                                         "amount_paid double );"
        c = conn.cursor()
        c.execute(sql)
        conn.close()

    except Error as e :
        messagebox.showinfo("Error",str( e )+ " during create")

def insert(conn,t_name,mnth,cons,amnt):
    try :
        sql = "insert into "+t_name+"(month,consumption,amount_paid)" \
                                    "values(?,?,?)"
        c = conn.cursor()
        c.execute(sql,(mnth,cons,amnt))
        conn.commit()
        conn.close()
        messagebox.showinfo("Done","Inserted in DB")

    except Error as e :
        messagebox.showinfo("Error", str(e) + " during insert ")


def retreive(conn,t_name):
    try:
        sql = "select * from "+t_name
        sql += " order by month desc limit 6"
        c = conn.cursor()
        c.execute(sql)

        rows = c.fetchmany(6)
        conn.close()
        return rows

    except Error as e:
        messagebox.showinfo("Error", str(e) + " during retreive ")

def retreive_for_draw(conn,t_name) :
    try :
        sql = "select * from "+t_name
        sql += " where month <> (select max(month) from "+t_name+")"
        sql += " order by month desc limit 6"
        c = conn.cursor()
        c.execute(sql)

        rows = c.fetchmany(6)
        conn.close()
        return rows

    except Error as e :
        messagebox.showinfo("Error", str(e) + " during retreive for draw ")

