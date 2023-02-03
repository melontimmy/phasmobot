import asyncio
import time
import cmds.nuke as nuke
import coreModule as core

command = "unnuke" 
help = "!unnuke **[@Name]**"
    
async def onMessage(p1, p2):
    nuke.loops[str(''.join(filter(str.isdigit, p2[1])))] = 0
    

