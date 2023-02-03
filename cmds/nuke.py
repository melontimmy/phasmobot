import asyncio
import time
import coreModule as core

command = "nuke" 
help = "!nuke **[@Name]** [Duration] [Multipler] [Message]"
    
loops = {}

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

async def onMessage(p1, p2):
    name = str( ''.join(filter(str.isdigit, p2[1])))
    nameStr = p2[1]
    duration = 10
    if len(p2) > 2 and p2[2] != "_"  and isfloat(p2[2]) and float(p2[2]) > 0 :
        duration = float(p2[2])
    multipler = 1
    if len(p2) > 3 and p2[3] != "_"  and isfloat(p2[2]) and float(p2[3]) > 1:
        multipler = round(float(p2[3]))
    message = nameStr
    if len(p2) > 4 and p2[4] != "_":
        message = nameStr + " " + core.reconstructString(p2, 4, len(p2)) + " "
    loops[name] = duration
    while loops[name] > 0:
        msg = await core.send(p1[0], p1[1], message * multipler)
        time.sleep(3)
        await msg.delete()
        loops[name] -= 1
    loops[name] = None


 
    

