import sys,json,os
import requests
from ecs.funcs import read_file
message = sys.argv[1::]

def send_alert(message):
    bots = read_file('conf.d/bot.list')
    for platform,bot in bots.items():
        url = bot['url'].format(bot_token=bot['bot_token'])
        payload = {
            'chat_id': bot['chat_id'],
            'text': message
            }
        try:
            response = requests.post(url, data=payload)
        except Exception as e:
            print(e)
send_alert(message)

