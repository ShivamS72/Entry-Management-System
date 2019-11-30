# This module is used to perform utilities related to check-out

# Import the necessary modules
from Email import *
from tkinter import messagebox
from Database import *
import mysql.connector
from datetime import datetime
from Config import MYSQL_ID, MYSQL_PASSWORD


# This functions searches the user in the database and checks whether check-out is applicable or not
def checkOut(vEmail):
    # Connect to the database jwt
    db = mysql.connector.connect(host="localhost", user=MYSQL_ID, passwd=MYSQL_PASSWORD,
                                 auth_plugin='mysql_native_password',
                                 database='entrym')
    cr = db.cursor()

    # Query to fetch entries with visitor's email
    formula = "select A.vName,A.vPhone,A.vEmail,B.hName,B.hEmail,B.hPhone,C.iTime,C.oTime,B.addr" \
              " from (time as C) inner join (visitor as A) on A.vEmail=C.vEmail inner join " \
              "(host as B) on C.hEmail=B.hEmail where A.vEmail=%s ORDER BY iTime ASC; "

    #select A.vName,A.vPhone,A.vEmail,B.hName,B.hEmail,B.hPhone,C.iTime,C.oTime,B.addr from time as C cross join visitor as A cross join host as B where A.vEmail="17ucs150@lnmiit.ac.in"
    # Execute the above query
    cr.execute(formula, (vEmail,))

    # Take null values in these variables
    vName = ""
    vPhone = ""
    hName = ""
    hEmail = ""
    hPhone = ""
    iTime = ""
    oTime = ""
    addr = ""

    # Fetch all the entries and store them in the database
    result = cr.fetchall()

    # If there are no entries with the specified email, check-out is invalid
    if not result:
        messagebox.showerror("Alert", "Please enter valid Email-id")

    # If there are entries with the specifief email
    else:

        # This loop ends with fetching the data of the last entry
        # Previous entries are not checked as the visitor might have checked in earlier also and then checked out
        # If check-out is valid or not, depends on the last entry
        # If the Check-out time in the last entry is null, that means that the visitor can check-out
        # else check-out is not applicable as the visitor has already checked-out
        for i in result:
            # Retrieve visitor's information from the last entry
            vName = i[0]
            vPhone = i[2]
            hName = i[3]
            hEmail = i[4]
            hPhone = i[5]
            iTime = i[6]
            oTime = i[7]
            addr = i[8]
        print("oTime:"+oTime)
        # If check-out time is not null, the visitor has already checked out
        if oTime:

            messagebox.showerror("Alert", "You have already checked out!")
            print("The user has already checked out")

        # Check-out is valid
        else:

            # Fetch the check-out time from the system
            out_time = datetime.now()
            # Converting it into MM/DD/YYYY, HH:MM:SS format
            oTime = out_time.strftime("%m/%d/%Y, %H:%M:%S")

            # Display check-out time on the terminal
            print("Check out time : ", oTime)
            user1 = (vName, vEmail, vPhone, hName, hEmail, hPhone, iTime, oTime, addr)

            # Update the database with check-out time
            updateDatabase(user1)

            # Show message alert of check-out
            messagebox.showinfo("Alert", "Checked-out successfully")

            # Email text
            text = vName + ", Here are your visit details : \nPhone : " + vPhone + "\nCheck In Time : " + iTime + \
                   "\nCheck Out Time : " + oTime + "\nHost : " + hName + "\nAddress Visited : " + addr
            # Subject of the email
            subject = "Thanks for your visit!"

            # Send email
            email(vEmail, subject, text)
