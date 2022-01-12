from telethon import TelegramClient
#from telethon import TelegramClient, functions, types
#from asyncio import run

import json

chat = 'satisface'
api_id = '17504125'
api_hash = '35edac267afc648dfd6ded76ed9b4462'

client = TelegramClient('anon', api_id, api_hash)

async def main():
    
    i = 0
    
    async for dialog in client.iter_dialogs():
    
        #info = client.get_entity(dialog.username)
        
        if ++i == 0:
            print(dialog)
        
        #++i
        
        #print(type(info))
    
        #try:
        #    if dialog.bot_info_version == None:
        #        print('DIALOG')
        #except:
        #    print(dialog.name)
            
        
        #print('\n')
        #print(json.loads(str(dialog)))
        #i
        #    print(dialog)
    
    #dialogs = client.iter_dialogs()
    
    #print(dialogs)
            
with client:
    client.loop.run_until_complete(main())