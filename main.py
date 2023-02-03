

import importlib
import os
import discord
import coreModule as core
from replit import db
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.members = True

commands = {}
help = {}

#Load commands in cmd folder and execute any start-up code
for file in os.listdir("cmds"):
    if file.endswith(".py"):
        module = importlib.import_module("cmds." + file[:-3])
        help[file] = module.help
        commands[module.command] = module.onMessage
        try:
            module.startUp()
        except AttributeError:
            pass


#Initalize events and start bot
client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} is online'.format(client))

@client.event
async def on_message(message):
    parameters = core.getParameters(message.content[1:])
    packData = [client, message.channel.id, message.channel.guild]
    if message.content.startswith('\\') and message.author != client.user:
        cmdLower = parameters[0].lower()
        if commands.get(cmdLower):
            await commands[cmdLower](packData, parameters)
        elif cmdLower == "list":
            cmdList = "Bold is mandatory parameters, rest can be omitted.\n\n"
            for key, value in help.items():
                cmdList += value + "\n"
            await core.send(client, message.channel.id, cmdList)

keep_alive()
client.run(os.environ['TOKEN'])    


