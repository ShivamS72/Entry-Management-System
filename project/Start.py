# This module is the initiator of the application

# Import the necessary modules
from Gui import *
from Database import *


# Through out all modules various variables have been used, some of which stand for the following:
# vName  - Visitor's name
# vEmail - Visitor's email
# vPhone - Visitor's phone number
# hName  - Host's name
# hEmail - Host's email
# hPhone - Host's phone number
# addr   - Address of the location


# This functions starts the application and calls the necessary functions
def start():

    # Call createDatabase() to create database jwt if no database exists
    createDatabase()

    # Call mainWindow() to show a user-interactive window
    mainWindow()


# Calls the start() function to start the application
start()
