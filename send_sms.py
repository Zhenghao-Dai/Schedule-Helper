from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc2eeb3fef1d869dcf306d1d8baec940a'
auth_token = 'c50abee06ec554616f15f18a8b942695'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='下周不想和我出去完了么!',
                              from_='+12132773001',
                              to= '+8615850802522'   #"+8618258170767" #'+8615850802522'
                          )

print(message.sid)