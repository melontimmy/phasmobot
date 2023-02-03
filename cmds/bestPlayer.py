import random
import asyncio
import coreModule as core

command = "bestplayer"
help = "!bestplayer **[Champion/Operator] [Player1]...[PlayerN]**"

async def onMessage(p1, p2):
    contestants, champName = p2[2:], p2[1]
    random.seed()
    deaths = ["'s asshole grew three times larger that day...",
              " spent an unpleasant night with the Cell Block A Ghost...",
              " dropped the soap...",
              " was brutally fisted by Phasmo Ghost...",
              " gained a new asshole...",
              " is dead as fuck™...",
              " was yeeted to the shadow realm...",
              " got destroyed by Phasmo Ghost's fiora deck...",
              " has been isekaied...",
              "'s holes were explored by Cell Block A Ghost"
              ]

    orderedList = []

    strO = ""
    while len(contestants) > 0:
        dead = contestants.pop(random.randint(0, len(contestants)-1))
        orderedList.append(dead)
        strO += dead + deaths.pop(random.randint(0, len(deaths)-1)) + "\n"
    strO += "\n"
  
    index = 1
    for player in orderedList:
        if index == 1:
            strO +=(player + " is the worst " + champName + " player") + "\n"
        elif index == 2:
            strO +=(player + " is the 2nd worst " + champName + " player") + "\n"
        elif index == 3:
            strO +=(player + " is the 3rd worst " + champName + " player") + "\n"
        else:
            strO +=(player + " is the " + str(index) + "th worst " + champName + " player") + "\n"
        index += 1

    await core.send(p1[0], p1[1], strO)