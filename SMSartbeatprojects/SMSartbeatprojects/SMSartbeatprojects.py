# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:52:30 2017

@author: Ivan artbeatprojects
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe4f4d1f43b8657b4220e2a2ac4a0084d" #ACCOUNT SID

# Your Auth Token from twilio.com/console
auth_token  = "abbdf0701bc514fe6097358e9ca1eddb" #AUTH TOKEN

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+447518 527690",  # replace with your phone number
    from_="+441344567837", # replace with your twilio number for artbeatprojects
    body="Hello from Python!")

print(message.sid)
