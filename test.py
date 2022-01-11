msg = { 'phone': '+38', 'name': 'Sam' } 

def parseRespMessage(message):
    return str(message['phone']) + ' : ' + str(message['name'])
    
print(parseRespMessage(msg))