import random
import asyncio
import coreModule as core
import random

command = "rattle"
help = "!rattle **[User]** [num times]"

async def onMessage(p1, p2):
    name = str( ''.join(filter(str.isdigit, p2[1])))
    nameStr = p2[1]
    reps = 3

    print(p2)
    if len(p2) > 2:
        print(p2[2])
        reps = int(p2[2])

    channels = p1[2].voice_channels
    currentChannel = None

    shuffleChannels = []

    for channel in channels:
        print(channel)
        for x in channel.members:
            print(x)
            print(name, x.id[2:], name==x.id[2:])
            if name == x.id[2:]:
                currentChannel = x
        if channel != currentChannel:
            shuffleChannels += [channel]

    if currentChannel:
        await core.send(p1[0], p1[1], "Rattling "+ nameStr)
        for x in range(reps):
            await name.move_to(random.choice(shuffleChannels))
            time.sleep(0.33)
        await name.move_to(currentChannel)
    else:
        await core.send(p1[0], p1[1], "User not found in voice channel")
            
        
