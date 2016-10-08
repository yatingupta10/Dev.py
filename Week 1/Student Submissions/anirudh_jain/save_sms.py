from twilio.rest import TwilioRestClient

account_sid = "{{ account_sid }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ auth_token }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="This thing is so damn cool !!!",
    to="+918527990741",    # Replace with your phone number
    from_="+12052094841") # Replace with your Twilio number

print(message.sid)