# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACfb24aebb5ee315c5e4f5093719d03887'
auth_token = '5a3d76fba7b84f09c8a5a3e6d96fe3c9'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="twilio를 통한 Package 실습",
                     from_='+12019322228',
                     to='+821066592628'
                 )

print(message.sid)
