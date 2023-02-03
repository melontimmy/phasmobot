import coreModule as core

command = "test"
help = "!test command"

async def onMessage(p1,p2):
    await core.send(p1[0], p1[1], "wow")
