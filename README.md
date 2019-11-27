#  Entry Management System

Innovaccer SummerGeeks 2020 SDE-Intern Assignment.

## Description

This software manages the visitors in and outside office.
  - Captures the name, email address, phone no of the visitor and the same information for the host on the front end.
  - Once the user enters the information in the form, the backend stores all of the information with time stamp of the entry.
  - An email and an SMS is sent the host informing him of the details of the visitor, when he checks-in
  - An email is sent to the visitor when he checks-out sending him details of his visit
  - Check-out time is stored into the database when the user checks-out


## Tech Stack

* [Python](https://www.python.org/about/) - Version 3.7
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - Standard Python interface to the Tk GUI toolkit
* [MySQL](https://www.mysql.com/) - Relational database management system
* [Twilio  ](https://www.twilio.com/)  - Cloud communications platform
* [smtplib](https://docs.python.org/3/library/smtplib.html) - SMTP protocol client used to send email

## Installation 

On Windows, please  install [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) .
To install dependencies, run the following command :
```sh 
pip install -r requirements.txt
```

in ```Config.py``` please update the following details:
```
USER_ID = "Your Email ID"
PASSWORD = "Your Email ID password"
MYSQL_ID = "Your MySQL ID"  
MYSQL_PASSWORD = "Your MySQL password"
AUTH_TOKEN = "Your Fast 2 SMS authorization key"
```
Please turn on access to **less secure apps** from your gmail account.

## Working
To start the application, please run the following command from terminal:
```
python start.py
```
After executing the above command, the user is prompted with a window ,  where he needs to fill the host as well as the visitor's details. 
![Check-in window](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/CheckInWindow.PNG)
Any invalidity needs to be ruled out, thus the following constraints need to be satisfied.
###  Constraints satisfied :
- User cannot leave an empty field.

     ![Empty fields](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/empty.PNG)

- If the user has already checked-in and has not checked out, he cannot check-in.

     ![Already Checked In](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/AlreadyCheckedIn.PNG)
- If the user has already checked out, he cannot check-out before another check-in.
     
     ![AlreadyCheckedOut](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/AlreadyCheckedOut.PNG)
- The Email-id of the host as well as the visitor should be valid.

     ![Invalid Email](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/InvalidEmail.PNG)
- Host and visitor cannot have the same email-id.

     ![Same Email](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/SameEmail.PNG)
- The phone number of the host as well as the visitor should be valid.

     ![Invalid Phone](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/InvalidPhone.PNG)
- Host and visitor cannot have the same phone number.
     
     ![Same Phone Number](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/SamePhone.PNG)

### Usage :

 
***Check In -*** After the user enters valid details and clicks on the '*Check In*' button, he will be prompted with a message of successful check-in. Then, an **Email** as well as an **SMS** will be sent to the host. Meanwhile,  all the entries will be updated in the database.

![Check In Window](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/CheckIn.PNG)

***Check Out -*** If the visitor wants to check-out, he needs to click on the  '*Go to Check Out*' button. Then a window will show up where-in he will be prompted to enter his email address. Invalid email address or an empty field will result in a popup message. After entering his email address, he needs to click on '*Check Out*' button. Then his check out time will be updated in the database.

   ![Check Out Window](https://github.com/ShivamS72/Entry-Management-System/blob/master/images/CheckOut.PNG)


If another visitor wants to check-in, valid details should be filled in and the Check In button should be clicked upon. 

## Database Design

```
entry
 |
 |--users
      |--vName
      |--vEmail
      |--vPhone
      |--hName
      |--hEmail
      |--hPhone
      |--iTime
      |--oTime
      |--addr
```
The following variables denote the following :
- vName - Visitor's name
- vEmail - Visitor's email address
- vPhone - Visitor's phone number
- hName - Visitor's name
- hEmail - Visitor's email address
- hPhone - Visitor's phone number
- iTime - Check-In time of the visitor
- oTime - Check-Out time of the visitor
- addr - Address of the building

