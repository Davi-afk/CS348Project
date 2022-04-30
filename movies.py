import tkinter #for gui design and implementation
import mysql.connector
from mysql.connector.constants import ClientFlag #for connecting to google cloud
def insertMovies(cursor, cnxn):
    # Top level window
        frame = tkinter.Tk()  # creates a gui window
        frame.title("TextBox Input")  # sets window title
        frame.geometry('1000x500')  # sets window size

        # Function for getting Input from textbox and table results to label widget
        def printInput():
                inp = inputtxt.get(1.0, "end-1c")  # gets input from first box
                inp2 = inputtxt2.get(1.0, "end-1c")  # gets input from second box
                inp3 = inputtxt3.get(1.0, "end-1c")  # gets input from third box
                inp4 = inputtxt4.get(1.0, "end-1c")
                # query to insert inputted data into movie table
                query = (
                        "INSERT INTO Movies (Movie_ID, Name, Release_Date, Runtime) VALUES(%s, %s, %s, %s)")  # query for prepared statement
                tuple1 = (inp, inp2, inp3, inp4)  # adding info to prepared statement
                cursor.execute(query, tuple1)  # executing query
                cnxn.commit()  # commits changes
                cursor.execute("CALL sp_GetMovies")  # query to get rows of movie table with stored procedure
                out = cursor.fetchall()
                for row in out:  # puts each row into label to be displayed in gui
                    lbl = tkinter.Label(frame, text=row)
                    lbl.pack()
                    print(row)
        # TextBox and their labels Creation
        lbl = tkinter.Label(frame, text="Movie ID")
        lbl.pack()
        inputtxt = tkinter.Text(frame, height=1, width=20)
        inputtxt.pack()
        lbl = tkinter.Label(frame, text="Movie Name")
        lbl.pack()
        inputtxt2 = tkinter.Text(frame, height=1, width=20)
        inputtxt2.pack()
        lbl = tkinter.Label(frame, text="Release Release_Date")
        lbl.pack()
        inputtxt3 = tkinter.Text(frame, height=1, width=20)
        inputtxt3.pack()
        lbl = tkinter.Label(frame, text="Runtime")
        lbl.pack()
        inputtxt4 = tkinter.Text(frame, height=1, width=20)
        inputtxt4.pack()

        # Button Creation
        printButton = tkinter.Button(frame, text="Enter", command=printInput)
        printButton.pack()

        # runs gui and closes connection to database
        frame.mainloop()
        cnxn.close()
