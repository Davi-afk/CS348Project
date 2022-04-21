import tkinter #for gui design and implementation
import mysql.connector
from mysql.connector.constants import ClientFlag #for connecting to google cloud
def insertEmployees(cursor, cnxn):
    # Top level window
    frame = tkinter.Tk()  # creates a gui window
    frame.title("TextBox Input")  # sets window title
    frame.geometry('1000x500')  # sets window size

    # Function for getting Input from textbox and table results to label widget
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")  # gets input from first box
        inp2 = inputtxt2.get(1.0, "end-1c")  # gets input from second box
        inp3 = inputtxt3.get(1.0, "end-1c")  # gets input from third box
        # query to insert inputted data into employee table
        query = (
            "INSERT INTO Employees (Employee_ID, Employee_Name, Salary) VALUES(%s, %s, %s)")  # query for prepared statement
        tuple1 = (inp, inp2, inp3)  # adding info to prepared statement
        cursor.execute(query, tuple1)  # executing query
        cnxn.commit()  # commits changes
        cursor.execute("CALL sp_GetEmployees")  # query to get rows of employee table with stored procedure
        out = cursor.fetchall()
        for row in out:  # puts each row into label to be displayed in gui
            lbl = tkinter.Label(frame, text=row)
            lbl.pack()
            print(row)

    # TextBox and their labels Creation
    lbl = tkinter.Label(frame, text="Employee ID")
    lbl.pack()
    inputtxt = tkinter.Text(frame, height=1, width=20)
    inputtxt.pack()
    lbl = tkinter.Label(frame, text="Employee Name")
    lbl.pack()
    inputtxt2 = tkinter.Text(frame, height=1, width=20)
    inputtxt2.pack()
    lbl = tkinter.Label(frame, text="Employee Salary")
    lbl.pack()
    inputtxt3 = tkinter.Text(frame, height=1, width=20)
    inputtxt3.pack()

    # Button Creation
    printButton = tkinter.Button(frame, text="Enter", command=printInput)
    printButton.pack()

    # runs gui and closes connection to database
    frame.mainloop()
    cnxn.close()