from itty import *
import urllib2
import json
from ciscosparkapi import CiscoSparkAPI
import config
import time

os.environ['SPARK_ACCESS_TOKEN'] = config.spark_token

api = CiscoSparkAPI() 


def processMessage(message):
    for message in messages:
        if (message.personId != botId): #message from other person
            _text = message.text + "BOT";
            _roomId = message.roomId
            api.messages.create(roomId=_roomId, toPersonId=None, toPersonEmail=None,text=_text,markdown=None,files=None)
            break
    # else:
    #     break
    

def getBotId():
    _me = api.people.me()
    return _me.id

@post('/')
def index(request):
    """
    When messages come in from the webhook, they are processed here.  The message text needs to be retrieved from Spark,
    using the sendSparkGet() function.  The message text is parsed.  If an expected command is found in the message,
    further actions are taken. i.e.
    /batman    - replies to the room with text
    /batcave   - echoes the incoming text to the room
    /batsignal - replies to the room with an image
    """
    print("Webhook received")
    webhook = json.loads(request.body)
    print(webhook)
    messageId = format(webhook['data']['id'])
    roomId = format(webhook['data']['roomId'])
    message = api.messages.get(messageId)
    text = message.text
    print("Message text: " + text)
    return "true"







####CHANGE THESE VALUES#####
# bot_email = "merakify@sparkbot.io"
# bot_name = "Merakify"
# bat_signal  = "https://upload.wikimedia.org/wikipedia/en/c/c6/Bat-signal_1989_film.jpg"
botId = getBotId()
run_itty(server='wsgiref', host='0.0.0.0', port=3010)


# if __name__ == '__main__':

#     while True:
#         rooms = api.rooms.list() #get list of rooms bot is in
#         print(rooms) #generator object
#         for room in rooms:
#             print(room.title) 
#             roomId = room.id
#             messages = api.messages.list(roomId)
#             processMessage(messages)
#         time.sleep(10)

