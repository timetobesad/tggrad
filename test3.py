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
    
    async for dialog in client.iter_dialogs():
        print(json.load(str(dialog))
        #if(dialog.bot_info_version == None)
        #    print(dialog)
        
with client:
    client.loop.run_until_complete(main())