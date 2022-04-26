import tkinter #for gui design and implementation
from tkinter import messagebox
from tkinter import *
import mysql.connector
from mysql.connector.constants import ClientFlag #for connecting to google cloud

def vars(c, c2, f): #sets up global vars for cursor, the sql executor, for cnxn, the sql connection, and for frame, the gui window
    global cursor
    cursor = c
    global cnxn
    cnxn = c2
    global frame
    frame = f
    employee() #calls employee
def back(): # goes back to main and the function for the main menu, these two function makes it so there is no duplicate screens
    from main import restart #solves the circular reference problem
    restart()
def back2(): #destroys the current widgets and frame then calls back
    for widget in frame.winfo_children():
        widget.destroy()
    frame.destroy()
    back()
def employee(): #function for the menu of whether to choose to change or view employees
    for widget in frame.winfo_children():
        widget.destroy()
    frame.title("Choose For Employees")
    lbl3 = tkinter.Label(frame, text="Would you like to change employees or view employees", bg="gray")
    lbl3.config(font=('Helvetica bold', 20))
    lbl3.pack()
    printButton4 = tkinter.Button(frame, text="Change", command=insertEmployees, width=20, height=10, bg="blue", fg="white") # change employees button
    printButton4.place(x=200, y=300)
    printButton4.config(font=('Helvetica bold', 15))
    printButton5 = tkinter.Button(frame, text="View", command=viewEmployees, width=20, height=10, bg="orange", fg="white") #view employees button
    printButton5.place(x=800, y=300)
    printButton5.config(font=('Helvetica bold', 15))
    global printButton6 # back button
    printButton6 = tkinter.Button(frame, text="Back", command=back2, width=15, height=7, bg="black", fg="white")
    printButton6.place(x=25, y=725)
    printButton6.config(font=('Helvetica bold', 5))

def printInput(): #function to insert new employees, should probably change the name
        id = inputtxt.get(1.0, "end-1c")  # gets input from first box
        name = inputtxt2.get(1.0, "end-1c")  # gets input from second box
        salary = inputtxt3.get(1.0, "end-1c")  # gets input from third box
        if not id or not name or not salary:#checks if all text boxes are empty
            messagebox.showerror('Python Error', 'All entries must be filled')  #how to do an error message in tkinter
            insertEmployees()
        else:
            query = ( "INSERT INTO Employees (Employee_ID, Employee_Name, Salary) VALUES(%s, %s, %s)")  # query for prepared statement
            tuple1 = (id, name, salary)  # adding info to prepared statement
            cursor.execute(query, tuple1)  # executing query
            cnxn.commit()  # commits changes
        insertEmployees()
def Edit(): #function to edit employees
    id = inputtxt4.get(1.0, "end-1c")  # gets input from first box
    newName = inputtxt5.get(1.0, "end-1c")  # gets input from second box
    newSalary = inputtxt6.get(1.0, "end-1c")  # gets input from third box
    if not id: #must have identifying employee id
        messagebox.showerror('Python Error', 'Employee ID must not be empty')
    elif not newName and not newSalary: # cant have both news empty
        messagebox.showerror('Python Error', 'Both new name and new salary cannot be empty')
    elif not newName: #updates new salary for specific id
        query = ("UPDATE Employees SET Salary = %s WHERE Employee_ID = %s")
        tuple1 = (newSalary, id)
        cursor.execute(query, tuple1)
        cnxn.commit()
    elif not newSalary: #updates new name for specific id
        query = ("UPDATE Employees SET Employee_Name = %s WHERE Employee_ID = %s")
        tuple1 = (newName, id)
        cursor.execute(query, tuple1)
        cnxn.commit()
    else: #updates new name and salary for specific id
        query = ("UPDATE Employees SET Employee_Name = %s, Salary = %s WHERE Employee_ID = %s")
        tuple1 = (newName, newSalary, id)
        cursor.execute(query, tuple1)
        cnxn.commit()
    insertEmployees() #loops back to same window

