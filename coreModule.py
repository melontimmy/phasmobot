import discord
import asyncio
from replit import db

test = "test"
async def send(client, channelID, message):
    return await client.get_channel(channelID).send(message)

def getParameters(message):
    parameters = []
    startIndex = 0

    while startIndex < len(message):
        space = message.find(" ", startIndex)

        if space > 0:
            parameters.append(message[startIndex:space])
            startIndex = space+1
        else:
            break

    parameters.append(message[startIndex:])
    return parameters

def reconstructString(parameters, startIndex, endIndex):
    str = ""
    for x in parameters[startIndex:endIndex]:
        str += x + " "
    return str

def tAdd(table, key, value):
    if table.get(key) != None:
        table[key] += value
    else:
        table[key] = value
    return table[key]

def tUnique(table, key, value):
    new = False
    if table.get(key) == None:
        table[key] = value
        new = True
        
    return table[key], new

def tDel(table, key):
    if table.get(key) != None:
        del table[key]
        return True
    else:
        return False

    


