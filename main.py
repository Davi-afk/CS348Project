import tkinter #for gui design and implementation
import mysql.connector
from mysql.connector.constants import ClientFlag #for connecting to google cloud
import employees
from movies import insertMovies
from orders import vars
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
"""Look in info.txt for information about what tables and stored procedures there are"""

query = ("SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED") #query to set transaction isolation level
cursor.execute(query) #executes query
cnxn.commit()  # commit changes
cursor.execute("SHOW TABLES") #gets all tables
out = cursor.fetchall() #stores query result in variable
for row in out: #prints out each row to terminal
    print(row)

def restart(): #makes a new main window then starts the loop
    global frame
    frame = tkinter.Tk()  # creates a gui window
    frame.title("Welcome")  # sets window title
    frame.geometry('1200x800')  # sets window size
    frame['bg'] = 'gray'
    loop()
def movies(): #add the call to movies
    for widget in frame.winfo_children():
        widget.destroy()
    insertMovies(cursor, cnxn, frame)
def orders(): #add the call to orders
    vars(cursor, cnxn, frame)
def chooseEmployee(): #gets rid of the widgets on the frame so it can be reused and then calls employees
    for widget in frame.winfo_children():
        widget.destroy()
    employees.vars(cursor, cnxn, frame)
def loop(): #sets up the labels and buttons for the main menu
    lbl = tkinter.Label(frame, text="Welcome to Computer Science Cinemas", bg="gray") #label bg is background color
    lbl.config(font=('Helvetica bold',40)) #sets font and size
    lbl.pack() #puts label at top
    lbl2 = tkinter.Label(frame, text="please select which category you would like to change or view", bg="gray")
    lbl2.config(font=('Helvetica bold',20))
    lbl2.pack()
    printButton = tkinter.Button(frame, text="Movies", command=movies, width=20, height=10, bg="blue", fg="white") #sets width, height, background color and text color for the button
    printButton.place(x = 200, y = 300) #sets the button where the x and y coordinates are
    printButton.config(font=('Helvetica bold',15))
    printButton2 = tkinter.Button(frame, text="Employees", command=chooseEmployee, width=20, height=10, bg="orange", fg="white")
    printButton2.place(x = 500, y = 300)
    printButton2.config(font=('Helvetica bold',15))
    printButton3 = tkinter.Button(frame, text="Orders", command=orders, width=20, height=10, bg="blue", fg="white")
    printButton3.place(x = 800, y = 300)
    printButton3.config(font=('Helvetica bold',15))
    frame.mainloop()#needed to make all the widgets display
restart()#starts the first loop