def Delete(): #function to delete employees
    id = inputtxt7.get(1.0, "end-1c")  # gets input from first box
    name = inputtxt8.get(1.0, "end-1c")  # gets input from second box
    if not id and not name:
        messagebox.showerror('Python Error', 'Both employee id and name cannot not be empty')
    elif not id: #prepared statement to delete all employees with the specific name
        query = ("DELETE FROM Employees WHERE Employee_Name = %s")
        tuple1 = (name,)
        cursor.execute(query, tuple1)
        cnxn.commit()
    elif not name: #prepared statement to delete all employees with the specific id
        query = ("DELETE FROM Employees WHERE Employee_ID = %s")
        tuple1 = (id,)
        cursor.execute(query, tuple1)
        cnxn.commit()
    else:
        messagebox.showerror('Python Error', 'Both employee id and name are not necessary')
    insertEmployees() #loop back to same window

def insertEmployees():
    query = ("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")  # query to set transaction isolation level
    cursor.execute(query)  # executes query
    cnxn.commit()  # commit changes
    for widget in frame.winfo_children():
        widget.destroy()
    frame.title("Change Employees")  # sets window title
    # TextBox and their labels Creation
    # for main labels
    insert = tkinter.Label(frame, text="Insert", bg="gray")
    insert.config(font=('Helvetica bold', 40))
    insert.place(x = 50, y = 20)
    edit = tkinter.Label(frame, text="Edit", bg="gray")
    edit.config(font=('Helvetica bold', 40))
    edit.place(x=450, y=20)
    delete = tkinter.Label(frame, text="Delete", bg="gray")
    delete.config(font=('Helvetica bold', 40))
    delete.place(x=850, y=20)
    # for insert function
    lbl = tkinter.Label(frame, text="Employee ID", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=50, y=120)
    global inputtxt #have to be global so other function can access what is input into them
    inputtxt = tkinter.Text(frame, height=2, width=30)
    inputtxt.place(x=50, y=170)
    lbl = tkinter.Label(frame, text="Employee Name", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=50, y=220)
    global inputtxt2
    inputtxt2 = tkinter.Text(frame, height=2, width=30)
    inputtxt2.place(x=50, y=270)
    lbl = tkinter.Label(frame, text="Employee Salary", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=50, y=320)
    global inputtxt3
    inputtxt3 = tkinter.Text(frame, height=2, width=30)
    inputtxt3.place(x=50, y=370)
    # Button Creation
    printButton = tkinter.Button(frame, text="Insert", command=printInput, width=10, height=2, bg="orange", fg="white")
    printButton.place(x=50, y=420)
    printButton6 = tkinter.Button(frame, text="Back", command=employee, width=15, height=7, bg="black", fg="white")
    printButton6.place(x=25, y=725)
    printButton6.config(font=('Helvetica bold', 5))
    # for edit function
    lbl = tkinter.Label(frame, text="Employee ID", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=450, y=120)
    global inputtxt4
    inputtxt4 = tkinter.Text(frame, height=2, width=30)
    inputtxt4.place(x=450, y=170)
    lbl = tkinter.Label(frame, text="New Employee Name", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=450, y=220)
    global inputtxt5
    inputtxt5 = tkinter.Text(frame, height=2, width=30)
    inputtxt5.place(x=450, y=270)
    lbl = tkinter.Label(frame, text="New Employee Salary", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=450, y=320)
    global inputtxt6
    inputtxt6 = tkinter.Text(frame, height=2, width=30)
    inputtxt6.place(x=450, y=370)
    editButton = tkinter.Button(frame, text="Edit", command=Edit, width=10, height=2, bg="blue", fg="white")
    editButton.place(x=450, y=420)
    # for delete function
    lbl = tkinter.Label(frame, text="Employee ID", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=850, y=120)
    global inputtxt7
    inputtxt7 = tkinter.Text(frame, height=2, width=30)
    inputtxt7.place(x=850, y=170)
    lbl = tkinter.Label(frame, text="Employee Name", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=850, y=220)
    global inputtxt8
    inputtxt8 = tkinter.Text(frame, height=2, width=30)
    inputtxt8.place(x=850, y=270)
    deleteButton = tkinter.Button(frame, text="Delete", command=Delete, width=10, height=2, bg="orange", fg="white")
    deleteButton.place(x=850, y=320)


