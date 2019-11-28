# This module is used to create user interface

# Import the necessary modules
from CheckOut import *
from CheckIn import *
from tkinter import *
import tkinter as tk


# This function creates the main window
def mainWindow():
    # A window is created
    window = Tk()

    # Title of the window is set to entry management
    window.title('Entry management')

    # The size of the window is set to 400x400
    window.geometry("400x450")

    # Display icon on the window
    window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='x.png'))

    # A background colour is added to the window
    c = Canvas(window, bg="#010b14", height="2000", width="2000")
    c.pack()

    # An image is added to the window in the following steps
    img = PhotoImage(file="image.png")
    img = img.subsample(4)
    c.create_image(50, 366, anchor=NW, image=img)

    label = Label(window, bg="#010b14", fg="white", text="Visitor's Details", font='40')
    label.place(x=155, y=10)

    # Label is created for visitor's name
    label = Label(window, bg="#010b14", fg="white", text="Name")
    label.place(x=84, y=10 + 35)
    # Entry space for visitor's name
    t1 = Entry(window, text="")
    t1.place(x=150, y=10 + 35)

    # Label is created for visitor's email
    label = Label(window, bg="#010b14", fg="white", text="Email")
    label.place(x=84, y=35 + 35)
    # Entry space for visitor's email
    t2 = Entry(window, text="")
    t2.place(x=150, y=35 + 35)

    # Label is created for visitor's phone number
    label = Label(window, bg="#010b14", fg="white", text="Phone")
    label.place(x=84, y=60 + 35)
    # Entry space for visitor's phone number
    t3 = Entry(window, text="")
    t3.place(x=150, y=60 + 35)

    label = Label(window, bg="#010b14", fg="white", text="Host's Details", font='40')
    label.place(x=160, y=131)

    # Label is created for host's name
    label = Label(window, bg="#010b14", fg="white", text="Name")
    label.place(x=84, y=85 + 81)
    # Entry space for host's name
    t4 = Entry(window, text="")
    t4.place(x=150, y=85 + 81)

    # Label is created for host's email
    label = Label(window, bg="#010b14", fg="white", text="Email")
    label.place(x=84, y=110 + 81)
    # Entry space for host's email
    t5 = Entry(window, text="")
    t5.place(x=150, y=110 + 81)

    # Label is created for host's phone number
    label = Label(window, bg="#010b14", fg="white", text="Phone")
    label.place(x=84, y=135 + 81)
    # Entry space for host's phone number
    t6 = Entry(window, text="")
    t6.place(x=150, y=135 + 81)

    # Label is created for Address of the location
    label = Label(window, bg="#010b14", fg="white", text="Address")
    label.place(x=84, y=160 + 81)
    # Entry space for  Address of the location
    t7 = Entry(window, text="")
    t7.place(x=150, y=160 + 81)

    # A button for Check-In is created which triggers the checkIn() function to perform the required operation
    btn = Button(window, bg="#ff0800", fg='white', text="Check In",
                 command=lambda: checkIn(t1.get(), t2.get(), t3.get(), t4.get(), t5.get(), t6.get(), t7.get()))
    # Place the button the specified co-ordinates
    btn.place(x=174, y=195 + 91)
    btn.bind("<Button-1>")

    # A button for Check-In is created which triggers the checkOut() function to perform the required operation
    btn2 = Button(window, bg="#ff0800", fg='white', text="Go to Check Out")
    # Place the button the specified co-ordinates
    btn2.place(x=154, y=225 + 95)
    # Bind the button to Check-Out window
    btn2.bind("<Button-1>", checkOutWindow)

    window.mainloop()


# This function creates a window for check-out
def checkOutWindow(event):
    # Create a check-out window
    window = Tk()
    window.title('Check-out')
    # Set size
    window.geometry("400x100+10+10")

    # Set background
    c = Canvas(window, bg="#010b14", height="500", width="500")
    c.pack()

    # Label for visitor's email
    # As email is unique for everybody, it can be used for check-out
    label = Label(window, bg="#010b14", text="Visitor's email", fg="white")
    label.place(x=60, y=10)
    # Entry for visitor's email
    t7 = Entry(window, text="")
    t7.place(x=150, y=10)

    # Button for check-out, triggers the checkOut() functions which does the required task
    btn = Button(window, text="Check Out", bg="red", fg='white', command=lambda: checkOut(t7.get()))
    btn.place(x=140, y=50)
    btn.bind("<Button-1>")
