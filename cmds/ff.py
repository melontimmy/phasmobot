import coreModule as core
from replit import db

command = "ff"
help = "!ff **[Killer] [Victim]** [Times Murdered]"
#def startUp():
 #   del db["killerT"]
  #  del db["victimT"]

async def onMessage(p1,p2):
    killer = p2[1].capitalize()
    victim = p2[2].capitalize()

    count = 1 
    if len(p2) > 3:
        count = float(p2[3])

    killerT = core.tUnique(db, "killerT", {})[0]
    victimT = core.tUnique(db, "victimT", {})[0]

    killerVictimT = core.tUnique(killerT, killer, {})[0]
    victimKillerT = core.tUnique(victimT, victim, {})[0]

    victimEntry, new = core.tUnique(killerVictimT, victim, 0)
    killerEntry = core.tUnique(victimKillerT, killer, 0)[0]

    if new: 
        await onMessage(p1, p2)
    else:
        killerVictimT[victim] = killerVictimT[victim] + count
        victimKillerT[killer] = victimKillerT[killer] + count
        strConstruct = "**" + killer + "** has killed **" + victim + "** " + str(killerVictimT[victim]) + " times so far"
        await core.send(p1[0], p1[1], strConstruct)
