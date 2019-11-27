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
![enter image description here](https://picasaweb.google.com/108798089808399014631/6764096883501894529#6764096889665217026 "Application window")
Any invalidity needs to be ruled out, thus the following constraints need to be satisfied.
###  Constraints satisfied :
- User cannot leave an empty field.
- If the user has already checked-in and has not checked out, he cannot check-in
- If the user has already checked out, he cannot check-out before another check-in.
- The Email-id of the host as well as the visitor should be valid.
- Host and visitor cannot have the same email-id.
- The phone number of the host as well as the visitor should be valid.
- Host and visitor cannot have the same phone number.

### Usage :

 
***Check In -*** After the user enters valid details and clicks on the '*Check In*' button, he will be prompted with a message of successful check-in. Then, an **Email** as well as an **SMS** will be sent to the host. Meanwhile,  all the entries will be updated in the database.

***Check Out -*** If the visitor wants to check-out, he needs to click on the  '*Go to Check Out*' button. Then a window will show up where-in he will be prompted to enter his email address. Invalid email address or an empty field will result in a popup message. After entering his email address

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
## Create files and folders

The file explorer is accessible using the button in left corner of the navigation bar. You can create a new file by clicking the **New file** button in the file explorer. You can also create folders by clicking the **New folder** button.

## Switch to another file

All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.

## Rename a file

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## Delete a file

You can delete the current file by clicking the **Remove** button in the file explorer. The file will be moved into the **Trash** folder and automatically deleted after 7 days of inactivity.

## Export a file

You can export the current file by clicking **Export to disk** in the menu. You can choose to export the file as plain Markdown, as HTML using a Handlebars template or as a PDF.


# Synchronization

Synchronization is one of the biggest features of StackEdit. It enables you to synchronize any file in your workspace with other files stored in your **Google Drive**, your **Dropbox** and your **GitHub** accounts. This allows you to keep writing on other devices, collaborate with people you share the file with, integrate easily into your workflow... The synchronization mechanism takes place every minute in the background, downloading, merging, and uploading file modifications.

There are two types of synchronization and they can complement each other:

- The workspace synchronization will sync all your files, folders and settings automatically. This will allow you to fetch your workspace on any other device.
	> To start syncing your workspace, just sign in with Google in the menu.

- The file synchronization will keep one file of the workspace synced with one or multiple files in **Google Drive**, **Dropbox** or **GitHub**.
	> Before starting to sync files, you must link an account in the **Synchronize** sub-menu.

## Open a file

You can open a file from **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Open from**. Once opened in the workspace, any modification in the file will be automatically synced.

## Save a file

You can save any file of the workspace to **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Save on**. Even if a file in the workspace is already synced, you can save it to another location. StackEdit can sync one file with multiple locations and accounts.

## Synchronize a file

Once your file is linked to a synchronized location, StackEdit will periodically synchronize it by downloading/uploading any modification. A merge will be performed if necessary and conflicts will be resolved.

If you just have modified your file and you want to force syncing, click the **Synchronize now** button in the navigation bar.

> **Note:** The **Synchronize now** button is disabled if you have no file to synchronize.

## Manage file synchronization

Since one file can be synced with multiple locations, you can list and manage synchronized locations by clicking **File synchronization** in the **Synchronize** sub-menu. This allows you to list and remove synchronized locations that are linked to your file.


# Publication

Publishing in StackEdit makes it simple for you to publish online your files. Once you're happy with a file, you can publish it to different hosting platforms like **Blogger**, **Dropbox**, **Gist**, **GitHub**, **Google Drive**, **WordPress** and **Zendesk**. With [Handlebars templates](http://handlebarsjs.com/), you have full control over what you export.

> Before starting to publish, you must link an account in the **Publish** sub-menu.

## Publish a File

You can publish your file by opening the **Publish** sub-menu and by clicking **Publish to**. For some locations, you can choose between the following formats:

- Markdown: publish the Markdown text on a website that can interpret it (**GitHub** for instance),
- HTML: publish the file converted to HTML via a Handlebars template (on a blog for example).

## Update a publication

After publishing, StackEdit keeps your file linked to that publication which makes it easy for you to re-publish it. Once you have modified your file and you want to update your publication, click on the **Publish now** button in the navigation bar.

> **Note:** The **Publish now** button is disabled if your file has not been published yet.

## Manage file publication

Since one file can be published to multiple locations, you can list and manage publish locations by clicking **File publication** in the **Publish** sub-menu. This allows you to list and remove publication locations that are linked to your file.


# Markdown extensions

StackEdit extends the standard Markdown syntax by adding extra **Markdown extensions**, providing you with some nice features.

> **ProTip:** You can disable any **Markdown extension** in the **File properties** dialog.


## SmartyPants

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|                |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|


## KaTeX

You can render LaTeX mathematical expressions using [KaTeX](https://khan.github.io/KaTeX/):

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> You can find more information about **LaTeX** mathematical expressions [here](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).


## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```
