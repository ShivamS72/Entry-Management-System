# This module checks whether check-in is valid or not, if valid calls necessary functions to add details to database

# Import the necessary modules
from Phone import *
from tkinter import messagebox
from Database import *
from Email import *
import mysql.connector
from validate_email import validate_email
from Config import MYSQL_ID, MYSQL_PASSWORD

# This function checks if the check-In is permitted and if yes then calls another function to add details to database
def checkIn(vName, vEmail, vPhone, hName, hEmail, hPhone, addr):

    # If any field is null, display appropriate message
    if (not vPhone) or (not vEmail) or (not hEmail) or (not hPhone) or (not vName) or (not hName) or (not addr):
        messagebox.showerror("Alert", "Please fill all the fields")

    # Check if the visitor's Phone number is valid or not
    elif not checkPhoneValidity(vPhone):
        messagebox.showerror("Alert", "Visitor's phone number is invalid")

    # Check if the host's Phone number is valid or not
    elif not checkPhoneValidity(hPhone):
        messagebox.showerror("Alert", "Host's phone number is invalid")

    # Check if the visitor and host's phone are same or not
    elif vPhone == hPhone:
        messagebox.showerror("Alert", "Host and visitor's phone number cannot be same")

    # Check if the visitor and host's email are same or not
    elif vEmail == hEmail:
        messagebox.showerror("Alert", "Host and visitor's email cannot be same")

    # Check if the visitor's email is valid or not
    elif not validate_email(vEmail, verify=True):
        messagebox.showerror("Alert", "Visitor's email is invalid")

    # Check if the host's email is valid or not
    elif not validate_email(hEmail, verify=True):
        messagebox.showerror("Alert", "Host's email is invalid")

    # Checking whether the values are null or not
    else:

        # Check if the user has already checked in or not
        # A cheked in visitor cannot check in again if he is still in the building
        flag = checkIfAlreadyCheckedIn(vEmail)

        # If he is still in the building, display appropriate error
        if flag:

            print("Check In not possible as the user has already checked in")
            messagebox.showerror("Alert", "Already checked in")

        # If all details are valid, allow him to check in
        else:

            # Display check-in success to the user
            messagebox.showinfo("Alert", "Check-In successful")

            addToDatabase(vName, vEmail, vPhone, hName, hEmail, hPhone, addr)

            # Send email to the host with visitor's details
            text = vName + " would like to visit you \nContact : " + vPhone + "\nEmail     :" + vEmail
            # Subject of the email
            subject = "Someone is here to visit you"
            email(hEmail, subject, text)
            # Send SMS to the host with visitor's details
            m = vName + " is here to visit you \n Contact : " + vPhone + "\nEmail :" + vEmail
            smsHost(hPhone,m)


# This function check whether the visitor has already checked in or not
# return true if he is still in the building else false
def checkIfAlreadyCheckedIn(vEmail):

    # Connect to the database
    db = mysql.connector.connect(host="localhost", user=MYSQL_ID, passwd=MYSQL_PASSWORD, auth_plugin='mysql_native_password',
                                 database="entrym")
    cr = db.cursor()

    formula = "select * from time where vEmail=%s ;"
    # Execute the above query
    cr.execute(formula, (vEmail,))

    # Fetch all the entries with the visitor's email
    result = cr.fetchall()

    # If there are no entries in the result, return false
    if not result:
        return False

    # If result contains entries
    else:
        oTime = ""
        iTime = ""

        # Go to the last entry
        for i in result:
            iTime = i[2]
            oTime = i[3]

        # IF the check-out time is null, return true
        if not oTime:
            return True
        # Check-in not allowed
        else:
            return False
