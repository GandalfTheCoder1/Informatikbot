import discord
import re
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import math
Client = discord.Client()

@Client.event
async def on_ready():
        print("logged in as: ")
        print(Client.user.name)
        print("ID: ")
        print(Client.user.id)
        print("ready to use!")

@Client.event
async def on_message(message):
        if message.author == Client.user:
                return
        elif message.content == "!ping":
                await Client.send_message(message.channel,"pong!")
        elif message.content == "!reichmuth":
                await Client.send_message(message.channel,"https://www.kanti-wohlen.ch/pictures/60/q5n5vkr2lly910o0qhyq4rj8qzfg2k/bild4-690-2x.jpg")
        elif message.content == "!hilfe":
                await Client.send_message(message.channel,"!reichmuth - *Es Bild vom Kachi* \n!widmer - *kachi nummer2* \n!makedictionary - *so macht mer es dictionary* \n!letztiufgab - *ufgab ide letzte stund bzw husufgabe*")
        elif message.content == "!makedictionary":
                await Client.send_message(message.channel,'thisdict =   \n{"brand": "Ford", \n"model": "Mustang",\n"year": 1964}')
        elif message.content == "!dictionaryhelp":
                await Client.send_message(message.channel,'im dictionary gibt es für jedes sogenannte "item" 2 Elemente: der key und der value. Beide Elemente können mithilfe verschiedener commands dargestellt werden. Für die Keys verwendet man "example.keys()" und für die values "example.values". Man kann sie in einer Liste darstellen mit "x = list(example.keys())" oder mit einer for Schleife verbinden.')
        elif message.content == "!widmer" or message.content == "!thwidmer":
                randompic = random.randint(1,2)
                if randompic == 1:
                        await Client.send_message(message.channel,"https://i.imgur.com/6UU6eoi.jpg")
                else:
                        await Client.send_message(message.channel,"https://i.imgur.com/ngWy3ix.jpg")
        elif message.content == "!letzti ufgab":
                        await Client.send_message(message.channel,'summe = 0'
                                                                  'for x in dishes.values():'
                                                                  '     summe += x'
                                                                  '     print(summe)')
Client.run("NTQ1OTE1MDI1Nzg1ODgwNjEw.D0gm0g.7sL5EmUO3eE35PJad-2LuW7gpgY")
