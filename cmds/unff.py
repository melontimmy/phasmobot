import coreModule as core
from replit import db

command = "unff"
help = "!unff **[Killer] [Victim]** (DELETES AN ENTRY FROM DATABASE, USE !FF TO MODIFY EXISTING STATS)"

async def onMessage(p1,p2):
    killer = p2[1].capitalize()
    victim = p2[2].capitalize()

    killerT = core.tUnique(db, "killerT", {})[0]
    victimT = core.tUnique(db, "victimT", {})[0]

    killerVictimT = core.tUnique(killerT, killer, {})[0]
    victimKillerT = core.tUnique(victimT, victim, {})[0]

    success = core.tDel(killerVictimT, victim)
    success2 = core.tDel(victimKillerT, killer)

    if success:
        await core.send(p1[0], p1[1], "Entries of **" + killer + "** killing **" + victim + "** and **" + victim + "** dying to **" + killer + "** has been removed")
    else:
        await core.send(p1[0], p1[1], "Entries not found")



