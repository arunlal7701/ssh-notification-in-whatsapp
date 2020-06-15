#/usr/bin/python3.7

from twilio.rest import Client
from sh import tail

# Your Account SID from twilio.com/console
account_sid = "AC43910e6cc2767b7664265adf96ec7304"
# Your Auth Token from twilio.com/console
auth_token  = "89ad4216e5fdb62264a61fde9142ea52"

client = Client(account_sid, auth_token)

for line in tail("-f", "/var/log/auth.log", _iter=True):
    k = line.split()
    if k[5] == 'Accepted':
        mess = 'login sucessful from' + k[10]

        

        message = client.messages.create(
            to="whatsapp:+91 9744031178",
            from_="whatsapp:+14155238886",
            body=mess)

#print(message.sid)
