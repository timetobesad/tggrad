import codecs
import json
from telethon import TelegramClient

from json import dumps as json_dumps

chat = 'me'
api_id = '17504125'
api_hash = '35edac267afc648dfd6ded76ed9b4462'

client = TelegramClient('anon', api_id, api_hash)

async def main():
    
    f = open('debug.txt', 'a', encoding='utf-8')
    
    for message in await client.get_messages('satisface', limit=50):
    
        if message.from_id == None:
            fromUser = 'satisface'
        else:
            fromUser = 'sam.cpp'
    
        msg = fromUser + '|' + message.text
        
        if message.media != None:
            attacPath = './'+str(message.id)+'.png'
            msg = msg + '|' + attacPath
            await client.download_media(message.media,attacPath)
        f.write(msg+'\n')
    
    f.close();
        
with client:
    client.loop.run_until_complete(main())