#todo app using sqlite3 and Tkinter 
from tkinter import *
import sqlite3

conn = sqlite3.connect('mydb.db')
c = conn.cursor()

#create table 
c.execute("create table if not exists tasks (id INTEGER PRIMARY key  AUTOINCREMENT, name varchar(20))")
conn.commit()

c.execute("select * from tasks")
data = c.fetchall()


def display_task(id,text):
    frame = Frame(root)
    w = Label(frame, text=text,font=("arial",18),anchor='w')
    w.config(width=18,pady=6)
    btn = Button(frame,text="X",command = lambda : remove_item(id,frame) ,bg="red"  )
    w.pack(side=LEFT)
    btn.pack(side=RIGHT)
    frame.pack()

def remove_item(id,frame):
    frame.destroy()
    c.execute("delete from tasks where id = {0}".format(id))
    conn.commit()

def add_item(name):
    c.execute("insert into tasks (name) values ('{0}')".format(name))
    conn.commit()
    display_task(c.lastrowid,name)   
    
#graphical interface
root = Tk()
root.title('Todo list ')
root.geometry('420x500')

container = Frame(root)
container.config(pady=20)

e = Entry(container)
e.pack(side=LEFT)
btn_add = Button(container,text="Add",command= lambda : add_item(e.get()))
btn_add.pack(side=RIGHT)
container.pack()

for row in data:
    display_task(row[0],row[1])

root.mainloop()