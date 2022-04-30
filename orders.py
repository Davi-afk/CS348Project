import tkinter
from tkinter import messagebox
from tkinter import *
import mysql.connector
from mysql.connector.constants import ClientFlag

def vars(c, c2, f):
    global cursor
    cursor = c
    global cnxn
    cnxn = c2
    global frame
    frame = f
    order()
    global t
    t = [""]
def back():
    from main import restart
    restart()
def back2():
    for widget in frame.winfo_children():
        widget.destroy()
    frame.destroy()
    back()
def order():
    for widget in frame.winfo_children():
        widget.destroy()
    frame.title("Choose For Orders")
    lbl3 = tkinter.Label(frame, text="Would you like to change orders or view orders", bg="gray")
    lbl3.config(font=('Helvetica bold', 20))
    lbl3.pack()
    printButton4 = tkinter.Button(frame, text="Change", command=insertOrders, width=20, height=10, bg="blue", fg="white")
    printButton4.place(x=200, y=300)
    printButton4.config(font=('Helvetica bold', 15))
    printButton5 = tkinter.Button(frame, text="View", command=viewOrders, width=20, height=10, bg="orange", fg="white")
    printButton5.place(x=800, y=300)
    printButton5.config(font=('Helvetica bold', 15))
    global printButton6
    printButton6 = tkinter.Button(frame, text="Back", command=back2, width=15, height=7, bg="black", fg="white")
    printButton6.place(x=25, y=725)
    printButton6.config(font=('Helvetica bold', 5))

def printInput():
    num = inputtxt1.get(1.0, "end-1c")

    empid = dropdown1.get()
    size = len(empid)
    empid = empid[1:size - 2]

    food = dropdown2.get()
    size = len(food)
    food = food[2:size - 3]

    movie = dropdown3.get()
    size = len(movie)
    movie = movie[2:size - 3]

    showtime = dropdown4.get()

    cost = 0
    if not empid or not num:
        messagebox.showerror('Python Error', 'Must have employee handling')
    elif not movie and not showtime and not food:
        messagebox.showerror('Python Error', 'Must buy at least one item')
    query = "SELECT * FROM Orders;"
    cursor.execute(query)
    cnxn.commit()
    x = cursor.fetchall()
    query = ("INSERT INTO Orders (Order_Number, Employee_ID) VALUES(%s, %s);")
    tuple1 = (num, empid)
    cursor.execute(query, tuple1)
    cnxn.commit()
    if food:
        query = ("SELECT Price FROM Food WHERE Food_Name = \'" + food + "\';")
        cursor.execute(query)
        cnxn.commit()
        cost = cursor.fetchone()
        cost = float(cost[0])
        query = ("INSERT INTO Items (Order_Number, Food_Name) VALUES(%s, %s);")
        tuple3 = (num, food)
        cursor.execute(query, tuple3)
        cnxn.commit()
    if movie:
        cost += 7.50
        query = ("SELECT Movie_ID FROM Movies WHERE Name = \'" + movie + "\';")
        cursor.execute(query)
        cnxn.commit()
        movid = cursor.fetchone()
        movid = int(movid[0])
        query = ("INSERT INTO Tickets (Order_Number, Movie_ID, Showtime, Ticket_price) VALUES(%s, %s, %s, %s)")
        tuple5 = (num, movid, showtime, cost)
        print(query, tuple5)
        cursor.execute(query, tuple5)
        cnxn.commit()
    insertOrders()

def Delete():  # function to delete employees
    id = dropdown5.get()  # gets input from first box
    size = len(id)
    id = id[1:size - 2]
    if not id:
        messagebox.showerror('Python Error', 'Order Number cannot not be empty')
    else:  # prepared statement to delete all employees with the specific name
        query = ("DELETE FROM Orders WHERE Order_Number = " + id + ";")
        cursor.execute(query)

        query = ("DELETE FROM Tickets WHERE Order_Number = " + id + ";")
        cursor.execute(query)

        query = ("DELETE FROM Items WHERE Order_Number = " + id + ";")
        cursor.execute(query)
        cnxn.commit()
    insertOrders()  # loop back to same window

