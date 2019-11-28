# This module is used to make changes to the database

# Import the necessary modules
from datetime import datetime
import mysql.connector
from Config import MYSQL_ID, MYSQL_PASSWORD


# This functions creates entry database if no such database exists
def createDatabase():
    # Establish connection, create a database and table in try block
    try:
        # Establishing connection
        db = mysql.connector.connect(host="localhost", user=MYSQL_ID, passwd=MYSQL_PASSWORD,
                                     auth_plugin='mysql_native_password')
        cr = db.cursor()

        # Query to create a database
        formula = "create database entrym ;"
        cr.execute(formula)

        print("Database created")

        # Commit changes to database
        db.commit()

        # Query to use the database created
        formula = "use entrym ;"
        cr.execute(formula)
        cr = db.cursor()

        # Query to create a table
        formula = "create table visitor (vName varchar (255), vEmail varchar(255) PRIMARY KEY , vPhone varchar(255));"
        # Execute the above query
        cr.execute(formula)

        # Query to create a table
        formula = "create table host (hName varchar (255), hEmail varchar(255) PRIMARY KEY, hPhone varchar(255), " \
                  "addr varchar(255)); "
        # Execute the above query
        cr.execute(formula)

        # Query to create a table
        formula = "create table time (vEmail varchar (255), hEmail varchar(255), iTime varchar(255), oTime varchar(" \
                  "255),PRIMARY KEY (vEmail,hEmail,iTime)); "
        # Execute the above query
        cr.execute(formula)

        # Print on the terminal
        print("Table created")

        # Commit changes to database
        db.commit()

    # If such a database or table already exists in the database, display a result on terminal
    except Exception as e:
        print(e)
        print("Database already exists on the system")

    # Initiate a call to mainWindow() to create a window


# This function adds the user details to the database
def addToDatabase(vName, vEmail, vPhone, hName, hEmail, hPhone, addr):
    # Establishing connection to database jwt
    db = mysql.connector.connect(host="localhost", user=MYSQL_ID, passwd=MYSQL_PASSWORD,
                                 auth_plugin='mysql_native_password', database="entrym")
    cr = db.cursor()

    # Fetch timestamp from the system
    now = datetime.now()
    # Converting it into MM/DD/YYYY, HH:MM:SS format
    iTime = now.strftime("%m/%d/%Y, %H:%M:%S")

    # Print the In-time on the terminal
    print("Check in time : ", iTime)
    try:
        formula = "insert into visitor (vName, vEmail, vPhone) values (%s,%s,%s)"
        user1 = (vName, vEmail, vPhone)
        # Execute the above query
        cr.execute(formula, user1)
    except:
        print("visitor already exists")

    try:
        formula = "insert into host (hName, hEmail, hPhone, addr) values (%s,%s,%s,%s)"
        user1 = (hName, hEmail, hPhone, addr)
        # Execute the above query
        cr.execute(formula, user1)
    except:
        print("host already exists")

    formula = "insert into time (vEmail, hEmail, iTime,oTime) values (%s,%s,%s,%s)"
    user1 = (vEmail, hEmail, iTime, "")
    # Execute the above query
    cr.execute(formula, user1)

    # Commit changes to the database
    db.commit()


# This function updates the necessary changes to the database
def updateDatabase(user):
    # Establishing connection to database jwt
    db = mysql.connector.connect(host="localhost", user=MYSQL_ID, passwd=MYSQL_PASSWORD,
                                 auth_plugin='mysql_native_password', database="entrym")
    cr = db.cursor()

    formula2 = "delete from time where iTime=%s ;"
    # Execute the above query
    cr.execute(formula2, (user[6],))

    user1 = (user[1], user[4], user[6], user[7])

    formula = "insert into time (vEmail, hEmail, iTime,oTime) values (%s,%s,%s,%s)"
    # Execute the above query
    cr.execute(formula, user1)

    # Commit changes to the database
    db.commit()
