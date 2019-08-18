from twilio.rest import Client

def send_sms(heavy_text):
	account_sid = "New"

	auth_token  = "New"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="+918007912787", 
	    from_="+17862458969",
	    body=heavy_text)

	#print(message.sid)