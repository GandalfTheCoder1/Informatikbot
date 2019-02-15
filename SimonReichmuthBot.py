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
        elif message.content == "!widmer" or message.content == "!thwidmer":
                randompic = random.randint(1,2)
                if randompic == 1:
                        await Client.send_message(message.channel,"https://i.imgur.com/6UU6eoi.jpg")
                else:
                        await Client.send_message(message.channel,"https://i.imgur.com/ngWy3ix.jpg")
        elif message.content == "!letztiufgab":
                        await Client.send_message(message.channel,'def char_frequency(str1):\n'
                                                                  '        dict = {}\n'
                                                                  '        for n in str1:\n'
                                                                  '               keys = dict.keys()\n'
                                                                  '               if n in keys: \n'
                                                                  '                       dict[n] += 1\n'
                                                                  '               else:\n'
                                                                  '                        dict[n] = 1\n'
                                                                  '       return dict\n'
                                                                  "print(char_frequency('google.com')) #das google.com kann beliebig angepasst werden durch anderen Text")
Client.run("NTQ1OTE1MDI1Nzg1ODgwNjEw.D0gm0g.7sL5EmUO3eE35PJad-2LuW7gpgY")
