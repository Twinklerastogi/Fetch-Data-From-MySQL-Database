# We will use one tkinter entry component 
# to display each data in the window. 
# In this variable emp is a tuple and it contains one row of data. 
# We used variable i as index for each row and variable j as each column of data.


import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.title('Records From Database')
my_w.geometry("400x250") 
my_connect = mysql.connector.connect(
    host='127.0.0.1', 
    user='root', 
    password='twi@mysql',
    database="employee",
    use_pure = True
)
my_conn = my_connect.cursor()

####### end of connection ####

my_conn.execute("SELECT * FROM employees limit 0,10")
i=0 
for emp in my_conn: 
    for j in range(len(emp)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, emp[j])
    i=i+1
my_w.mainloop()