import tkinter #for gui design and implementation
import mysql.connector
from mysql.connector.constants import ClientFlag #for connecting to google cloud

config = {
    'user': 'root',
    'password': '723307009',
    'host': '104.197.74.226',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
} #all necessary info for connecting to google cloud database

config['database'] = 'CS_Cinema'  # add new database to config dict
cnxn = mysql.connector.connect(**config) #starts connextion
cursor = cnxn.cursor(buffered=True) #cursor to run commands
cursor.execute('''DROP TABLE IF EXISTS Employees;''') # how to drop tables
cursor.execute("CREATE TABLE Employees ("
               "Employee_ID INTEGER PRIMARY KEY,"
               "Employee_Name VARCHAR(255),"
               "Salary INTEGER)") # how to add tables
cnxn.commit()  # this commits changes to the database
query = ("INSERT INTO Employees (Employee_ID, Employee_Name, Salary) VALUES(1, 'John', 20000)") #query to inserts some data into employee table
cursor.execute(query) #inserts data into employee table
cnxn.commit()  # and commit changes
cursor.execute("Select * from Employees") #gets all data from employee table
out = cursor.fetchall() #stores query result in variable
for row in out: #prints out each row to terminal
    print(row)

# Top level window
frame = tkinter.Tk() #creates a gui window
frame.title("TextBox Input") #sets window title
frame.geometry('1000x500') # sets window size

# Function for getting Input from textbox and table results to label widget
def printInput():
    inp = inputtxt.get(1.0, "end-1c") #gets input from first box
    inp2 = inputtxt2.get(1.0, "end-1c") #gets input from second box
    inp3 = inputtxt3.get(1.0, "end-1c") #gets input from third box
    # query to insert inputted data into employee table
    cursor.execute("INSERT INTO Employees (Employee_ID, Employee_Name, Salary) VALUES( \'" + inp + "\' , \'" + inp2 + "\', \'" + inp3 + "\')")
    cnxn.commit() # commits changes
    cursor.execute("Select * from Employees") # query to get rows of employee table
    out = cursor.fetchall()
    for row in out: #puts each row into label to be displayed in gui
        lbl = tkinter.Label(frame, text=row)
        lbl.pack()

# TextBox and their labels Creation
lbl = tkinter.Label(frame, text="Employee ID")
lbl.pack()
inputtxt = tkinter.Text(frame,height=1,width=20)
inputtxt.pack()
lbl = tkinter.Label(frame, text="Employee Name")
lbl.pack()
inputtxt2 = tkinter.Text(frame,height=1,width=20)
inputtxt2.pack()
lbl = tkinter.Label(frame, text="Employee Salary")
lbl.pack()
inputtxt3 = tkinter.Text(frame,height=1,width=20)
inputtxt3.pack()

# Button Creation
printButton = tkinter.Button(frame, text="Enter", command=printInput)
printButton.pack()

# runs gui and closes connection to database
frame.mainloop()
cnxn.close()