from telethon import TelegramClient
from datetime import datetime
from datetime import timedelta

chat = 'satisface'
api_id = '17504125'
api_hash = '35edac267afc648dfd6ded76ed9b4462'

client = TelegramClient('anon', api_id, api_hash)

async def main():
    
    
    
    for i in range(10):
    
        fileName = chat+'_'+str(i)+'.txt'
        f = open(fileName, 'a', encoding='utf-8')
        
        tmpMsg = await client.get_messages(chat, limit=1)
        
        lastId = tmpMsg[0].id
    
        for message in await client.get_messages(chat, limit=200, offset_id=lastId - i*200):
        
            if message.from_id == None:
                fromUser = 'satisface'
            else:
                fromUser = 'sam.cpp'
                
            dateMsg = str(message.date)[:-6]
            dateObj = datetime.strptime(dateMsg, '%Y-%m-%d %H:%M:%S') + timedelta(hours=2)
                
            if type(message.text) == str:
                text = message.text
            else:
                text = ' '
                
            msg = str(dateObj) + '|' + fromUser + '|' + text
            
            if message.media != None:
                attacPath = './'+str(message.id)+'.png'
                msg = msg + '|' + attacPath
                #await client.download_media(message.media,attacPath)
            f.write(msg+'\n')
            
        f.close()
        
with client:
    client.loop.run_until_complete(main())