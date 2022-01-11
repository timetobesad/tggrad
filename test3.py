import codecs
import json
from telethon import TelegramClient

from json import dumps as json_dumps

chat = 'me'
api_id = '17504125'
api_hash = '35edac267afc648dfd6ded76ed9b4462'

client = TelegramClient('anon', api_id, api_hash)

async def main():
    
    async for dialog in client.iter_dialogs():
            print(dialog)
            print('\n')
        
with client:
    client.loop.run_until_complete(main())