def search(): #function to display the reports on employees, could maybe add number of orders
    start = 50 #for initial x value of labels
    add = 325 # for what to add to x value of labels
    for widget in frame.winfo_children(): # deletes old reports but not the main text labels
        temp = str(widget)
        if "label" in temp:
            num = temp[7:]
            num = int(num)
        if "label" in temp and num > tobeat:
            widget.destroy()
    # lots of sp's to make some of the combos that can be selected, didn't do all as sp's because that would be too many
    if one.get() == "Default" and two.get() == "Default" and three.get() == "Default":
        query = ("CALL sp_GetEmployeesALL")
    elif one.get() == "None" and two.get() == "None" and three.get() == "None":
        messagebox.showerror('Python Error', 'Both employee id and name cannot be none')
    elif one.get() == "None" and two.get() == "None" and three.get() != "None":
        messagebox.showerror('Python Error', 'Both employee id and name cannot be none')
    elif one.get() == "None" and two.get() == "Default" and three.get() == "None":
        start = start + add
        query = ("CALL sp_GetEmployeesDefaultName")
    elif one.get() == "None" and two.get() == "Name ASC." and three.get() == "None":
        start = start + add
        query = ("CALL sp_GetEmployeesNameASC")
    elif one.get() == "None" and two.get() == "Name DESC." and three.get() == "None":
        start = start + add
        query = ("CALL sp_GetEmployeesNameDESC")
    elif one.get() == "Default" and two.get() == "None" and three.get() == "None":
        query = ("CALL sp_GetEmployeesDefaultID")
    elif one.get() == "ID ASC." and two.get() == "None" and three.get() == "None":
        query = ("CALL sp_GetEmployeesIDASC")
    elif one.get() == "ID DESC." and two.get() == "None" and three.get() == "None":
        query = ("CALL sp_GetEmployeesIDDESC")
    else: # builds query for the other combos
        q = ""
        if one.get() != "None" and two.get() != "None" and three.get() != "None": #the option
            q = "SELECT Employee_ID, Employee_Name, Salary FROM Employees ORDER BY" # initial query
            if "ASC." in one.get(): #things to be added
                q = q + " Employee_ID ASC,"
            elif "DESC." in one.get():
                q = q + " Employee_ID DESC,"
            if "ASC." in two.get():
                q = q + " Employee_Name ASC,"
            elif "DESC." in two.get():
                q = q + " Employee_Name DESC,"
            if "ASC." in three.get():
                q = q + " Salary ASC,"
            elif "DESC." in three.get():
                q = q + " Salary DESC,"
            if q[-1] == ",": #if q ends in "," remove it
                query = (q[:-1])
            else: #else query is initial minus order by
                query = ("SELECT Employee_ID, Employee_Name, Salary FROM Employees")
        elif one.get() != "None" and two.get() != "None":
            q = "SELECT Employee_ID, Employee_Name FROM Employees ORDER BY"
            if "ASC." in one.get():
                q = q + " Employee_ID ASC,"
            elif "DESC." in one.get():
                q = q + " Employee_ID DESC,"
            if "ASC." in two.get():
                q = q + " Employee_Name ASC,"
            elif "DESC." in two.get():
                q = q + " Employee_Name DESC,"
            if q[-1] == ",":
                query = (q[:-1])
            else:
                query = ("SELECT Employee_ID, Employee_Name FROM Employees")
        elif one.get() != "None" and three.get() != "None":
            add = add + add
            q = "SELECT Employee_ID, Salary FROM Employees ORDER BY"
            if "ASC." in one.get():
                q = q + " Employee_ID ASC,"
            elif "DESC." in one.get():
                q = q + " Employee_ID DESC,"
            if "ASC." in three.get():
                q = q + " Salary ASC,"
            elif "DESC." in three.get():
                q = q + " Salary DESC,"
            if q[-1] == ",":
                query = (q[:-1])
            else:
                query = ("SELECT Employee_ID, Salary FROM Employees")
        elif two.get() != "None" and three.get() != "None":
            start = start + add
            q = "SELECT Employee_Name, Salary FROM Employees ORDER BY"
            if "ASC." in two.get():
                q = q + " Employee_Name ASC,"
            elif "DESC." in two.get():
                q = q + " Employee_Name DESC,"
            if "ASC." in three.get():
                q = q + " Salary ASC,"
            elif "DESC." in three.get():
                q = q + " Salary DESC,"
            if q[-1] == ",":
                query = (q[:-1])
            else:
                query = ("SELECT Employee_Name, Salary FROM Employees")
    cursor.execute(query)  # query to get rows of employee table
    out = cursor.fetchall() #stores results
    y1 = 170 #initial y value of labels
    for row in out:  # puts each row into label to be displayed in gui
        x1 = start
        for n in row:
            lbl = tkinter.Label(frame, text=n, bg="gray")
            lbl.config(font=('Helvetica bold', 10))
            lbl.place(x=x1, y=y1)
            x1 = x1 + add
        y1 = y1 + 40
    cnxn.reconnect() #neccessary to not get error after calling stored procedure

