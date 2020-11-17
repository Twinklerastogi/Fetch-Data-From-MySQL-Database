import mysql.connector

#Try connecting to the database 'employee'
mydb = mysql.connector.connect(
    host='127.0.0.1', 
    user='root', 
    password='twi@mysql',
    database="employee",
    use_pure = True
)
mycursor = mydb.cursor()

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
