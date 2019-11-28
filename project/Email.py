# This module is used to send email to a user

# Import the necessary modules
import smtplib
from Config import  USER_ID, PASSWORD


# This function is used to send an email
def email(recp, subject, text):
    # Port number
    port = 587
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Login in to the gmail account
    s.login(USER_ID, PASSWORD)

    # Text body of the email

    # Message to be sent, includes subject as well as text body
    message = 'Subject: {}\n\n{}'.format(subject, text)

    # Print message on terminal
    print("Sending Email to " + recp + " ..")

    # Send email
    s.sendmail("innovacerhelp@gmail.com", recp, message)

    # Print message on terminal
    print("Email sent successfully")

    # Terminate session
    s.quit()
