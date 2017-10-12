
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:52:30 2017

@author: Ivan inecsoft
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc02cb8f48ad629283c12c60a7e5f0356" #ACCOUNT SID

# Your Auth Token from twilio.com/console
auth_token  = "8e3645e4b93954b2f73edab3cb7a2e9a" #AUTH TOKEN

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+447518 527690",  # replace with your phone number
    #from_="+441865951142", # replace with your twilio number for inecsoft
	from_="+441344567837", # replace with your twilio number for artbeatprojects
    body="Hello from Python!")

print(message.sid)