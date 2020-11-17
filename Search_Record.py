import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_connect = mysql.connector.connect(
    host='127.0.0.1', 
    user='root', 
    password='twi@mysql',
    database="employee",
    use_pure = True
)
my_cursor = my_connect.cursor()
####### end of connection ####

my_w = tk.Tk()
my_w.geometry("400x200") 

# add one Label 
l1 = tk.Label(my_w,  text='Enter Employee ID: ', width=25 )  
l1.grid(row=1,column=1) 

# add one text box
t1 = tk.Text(my_w,  height=1, width=4,bg='yellow') 
t1.grid(row=1,column=2) 

b1 = tk.Button(my_w, text='Show Details', width=15,bg='red',
    command=lambda: my_details(t1.get('1.0',END)))
b1.grid(row=1,column=4) 

my_str = tk.StringVar()
# add one Label 
l2 = tk.Label(my_w,  textvariable=my_str, width=30,fg='red' )  
l2.grid(row=3,column=1,columnspan=2) 

my_str.set("Output")

def my_details(id):
    try:
        val = int(id) # check input is integer or not
        try:
            my_cursor.execute("SELECT * FROM employees WHERE EMPLOYEE_ID="+str(id))
            employees = my_cursor.fetchone()
            #print(employees)
            my_str.set(employees)
    
        except : 
             my_str.set("Database error")
    except:
        my_str.set("Check input")
my_w.mainloop()