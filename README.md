# Fetch-Data-From-MySQL-Database

Python framework to fetch the data from MySQL database.

Requirements:
* install Tkinter
* install MySQL

### Database.py
* Connect database (employee)
* Create table if not exist (employees)
* Insert data

### Display_Records.py
We will use one tkinter entry component to display each data in the window. 
In this variable emp is a tuple and it contains one row of data. We used variable i as index for each row and variable j as each column of data.

### Search_Record.py
* Adding components to tkinter First add t1 the Text box to receive employees id from the user. This id we will use to collect matching record from the employees table.
First add t1 the Text box to receive employee id from the user. This id we will use to collect matching record from the employee table. We will add one Lebel l1 to display text Enter employee ID: before the text box t1.

* We need one more Lebel ( l2) to display the returned details of the employee. This Label initially will display the string Output. We will be displaying data as we are getting from MySQL table, so we will declare one tkinter string variable ( StringVar() ) connected to our Label. We declared my_str = tk.StringVar() for this.
We will add one Button b1 to pass user entered data to a function to get the record details.

* On click of the Button b1 , my_details() function will receive the string id as input parameter. This is the id of the employee for which all the detail of the record will be taken from employee table and displayed by using l2 label.

* Here data ( id ) is entered by user through the text field ( t1 ). So before using this data in our database Query, we must check this input data. Inside the function my_details() we will use try except code blocks to check if the user entered data id is Integer or not. If it is not integer then except: part of the code block will display message Check input.

