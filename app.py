from telethon import TelegramClient

chat = 'me'
api_id = '17504125'
api_hash = '35edac267afc648dfd6ded76ed9b4462'

client = TelegramClient('anon', api_id, api_hash)

async def main():
    
    f = open('debug.txt', 'a', encoding='utf-8')
    
    for message in await client.get_messages('satisface', limit=100):
    
        if message.from_id == None:
            fromUser = 'satisface'
        else:
            fromUser = 'sam.cpp'
            
        if type(message.text) == str:
            text = message.text
        else:
            text = ' '
            
        msg = fromUser + '|' + text
        
        if message.media != None:
            attacPath = './'+str(message.id)+'.png'
            msg = msg + '|' + attacPath
            #await client.download_media(message.media,attacPath)
        f.write(msg+'\n')
    
    f.close();
        
with client:
    client.loop.run_until_complete(main())