def insertOrders():
    query = ("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")  # query to set transaction isolation level
    cursor.execute(query)  # executes query
    cnxn.commit()  # commit changes
    for widget in frame.winfo_children():
        widget.destroy()
    frame.title("Change Orders")  # sets window title
    # TextBox and their labels Creation
    # for main labels
    insert = tkinter.Label(frame, text="Insert", bg="gray")
    insert.config(font=('Helvetica bold', 40))
    insert.place(x = 50, y = 20)
    # edit = tkinter.Label(frame, text="Edit", bg="gray")
    # edit.config(font=('Helvetica bold', 40))
    # edit.place(x=450, y=20)
    delete = tkinter.Label(frame, text="Delete", bg="gray")
    delete.config(font=('Helvetica bold', 40))
    delete.place(x=850, y=20)
    # for insert function

    lbl = tkinter.Label(frame, text="Order Number", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=50, y=120)
    global inputtxt1
    inputtxt1 = tkinter.Text(frame, height=2, width=30)
    inputtxt1.place(x=50, y=170)

    lbl = tkinter.Label(frame, text="Employee ID", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=50, y=220)
    query = ("SELECT Employee_ID FROM Employees;")
    cursor.execute(query)
    cnxn.commit()
    employee_ids = cursor.fetchall()
    employee_ids = t + employee_ids
    global dropdown1 #have to be global so other function can access what is input into them
    dropdown1 = StringVar(frame)
    dropdown1.set(employee_ids[0])
    w1 = tkinter.OptionMenu(frame, dropdown1, *employee_ids)
    w1.place(x=50, y=270)

    lbl = tkinter.Label(frame, text="Food Name", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=50, y=320)
    query = ("SELECT Food_Name FROM Food;")
    cursor.execute(query)
    cnxn.commit()
    foods = cursor.fetchall()
    foods = t + foods
    global dropdown2
    dropdown2 = StringVar(frame)
    dropdown2.set(foods[0])
    w2 = tkinter.OptionMenu(frame, dropdown2, *foods)
    w2.place(x=50, y=370)

    # query = ("INSERT INTO Movies (Movie_ID, Name) VALUES(1, \"Avengers\")")
    # cursor.execute(query)
    # cnxn.commit()

    lbl = tkinter.Label(frame, text="Movies", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=50, y=420)
    query = ("SELECT Name FROM Movies;")
    cursor.execute(query)
    cnxn.commit()
    movies = cursor.fetchall()
    movies = t + movies
    global dropdown3
    dropdown3 = StringVar(frame)
    dropdown3.set(movies[0])
    w3 = tkinter.OptionMenu(frame, dropdown3, *movies)
    w3.place(x=50, y=470)

    lbl = tkinter.Label(frame, text="Showtimes", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=50, y=520)
    showtimes = ["5:00", "5:30", "6:00", "6:30", "7:00", "7:30"]
    global dropdown4
    dropdown4 = StringVar(frame)
    dropdown4.set(showtimes[0])
    w4 = tkinter.OptionMenu(frame, dropdown4, *showtimes)
    w4.place(x=50, y=570)
    # Button Creation
    printButton = tkinter.Button(frame, text="Insert", command=printInput, width=10, height=2, bg="orange", fg="white")
    printButton.place(x=50, y=620)
    printButton6 = tkinter.Button(frame, text="Back", command=order, width=15, height=7, bg="black", fg="white")
    printButton6.place(x=25, y=725)
    printButton6.config(font=('Helvetica bold', 5))

    # for edit function
    # lbl = tkinter.Label(frame, text="Employee ID", bg="gray")
    # lbl.config(font=('Helvetica bold', 20))
    # lbl.place(x=450, y=120)
    # global inputtxt4
    # inputtxt4 = tkinter.Text(frame, height=2, width=30)
    # inputtxt4.place(x=450, y=170)
    # lbl = tkinter.Label(frame, text="New Employee Name", bg="gray")
    # lbl.config(font=('Helvetica bold', 20))
    # lbl.place(x=450, y=220)
    # global inputtxt5
    # inputtxt5 = tkinter.Text(frame, height=2, width=30)
    # inputtxt5.place(x=450, y=270)
    # lbl = tkinter.Label(frame, text="New Employee Salary", bg="gray")
    # lbl.config(font=('Helvetica bold', 20))
    # lbl.place(x=450, y=320)
    # global inputtxt6
    # inputtxt6 = tkinter.Text(frame, height=2, width=30)
    # inputtxt6.place(x=450, y=370)
    # editButton = tkinter.Button(frame, text="Edit", command=Edit, width=10, height=2, bg="blue", fg="white")
    # editButton.place(x=450, y=420)

    # for delete function
    lbl = tkinter.Label(frame, text="Order Num", bg="gray")
    lbl.config(font=('Helvetica bold', 20))
    lbl.place(x=850, y=120)
    query = ("SELECT Order_Number FROM Orders")
    cursor.execute(query)
    cnxn.commit()
    ordernums = cursor.fetchall()
    ordernums = t + ordernums
    global dropdown5
    dropdown5 = StringVar(frame)
    dropdown5.set(ordernums[0])
    w5 = tkinter.OptionMenu(frame, dropdown5, *ordernums)
    w5.place(x=850, y=170)

    deleteButton = tkinter.Button(frame, text="Delete", command=Delete, width=10, height=2, bg="orange", fg="white")
    deleteButton.place(x=850, y=320)