def viewEmployees(): #function to implement the gui of view employees
    query = ("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")  # query to set transaction isolation level
    cursor.execute(query)  # executes query
    cnxn.commit()
    global tobeat # var for label number
    tobeat = 0
    for widget in frame.winfo_children():
        widget.destroy()
    frame.title("View Employees")  # sets window title
    lbl3 = tkinter.Label(frame, text="Select what you want to view from employees", bg="gray")
    lbl3.config(font=('Helvetica bold', 40))
    lbl3.pack()
    lbl1 = tkinter.Label(frame, text="Employee ID:", bg="gray")
    lbl1.config(font=('Helvetica bold', 20))
    lbl1.place(x=50, y=120)
    global one # global var for dropdown menu
    one = StringVar(frame) #initialise dropdown menu
    one.set("Default")  # default value of dropdown menu
    drop1 = OptionMenu(frame, one, "Default", "ID ASC.", "ID DESC.", "None") #how to implement drop menus, "" are the options
    drop1.config(bg="orange", fg="white") #sets bg and fg colors
    drop1.place(x=225, y=120) #places drop menu
    lbl2 = tkinter.Label(frame, text="Employee Name:", bg="gray")
    lbl2.config(font=('Helvetica bold', 20))
    lbl2.place(x=350, y=120)
    global two
    two = StringVar(frame)
    two.set("Default")  # default value
    drop2 = OptionMenu(frame, two, "Default", "Name ASC.", "Name DESC.", "None")
    drop2.config(bg="blue", fg="white")
    drop2.place(x=570, y=120)
    lbl4 = tkinter.Label(frame, text="Salary:", bg="gray")
    lbl4.config(font=('Helvetica bold', 20))
    lbl4.place(x=695, y=120)
    global three
    three = StringVar(frame)
    three.set("Default")  # default value
    drop3 = OptionMenu(frame, three, "Default", "Salary ASC.", "Salary DESC.", "None")
    drop3.config(bg="orange", fg="white")
    drop3.place(x=795, y=120)
    printButton6 = tkinter.Button(frame, text="Back", command=employee, width=15, height=7, bg="black", fg="white")
    printButton6.place(x=25, y=725)
    printButton6.config(font=('Helvetica bold', 5))
    for widget in frame.winfo_children(): #gets the number identifying main labels so they aren't deleted
        temp = str(widget)
        if "label" in temp:
            num = temp[7:]
            num = int(num)
            tobeat = num
    searchButton = tkinter.Button(frame, text="Search", command=search, width=10, height=1, bg="blue", fg="white")
    searchButton.place(x=1000, y=125)





