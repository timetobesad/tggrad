import codecs
import json
from telethon import TelegramClient

from json import dumps as json_dumps

from datetime import datetime
from datetime import timedelta

chat = 'satisface'
api_id = '17504125'
api_hash = '35edac267afc648dfd6ded76ed9b4462'

client = TelegramClient('anon', api_id, api_hash)

async def main():
    
        tmpMsg = await client.get_messages(chat, limit=1)
        #print(tmpMsg[0].date)
        dateMsg = str(tmpMsg[0].date)[:-6]
        dateObj = datetime.strptime(dateMsg, '%Y-%m-%d %H:%M:%S') + timedelta(hours=2)
        
        print(str(dateObj))
        
with client:
    client.loop.run_until_complete(main())