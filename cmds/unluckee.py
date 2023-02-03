import coreModule as core
from replit import db

command = "unluckee"
help = "!unluckee (Shows victim table of friendly fire)"

async def onMessage(p1,p2):
    victimT = core.tUnique(db, "victimT", {})[0]
    
    strConstruct = "```Victim Table:\n"
    for victim, killerTable in victimT.items():
        totalDeaths = 0
        for killer, timesKilled in killerTable.items():
            totalDeaths += timesKilled
        if totalDeaths > 0:
            strConstruct += "\n" + victim + "'s Deaths\n"
            strConstruct += "	Total Deaths: " + str(totalDeaths) +"\n"
            strConstruct += "	Killers:\n"
            for killer, timesKilled in killerTable.items():
                if totalDeaths > 0:
                    strConstruct += "		" + killer + ": " + str(timesKilled) + " (" + str(int((timesKilled/totalDeaths)*1000)/10) + "%)\n"
    
    await core.send(p1[0], p1[1], strConstruct + "```")
