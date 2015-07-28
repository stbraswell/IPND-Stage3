from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC8238efca904dd9e838cdea89dc2db87a"
auth_token  = "e6e70341d0b7b4eba8cbb9891bc8ab65"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="I Love You! -Troy",
    to="+15305203250",    # Replace with your phone number / cannot send to others unless you pay twilio
    from_="+14152341552") # Replace with your Twilio number
print message.sid
