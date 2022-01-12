from telethon import TelegramClient
from datetime import datetime
from datetime import timedelta

import re

api_id = '17504125'
api_hash = '35edac267afc648dfd6ded76ed9b4462'

client = TelegramClient('anon', api_id, api_hash)

def isDialog(dialog):
    
    if str(type(dialog.entity)) == "<class 'telethon.tl.types.User'>":
        if not dialog.entity.bot:
            return True
    else:
        return False
        
async def downloadDialog(dialogId, title):
    for i in range(10):
    
        fileName = 'chats/'+title+'_'+str(i)+'.txt'
        f = open(fileName, 'a', encoding='utf-8')
        
        tmpMsg = await client.get_messages(dialogId, limit=1)
        
        lastId = tmpMsg[0].id
    
        for message in await client.get_messages(dialogId, limit=200, offset_id=lastId - i*200):
        
            if message.from_id == None:
                fromUser = title
            else:
                fromUser = 'Вы'
                
            dateMsg = str(message.date)[:-6]
            dateObj = datetime.strptime(dateMsg, '%Y-%m-%d %H:%M:%S') + timedelta(hours=2)
                
            if type(message.text) == str:
                text = (message.text).replace('\n', '(!)')
            else:
                text = ' '
                
            msg = str(dateObj) + '|' + fromUser + '|' + text
            
            if message.media != None:
                attacPath = './img/'+str(message.id)+'.png'
                msg = msg + '|' + attacPath
                await client.download_media(message.media,attacPath)
            f.write(msg+'\n')
            
        f.close()

async def main():
    
    fileListDialog = open('list.txt', 'a', encoding='utf-8')
    
    idDialog = 0
    chatList = dict()
    
    async for dialog in client.iter_dialogs():
        if isDialog(dialog):
           title = re.sub(r"[^a-zA-Zа-яА-Я]+", "", dialog.name);
           fileListDialog.write(title+'\n')
           await downloadDialog(dialog.id, title)

    fileListDialog.close();
with client:
    client.loop.run_until_complete(main())