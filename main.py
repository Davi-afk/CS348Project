import tkinter #for gui design and implementation
import mysql.connector
from mysql.connector.constants import ClientFlag #for connecting to google cloud
from employees import *
from movies import *
from orders import *
config = {
    'user': 'root',
    'password': '723307009',
    'host': '34.67.71.254',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
} #all necessary info for connecting to google cloud database

config['database'] = 'CS_Cinema'  # add new database to config dict
cnxn = mysql.connector.connect(**config) #starts connextion
cursor = cnxn.cursor(buffered=True) #cursor to run commands
"""Tables:
Employees(Employee_ID int PK, Employee_Name char(50), Salary int)
Theater(Theater_Name char(50) PK, Location char(50))
Orders(Order_Number int PK, Employee_ID int)
Items(Order_Number int PK, Food_Name char(50))
Food(Food_Name char(50) PK, Price float(2), Type char(50))
Auditoriums(Auditorium_ID int PK, Theater_Name char(50) PK, Capacity int)
Tickets(Order_Number int PK, Movie_ID int, Showtime time, Ticket_price float(2))
Movies(Movie_ID int PK, Name char(50), Release_Date date, Runtime time) """

#query = ("CREATE PROCEDURE sp_GetEmployees() BEGIN select Employee_Name,Employee_ID from Employees; END") #query to inserts a stored procedure
#cursor.execute(query) #inserts stored procedure
#cnxn.commit()  # and commit changes
cursor.execute("SHOW TABLES") #gets all tables
out = cursor.fetchall() #stores query result in variable
for row in out: #prints out each row to terminal
    print(row)
frame = tkinter.Tk()  # creates a gui window
frame.title("TextBox Input")  # sets window title
frame.geometry('1000x500')  # sets window size
def employee():
    frame.destroy()
    global frame2
    frame2 = tkinter.Tk()
    frame2.title("TextBox Input")  # sets window title
    frame2.geometry('1000x500')
    printButton = tkinter.Button(frame2, text="Insert", command=insertemp)
    printButton.pack()
    printButton2 = tkinter.Button(frame2, text="View", command=employee)
    printButton2.pack()
def insertemp():
    frame2.destroy()
    insertEmployees(cursor, cnxn)
printButton = tkinter.Button(frame, text="Movies", command=employee)
printButton.pack()
printButton2 = tkinter.Button(frame, text="Employees", command=employee)
printButton2.pack()
printButton3 = tkinter.Button(frame, text="Orders", command=employee)
printButton3.pack()
frame.mainloop()


