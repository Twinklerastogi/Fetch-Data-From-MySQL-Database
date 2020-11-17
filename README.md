# Fetch-Data-From-MySQL-Database

Python framework to fetch the data from MySQL database.

Requirements:
* install Tkinter
* install MySQL

### Database.py
* Connect database (employee)
* Create table if not exist (employees)
* Insert data
# Create table if not exist
mycursor.execute("CREATE TABLE IF NOT EXISTS employees ( EMPLOYEE_ID INT AUTO_INCREMENT PRIMARY KEY, NAME varchar(20) DEFAULT NULL, GENDER varchar(25) NOT NULL, SALARY decimal(8,2) DEFAULT NULL)")

#Insert Data

mycursor = mydb.cursor()

Data = "INSERT INTO employees (EMPLOYEE_ID,NAME, GENDER, SALARY) VALUES (%s,%s, %s, %s)"
val = [
    (17,'ARJUN', 'MALE', 7000),
    (18,'ABHINAV', 'MALE', 9000),
    (19,'AMAN', 'MALE', 8700),
    (20,'CHARUL', 'FEMALE', 7900),
    (21,'KRITIKA', 'FEMALE', 9000),
    (22,'PARUL', 'FEMALE', 10000),
    (23,'PRANAV', 'MALE', 7080),
    (24,'PRADUL', 'MALE', 4000)
]

mycursor.executemany(Data, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")


### Display_Records.py
We will use one tkinter entry component to display each data in the window. 
In this variable emp is a tuple and it contains one row of data. We used variable i as index for each row and variable j as each column of data.

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

### Search_Record.py
Adding components to tkinter First add t1 the Text box to receive employees id from the user. This id we will use to collect matching record from the employees table.
First add t1 the Text box to receive employee id from the user. This id we will use to collect matching record from the employee table. We will add one Lebel l1 to display text Enter employee ID: before the text box t1.
We need one more Lebel ( l2) to display the returned details of the employee. This Label initially will display the string Output. We will be displaying data as we are getting from MySQL table, so we will declare one tkinter string variable ( StringVar() ) connected to our Label. We declared my_str = tk.StringVar() for this.
We will add one Button b1 to pass user entered data to a function to get the record details.
On click of the Button b1 , my_details() function will receive the string id as input parameter. This is the id of the employee for which all the detail of the record will be taken from employee table and displayed by using l2 label.
Here data ( id ) is entered by user through the text field ( t1 ). So before using this data in our database Query, we must check this input data. Inside the function my_details() we will use try except code blocks to check if the user entered data id is Integer or not. If it is not integer then except: part of the code block will display message Check input.

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
