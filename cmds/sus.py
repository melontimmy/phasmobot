import coreModule as core
from replit import db

command = "sus"
help = "!sus (Shows killer table of friendly fire)"

async def onMessage(p1,p2):
    killerT = core.tUnique(db, "killerT", {})[0]

    strConstruct = "```Killer Table:\n"
    for killer, victimTable in killerT.items():
        totalKills = 0
        for victim, timesDied in victimTable.items():
            totalKills += timesDied
        if totalKills > 0:
            strConstruct += "\n" + killer + "'s FFs\n" 
            strConstruct += "	Total FFs: "+ str(totalKills) + "\n"
            strConstruct += "	Victims:\n"
            for victim, timesDied in victimTable.items():
                strConstruct += "		" + victim + ": " + str(timesDied) + " (" + str(int((timesDied/totalKills)*1000)/10) + "%)\n"
    
    await core.send(p1[0], p1[1], strConstruct + "```")
