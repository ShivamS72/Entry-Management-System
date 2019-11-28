# This module is used to do send SMS as well as check phone number validity

# Import the necessary modules
from twilio.rest import Client
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
import requests
from Config import AUTH_TOKEN


# This function checks if the phone number user entered is valid or not
def checkPhoneValidity(ph):
    ph = "+91" + ph
    x = False
    try:
        x = carrier._is_mobile(number_type(phonenumbers.parse(ph)))

    except Exception as e:
        print(e)
        print("Invalid phone number")
    return x


# This function sends an sms to the the Host with the required details
# The message facility used is Fast 2 SMS
def smsHost(recp, m):
    # Fast 2 SMS URL
    url = "https://www.fast2sms.com/dev/bulk"

    # Creating the payload to be sent
    payload = "sender_id=FSTSMS&message=" + m + "&language=english&route=p&numbers=" + recp
    headers = {
        'authorization': AUTH_TOKEN,
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    # Send SMS
    response = requests.request("POST", url, data=payload, headers=headers)

    # Print response on terminal
    print(response.text)