def search():
    start = 50
    add = 150
    for widget in frame.winfo_children():
        temp = str(widget)
        if "label" in temp:
            num = temp[7:]
            num = int(num)
        if "label" in temp and num > tobeat:
            widget.destroy()
    if one.get() == "Default" and two.get() == "Default" and three.get() == "Default":
        query = ("""SELECT o.Order_Number, e.Employee_Name, i.Food_Name, t.Showtime, m.Name, t.Ticket_price  
                   FROM Orders o JOIN Employees e ON o.Employee_ID = e.Employee_ID 
                   JOIN Items i ON i.Order_Number = o.Order_Number
                   JOIN Tickets t ON t.Order_Number = o.Order_Number
                   JOIN Movies m ON m.Movie_ID = t.Movie_ID""")
    cursor.execute(query)  # query to get rows of employee table
    cnxn.commit()
    out = cursor.fetchall()  # stores results
    y1 = 220  # initial y value of labels
    for row in out:  # puts each row into label to be displayed in gui
        x1 = start
        for n in row:
            lbl = tkinter.Label(frame, text=n, bg="gray")
            lbl.config(font=('Helvetica bold', 10))
            lbl.place(x=x1, y=y1)
            x1 = x1 + add
        y1 = y1 + 40
    cnxn.reconnect()  # neccessary to not get error after calling stored procedure

def viewOrders():
    query = ("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")
    cursor.execute(query)
    cnxn.commit()
    global tobeat
    tobeat = 0
    for widget in frame.winfo_children():
        widget.destroy()
    frame.title("View Orders")
    lbl3 = tkinter.Label(frame, text="Select what you want to view from orders", bg="gray")
    lbl3.config(font=('Helvetica bold', 40))
    lbl3.pack()
    lbl1 = tkinter.Label(frame, text="Order ID:", bg="gray")
    lbl1.config(font=('Helvetica bold', 20))
    lbl1.place(x=50, y=120)
    global one
    one = StringVar(frame)
    one.set("Default")
    # drop1 = OptionMenu(frame, one, "Default", "ID ASC.", "ID DESC.", "None")
    # drop1.config(bg="orange", fg="white")
    # drop1.place(x=50, y=170)
    lbl2 = tkinter.Label(frame, text="Employee:", bg="gray")
    lbl2.config(font=('Helvetica bold', 20))
    lbl2.place(x=190, y=120)
    global two
    two = StringVar(frame)
    two.set("Default")  # default value
    # drop2 = OptionMenu(frame, two, "Default", "Name ASC.", "Name DESC.", "None")
    # drop2.config(bg="blue", fg="white")
    # drop2.place(x=220, y=170)
    lbl4 = tkinter.Label(frame, text="Food:", bg="gray")
    lbl4.config(font=('Helvetica bold', 20))
    lbl4.place(x=350, y=120)
    global three
    three = StringVar(frame)
    three.set("Default")  # default value
    # drop3 = OptionMenu(frame, three, "Default", "Food ASC.", "Food DESC.", "None")
    # drop3.config(bg="orange", fg="white")
    # drop3.place(x=400, y=170)

    lbl5 = tkinter.Label(frame, text="Showtime:", bg="gray")
    lbl5.config(font=('Helvetica bold', 20))
    lbl5.place(x=480, y=120)
    global four
    four = StringVar(frame)
    four.set("Default")  # default value
    # drop4 = OptionMenu(frame, four, "Default", "Time ASC.", "Time DESC.", "None")
    # drop4.config(bg="orange", fg="white")
    # drop4.place(x=580, y=170)

    lbl6 = tkinter.Label(frame, text="Movie:", bg="gray")
    lbl6.config(font=('Helvetica bold', 20))
    lbl6.place(x=640, y=120)
    global five
    five = StringVar(frame)
    five.set("Default")  # default value
    # drop5 = OptionMenu(frame, five, "Default", "Movie ASC.", "Movie DESC.", "None")
    # drop5.config(bg="orange", fg="white")
    # drop5.place(x=770, y=170)

    lbl7 = tkinter.Label(frame, text="Price:", bg="gray")
    lbl7.config(font=('Helvetica bold', 20))
    lbl7.place(x=780, y=120)

    printButton6 = tkinter.Button(frame, text="Back", command=order, width=15, height=7, bg="black", fg="white")
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