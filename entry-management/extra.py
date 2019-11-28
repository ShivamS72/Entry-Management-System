import smtplib
# This function sends an email to the Host with the required details
# A new Gmail account was created for the purpose
def emailHost(vName, vEmail, vPhone, hName, hEmail, hPhone):
    # Port number
    port = 587
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Login in to the gmail account
    s.login("innovacerhelp@gmail.com", "innovacer")

    # Text body of the email
    text = vName + " would like to visit you \nContact : " + vPhone + "\nEmail     :" + vEmail
    # Subject of the email
    subject = "Someone is here to visit you"

    # Message to be sent, includes subject as well as text body
    message = 'Subject: {}\n\n{}'.format(subject, text)

    # Print message on terminal
    print("Sendig Email to host..")

    # Send email
    s.sendmail("innovacerhelp@gmail.com", hEmail, message)

    # Print message on terminal
    print("Email sent successfully")

    # Terminate session
    s.quit()


# This function sends an email to the Visitor with the required details
# A new gmail account was created for the purpose
def emailVisitor(vName, vEmail, vPhone, hName, hEmail, hPhone, iTime, oTime, addr):
    # Port number
    port = 587
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Login in to the gmail account
    s.login("innovacerhelp@gmail.com", "innovacer")

    # Text body of the email
    text = vName + ", Here are your visit details : \nPhone : " + vPhone + "\nCheck In Time : " + iTime + \
           "\nCheck Out Time : " + oTime + "\nHost : " + hName + "\nAddress Visited : " + addr
    # Subject of the email
    subject = "Thanks for your visit!"

    # Message to be sent, includes subject as well as text body
    message = 'Subject: {}\n\n{}'.format(subject, text)

    # Print message on terminal
    print("Sending Email to Visitor..")

    # Send email
    s.sendmail("innovacerhelp@gmail.com", hEmail, message)

    # Print message on terminal
    print("Email sent successfully")

    # Terminate session
    s.quit()

def smsHost2(recp, m):
    # ID and token of Twilio account
    account_sid = 'ACf7cbb938361df37fbd7aec229fc84250'
    auth_token = '9e3cca774b049d252e9c0a9abea5386f'

    # The required message

    client = Client(account_sid, auth_token)

    # Print information on terminal
    print("Sending SMS to host..")
    # Send sms
    message = client.messages.create(body=m, from_='+16788253871', to=recp)

    # Print reference id on terminal
    print("SMS sent, Reference id:", message.sid)