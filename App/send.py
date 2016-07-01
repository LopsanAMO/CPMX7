from twilio.rest import TwilioRestClient
from twilio import twiml

def mensajes(mensaje):
    ACCOUNT_SID = "ACd29836c6dfff4b8edbf3114ebe698938"
    AUTH_TOKEN = "5a2088fc51efa56bd511240a1fba498b"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
    	to="+525569626596",
    	from_="12513334049",
    	body=mensaje,
    )
