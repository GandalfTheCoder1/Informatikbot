import discord
import re
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import math
Client = discord.Client()
inilist = ['INI Liste:\n']
iniuser = []
userlep = []
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
        elif message.content == "!":
                uid = str(message.author.id)
                x = str(random.randint(1,20))
                await Client.send_message(message.channel,'<@!'+uid+'>  ' + x)
        elif message.content == "!developer":
                await Client.send_message(message.channel,"Developer of this Bot is Gandalf. Here is my Discord server: https://discord.gg/3fnvP7z")
        elif message.content.startswith("(") and message.content.endswith(")"):
                uid = str(message.author.id)
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                if len(a) == 2:
                        rolls = []
                        sumrolls = 0
                        while a[0] != 0:
                                x = random.randint(1,a[1])
                                sumrolls += x
                                rolls.append(x)
                                a[0] -= 1
                        if len(rolls) > 1:
                                rollsstr = "+".join(str(x) for x in rolls)+" = " + str(sumrolls)
                        else:
                                rollsstr = "+".join(str(x) for x in rolls)
                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                elif len(a) == 3:
                        if '+' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                rolls.append(mod)
                                sumrolls += mod
                                rollsstr = "+".join(str(x) for x in rolls)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif '-' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                sumrolls -= mod
                                rollsstr = "+".join(str(x) for x in rolls)+"-"+str(mod)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif '*' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                sumrolls *= mod
                                rollsstr = "+".join(str(x) for x in rolls)+"*"+str(mod)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif '/' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                sumrolls /= mod
                                rollsstr = "+".join(str(x) for x in rolls)+"/"+str(mod)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
        elif message.content.startswith("!"):
                uid = str(message.author.id)
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                value1 = a[0]
                o = 3
                if len(a) == 4:
                        value2 = a[1]
                        value3 = a[2]
                        value4 = a[3]
                        checkfor1 = 0
                        checkfor20 = 0
                        rolls = []
                        while o != 0:
                                x = random.randint(1,20)
                                rolls.append(x)
                                if x == 1:
                                        checkfor1 += 1
                                elif x == 20:
                                        checkfor20 += 1
                                o -= 1
                        roll1 = rolls[0]
                        roll2 = rolls[1]
                        roll3 = rolls[2]
                        while roll1 > value1:
                                value4 -= 1
                                roll1 -= 1
                        while roll2 > value2:
                                value4 -= 1
                                roll2 -= 1
                        while roll3 > value3:
                                value4 -= 1
                                roll3 -= 1
                        maxrollindex = rolls.index(max(rolls))
                        maxroll = max(rolls)
                        maxeig = a[maxrollindex]
                        if maxeig > maxroll:
                                maxersch0 = maxeig - maxroll
                                maxersch = str(maxersch0 + value4)
                        else:
                                maxersch = str(value4)
                        rollsstrf = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==>"+" Misslungen!"
                        rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen! \nMaximale Erschwernis: "+maxersch
                        if checkfor1 == 2 or checkfor1 == 3:
                                rollsstrc = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " ==> KRITISCHER ERFOLG!"
                                await Client.send_message(message.channel,  '<@!'+uid+'>  ' + rollsstrc)
                        elif checkfor20 == 2 or checkfor20 == 3:
                                rollsstrb = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " ==> PATZER!"
                                await Client.send_message(message.channel,  '<@!'+uid+'>  ' + rollsstrb)
                        elif value4 == 0:
                                qualitylevel1 = 1
                                rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: 1 ==> Gelungen! \nMaximale Erschwernis: "+maxersch
                                await Client.send_message(message.channel,  '<@!'+uid+'>  ' + rollsstrs)
                        elif value4 > 0:
                                await Client.send_message(message.channel,  '<@!'+uid+'>  ' + rollsstrs)
                        elif value4 < 0:
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrf)

                elif len(a) == 1:
                        uid = str(message.author.id)
                        rolls = []
                        x = random.randint(1,20)
                        checkfor1 = 0
                        checkfor20 = 0
                        maxersch = str(a[0] - x)
                        benerl = str(x - a[0])
                        m_success = "Du hast gewürfelt: "+str(x)+" ==> Gelungen! \nMaximale Erschwernis: "+maxersch
                        m_failure = "Du hast gewürfelt: "+str(x)+" ==> Misslungen! \nBenötigte Erleichterung: "+benerl
                        if x < a[0] and x != 1:
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                        elif x == a[0]:
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                        elif x > a[0]and x!= 20:
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_failure)
                        elif x == 20:
                                rolls.append(x)
                                x = random.randint(1,20)
                                rolls.append(x)
                                if  x > a[0]:
                                        rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Patzer bestätigen: " +str(rolls[1])+ " ==> PATZER!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                else:
                                        rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Patzer bestätigen: "+str(rolls[1])+" ==> Misslungen(Patzer nicht bestätigt) \nBenötigte Erleichterung: "+benerl
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif x == 1:
                                rolls.append(x)
                                x = random.randint(1,20)
                                rolls.append(x)
                                if  x < a[0]:
                                        rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Kritischer Erfolg bestätigen: " +str(rolls[1])+ " ==> KRITISCHER ERFOLG!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                else:
                                        rollsstr= "Du hast gewürfelt: "+str(rolls[0])+" Kritischer Erfolg bestätigen: "+str(rolls[1])+" ==> Gelungen(Kritischer Erfolg nicht bestätigt) \nMaximale Erschwernis: "+maxersch
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                elif len(a) == 5:
                        uid = str(message.author.id)
                        if '-' in message.content:
                                value4 = a[3] + a[4]
                                checkfor1 = 0
                                checkfor20 = 0
                                rolls = []
                                while o != 0:
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if x == 1:
                                                checkfor1 += 1
                                        elif x == 20:
                                                checkfor20 += 1
                                        o -= 1
                                roll1 = rolls[0]
                                roll2 = rolls[1]
                                roll3 = rolls[2]
                                while roll1 > a[0]:
                                        value4 -= 1
                                        roll1 -= 1
                                while roll2 > a[1]:
                                        value4 -= 1
                                        roll2 -= 1
                                while roll3 > a[2]:
                                        value4 -= 1
                                        roll3 -= 1
                                maxrollindex = rolls.index(max(rolls))
                                maxroll = max(rolls)
                                maxeig = a[maxrollindex]
                                if maxeig > maxroll:
                                        maxersch0 = maxeig - maxroll
                                        maxersch = str(maxersch0 + value4)
                                else:
                                        maxersch = str(value4)
                                if value4 > a[3]:
                                        value4 = a[3]
                                else:
                                        value4 = value4
                                rollsstrf = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==>"+" Misslungen!!"
                                rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen! \nMaximaler zusätzlicher Modifikator: "+maxersch
                                if checkfor1 == 2 or checkfor1 == 3:
                                        rollsstrc = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> KRITISCHER ERFOLG!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrc)
                                elif checkfor20 == 2 or checkfor20 == 3:
                                        rollsstrb = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> PATZER!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrb)
                                elif value4 == 0:
                                        qualitylevel = 1
                                        rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: 1 ==> Gelungen! \nMaximaler zusätzlicher Modifikator: "+maxersch
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 > 0 or value4 == 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 < 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrf)
                        elif '+' in message.content:
                                value4 = a[3] - a[4]
                                if value4 < 0:
                                        a[0] = a[0] + value4
                                        a[1] = a[1] + value4
                                        a[2] = a[2] + value4
                                        value4 = 0
                                checkfor1 = 0
                                checkfor20 = 0
                                rolls = []
                                while o != 0:
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if x == 1:
                                                checkfor1 += 1
                                        elif x == 20:
                                                checkfor20 += 1
                                        o -= 1
                                roll1 = rolls[0]
                                roll2 = rolls[1]
                                roll3 = rolls[2]
                                while roll1 > a[0]:
                                        value4 -= 1
                                        roll1 -= 1
                                while roll2 > a[1]:
                                        value4 -= 1
                                        roll2 -= 1
                                while roll3 > a[2]:
                                        value4 -= 1
                                        roll3 -= 1
                                maxrollindex = rolls.index(max(rolls))
                                maxroll = max(rolls)
                                maxeig = a[maxrollindex]
                                if maxeig > maxroll:
                                        maxersch0 = maxeig - maxroll
                                        maxersch = str(maxersch0 + value4)
                                else:
                                        maxersch = str(value4)
                                qualitylevel = value4/3
                                qualitylevel1 = math.ceil(qualitylevel)
                                rollsstrf = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Misslungen!"
                                rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen! \nMaximaler zusätzlicher Modifikator: "+maxersch
                                if checkfor1 == 2 or checkfor1 == 3:
                                        rollsstrc = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " ==> KRITISCHER ERFOLG!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrc)
                                elif checkfor20 == 2 or checkfor20 == 3:
                                        rollsstrb = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " ==> PATZER!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrb)
                                elif value4 == 0:
                                        qualitylevel = 1
                                        rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: 1 ==> Gelungen! \nMaximaler zusätzlicher Modifikator: "+maxersch
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 > 0 or value4 == 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 < 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrf)
                        else:
                                value4 = a[3] - a[4]
                                if value4 < 0:
                                        a[0] = a[0] + value4
                                        a[1] = a[1] + value4
                                        a[2] = a[2] + value4
                                        value4 = 0
                                checkfor1 = 0
                                checkfor20 = 0
                                rolls = []
                                while o != 0:
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if x == 1:
                                                checkfor1 += 1
                                        elif x == 20:
                                                checkfor20 += 1
                                        o -= 1
                                roll1 = rolls[0]
                                roll2 = rolls[1]
                                roll3 = rolls[2]
                                while roll1 > a[0]:
                                        value4 -= 1
                                        roll1 -= 1
                                while roll2 > a[1]:
                                        value4 -= 1
                                        roll2 -= 1
                                while roll3 > a[2]:
                                        value4 -= 1
                                        roll3 -= 1
                                maxrollindex = rolls.index(max(rolls))
                                maxroll = max(rolls)
                                maxeig = a[maxrollindex]
                                if maxeig > maxroll:
                                        maxersch0 = maxeig - maxroll
                                        maxersch = str(maxersch0 + value4)
                                else:
                                        maxersch = str(value4)
                                qualitylevel = value4/3
                                qualitylevel1 = math.ceil(qualitylevel)
                                rollsstrf = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Misslungen!"
                                rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen! \nMaximaler zusätzlicher Modifikator: "+maxersch
                                if checkfor1 == 2 or checkfor1 == 3:
                                        rollsstrc = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " ==> KRITISCHER ERFOLG!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrc)
                                elif checkfor20 == 2 or checkfor20 == 3:
                                        rollsstrb = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " ==> PATZER!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrb)
                                elif value4 == 0:
                                        qualitylevel = 1
                                        rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: 1 ==> Gelungen!\n Maximaler zusätzlicher Modifikator: "+maxersch
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 > 0 or value4 == 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 < 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrf)

                elif len(a) == 2:
                        if '-' in message.content:
                                rolls = []
                                x = random.randint(1,20)
                                newval = a[0] + a[1]
                                maxersch = str(newval - x)
                                benerl = str(x - newval)
                                checkfor1 = 0
                                checkfor20 = 0
                                m_success = "Du hast gewürfelt: "+str(x)+" ==> Gelungen! \nMaximale Erschwernis: "+maxersch
                                m_failure = "Your roll: "+str(x)+" ==> Misslungen! \nBenötigte Erleichterung: "+benerl
                                if x < newval and x != 1:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x == newval:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x > newval and x!= 20:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_failure)
                                elif x == 20:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x > newval:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Patzer bestätigen: " +str(rolls[1])+ " ==> PATZER"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Patzer bestätigen: "+str(rolls[1])+" ==> Misslungen(Patzer nicht bestätigt)\nBenötigte Erleichterung: "+benerl
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                elif x == 1:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x < a[0] or x == a[0]:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Auf kritischen Erfolg überprüfen: " +str(rolls[1])+ " ==> KRITISCHER ERFOLG!"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Auf kritischen Erfolg überprüfen: "+str(rolls[1])+" ==> Gelungen(Kritischer Erfolg nicht bestätigt) \nMaximale Erschwernis: "+maxersch
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif '+' in message.content:
                                rolls = []
                                x = random.randint(1,20)
                                newval = a[0] - a[1]
                                maxersch = str(newval - x)
                                benerl = str(x - newval)
                                checkfor1 = 0
                                checkfor20 = 0
                                m_success = "Du hast gewürfelt: "+str(x)+" ==> Gelungen! \nMaximale Erschwernis: "+maxersch
                                m_failure = "Du hast gewürfelt: "+str(x)+" ==> Misslungen! \nBenötigte Erleichterung: "+benerl
                                if x < newval and x != 1:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x == newval:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x > newval and x!= 20:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_failure)
                                elif x == 20:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x > newval:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Patzer bestätigen: " +str(rolls[1])+ " ==> PATZER"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Patzer bestätigen: "+str(rolls[1])+" ==> Misslungen(Patzer nicht bestätigen)"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        else:
                                rolls = []
                                x = random.randint(1,20)
                                newval = a[0] - a[1]
                                maxersch = str(newval - x)
                                benerl = str(x - newval)
                                checkfor1 = 0
                                checkfor20 = 0
                                m_success = "Du hast gewürfelt: "+str(x)+" ==> Gelungen! \nMaximale Erschwernis: "+maxersch
                                m_failure = "Du hast gewürfelt: "+str(x)+" ==> Misslungen! \nBenötigte Erleichterung: "+benerl
                                if x < newval and x != 1:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x == newval:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x > newval and x!= 20:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_failure)
                                elif x == 20:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x > newval:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Patzer bestätigen: " +str(rolls[1])+ " ==> PATZER"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Patzer bestätigen: "+str(rolls[1])+" ==> Misslungen(Patzer nicht bestätigt)\nBenötigte Erleichterung: "+benerl
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                elif x == 1:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x < a[0]:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Auf kritischen Erfolg überprüfen: " +str(rolls[1])+ " ==> KRITISCHER ERFOLG!"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Auf kritischen Erfolg überprüfen: "+str(rolls[1])+" ==> Gelungen(kritischer Erfolg nicht bestätigt) \nMaximale Erschwernis: "+maxersch
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
        elif message.content.startswith('*'):
                uid = str(message.author.id)
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                if len(message.content) in range(2,4):
                        x = random.randint(1,100)
                        hard1 = a[0]/2
                        hard = math.ceil(hard1)
                        crit1 = a[0]/5
                        crit = math.ceil(crit1)
                        if x < crit or x == crit:
                                 answer = "Your roll: "+str(x)+" ==> CRITICAL SUCCESS"
                                 await Client.send_message(message.channel, '<@!'+uid+'>  ' + answer)
                        elif x < hard or x == crit:
                                answer = "Your roll: "+str(x)+" ==> HARD SUCCESS"
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + answer)
                        elif x < a[0] or x == a[0]:
                                answer = "Your roll: "+str(x)+" ==> SUCCESS"
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + answer)
                        elif x >a[0]:
                                answer = "Your roll: "+str(x)+" ==> Failed"
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + answer)
        elif message.content.startswith('+'):
                uid = str(message.author.id)
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                rolls = []
                successcount = 0
                botchcount = 0
                botchcheck = a[0]/2
                while a[0] != 0:
                        x = random.randint(1,6)
                        rolls.append(x)
                        if x == 5 or x == 6:
                                successcount += 1
                        elif x == 1:
                               botchcount += 1
                        a[0] -= 1
                answer = "<@!"+uid+"> Your rolls: "+",".join(str(x) for x in rolls)+" ==> "+str(successcount)+" success(es)"
                if botchcount < botchcheck:
                        await Client.send_message(message.channel,answer)
                elif botchcount > botchcheck and successcount == 0:
                        answer = "<@!"+uid+"> Your rolls: "+",".join(str(x) for x in rolls)+" ==> CRITICAL BOTCH!"
                        await Client.send_message(message.channel,answer)
                elif botchcount > botchcheck:
                        answer = "<@!"+uid+"> Your rolls: "+",".join(str(x) for x in rolls)+" ==> BOTCH! "+str(successcount)+" success(es)"
                        await Client.send_message(message.channel,answer)

        elif message.content == '%help' :
                await Client.send_message(message.channel, "Common Commands: \n -`(<how many dices?>d<how many sides>)` lets you roll various dices. you can even add, multiply, subtract, or divide a number from the sum of all dices. EXAMPLE: (3d6+5) \n - `!` rolls 1d20 \n\n The Dark eye Commands:\n\n- `!<attribute>` lets you roll for a specific attribute. You can even add a modifier. EXAMPLE: !13,+2 \n- `!<attribute>,<attribute>,<attribute>,<skill value>` lets you roll for a Skill. You can even add a modifier. EXAMPLE: !13,14,13,5,-3 \n\nCall of Cthulhu Commands:\n\n- `*<Skill>` lets you roll for a skill. EXAMPLE: *50")
        elif message.content == 'zone':
                x = random.randint(1,20)
                if x == 1 or x == 3 or x == 5:
                        zone = str(x)+": linkes Bein \nErste und zweite Wunde: AT, PA, GE, INI-Basis -2, GS -1 \nDritte Wunde: Sturz, kampfunfähig"
                elif x == 2 or x == 4 or x == 6:
                        zone = str(x)+": rechtes Bein \nErste und zweite Wunde: AT, PA, GE, INI-Basis -2, GS -1 \nDritte Wunde: Sturz, kampfunfähig"
                elif x in range(7,8):
                        zone = str(x)+": Bauch \nErste und zweite Wunde: AT, PA, KO, KK, GS, INI-Basis -1, 1W6 TP \nDritte Wunde: Bewusstlos, Blutverlust"
                elif x == 9 or x == 11 or x == 13:
                        zone = str(x)+": linker Arm: \nErste und zweite Wunde: AT, PA, KK, FF -2 mit diesem Arm \nDritte Wunde: Arm handlungsunfähig"
                elif x == 10 or x == 12 or x == 14:
                        zone = str(x)+": rechter Arm: \nErste und zweite Wunde: AT, PA, KK, FF -2 mit diesem Arm \nDritte Wunde: Arm handlungsunfähig"
                elif x in range(15,18):
                        zone = str(x)+": Brust: \nErste und zweite Wunde: AT, PA, KO, KK -1, 1W6 TP \nDritte Wunde: bewusstlos, Blutverlust"
                elif x == 19 or x == 20:
                        zone = str(x)+": Kopf: \nEste und zweite Wunde: MU, KL, IN, INI-Basis -2, INI -2w6 \nDritte Wunde: 2W6 TP, Blutverlust"
                await Client.send_message(message.channel, zone)
        elif message.content == 'patzer':
                x = random.randint(1,6)
                y = random.randint(1,6)
                result = x + y
                if result == 2:
                        patzer = str(result)+": Waffe zerstört! \nINI -4 wegen Desorientierung; Hat die Waffe einen BF 0 oder weniger, so wird das Ergebnis als 'Waffe verloren' gewertet und der BF der Waffe steigt um 2; Greift man mit der Faust an, gilt dieses Ergebnis als 'schwerer Eigentreffer'"
                elif result in range(3,5):
                        patzer = str(result)+": Sturz! \nDer Patzende liegt auf dem Boden und bekommt dementsprechend erschwernisse(WdS S. 57), bis er wieder aufstehen kann. Dies benötigt eine Aktion Position und eine um seine BE erschwerte GE-Probe. Ein Held mit SF Standfest oder dem Vorteil Balance kann einen Sturz in ein Stolpern umwandeln wenn ihm eine GE-Probe(Standfest: +2, Balance: +-0, herausragende Balance: -4), die um die BE erschwert ist, gelingt. INI -2 wegen Desorientierung."
                elif result in range(6,8):
                        patzer = str(result)+": Stolpern! \nINI -2 wegen Desorientierung"
                elif result in range(9,10):
                        patzer = str(result)+": Waffe verloren! \nDer Patzende muss in der folgenden Runde die Aktion Position aufwenden, um eine GE-Probe abzulegen, bei deren gelingen er an seine Waffe gelangt; oder aber er wechselt die Waffe oder flieht. Handelt es sich bei der Waffe um Fäuste und Füsse, so wird das Ergebnis als Sturz gewertet. INI -2 wegen Desorientierung."
                elif result == 11:
                        patzer = str(result)+": An eigener Waffe verletzt! \nDer betroffene erleidet Waffenschaden durch eigene Waffe(TP auswürfeln; keine zusätzlichen TP aus hoher KK oder Ansagen) und eventuell sogar eine Wunde (bei mehr als KO/2 SP) mit den dort genannten Folgen; INI -3 wegen Desorientierung."
                elif result == 12:
                        patzer = str(result)+": Schwerer Eigentreffer! \nINI -4. Der Betroffene erleidet schweren Schaden durch eigene Waffe(TP auswürfeln und verdoppeln; keine zusätzlichen TP aus hoher KK oder Ansagen) und eventuell sogar eine Wunde(bei mehr als KO/2 SP) mit den dort genannten Folgen; INI -4 wegen Desorientierung."
                await Client.send_message(message.channel, patzer)
        elif message.content.startswith('INI') or message.content.startswith('ini'):
                findname = re.sub("[^\w]", " ", message.content).split()
                if len(findname) == 3:
                        if '+' in message.content:
                                a = [int(num) for num in re.findall(r"\d+", message.content)]
                                name = findname[1]
                                for i in inilist:
                                        if name in i:
                                                b = [int(num) for num in re.findall(r"\d+", i)]
                                                inilist.remove(i)
                                                newini = a[0] + b[0]
                                                newentry = name+': '+str(newini)
                                                inilist.append(newentry)
                                                await Client.send_message(message.channel, 'Die INI von '+name+' wurde um '+str(a[0])+' erhöht')
                                        else:
                                                await Client.send_message(message.channel, name+' ist nicht in der INI-Liste drin...')
                        elif '-' in message.content:
                                a = [int(num) for num in re.findall(r"\d+", message.content)]
                                name = findname[1]
                                for i in inilist:
                                        x = 0
                                        if name in i:
                                                b = [int(num) for num in re.findall(r"\d+", i)]
                                                newini = b[0] - a[0]
                                                inilist.remove(i)
                                                newentry = name+': '+str(newini)
                                                await Client.send_message(message.channel, 'Die INI von '+name+' wurde um '+str(a[0])+' verringert')
                                                x = 1
                                if x == 0:
                                        await Client.send_message(message.channel, name+' ist nicht in der INI-Liste drin...')
                                inilist.append(newentry)



                        elif 'alle löschen' in message.content:
                                if len(inilist) > 0:
                                        await Client.send_message(message.channel, 'Die INI-Liste wurde gelöscht')
                                        inilist.clear()
                                        iniuser.clear()
                                else:
                                        await Client.send_message(message.channel, 'Die INI-Liste ist bereits leer...')
                        elif 'löschen' in message.content:
                                findname = re.sub("[^\w]", " ", message.content).split()
                                name = findname[1]
                                for i in inilist:
                                        if name in i:
                                                inilist.remove(i)
                                                iniuser.remove(name)
                                                await Client.send_message(message.channel, name+" wurde aus der INI-Liste entfernt!")
                        else:
                                name = findname[1]
                                inibase = int(findname[2])
                                die = random.randint(1,6)
                                yourini = die + inibase
                                ininame = name+': ' + str(yourini)
                                if name in iniuser:
                                        await Client.send_message(message.channel, name+' ist bereits in der INI-Liste...')
                                else:
                                        iniuser.append(name)
                                        inilist.append(ininame)
                                        await Client.send_message(message.channel, 'die INI von '+name+' wurde der Liste hinzugefügt und beträgt '+str(yourini))

                if 'liste' in message.content:
                        if len(inilist) > 0:
                                inistr = '\n'.join(inilist)
                                await Client.send_message(message.channel, inistr)
                        else:
                                await Client.send_message(message.channel, 'Die INI-Liste ist leer!')
        elif message.content.startswith('BF'):
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                roll1 = random.randint(1,6)
                roll2 = random.randint(1,6)
                BF = roll1 + roll2
                weapon = a[0]
                if BF == weapon or BF < weapon:
                        await Client.send_message(message.channel, 'Dein Ergebnis: '+str(BF)+'\nDeine Waffe zerbricht!')
                elif BF == 12:
                        await Client.send_message(message.channel, 'Dein Ergebnis: '+str(BF)+'\nDer Bruchfaktor verändert sich nicht. Der Angreifer muss auch einen Bruchtest ablegen.')
                else:
                        await Client.send_message(message.channel, 'Dein Ergebnis: '+str(BF)+'\nDer Bruchfaktor erhöht sich um 1. Der Angreifer muss auch einen Bruchtest ablegen.')
        elif message.content.startswith('LeP'):
                findname = re.sub("[^\w]", " ", message.content).split()
                if 'neu' in message.content:
                        name = findname[1]
                        a = [int(num) for num in re.findall(r"\d+", message.content)]
                        lepname = name+': '+str(a[0])
                        if name in userlep:
                                await Client.send_message(message.channel, 'Du hast deine LeP bereits notiert...')
                        else:
                                userlep.append(lepname)
                                await Client.send_message(message.channel, 'Du hast die LeP von '+name+' notiert')
                elif 'liste' in message.content:
                        if len(userlep) > 0:
                                inistr = '\n'.join(userlep)
                                await Client.send_message(message.channel, inistr)
                        else:
                                await Client.send_message(message.channel, 'Die LeP-Liste ist leer!')
                elif '-' in message.content:
                        name = findname[1]
                        a = [int(num) for num in re.findall(r"\d+", message.content)]
                        for i in userlep:
                                        x = 0
                                        if name in i:
                                                b = [int(num) for num in re.findall(r"\d+", i)]
                                                newini = b[0] - a[0]
                                                newentry = name+': '+str(newini)
                                                await Client.send_message(message.channel, 'Die LeP von '+name+' wurde um '+str(a[0])+' verringert')
                                                x = 1
                                                userlep.remove(i)
                        if x == 0:
                                await Client.send_message(message.channel, name+' ist nicht in der INI-Liste drin...')
                        userlep.append(newentry)
                elif '+' in message.content:
                        name = findname[1]
                        a = [int(num) for num in re.findall(r"\d+", message.content)]
                        for i in userlep:
                                        x = 0
                                        if name in i:
                                                b = [int(num) for num in re.findall(r"\d+", i)]
                                                newini = b[0] + a[0]
                                                newentry = name+': '+str(newini)
                                                await Client.send_message(message.channel, 'Die LeP von '+name+' wurde um '+str(a[0])+' erhöht')
                                                x = 1
                                                userlep.remove(i)
                        if x == 0:
                                await Client.send_message(message.channel, name+' ist nicht in der LeP-Liste drin...')
                        userlep.append(newentry)
                elif 'löschen' in message.content:
                                findname = re.sub("[^\w]", " ", message.content).split()
                                name = findname[1]
                                for i in userlep:
                                        if name in i:
                                                userlep.remove(i)
                                                await Client.send_message(message.channel, name+" wurde aus der LeP-Liste entfernt!")
                elif 'alle löschen' in message.content:
                                if len(userlep) > 0:
                                        await Client.send_message(message.channel, 'Die LeP-Liste wurde gelöscht')
                                        userlep.clear()
                                else:
                                        await Client.send_message(message.channel, 'Die LeP-Liste ist bereits leer...')



        elif message.content.startswith('SF'):
                if 'Aufmerksamkeit' in message.content:
                        await Client.send_message(message.channel, 'Aufmerksamkeit:\n Ein Held mit dieser Fähigkeit benötigt nureine Aktion (anstatt zweier), um sich im '
                        'Kampf Orientierung (die gleichnamige längerfristige '
                        'Aktion; Seite 54) zu verschaffen '
                        'und seinen INI-Wert auf das mögliche Maximum '
                        '(entsprechend einem Wurf von 6 auf '
                        'W6 bei der Initiativbestimmung; für Klingentänzer: '
                        '12) anzuheben; er muss hierzu auch '
                        'keine IN-Probe ablegen. '
                        'Die IN-Probe, um Überraschung zu verhindern '
                        'oder bei einem Hinterhalt schnell zu '
                        'reagieren, ist von vornherein um 4 Punkte '
                        'erleichtert. Ein Held mit Aufmerksamkeit '
                        'hat genügend Übersicht, um sich nicht in '
                        'Reichweite eines Passierschlags zu bringen '
                        'oder diesen vorauszuahnen: Gegen ihn ist '
                        'ein Passierschlag um zusätzliche 4 Punkte erschwert. '
                        'Außerdem muss er nicht zu Beginn einer '
                        'Kampfrunde ankündigen, ob er eine '
                        'Angriffsaktion in eine Abwehraktion umwandeln '
                        'will oder umgekehrt, sondern erst '
                        'unmittelbar bevor er seine erste eigene Angriffs- '
                        'oder Abwehraktion in dieser Kampfrunde '
                        'ausführt.\n'
                        'Voraussetzungen: IN 12\n'
                        'Verbreitung: 4, durch Praxis\n '
                        'Kosten: 200 AP')
                elif 'Ausfall' in message.content:
                        await Client.send_message(message.channel, 'Ausfall:\n'
                        'Ermöglicht dem Kämpfer, das gleichnamige '
                        'Manöver (Seite 59) durchzuführen: Er wandelt '
                        'seine Abwehraktion ohne Malus in eine '
                        'Angriffsaktion um und zwingt den Gegner '
                        'zum umgekehrten Verhalten (dieser muss '
                        'also zweimal parieren); dabei treibt er ihn '
                        'langsam zurück. (Angriffsmanöver; +4 zum Einleiten)\n'
                        'Voraussetzungen: KO 12; SF Finte\n'
                        'Verbreitung: 4, professionelle Kämpfer\n'
                        'Kosten: 200 AP')
                elif 'Ausweichen' in message.content:
                        await Client.send_message(message.channel, 'Ausweichen 1 / 11 / 111:\n'
                        'Ein Held mit diesen Sonderfertigkeiten hat '
                        'sich auf seine Beweglichkeit im Kampf konzentriert '
                        'und ist in der Lage, seine Ausweichen- '
                        'Proben (eine Abwehraktion, bei der auf '
                        'den Parade-Basiswert gewürfelt wird, siehe '
                        'Seite 66) mit 3 / 6 / 9 Punkten Bonus abzulegen; '
                        'dies gilt auch für das Ausweichen vor '
                        'Fernkampf- oder Sturmangriffen.\n '
                        'Voraussetzungen: GE 10 / 12 / 15; zum Erlernen '
                        'von Ausweichen II wird die Kenntnis '
                        'von Ausweichen I und Aufmerksamkeit benötigt, '
                        'zum Erlernen von Ausweichen III '
                        'die Sonderfertigkeiten Ausweichen II und '
                        'Kampfreflexe.\n '
                        'Verbreitung: 5 / 4 / 3, jeweils durch Praxis\n '
                        'Kosten: 300 / 200 / 200 AP, jeweils verbilligt '
                        'für Helden mit dem Vorteil Schlangenmensch'
                        '(150 / 100 / 100 AP)')
                elif 'Beidhändiger Kampf' in message.content:
                        await Client.send_message(message.channel, 'Beidhändiger Kampf 1:\n'
                        'Diese Fertigkeit gibt einem Kämpfer bessere '
                        'Kontrolle über sämtliche Kampf-Handlungen '
                        'mit der ‘falschen’ Hand. Sie vermindert '
                        'die Abzüge im Kampf mit links (bzw. '
                        'rechts für Linkshänder) auf –3/–3 und erlaubt '
                        'zusätzliche Manöver sowie die Nutzung des '
                        'KK-Bonus auf die TP für die linke Hand.\n '
                        'Voraussetzungen: GE 12, SF Linkhand\n '
                        'Verbreitung: 3, vornehmlich bei Gladiatoren '
                        'und Schaukämpfern, im tulamidischen und '
                        'südaventurischen Raum\n '
                        'Kosten: 100 AP; billiger für Helden mit den '
                        'Vorteilen Beidhändig (50 AP) oder Linkshändig '
                        '(75 AP)\n '
                        'Beidhändiger Kampf 11: \n '
                        'Der Erwerb dieser Sonderfertigkeit bedeutet, '
                        'dass der Held die Perfektion im Linkshändigen '
                        'Kampf erreicht hat und keinerlei Abzüge auf '
                        'AT und PA bei der Verwendung der falschen '
                        'Hand hinnehmen muss. Diese Sonderfertigkeit '
                        'erlaubt einige zusätzliche Manöver (siehe Seite '
                        '72) und stellt eine zusätzliche Angriffs- oder '
                        'Abwehr-Aktion pro Kampfrunde (nicht kumulativ '
                        'mit der aus Tod von Links oder Parierwaffen '
                        'II) mit der Zweitwaffe zur Verfügung.\n'
                        'Voraussetzungen: GE 15, SF Beidhändiger '
                        'Kampf I \n'
                        'Verbreitung: 2, vornehmlich bei Gladiatoren '
                        'und Schaukämpfern, im tulamidischen und '
                        'südaventurischen Raum \n'
                        'Kosten: 400 AP; billiger für Helden mit den '
                        'Vorteilen Beidhändig (200 AP) oder Linkshändig '
                        '(300 AP). Wenn der Held schon die '
                        'Sonderfertigkeit Tod von Links beherrscht, '
                        'werden die dafür aufgebrachten AP beim '
                        'Erwerb von Beidhändiger Kampf II in voller '
                        'Höhe als Rabatt angerechnet. ')
                elif 'Betäubungsschlag' in message.content:
                        await Client.send_message(message.channel, 'Betäubungsschlag: \n'
                        'Diese Sonderfertigkeit ermöglicht es einem '
                        'Kämpfer, einen sehr gezielten Schlag mit der '
                        'stumpfen Seite seiner Waffe – das Manöver '
                        'Betäubungsschlag (Seite 61) – auszuführen '
                        'und den Gegner damit möglicherweise sofort '
                        'ins Reich der Träume zu schicken. Außerdem '
                        'kann er die Erschwernisse bei einem Stumpfen '
                        'Schlag halbieren.\n'
                        'Voraussetzungen: SF Finte und Wuchtschlag\n'
                        'Verbreitung: 3, bei Wundärzten, Tierfängern '
                        'oder zwielichtigen Personen\n'
                        'Kosten: 200 AP')
                elif 'Binden' in message.content:
                        await Client.send_message(message.channel, 'Binden: '
                        'Mit dieser Sonderfertigkeit kann ein Kämpfer '
                        'mittels des gleichnamigen Manövers bei '
                        'seiner Parade die gegnerische Waffe behindern '
                        'und somit die nächste gegnerische PA '
                        'erschweren und die eigene AT erleichtern. \n'
                        'Voraussetzungen: IN und GE je 12; Sonderfertigkeit '
                        'Meisterparade oder Parierwaffen I \n'
                        'Verbreitung: 4, vor allem bei Schwert- und '
                        'Fechtwaffenkämpfern \n'
                        'Kosten: 200 AP ')
                elif 'Blindkampf' in message.content:
                        await Client.send_message(message.channel, 'Blindkampf:\n'
                        'Ein Nahkämpfer mit dieser seltenen '
                        'Sonderfertigkeit ist in der Lage, auch '
                        'mit verbundenen Augen, in völliger '
                        'Dunkelheit, gegen Unsichtbare oder gar '
                        'bei Verlust des Augenlichts mit nur geringen '
                        'Einbußen zu kämpfen: Seine Abzüge auf AT/'
                        'PA durch schlechte Sicht betragen maximal '
                        '–2/–2. Kämpfe in der Distanzklasse Pike sind '
                        'jedoch nicht erleichtert, ebenso wenig Lanzenreiten- '
                        'oder Peitschen-Angriffe. In einer '
                        'Überraschungs- oder Hinterhalt-Situation '
                        'sind die IN-Proben eines solcherart aufmerksamen '
                        'Kämpfers um 2 Punkte erleichtert.\n '
                        'Voraussetzungen: GE 12; TaW Sinnenschärfe '
                        '15; SF Kampfgespür; gilt nicht für Fernkampffertigkeiten.\n '
                        'Verbreitung: 1, Mystiker und Ordenskrieger '
                        'Kosten: 200 AP ')
                elif 'Defensiver Kampfstil' in message.content:
                        await Client.send_message(message.channel, 'Defensiver Kampfstil:\n'
                        'Diese Sonderfertigkeit ist nur sinnvoll im Zusammenhang '
                        'mit den Regeln zum Umwandeln '
                        'von Angriffs- in Abwehraktionen (siehe '
                        'Seite 81). Sie ermöglicht das Umwandeln '
                        'einer Angriffs- in eine Abwehraktion ohne '
                        'den beim Umwandeln üblichen Malus von '
                        '4 Punkten, so dass dem Kämpfer damit zwei '
                        'Abwehraktionen pro Kampfrunde zur Verfügung '
                        'stehen (Seite 81). Die Absicht zu einer '
                        'solchen Umwandlung muss zu Beginn der '
                        'Kampfrunde verkündet werden, selbst dann, '
                        'wenn der Kämpfer die SF Aufmerksamkeit '
                        'oder Kampfgespür beherrscht. \n'
                        'Voraussetzungen: GE 12, SF Meisterparade \n'
                        'Verbreitung: 4, bei vielen professionellen '
                        'Kämpfern\n '
                        'Kosten: 100 AP ')
                elif 'Doppelangriff' in message.content:
                        await Client.send_message(message.channel, 'Doppelangriff:\n'
                        'Diese Sonderfertigkeit erlaubt das gleichzeitige '
                        'Zuschlagen mit zwei (möglichst '
                        'ähnlichen) Nahkampfwaffen gegen einen '
                        'einzigen Gegner in einem einzigen Manöver '
                        '(Seite 61). Der Verteidiger muss zwei Abwehraktionen '
                        'aufwenden, um beide Angriffe '
                        'abzuwehren.\n'
                        'Voraussetzungen: SF Beidhändiger Kampf I\n'
                        'Verbreitung: 3, bei Kämpfern, die beidhändigen '
                        'Kampfstil pflegen\n'
                        'Kosten: 100 AP; für Helden mit dem Vorteil '
                        'Beidhändig verbilligt (75 AP)')
                elif 'Entwaffnen' in message.content:
                        await Client.send_message(message.channel, 'Entwaffnen:\n'
                        'Ermöglicht einen Entwaffnungsangriff gegen '
                        'die Waffe eines Gegners: entweder mit '
                        'einer um 8 Punkte erschwerten Angriffsaktion '
                        'oder mit einer entsprechend erschwerten '
                        'Abwehraktion (was die zusätzliche Sonderfertigkeit '
                        'Meisterparade oder eine Parierwaffe '
                        'und die Sonderfertigkeit Parierwaffen I '
                        'verlangt). Das Entwaffnen eines Kämpfers, '
                        'der mit einer zweihändig geführten Waffe '
                        'kämpft, ist mit dieser Sonderfertigkeit '
                        'nicht möglich – dafür wird Meisterliches '
                        'Entwaffnen benötigt.\n '
                        'Voraussetzungen: KK 12; SF Binden\n '
                        'Verbreitung: 3, vor allem bei Schwertgesellen\n '
                        'Kosten: 200 AP ')
                elif 'Festnageln' in message.content:
                        await Client.send_message(message_channel, 'Festnageln:\n'
                        'Ein Kämpfer mit dieser Sonderfertigkeit '
                        'kann mit einer entsprechend geeigneten '
                        'Waffe das gleichnamige Manöver (Seite 62) '
                        'ausführen und damit einen Gegner am Boden '
                        'halten.\n '
                        'Voraussetzungen: GE 13, KK 13\n'
                        'Verbreitung: 4, vor allem bei Großwildjägern\n'
                        'Kosten: 200 AP\n')
                elif 'Finte' in message.content:
                        await Client.send_message(message_channel, 'Finte:\n'
                        'Diese Sonderfertigkeit ermöglicht es dem '
                        'Kämpfer, Finten zu schlagen, also sich selbst '
                        'den AT-Wurf zu erschweren, um dadurch die '
                        'gegnerische PA um den gleichen Betrag zu '
                        'senken. Finten sind auch ohne die Kenntnis '
                        'dieser SF möglich, dann jedoch weniger effektiv '
                        '(siehe Seite 62). Finten sind bei Benutzung '
                        'eines Schildes erschwert.\n '
                        'Voraussetzungen: GE 12; AT-Basiswert '
                        'mindestens 8\n '
                        'Verbreitung: 6, fast überall außer bei Barbaren- '
                        'Kulturen\n '
                        'Kosten: 200 AP ')
                elif 'Formation' in message.content:
                        await Client.send_message(message_channel, 'Formation:\n'
                        'Kämpfer, die diese Sonderfertigkeit erlernt '
                        'haben, sind in der Lage, in einer Formation '
                        'von mindestens drei Personen ihre Angriffsund '
                        'Abwehrfähigkeiten mit ihren Kameraden '
                        'zu koordinieren (Seite 68). '
                        'Voraussetzungen: SF Aufmerksamkeit\n '
                        'Verbreitung: 5, bei allen Heeren, die mit '
                        'Speeren oder Infanteriewaffen ausgestattet '
                        'sind\n'
                        'Kosten: 100 AP')
                elif 'Gegenhalten' in message.content:
                        await Client.send_message(message_channel, 'Gegenhalten:\n'
                        'Kenntnis dieser Sonderfertigkeit ermöglicht '
                        'einen Gegenangriff in einen feindlichen Angriff '
                        'hinein. Dieses Manöver (Seite 68) gilt '
                        'als Abwehraktion, erfordert also einen gegnerischen '
                        'Angriff.\n '
                        'Voraussetzungen: MU 15, GE 12; SF Meisterparade\n '
                        'Verbreitung: 3, typischerweise bei eher Duell'
                        'orientierten Kämpfern\n'
                        'Kosten: 200 AP ')
                elif 'Gezielter Stich' in message.content:
                        await Client.send_message(message.channel,'Gezielter Stich:\n'
                        'Erlaubt einen gezielten Angriff auf einen wenig '
                        'geschützten Bereich des Gegners, der die '
                        'Rüstung umgeht, leichter Wunden erzeugt '
                        'als normale Schläge und automatisch eine '
                        'Wunde anrichtet. Siehe Seite 62.\n '
                        'Voraussetzungen: SF Finte\n '
                        'Verbreitung: 4, bei vielen Speer- und Fechtwaffen-'
                        'Kämpfern\n'
                        'Kosten: 100 AP ')
                elif 'Halbschwert' in message.content:
                        await Client.send_message(message.channel, 'Halbschwert:\n'
                        'Diese Experten-Technik erlaubt es einem '
                        'Kämpfer, mit bestimmten Waffen in kürzerer '
                        'Distanzklasse zu kämpfen als für die Waffe '
                        'üblich, und dabei nur geringere Abzüge in '
                        'AT- und PA-Werten hinnehmen zu müssen. '
                        'Außerdem kann er in der kürzeren Distanzklasse '
                        'auch bestimmte Manöver wie den Defensiven '
                        'Kampf oder den Gezielten Stich anwenden, '
                        'dafür ist die Wucht der Waffe etwas '
                        'geringer. Siehe Seite 72.\n '
                        'Voraussetzungen: SF Aufmerksamkeit \n'
                        'Verbreitung: 5, bei professionellen Zweihandschwert- '
                        'und Infanteriewaffen-Kämpfern\n '
                        'Kosten: 150 AP ')
                elif 'Hammerschlag' in message.content:
                        await Client.send_message(message.channel, '(Angriffsaktion +8 +Ansage; verbraucht alle Aktionen der KR)\n'
                        'Sieht sich ein Kämpfer einem Gegner gegenüber, den er jetzt und auf '
                        'der Stelle außer Gefecht setzen muss, um z.B. an anderem Ort einem '
                        'Kameraden beizustehen, kann er das Risiko auf sich nehmen, einen '
                        'Schlag unter vollem Einsatz zu führen, um den Gegner möglichst '
                        'schnell kampfunfähig zu machen. '
                        'Um einen derartigen vernichtenden Hammerschlag auszuführen, '
                        'muss er freiwillig alle anderen Aktionen (nicht aber Freien Aktionen) '
                        'der Kampfrunde aufgeben. Ist er bereits vor seiner Initiativphase gezwungen '
                        'zu parieren, muss er entweder auf die Abwehraktion oder '
                        'auf einen Hammerschlag in der laufenden Runde verzichten. '
                        'Der Hammerschlag kann mit Anderthalbhändern (außer Nachtwind), '
                        'Hiebwaffen, Infanteriewaffen, Kettenwaffen, Zweihandflegeln, Zweihand- '
                        'Hiebwaffen und Zweihandschwertern/-säbeln ausgeführt werden und der '
                        'Angreifer muss die Sonderfertigkeit Hammerschlag beherrschen. '
                        'Um einen erfolgreichen Hammerschlag durchzuführen, muss dem '
                        'Angreifer eine AT +8 gelingen, und da es sich um eine Variante des '
                        'Wuchtschlags handelt, kann er sich diese Angriffsaktion noch weiteren, '
                        'freiwilligen Ansagen zur Schadenserhöhung erschweren. Es ist auch '
                        'möglich, den Hammerschlag mit einer Finte zu kombinieren, um die '
                        'gegnerische Parade zu erschweren. '
                        'Gelingt der Angriff, so muss dem Verteidiger eine unmodifizierte Parade '
                        'gelingen (was ab einer Zusatzansage von +2 auch einen Bruchtest '
                        'nach sich zieht; Seite 85). Misslingt die Parade, erleidet der Verteidiger '
                        'massiven Schaden: Sowohl die erwürfelten TP als auch eventuell '
                        'zur Schadenserhöhung angesagte Punkte werden verdreifacht. '
                        'Ein Hammerschlag ist nicht gegen sehr große Gegner möglich oder '
                        'gegen solche, die einen großen oder sehr großen Schild tragen. '
                        'Misslingt der Hammerschlag, so steht dem Verteidiger auf jeden Fall '
                        'ein Passierschlag zu – und der Angreifer hat keine Abwehraktion mehr '
                        'in dieser Kampfrunde. ')
                elif 'Improvisierte Waffen' in message.content:
                        await Client.send_message(message.channel, 'Improvisierte Waffen: \n'
                        'Wer sich mit dieser Sonderfertigkeit lange '
                        'genug beschäftigt hat, ist in der Lage, fast '
                        'jeden Gegenstand als Waffe zu verwenden '
                        '– und damit allerlei Tricks zu veranstalten, '
                        'die normalerweise mit improvisierten Waffen '
                        'nicht möglich sind. Außerdem ist ihre Patzer- '
                        'Chance wie bei normalen Waffen, nicht '
                        'erhöht wie sonst bei der Verwendung von improvisierten '
                        'Waffen (Seite 115). '
                        'Die Sonderfertigkeit gilt auch eingeschränkt '
                        'für improvisierte Wurfwaffen.\n '
                        'Voraussetzungen: IN 12, GE 12; TaW Raufen '
                        '10; um die SF auch mit Wurfwaffen nutzen '
                        'zu können, muss der TaW einer Wurfwaffe '
                        'mindestens 10 betragen.\n '
                        'Verbreitung: 2; im Umfeld ‘heimlicher’ Kulte '
                        'und Orden, bei Schaukämpfern \n'
                        'Kosten: 100 AP ')
                elif 'Kampf im Wasser' in message.content:
                        await Client.send_message(message.channel, 'Kampf im Wasser:\n '
                        'Normalerweise erleiden Kämpfer, deren Element '
                        'das Land ist, beim Kampf im knie-, '
                        'hüft- oder schultertiefen Wasser Abzüge auf '
                        'ihre Kampfwerte (siehe Seite 58). Einige '
                        'Kämpfer, die sich häufig mit Flachwasser- '
                        'Monstrositäten auseinandersetzen müssen, '
                        'typische Speerfischer, aber auch Seekrieger '
                        '(die ja auch am Ufer kämpfen müssen) '
                        'sind in der Lage, den unsicheren Grund, die '
                        'Einschränkungen der Bewegungen und den '
                        'Wellengang beim Kampf im Wasser teilweise '
                        'auszugleichen. Sie erleiden nur die Hälfte '
                        'der Abzüge. Sie können im Wasser auch '
                        'einige Manöver anwenden, die ungeübten '
                        'Kämpfern nicht erlaubt sind (siehe Seite 86). '
                        'Die SF kann in schultertiefem Wasser nur '
                        'mit den Talenten Dolche, Infanteriewaffen '
                        'und Speere genutzt werden, ansonsten mit allen '
                        'Nahkampffertigkeiten außer Peitsche und '
                        'Lanzenreiten.\n '
                        'Voraussetzungen: GE 12, TaW Körperbeherrschung '
                        '7\n '
                        'Verbreitung: 4, bei Kulturen, die an Flussoder '
                        'Seeufern leben, bei den verschiedenen '
                        'Kämpfern zur See\n '
                        'Kosten: 100 AP ')
                elif 'Kampfgespür' in message.content:
                        await Client.send_message(message.channel, 'Kampfgespür:\n'
                        'Ein Kämpfer mit Kampfgespür bewegt sich '
                        'mit schier traumwandlerischer Sicherheit '
                        'über das Kampffeld: Sein Initiative-Basiswert '
                        'steigt um 2 Punkte (zusätzlich zu den '
                        '4 Punkten aus der Sonderfertigkeit Kampfreflexe), '
                        'und ein Passierschlag gegen ihn ist '
                        'um 2 Punkte erschwert (zusätzlich zu den 4 '
                        'Punkten aus Aufmerksamkeit und den normalen '
                        '4 Punkten; Seite 83). Er kann jederzeit '
                        'Angriffs- in Abwehraktionen umwandeln '
                        'und umgekehrt, ohne dies vorher ankündigen '
                        'zu müssen – die Probenerschwernis von '
                        '4 Punkten gilt jedoch auch für ihn. Außerdem '
                        'ist seine IN-Probe, um zu verhindern, '
                        'dass er überrascht wird (Seite 78), um 4 '
                        'Punkte erleichtert (ebenfalls zusätzlich zu '
                        'den 4 Punkten aus Aufmerksamkeit). '
                        'Ein Kämpfer, der diese Fähigkeit mit den '
                        'Sonderfertigkeiten Klingensturm (Seite 75) '
                        'oder Klingenwand (ebenfalls Seite 75) kombiniert, '
                        'ist zudem in der Lage, seinen AT- oder '
                        'PA-Wert nach Belieben aufzuspalten, anstatt '
                        'ihn jeweils zu halbieren.\n '
                        'Voraussetzungen: IN 15; SF Aufmerksamkeit '
                        'und Kampfreflexe \n'
                        'Verbreitung: 3, bei erfahrenen Einzelkämpfern '
                        'Kosten: 300 AP\n ')
                elif 'Kampfreflexe' in message.content:
                        await Client.send_message(message.channel, 'Kampfreflexe:\n '
                        'Ein Kämpfer mit dieser Fähigkeit hat einen '
                        'um 4 Punkte erhöhten Initiative-Wert und ist '
                        'daher im Kampf häufig als erster an der Reihe. '
                        'Diese Fähigkeit kommt nur dann zum Tragen, '
                        'wenn der Kämpfer eine Rüstung mit einer BE '
                        'von maximal 4 trägt (Rüstungsgewöhnung gilt).\n '
                        'Voraussetzungen: INI-Basiswert 10\n '
                        'Verbreitung: 4, professionelle Kämpfer\n '
                        'Kosten: 300 AP ')
                elif 'Klingensturm' in message.content:
                        await Client.send_message(message.channel, 'Klingensturm:\n'
                        'Ein Kämpfer mit dieser Sonderfertigkeit '
                        'ist in der Lage, seinen durch '
                        'das Manöver (Seite 63) verbesserten '
                        'AT-Wert gleichmäßig aufzuspalten '
                        'und so zwei Angriffe mit '
                        'niedrigeren AT-Werten durchzuführen; '
                        'verfügt er darüber hinaus '
                        'noch über die Sonderfertigkeit '
                        'Kampfgespür, kann er seinen ATWert '
                        'sogar beliebig aufspalten, ein '
                        'Klingentänzer auch gegen drei Gegner.\n '
                        'Voraussetzungen: AT-Basiswert 9; SF '
                        'Ausfall und Kampfreflexe\n '
                        'Verbreitung: 3, typisch für Schwert-, Säbel- und '
                        'Fechtwaffenkämpfer\n '
                        'Kosten: 100 AP ')
                elif 'Klingentänzer' in message.content:
                        await Client.send_message(message.channel, 'Klingentänzer:\n'
                        'Ein Kämpfer mit dieser SF darf '
                        'zur Bestimmung seiner Initiative '
                        '2W6 würfeln, hat also eine INI von '
                        'Initiative-Basiswert +6 (aus Kampfgespür '
                        'und -reflexe) +2W6. Er muss '
                        'nach misslungenen Ansagen nur '
                        'die Hälfte der angesagten Punkte als '
                        'Zuschlag auf seine nächste Aktion hinnehmen. '
                        'Bei Klingensturm und Klingenwand '
                        'darf er die AT/PA-Werte gegen bis '
                        'zu drei Gegner einsetzen (siehe dort). '
                        'Einsatz all dieser besonderen Fertigkeiten '
                        'nur bei einer BE von maximal 2.\n '
                        'Voraussetzungen: GE 15, SF Kampfgespür, '
                        'Klingensturm, Klingenwand\n '
                        'Verbreitung: 1; einige wenige – vornehmlich '
                        'tulamidische – Schwertmeister\n '
                        'Kosten: 400 AP ')
                elif 'Klingenwand' in message.content:
                        await Client.send_message(message.channel, 'Klingenwand:\n'
                        'Ein Kämpfer mit dieser Fähigkeit ist in der '
                        'Lage, seinen durch das Manöver (Seite 69) '
                        'verbesserten PA-Wert gleichmäßig aufzuspalten '
                        'und so gegen zwei Angriffe einzusetzen; '
                        'verfügt er darüber hinaus noch über die Sonderfertigkeit '
                        'Kampfgespür, kann er seinen '
                        'PA-Wert sogar beliebig aufspalten. Klingentänzer '
                        'können gegen maximal drei Angriffe '
                        'parieren und ihre PA-Punkte sogar nach Bedarf '
                        'punktgenau verteilen.\n '
                        'Voraussetzungen: PA-Basiswert 9; SF Defensiver '
                        'Kampfstil und Kampfreflexe\n '
                        'Verbreitung: 3, typisch für Schwert-, Säbelund '
                        'Fechtwaffenkämpfer\n '
                        'Kosten: 100 AP ')
                elif 'Linkhand' in message.content:
                        await Client.send_message(message.channel, 'Linkhand:\n'
                        'Dies repräsentiert die grundsätzliche Erfahrung, '
                        'die ein Held haben muss, um Schilde, '
                        'Parierwaffen und Zweitwaffen effektiv '
                        'zu führen und die Bewegungen der linken '
                        'Hand mit denen der rechten Hand zu koordinieren; '
                        'zum Führen von Parierwaffen und '
                        'Zweitwaffen ist diese Sonderfertigkeit sogar '
                        'eine Grundbedingung. '
                        'Diese Fertigkeit gibt einem Schildkämpfer '
                        'einen Bonuspunkt auf den PA-Wert (so dass '
                        'dieser sich aus Parade-Basis + PA-Modifikator '
                        'des Schildes +1 errechnet). Außerdem vermindert '
                        'diese Fertigkeit die Abzüge im Kampf '
                        'mit der falschen Hand auf AT –6 / PA –6.\n '
                        'Voraussetzungen: KK 10, GE 10 \n'
                        'Verbreitung: 6, eigentlich überall, wo Schilde '
                        'oder Parierwaffen verbreitet sind \n'
                        'Kosten: 300 AP (225 AP für Helden mit '
                        'Linkshändig, 150 AP für Helden mit Beidhändig) ')
                elif 'Meisterliches Entwaffnen' in message.content:
                        await Client.send_message(message.channel, 'Meisterliches Entwaffnen:\n'
                        'Mit dieser Sonderfertigkeit ist es möglich, '
                        'auch Kämpfer mit Zweihandwaffen zu entwaffnen '
                        '(Seite 61). Außerdem ist die KKProbe '
                        'des Verteidigers erschwert, wenn er von '
                        'einem Meister des Entwaffnens seiner Waffe '
                        'beraubt werden soll und eine Einhandwaffe '
                        'führt.\n '
                        'Voraussetzungen: GE 15, SF Entwaffnen\n '
                        'Verbreitung: 2, bei Duellkämpfern, Schwertgesellen, '
                        'Rondra-Geweihten\n '
                        'Kosten: 100 AP ')
                elif 'Meiterparade' in message.content:
                        await Client.send_message(message.channel, 'Meisterparade:\n'
                        'Dies ist die grundsätzliche Fertigkeit, ein komplizierteres '
                        'Parade-Manöver auszuführen und '
                        'damit einen Gegenangriff vorzubereiten. Der '
                        'Verteidiger erschwert sich seine Parade um einen '
                        'bestimmten Punktbetrag; gelingt die Parade, '
                        'so hat er für seine nächste Angriffs- oder '
                        'Abwehraktion einen um diesen Punktbetrag '
                        'erhöhten AT- oder PA-Wert.\n '
                        'Voraussetzungen: PA-Basiswert '
                        'mindestens 8\n '
                        'Verbreitung: 5, bei vielen '
                        'Kämpfern mit Einhandwaffe '
                        '(und Schild)\n '
                        'Kosten: 200 AP ')
                elif 'Niederwerfen' in message.content:
                        await Client.send_message(message.channel, 'Niederwerfen:\n'
                        'Dies ist eine besondere Form '
                        'des Wuchtschlags. Mit einem Angriff '
                        'zum Niederwerfen (Seite 63), einer um '
                        '4 Punkte erschwerten Attacke, '
                        'kann man einen Gegner von '
                        'den Beinen holen. Mit den '
                        'Punkten einer zusätzlichen '
                        'Ansage kann man die KKProbe '
                        'zum Stehen bleiben des '
                        'Gegners erschweren.\n '
                        'Voraussetzungen: SF Wuchtschlag '
                        'Verbreitung: 4, vor allem bei '
                        'Kämpfern mit Äxten oder '
                        'Hämmern '
                        'Kosten: 100 AP ')
                elif 'Parierwaffen' in message.content:
                        await Client.send_message(message.channel, 'Parierwaffen 1:\n'
                        'Kenner dieser Sonderfertigkeit sind in der '
                        'Lage, Parierwaffen effektiver einzusetzen; sie '
                        'verwenden mit einer solchen Waffe den PAWert '
                        'der Hauptwaffe –1 plus den PA-WM der '
                        'Parierwaffe. Sie erhalten die Möglichkeit, bestimmte '
                        'Manöver mit einer Parierwaffe in der '
                        'linken Hand einzusetzen. Zum Kampf mit '
                        'Parierwaffen siehe Seite 70.\n '
                        'Voraussetzungen: GE 12, SF Linkhand\n '
                        'Verbreitung: 4, bei entsprechenden Kulturen\n '
                        'Kosten: 200 AP; für Helden mit dem Vorteil '
                        'Beidhändig verbilligt (150 AP)\n '
                        'Parierwaffen 11:\n '
                        'Diese weiterführende Fertigkeit im Umgang '
                        'mit Parierwaffen bedeutet, dass der Kämp '
                        'fer mit einer Parierwaffe den PA-Wert der '
                        'Hauptwaffe +2 plus dem PA-WM der Parierwaffe '
                        'verwendet. Die SF ermöglicht das '
                        'Erlernen von Tod von Links und erlaubt eine '
                        'zusätzliche Parade mit der Parierwaffe. Zum '
                        'Kampf mit Parierwaffen siehe Seite 70.\n '
                        'Voraussetzungen: GE 15, SF Parierwaffen I\n '
                        'Verbreitung: 3, bei entsprechenden Kulturen '
                        'Kosten: 200 AP; für Helden mit dem Vorteil\n '
                        'Beidhändig verbilligt (150 AP) ')
                elif 'Rüstungsgewöhnung' in message.content:
                        await Client.send_message(message.channel, 'Rüstungsgewöhnung 1:\n '
                        'Stadtgardisten tragen selten eine andere Rüstung '
                        'als einen Wattierten Waffenrock und '
                        'einen Helm; ebenso typisch ist es für Ambosszwerge, '
                        'in Kettenrüstung herumzulaufen. '
                        'Im Lauf der Zeit haben diese Leute sich so '
                        'sehr an ihre Rüstung gewöhnt, dass sie davon '
                        'weniger eingeschränkt werden als üblich. Die '
                        'Rüstungsgewöhnung I bezieht sich nur auf einen '
                        'bestimmten Typ Rüstung, und wenn der '
                        'Held diese Rüstung trägt, behindert sie ihn '
                        'um einem Punkt weniger als angegeben. Dies '
                        'gilt für den Gesamt-RS und nicht für jedes '
                        'einzelne Rüstungsteil. Wenn die gewählte '
                        'Rüstung mehrteilig ist, muss der '
                        'Held den Hauptteil der Rüstung tragen '
                        '(üblicherweise die Rumpf-Rüstung), '
                        'um den Bonus in Anspruch nehmen '
                        'zu können. Im oben genannten Fall kann '
                        'der Stadtgardist also die Rüstungsgewöhnung '
                        'auch dann anwenden, wenn er nur den '
                        'Waffenrock, nicht aber den Helm trägt. '
                        'Die Senkung der BE gilt nicht nur für die '
                        'Berechnung der eBE im Kampf oder beim '
                        'Talenteinsatz, sondern auch für alle anderen '
                        'Fälle, bei denen BE-Randbedingungen und '
                        '-Schwellen angegeben werden, also zum '
                        'Beispiel beim Einsatz von anderen Sonderfertigkeiten, '
                        'der Bestimmung der GS und der '
                        'Initiative-Berechnung. \n'
                        'Voraussetzungen: KK 10\n '
                        'Verbreitung: 6, mindestens einjährige Praxis \n'
                        'Kosten: 150 AP; verteuert für Helden mit '
                        'dem Vorteil Akademische Ausbildung (Magier) '
                        '(225 AP)\n '
                        'Rüstungsgewöhnung 11:\n '
                        'Wer längere Zeit (etwa ein Jahr) in verschiedenen '
                        'Formen behindernder Rüstung (BE 4 '
                        'oder höher) kämpft und auch bei weiteren '
                        'körperlichen Aktivitäten meist Rüstung trägt, '
                        'der gewöhnt sich schließlich so sehr daran, '
                        'dass ihn jegliche Rüstung (gemeint ist die '
                        'gesamte Rüstung, nicht einzelne Rüstungsteile) '
                        'um 1 Punkt weniger behindert als in '
                        'der Tabelle angegeben. (Dieser Punkt zählt '
                        'nicht zusätzlich zu dem Punkt aus Rüstungsgewöhnung '
                        'I.) '
                        'Auch hier gilt, dass sich die Senkung der BE '
                        'nicht nur auf die eBE-Berechnung, sondern '
                        'auf alle Anwendungen des Werts BE bezieht.\n '
                        'Voraussetzungen: KK 12; SF Rüstungsgewöhnung '
                        'I Verbreitung: 4, durch Praxis\n '
                        'Kosten: 300 AP; verteuert für Helden mit '
                        'dem Vorteil Akademische Ausbildung (Magier) '
                        '(450 AP)\n '
                        'Rüstungsgewöhnung 111:\n '
                        'Wer sich so weit an das Tragen von Rüstungen '
                        'gewöhnt hat, dass er diese Sonderfertigkeit '
                        'erlernt hat, der wird von jeglicher Form '
                        'von Rüstung um 2 Punkte weniger behindert '
                        '(natürlich nicht kumulativ mit Rüstungsgewöhnung '
                        'I oder II) und muss außerdem nur '
                        'die Hälfte INI-Abzüge der Rüstung hinnehmen, '
                        'also (BE–2)/2. '
                        'Um diese Erfahrung zu erlangen, sollte man '
                        'mindestens zwei Jahre lang nach dem Erwerb '
                        'von Rüstungsgewöhnung II möglichst alle '
                        'Kämpfe und auch weitere körperliche Aktivitäten '
                        'wie Marschieren, Klettern oder Reiten '
                        'in schwerer Rüstung (BE 5+ vor Abzug eventueller '
                        'Gewöhnungsboni) absolviert haben.\n '
                        'Voraussetzungen: KK 15; SF Rüstungsgewöhnung '
                        'II \n'
                        'Verbreitung: 2, durch Praxis \n'
                        'Kosten: 450 AP; verteuert für Helden mit '
                        'dem Vorteil Akademische Ausbildung (Magier) '
                        '(675 AP) ')
                elif 'Schildkampf' in message.content:
                        await Client.send_message(message.channel, 'Schildkampf 1:\n'
                        'Diese Fertigkeit im Umgang mit Schilden, '
                        'die auf der SF Linkhand basiert, gibt einem '
                        'Schildkämpfer 2 weitere zusätzliche Punkte '
                        'auf seinen Parade-Basiswert (so dass der '
                        'PA-Wert mit dem Schild sich insgesamt aus '
                        'PA-Basis + PA-Modifikator des Schildes +3 '
                        'errechnet). Ein Kämpfer mit dieser SF ist '
                        'zudem in der Lage, seinen Schild mit dem '
                        'Talent Raufen für eine Angriffsaktion zu '
                        'nutzen. Zum Schildkampf allgemein siehe '
                        'Seite 70, zum Schildangriff Seite 63.\n '
                        'Voraussetzungen: KK 12; SF Linkhand\n '
                        'Verbreitung: 6, bei vielen professionellen '
                        'Kämpfern\n '
                        'Kosten: 200 AP; für Helden mit dem Vorteil '
                        'Beidhändig verbilligt (150 AP)\n '
                        'Schildkampf 11:\n '
                        'Diese nochmals weiterführende Fertigkeit '
                        'im Umgang mit Schilden gibt einem Schildkämpfer '
                        '2 weitere zusätzliche Punkte auf '
                        'seinen Parade-Basiswert (so dass der PA-Wert '
                        'mit dem Schild sich aus PA-Basis + PA-Modifikator '
                        'des Schildes +5 errechnet). Kämpfer, '
                        'die Schildkampf II beherrschen, dürfen '
                        'in einer Kampfrunde zwei Schildparaden '
                        'zusätzlich zu ihrer Angriffsaktion durchführen. '
                        'Zum Schildkampf siehe Seite 70.\n '
                        'Voraussetzungen: KK 15; SF Schildkampf I\n '
                        'Verbreitung: 3, bei professionellen Kämpfern\n '
                        'Kosten: 200 AP; für Helden mit dem Vorteil '
                        'Beidhändig verbilligt (150 AP) ')
                elif 'Schildspalter' in message.content:
                        await Client.send_message(message.channel, 'Schildspalter:\n'
                        'Der Kämpfer ist in der Lage, einen gezielten '
                        'Angriff auf einen gegnerischen Schild durchzuführen '
                        '(Seite 64) und diesen eventuell mit '
                        'einem Schlag unbrauchbar zu machen.\n '
                        'Voraussetzungen: KK 15; SF Niederwerfen \n'
                        'Verbreitung: 3, vor allem bei Axtkämpfern \n'
                        'Kosten: 100 AP ')
                elif 'Schnellziehen' in message.content:
                        await Client.send_message(message.channel, 'Schnellziehen:\n'
                        'Dies ist die Fertigkeit, eine Waffe möglichst '
                        'schnell aus der Scheide zu ziehen und kampfbereit '
                        'zu haben. Ein Held, der Schnellziehen '
                        'beherrscht, benötigt nur eine Freie Aktion, um '
                        'eine Waffe aus einer Gürtelscheide zu ziehen, '
                        'eine (volle) Aktion, um eine Waffe aus '
                        'einer Rückenscheide zu ziehen, und drei Aktionen, '
                        'um einen Schild vom Rücken an den '
                        'Arm zu bringen. Diese Fertigkeit gilt auch '
                        'für den Umgang mit Wurfspeeren, Wurfäxten '
                        'und Wurfmessern (wobei bei letzterem '
                        'Brustgurte und Armscheiden auch als ‘Gürtelscheiden’ '
                        'zählen), muss aber nicht für jede '
                        'Waffe gesondert erlernt werden. Sie kann nur '
                        'eingesetzt werden, wenn der Kämpfer eine '
                        'Rüstung mit einer BE von maximal 4 trägt '
                        '(Rüstungsgewöhnung gilt).\n '
                        'Voraussetzungen: GE 12, FF 10\n '
                        'Verbreitung: 4, im tulamidischen Raum \n'
                        'Kosten: 200 AP; verbilligt bei Vorteil Schlangenmensch '
                        '(100 AP) ')
                elif 'Spießgespann' in message.content:
                        await Client.send_message(message.channel, 'Spießgespann:\n'
                        'Mit dieser Sonderfertigkeit kann ein überlanger '
                        'Spieß (Pike, Drachentöter) gleichzeitig '
                        'von zwei Personen geführt werden; wenn '
                        'beiden eine AT oder PA gelingt, gelingt die '
                        'gesamte Angriffs- oder Abwehraktion. Gelingt '
                        'die Attacke, so richtet ein Spießgespann '
                        'doppelt so viele TP an wie bei der Waffe angegeben; '
                        'zudem können die Kämpfer ihre '
                        'Körperkraft addieren, um den Schadensbonus '
                        'der Waffe (TP/KK) zu nutzen. Die Initiative '
                        'eines Spießgespanns ist so hoch wie '
                        'die niedrigste INI der beiden Kämpfer, modifiziert '
                        'um den Wert der Waffe. Zusätzliche '
                        'Manöver (wie der Sturmangriff) und SF können '
                        'von einem Spießgespann nur dann eingesetzt '
                        'werden, wenn beiden Kämpfern die '
                        'entsprechenden Proben gelingen und beide '
                        'Kämpfer die Voraussetzungen erfüllen. \n'
                        'Voraussetzungen: TaW Speere 10; SF Sturmangriff \n'
                        'Verbreitung: 2, fast nur bei Angroschim \n'
                        'Kosten: 100 AP ')
                elif 'Sturmangriff' in message.content:
                        await Client.send_message(message.channel, 'Sturmangriff:\n'
                        'Diese Sonderfertigkeit ermöglicht das gleichnamige '
                        'Manöver, das eine TP-Erhöhung um '
                        '(GS/2)+4 Punkte bei einem um 4 Punkte '
                        'erschwerten Angriff aus vollem Lauf mit sich '
                        'bringt. \n'
                        'Voraussetzungen: MU 12; SF Wuchtschlag \n'
                        'Verbreitung: 3, vor allem bei Kulturen, die \n'
                        'mit Äxten oder Speeren kämpfen \n'
                        'Kosten: 100 AP ')
                elif 'Tod von Links' in message.content:
                        await Client.send_message(message.channel,
                        'Tod von Links:\n'
                        'Mit dieser Sonderfertigkeit kann ein Kämpfer '
                        'einen zusätzlichen Angriff pro Kampfrunde '
                        'mit einer Parierwaffe durchführen. Diese zusätzliche '
                        'Aktion (Seite 65) erhöht nicht die '
                        'Zahl der Freien Aktionen pro Runde. Nicht '
                        'kumulativ mit der Zusatzaktion aus Beidhändiger '
                        'Kampf II oder Parierwaffen II. '
                        'Voraussetzungen: SF Beidhändiger Kampf I '
                        'und Parierwaffen II\n '
                        'Verbreitung: 3, bei Parierwaffen-Kämpfern '
                        '(v.a. im Horasreich) \n'
                        'Kosten: 100 AP; für Helden mit dem Vorteil '
                        'Beidhändig verbilligt (75 AP) ')
                elif 'Todesstoß' in message.content:
                        await Client.send_message(message.channel, 'Todesstoß:\n'
                        'Erlaubt ein Alles-oder-Nichts-Manöver (Seite '
                        '65) mit einer zum Stich geeigneten Waffe, '
                        'um einen Kampf mit einem Schlag zu beenden: '
                        'Bei gelungener erschwerter Attacke (+8 '
                        '+halber gegnerischer RS) und misslungener '
                        'gegnerischer Abwehr werden deutlich leichter '
                        'und mehr Wunden angerichtet. \n'
                        'Voraussetzungen: MU 15; SF Gezielter Stich \n'
                        'Verbreitung: 3, für Speerkämpfer bei erfahrenen '
                        'Jägern, für Fechter bei Duellisten und \n'
                        'Klingenmeistern im Horasreich und Almada '
                        'Kosten: 200 AP ')
                elif 'Umreißen' in message.content:
                        await Client.send_message(message.channel, 'Umreißen:\n'
                        'Erlaubt mit bestimmten Waffen ein Angriffsmanöver '
                        '(Seite 65), das keinen Schaden anrichtet, '
                        'sondern den Gegner durch geschickte '
                        'Technik von den Beinen holen soll. \n'
                        'Voraussetzungen: KK 12; SF Finte \n'
                        'Verbreitung: 3, vor allem bei Hellebardieren '
                        'und klassischen Doppelsöldnern \n'
                        'Kosten: 100 AP ')
                elif 'Unterwasserkampf' in message.content:
                        await Client.send_message(message.channel, 'Unterwasserkampf:\n'
                        'Ein Held mit dieser ungewöhnlichen Sonderfertigkeit '
                        'ist in der Lage, seine Bewegungen '
                        'dem Widerstand des Wassers anzupassen '
                        'und gerade so schnell zuzustoßen oder zuzugreifen, '
                        'wie es effektiv ist – er erleidet nicht '
                        'die üblichen Einbußen von AT/PA –6/–6 '
                        'beim Kampf unter Wasser (Seite 86). Kann '
                        'nur mit den Nahkampf-Talenten Dolche, '
                        'Fechtwaffen, Raufen, Ringen und Speere eingesetzt '
                        'werden. Unter Wasser ist nur eine '
                        'eingeschränkte Zahl von Manövern möglich. \n'
                        'Voraussetzungen: TaW Schwimmen 10; zur '
                        'Anwendung dieser SF muss der Held in der '
                        'Lage sein, unter Wasser zu atmen oder lange '
                        'genug die Luft anhalten zu können. \n'
                        'Verbreitung: 1, bei einigen wenigen Seekämpfern, '
                        'ansonsten nur bei Unterwasserwesen '
                        '(Necker, Risso etc.) \n'
                        'Kosten: 200 AP ')
                elif 'Waffe zerbrechen' in message.content:
                        await Client.send_message(message.channel, 'Waffe zerbrechen:\n'
                        'Mit dieser Sonderfertigkeit kann ein Kämpfer '
                        'bei seiner Parade durch ein spezielles Manöver '
                        '(Seite 71) die gegnerische Klinge mit der dafür '
                        'ausgestatteten Parierwaffe (Linkhand, Hakendolch '
                        'oder Drachenklaue) auffangen und mit '
                        'einer schnellen Bewegung zerbrechen. \n'
                        'Voraussetzungen: KK 12; PA-Basis 9; SF '
                        'Binden \n'
                        'Verbreitung: 3, bei Parierwaffen-Kämpfern '
                        'im yaquirischen oder tulamidischen Umfeld \n'
                        'Kosten: 200 AP ')
                elif 'Waffenmeister' in message.content:
                        await Client.send_message(message.channel, 'Waffenmeister (Waffe) '
                        'und Waffenmeister (Schild):\n'
                        'Ein Held mit dieser Sonderfertigkeit gehört '
                        'zu den unangefochtenen Meistern seiner '
                        'Waffengattung, von denen auf dem ganzen '
                        'Kontinent zu keiner Zeit mehr als eine '
                        'Handvoll existieren. Die SF Waffenmeister '
                        'erlangt man immer in einer bestimmten Waffenart, '
                        'sie funktioniert also ähnlich wie die '
                        'SF Waffenspezialisierung. '
                        'Die möglichen Vorteile (ein ‘Auswahlkatalog’), '
                        'die sich aus der SF ergeben, sind im '
                        'Kapitel Waffenmeister ab Seite 190 zu finden. '
                        'Der Waffenmeister kommt automatisch '
                        'in den Genuss dieser Vorteile, wenn er bei '
                        'einem Kampf eine Waffe der entsprechenden '
                        'Waffenart einsetzt und die anderen genannten '
                        'Bedingungen erfüllt. \n'
                        'Voraussetzungen: je nach Waffe, allgemein '
                        'aber lange Kampferfahrung – repräsentiert '
                        'durch mindestens 2.500 AP in Kampf-Sonderfertigkeiten '
                        '(der hier in der Liste angegebene '
                        'Grundwert zählt) –, TaW 18 im dazugehörigen '
                        'Kampf-Talent (ohne Spezialisierung), '
                        'Spezialisierung auf die gewünschte Waffenart '
                        '(wo erlaubt), bei Schilden die Sonderfertigkeiten '
                        'Schildkampf II, Beidhändiger Kampf '
                        'I und Parierwaffen I. Dazu kommen meist '
                        'noch hohe Eigenschafts-Voraussetzungen. \n'
                        'Verbreitung: 1–2, je nach Waffe \n'
                        'Kosten: 400 AP ')
                elif 'Waffenspezialisierung' in message.content:
                        await Client.send_message(message.channel, 'Waffenspezialisierung:\n'
                        'Es ist möglich, sich auf eine bestimmte Waffe '
                        'zu spezialisieren, um mit dieser Waffe besser '
                        'kämpfen zu können. Genau wie die Spezialisierung '
                        'bei anderen Talenten (siehe Seite 16) '
                        'gibt eine Spezialisierung auf eine bestimmte '
                        'Waffe Bonuspunkte auf das Talent, verändert '
                        'aber sonst nichts am Talentwert oder dessen '
                        'Steigerungsmöglichkeiten. '
                        'Eine Spezialisierung auf eine Waffe bedeutet, '
                        'dass der Held je 1 Punkt mehr auf AT und '
                        'PA mit dieser Art von Waffe aufweist (beim '
                        'Talent Peitsche 2 Punkte auf die Attacke). '
                        'Spezialisierung heißt, dass man sich eine Waffenart '
                        'aus der Waffengattung konzentriert '
                        'hat, die durch dieses Talent repräsentiert '
                        'wird, nicht auf ein bestimmtes Exemplar. Ein '
                        'thorwalscher Held spezialisiert sich also nicht '
                        'auf seine traditionelle Familienaxt ‘Haarspalter’, '
                        'sondern auf die Waffenart ‘Orknase’. '
                        'Ein Held kann mehrere Spezialisierungen, '
                        'auch aus verschiedenen Kampftechnik-Talenten '
                        'erwerben. Es ist nicht möglich, sich '
                        'auf improvisierte Waffen zu spezialisieren '
                        'und nicht bei den Talenten Blasrohr, Diskus, '
                        'Kettenstäbe, Lanzenreiten, Peitsche und Zweihandflegel. '
                        'Die Bonuspunkte aus Waffenspezialisierung '
                        'und aus einer Persönlichen Waffe '
                        'sind kumulativ. \n'
                        'Voraussetzungen: Um eine Spezialisierung '
                        'zu erwerben, muss ein Held in der dazugehörigen '
                        'Kampftechnik einen TaW von mindestens '
                        '7 aufweisen, für eine Spezialisierung '
                        'auf eine zweite Waffe aus dieser Gattung sogar '
                        'einen TaW von 14, für eine dritte TaW '
                        '21, für eine vierte einen TaW von 28. Es ist '
                        'nicht möglich, sich innerhalb eines Talents '
                        'zweimal auf ein und dieselbe Waffe zu spezialisieren. \n'
                        'Verbreitung: 2–4, je nach Art und Verbreitung '
                        'der Waffe oder durch langjährige Praxis \n'
                        'Kosten: 20 mal Aktivierungsfaktor AP; eine '
                        'zweite Spezialisierung in derselben Kampftechnik '
                        'kostet jeweils das Doppelte, eine dritte '
                        'das Dreifache usw. ')
                elif 'Windmühle' in message.content:
                        await Client.send_message(message.channel, 'Windmühle:\n'
                        'Unter Einsatz dieser Sonderfertigkeit '
                        'kann ein Kämpfer mit dem gewagten '
                        'gleichnamigen Manöver (Seite 71) besonderen '
                        'Gewinn aus einem kraftvollen '
                        'Angriff seines Gegners ziehen und einen '
                        'gegnerischen Wuchtschlag in einen eigenen '
                        'Angriff umwandeln. \n'
                        'Voraussetzungen: SF Gegenhalten und '
                        'Wuchtschlag \n'
                        'Verbreitung: 2, bei erfahrenen Kämpfern mit '
                        'Schwert, Anderthalbhänder und Zweihänder \n'
                        'Kosten: 200 AP ')
                elif 'Wuchtschlag' in message.content:
                        await Client.send_message(message.channel, 'Wuchtschlag:\n'
                        'Dies ist eine besondere Form der Attacke, die '
                        'mit all jenen Waffen ausführt werden kann, '
                        'deren Wirkung auf Wucht beruht (speziell '
                        'also Hiebwaffen und Schwerter, egal, ob ein oder '
                        'zweihändig). Bei einem Wuchtschlag '
                        'erschwert sich der Angreifer seinen AT-Wurf '
                        'um eine bestimmte Anzahl von Punkten, um '
                        'dieselbe Zahl zu seinen Trefferpunkten zu '
                        'addieren. Wuchtschläge sind auch ohne die '
                        'Kenntnis dieser SF möglich, dann jedoch '
                        'weniger effektiv (siehe Seite 65). '
                        'Voraussetzungen: KK 12 \n'
                        'Verbreitung: 7, durch Praxis \n'
                        'Kosten: 200 AP ')
                elif 'Berufsgeheimnis' in message.content:
                        await Client.send_message(message.channel, 'Berufsgeheimnis:\n Der Held hat von einem '
                        'Zunftmeister ein Geheimnis der Handwerkskunst '
                        '(selten einmal einer anderen '
                        'Talentgruppe) erfahren, das ihm besondere '
                        'Herstellungsverfahren oder die Verwendung '
                        'spezieller Materialien erlaubt. Typische Beispiele '
                        'stammen hier in erster Linie aus der '
                        'Schmiedekunst, wo z.B. Damaszierungs- '
                        'Techniken oder Zwergenspan jeweils ein solches '
                        'Berufsgeheimnis darstellen. Die Verarbeitung '
                        'von echtem (Elfen-)Bausch oder die '
                        'Herstellung von Spinnenseide fallen ebenso '
                        'in den Bereich der Berufsgeheimnisse wie die '
                        'Konstruktion von Hand-Torsionswaffen. Die '
                        'entsprechenden Regelungen bzw. Boni dürfen '
                        'nur genutzt werden, wenn der Held das '
                        'entsprechende Berufsgeheimnis kennt. '
                        'Dieses Ausschließlichkeitskriterium unterscheidet '
                        'die Sonderfertigkeit Berufsgeheimnis '
                        'von einer Talentspezialisierung (wenn auch '
                        'letztere je nach Talent durchaus im Erlernen '
                        'eingeschränkt sein kann). Nicht als Berufsgeheimnis '
                        'im regeltechnischen Sinn gelten '
                        '(alchimistische) Rezepte; diese müssen im '
                        'Spielverlauf erworben werden (wobei wiederum '
                        'das Hylailer Feuer ein Berufsgeheimnis '
                        'ist, das sich auf den Herstellungsprozess, '
                        'nicht aber das eigentliche Rezept bezieht). '
                        'Ein einzelnes Berufsgeheimnis kann sich '
                        'durchaus auf mehrere Talente beziehen (wie '
                        'Spinnenseide, das erst bestimmte Proben auf '
                        'Tierkunde wie auch auf Webkunst ermöglicht). '
                        'Talente '
                        'Voraussetzung: das passende Handwerkstalent \n'
                        'auf TaW 15 oder höher, ein bis zwei passende '
                        'Hilfs-Talente jeweils auf TaW 7+ \n'
                        'Verbreitung: 2, üblicherweise bei Zunftmeistern '
                        'und ähnlichen Veteranen \n'
                        'Kosten: 100 AP (selten weniger, bisweilen '
                        'mehr) ')
                elif 'Fälscher' in message.content:
                        await Client.send_message(message.channel, 'Fälscher:\n ermöglicht das effektive Fälschen '
                        'von Schriftstücken und Kunstwerken. Diese '
                        'Sonderfertigkeit beinhaltet das Nachahmen '
                        'von fremden Schriften, die Herstellung von '
                        'falschen Siegeln, die Auswahl des richtigen '
                        'Papiers und Farben, verschiedene '
                        'Alterungstechniken und ähnliches. '
                        'Sie erleichtert alle Proben (also meist '
                        'solche auf Schriftlicher Ausdruck, Alchimie, '
                        'Malen/Zeichnen und andere '
                        'handwerkliche Talente), die sich um eine '
                        'solche Fälschung drehen, um 3 Punkte. '
                        'Proben auf Sinnenschärfe oder passende Wissenstalente '
                        'zum Enttarnen einer solchen '
                        'professionellen Fälschung sind zusätzlich '
                        'zu den bei den Proben übrigen TaP* um 5 '
                        'Punkte erschwert. '
                        'Jedoch hilft diese Sonderfertigkeit auch beim '
                        'Erkennen solcher Fälschungen. Diese Proben '
                        'sind um 5 Punkte erleichtert. \n'
                        'Verbreitung: 2 \n'
                        'Voraussetzungen: Alchimie 5, Malen/Zeichnen \n'
                        '7, Schriftlicher Ausdruck 5; passende '
                        'Schriften 7+ \n'
                        'Kosten: 100 AP ')
                elif 'Geländekunde' in message.content:
                        await Client.send_message(message.channel, 'Geländekunde: Diese Fertigkeit steht einem '
                        'Helden offen, wenn er längere Zeit '
                        'in einer bestimmten Art von Wildnis '
                        'verbringt. Er ist mit dieser Art von '
                        'Umgebung besonders vertraut, so dass '
                        'für ihn alle Proben, die sich auf den '
                        'Umgang mit dieser speziellen Form '
                        'von Wildnis beziehen, um 3 Punkte '
                        'erleichtert sind. Das bezieht sich vor '
                        'allem auf die Natur- und Wissens-Talente '
                        'Orientierung, Wettervorhersage, '
                        'Wildnisleben, Tier- und Pflanzenkunde '
                        'sowie (je nach Meister-Maßgabe) '
                        'auch auf Sinnenschärfe und Fährtensuchen '
                        'und Fallenstellen. Seltene, aber '
                        'mögliche andere Anwendungsgebiete '
                        'sind die Identifikation bestimmter, vor '
                        'allem regional vorkommender Gifte '
                        'oder Krankheiten mittels der entsprechenden '
                        'Heilkunde-Talente oder die '
                        'Einschätzung bestimmter Gewässer '
                        'mit Seefahrt-Proben. '
                        'Vor allem ist ein geländekundiger '
                        'Held in der Lage, im '
                        'entsprechenden Gebiet mittels '
                        'Wettervorhersage- oder Wildnisleben- '
                        'Proben sehr plötzliche '
                        'Phänomene vorauszusehen, '
                        'die ein mit diesem Gebiet '
                        'weniger vertrauter Held nicht '
                        'erahnen kann (zum Beispiel einen für diese '
                        'Region typischen plötzlichen Wetterumschwung, '
                        'oder auch tückische Sumpflöcher '
                        'oder Schneewehen). '
                        'Folgende Arten von Geländekunde sind '
                        'möglich: Dschungelkundig, Eiskundig, Gebirgskundig, '
                        'Höhlenkundig, Maraskankundig, '
                        'Meereskundig, Steppenkundig, Sumpfkundig, '
                        'Waldkundig, Wüstenkundig. '
                        'Geländekunde kann mehrfach (also für verschiedene '
                        'Geländetypen) gewählt werden. \n'
                        'Voraussetzungen: kann nur durch längeren '
                        'Aufenthalt (mindestens 12 Monate) im entsprechenden '
                        'Gelände erlernt werden; es ist '
                        'allerdings auch kein weiterer Lernzeit-Aufwand '
                        'erforderlich. Die 12 Monate können '
                        'unterbrochen werden, längere Unterbrechungen '
                        'können dann jedoch zusätzliche '
                        'Zeit erfordern. \n'
                        'Verbreitung: 7, kann ohne Lehrmeister erlernt '
                        'werden \n'
                        'Lernkosten: 150 AP für die erste Geländekunde, '
                        'jedes zusätzliche Gelände je 100 AP ')
                elif 'Kulturkunde' in message.content:
                        await Client.send_message(message.channel, 'Kulturkunde:\n“Wenn zwei das Gleiche machen, '
                        'ist es doch nicht dasselbe.” Die Lebewesen '
                        'aller Kulturen müssen essen, kennen '
                        'überderische Wesen, horten einen Schatz aus '
                        'Sagen und Legenden, kleiden oder schmücken '
                        'sich, halten ihre Herrscher oder Ältesten '
                        'in Ehren – aber alle auf unterschiedliche '
                        'Art und Weise. '
                        'Proben auf alle Gesellschaftlichen und bestimmte '
                        'Wissens-Talente (Geschichtswissen, '
                        'Götter/Kulte, Heraldik, Philosophie, Rechtskunde, '
                        'Sagen/Legenden, Staatskunst, unter '
                        'Umständen auch Baukunst, Brettspiel, Kriegskunst, '
                        'Kryptographie, Magiekunde, Schätzen '
                        'und Sprachenkunde), teilweise auch auf die '
                        'Eigenschaft Charisma, sind außerhalb der '
                        'eigenen Kultur bzw. ‘kulturübergreifend’ '
                        'meist erschwert (um mindestens 3, eher 7, '
                        'teilweise auch bis zu 15 Punkten; siehe die '
                        'Anmerkung zu Gesellschaftlichen Talenten '
                        'auf Seite 22–23). Die Sonderfertigkeit Kulturkunde '
                        'erlaubt es, diese Erschwernisse zu '
                        'ignorieren. Zuschläge, die auch ein Mitglied '
                        'der entsprechenden Kultur betreffen würden '
                        '– etwa SO-Differenz –, werden hierdurch '
                        'nicht beeinflusst. '
                        'Als wählbare Kulturen für diese Sonderfertigkeit '
                        'gelten die Kulturen Mittelreich, Almada, '
                        'Andergast und Nostria, Bornland, Svellttal, '
                        'Nordlande, Horasreich, Zyklopeninseln, '
                        'Amazonen, Aranien, Tulamidenlande, Novadi, '
                        'Ferkina, Zahori, Thorwal, Gjalskerländer, Fjarninger, '
                        'Waldmenschen, Tocamuyac, Maraskan, '
                        'Südaventurien, Bukanier, Nivesen, Norbarden, '
                        'Trollzacker, Schwarze Lande, Ambosszwerge, '
                        'Brillantzwerge, Erzzwerge, Hügelzwerge, '
                        'Brobim, Auelfen, Waldelfen, Firnelfen, Steppenelfen, '
                        'Orks, Goblins, Archaische Achaz, Stammes- '
                        'Achaz, Trolle, Grolme sowie evtl. weitere '
                        'bei der Entdeckung ‘neuer’ Kulturen.')
                elif 'Meister der Improvisation' in message.content:
                        await Client.send_message(message.channel, 'Meister der Improvisation:\n'
                        'Wer über diese Sonderfertigkeit '
                        'verfügt, der kann fehlendes '
                        'Werkzeug durch improvisierte '
                        'Hilfsmittel kompensieren. Als '
                        'Meister sollten Sie eventuelle '
                        'Probenzuschläge halbieren, die '
                        'durch schlechtes, unvollständiges oder nicht '
                        'vorhandenes Werkzeug entstehen, wenn der '
                        'Held genügend Zeit hat, andere Hilfsmittel '
                        'zu suchen: einen Stein als Hammer, Gräser '
                        'als Schnüre, etwas Scharfkantiges als Schneidewerkzeug '
                        'und dergleichen. '
                        'Wenn ein Meister der Improvisation eine Probe '
                        'in einem Handwerkstalent ablegen soll, '
                        'das er nicht hat, so dass er auf ein anderes '
                        'Talent ausweichen muss (siehe Seite 13), '
                        'gelten für ihn nur die Hälfte der verhängten '
                        'Erschwernisse. \n'
                        'Voraussetzungen: IN und FF mindestens 12 \n'
                        'Verbreitung: 7, ergibt sich vor allem aus Praxis \n'
                        'Kosten: 200 AP ')
                elif 'Nandusgefälliges Wissen' in message.content:
                        await Client.send_message(message.channel, 'Nandusgefälliges Wissen:\n Wer über diese '
                        'Sonderfertigkeit verfügt, der besitzt eine für '
                        'aventurische Verhältnisse fantastische Allgemeinbildung '
                        'und ist in der Lage, Wissen '
                        'aus verwandten Gebieten zu kombinieren '
                        'und daraus die richtigen Schlüsse zu ziehen. '
                        'Beim Ableiten eines nicht vorhandenen '
                        'Wissenstalents gelten für einen Besitzer dieser '
                        'Sonderfertigkeit nur die Hälfte der verhängten '
                        'Erschwernisse, insbesondere auch '
                        'beim Ableiten auf die Eigenschaft Klugheit '
                        '(Näheres zum Ableiten siehe Seite 13/14). '
                        'Dies kommt insbesondere bei Kenntnissen '
                        'zum Tragen, die nur schwer von einem existierenden '
                        'Wissens-Talent abgedeckt werden, '
                        'z.B. die Kenntnis bedeutender Künstler '
                        'und Kunstwerke, verbreiteter Gedichte und '
                        'Standorte großer Bibliotheken. Der Held hat '
                        'große Übung in der Bibliotheksrecherche und '
                        'braucht nur die halbe Zeit, um interessante '
                        'Dinge in Büchern ausfindig zu machen. \n'
                        'Voraussetzungen: KL und IN mindestens 12 \n'
                        'Verbreitung: 4, bei allen Kulten und Professionen, '
                        'die auf Allgemeinbildung Wert legen \n'
                        'Kosten: 200 AP; automatisch beim Vorteil '
                        'Akademische Ausbildung (Gelehrter) ')
                elif 'Ortskenntnis' in message.content:
                        await Client.send_message(message.channel, 'Ortskenntnis: \nDer Held hat Kenntnis eines '
                        'bestimmten Gebiets, seiner Weghindernisse, '
                        'Wetterverhältnisse, Straßenbedingungen, wilden '
                        'Tiere und dergleichen. Das Gebiet sollte '
                        'nicht größer als 100 Rechtmeilen (Quadratkilometer) '
                        'sein, kann aber auch (im Falle '
                        'eines Flusses oder einer Küste) eine Strecke '
                        'von 100 mal 1 Meile oder gar eine Straße '
                        'und deren nächste Umgebung (also etwa '
                        '250 Schritt mal 400 Meilen) sein. In einer '
                        'Kleinstadt bedeutet dies Kenntnis der Stadt, '
                        'ihrer Abkürzungen, Kanalisationsanlagen, '
                        'des Verhaltens der Garde und so fort; in einer '
                        'aventurischen Großstadt (ab ca. 10.000 '
                        'Einwohnern) steht Ortskenntnis nur für die '
                        'Kenntnis eines einzelnen Stadtteils. Diese '
                        'Sonderfertigkeit kann mehrfach (wie für benachbarte '
                        'Stadtteile, den Verlauf des Großen '
                        'Flusses und mehr) gewählt werden. '
                        'Spieltechnisch erlaubt diese Sonderfertigkeit, '
                        'bis zu 7 Punkte aus Probenzuschlägen auf '
                        'passende Talente (Wildnisleben und Orientierung '
                        'in der freien Natur, Gassenwissen und '
                        'Orientierung in Städten) zu ignorieren, wenn '
                        'sich der Held am passenden Ort aufhält. \n'
                        'Voraussetzungen: längerer Aufenthalt an '
                        'gewünschtem Ort oder häufigere Reisen '
                        'entlang der Strecke (Meisterentscheid; bei '
                        '‘Aufenthalt’ jedoch nicht unter einem halben '
                        'Jahr); es ist allerdings auch kein weiterer Aufwand '
                        'an Lernzeit erforderlich. \n'
                        'Verbreitung: 7, aus der Praxis heraus \n'
                        'Kosten: 150 AP pro bekannter Örtlichkeit / '
                        'Strecke für die erste Ortskenntnis, 100 AP für '
                        'alle folgenden')
                elif 'Rosstäuscher' in message.content:
                        await Client.send_message(message.channel, 'Rosstäuscher: \nMit Hilfe dieser Sonderfertigkeit '
                        'kann ein Tier (auch aventurisch fast '
                        'ausschließlich Pferde – daher der Name) '
                        'gezielt ‘geschminkt’, d.h. optisch aufgewertet, '
                        'werden, um einen höheren Preis beim '
                        'Verkauf zu erzielen. Der Held kennt viele '
                        'Methoden und kann sie selbst anwenden '
                        '(siehe Zoo-Botanica Aventurica). Bei allen '
                        'Tätigkeiten, die mit dem Verschönern von '
                        'Pferden zusammenhängen (also vor allem '
                        'Sich Verkleiden, Tierkunde, Abrichten, Pflanzenkunde, '
                        'Alchimie, Menschenkenntnis und '
                        'Überreden), hat der Held einen um 5 Punkte '
                        'verbesserten Talentwert. Dieser Bonus wird '
                        'auch angerechnet, wenn der Held auf dem '
                        'Pferdemarkt feststellen will, ob ein Tier mittels '
                        'solcher Methoden behandelt worden ist. \n'
                        'Voraussetzung: Reiten, Sich Verkleiden, Abrichten '
                        'und Überreden jeweils TaW 7 \n'
                        'Verbreitung: 4 \n'
                        'Kosten: 100 AP ')
                elif 'Standfest' in message.content:
                        await Client.send_message(message.channel, 'Standfest: \nDies ist die erlernbare, schwächere '
                        'Variante des Vorteils Balance. Helden, die diese '
                        'Sonderfertigkeit erlernt haben, dürfen alle '
                        'Körperbeherrschungs-, Athletik- und Akrobatik- '
                        'Proben um 2 Punkte und alle GE-Proben '
                        'um 1 Punkt erleichtert ablegen, wenn diese '
                        'mit dem Balancehalten oder dem Stehenbleiben '
                        'auf schwankendem Untergrund zu tun '
                        'haben. Weiterhin hilft Standfest im Kampf, '
                        'nach bestimmten Kampfmanövern stehen '
                        'zu bleiben (siehe die Manöver Umreißen und '
                        'Niederwerfen auf den Seiten 65 bzw. 63) oder '
                        'einen Sturz bei einem Patzer (Seite 85) zu '
                        'vermeiden. \n'
                        'Voraussetzungen: GE 12 \n'
                        'Verbreitung: 4, bei Kulturen und Professionen, '
                        'die viel mit schwankendem '
                        'oder unsicherem Untergrund (Schiffe, '
                        'Gebirge) zu tun haben \n'
                        'Kosten: 200 AP; ist in den Vorteilen Balance '
                        '/ Herausragende Balance enthalten ')
                elif 'Talentspezialisierung' in message.content:
                        await Client.send_message(message.channel, 'Talentspezialisierung: \nOft sind Spezialisierungen '
                        'möglich, weil der Held sich besonders '
                        'mit einem bestimmten Bereich des Talents '
                        'beschäftigt hat. Eine Auflistung, welche '
                        'Spezialisierungen in welchem Talent möglich '
                        'sind, finden Sie oben bei der detaillierten '
                        'Beschreibung der Talente. Im gewählten '
                        'Spezialgebiet verfügt der Held dann über einen '
                        'um 2 Punkte höheren effektiven TaW. \n'
                        'Voraussetzungen: TaW 7 für die erste Spezialisierung, '
                        'TaW 14 für die zweite Spezialisierung, '
                        'TaW 21 für die dritte Spezialisierung, '
                        'TaW 28 für eine eventuelle vierte Spezialisierung \n'
                        'Verbreitung: je nach Talent bei entsprechend '
                        'Vorgebildeten oder durch langjährige Praxis \n'
                        'Kosten: Der Erwerb der ersten Spezialisierung '
                        'in einem Talent kostet 20 AP mal Aktivierungsfaktor, '
                        'also zum Beispiel 60 AP für '
                        'ein Talent der Kategorie C. Der Erwerb einer '
                        'zweiten Spezialisierung in einem Talent kostet '
                        'das Doppelte, eine dritte das Dreifache, '
                        'eine Vierte das Vierfache. Die Steigerungskosten '
                        'des TaW eines spezialisierten Talents '
                        'werden immer gemäß den Kosten des (unspezialisierten) '
                        'Grundwerts berechnet. ')
                elif 'Bornländisch' in message.content:
                        await Client.send_message(message.channel, 'Bornländisch:\n'
                        'Redet man von Freistil- oder ‘bornischem’ Ringkampf, meint man meist '
                        'eine Prügelei mit Kratzen, Beißen und Treten (und Brüllen und Spucken), '
                        'die genau zwei Regeln kennt: Es werden keine Waffen eingesetzt. '
                        'Es wird bis zur Kampfunfähigkeit eines der Beteiligten gekämpft. '
                        'Voraussetzungen: TaW Raufen und Ringen je 5 \n'
                        'Verbreitung: 6, trotz des Namens aventurienweit \n'
                        'Kosten: 100 AP \n'
                        'Manöver: Auspendeln, Biss, Block, Fußfeger, Griff, Halten, '
                        'Klammer, Knie, Kopfstoß, Niederringen, Schmutzige Tricks, '
                        'Schwitzkasten, Tritt, Wurf, Würgegriff \n'
                        'Besonderheit: verbessert AT und PA beim Ringen um je 1 Punkt. ')
                elif 'Gladiatorenstil' in message.content:
                        await Client.send_message(message.channel, 'Gladiatorenstil:\n'
                        'Dieser Stil entstammt den Blutgruben Fasars und den Arenen '
                        'Al’Anfas und dient in erster Linie der Belustigung des Publikums – die '
                        'meisten Schläge sehen spektakulär aus, hinterlassen aber kaum einmal '
                        'einen blauen Fleck; Gladiatoren und Schaukämpfer sind schließlich '
                        'zu wertvoll, um sie an einem Nachmittag zu verbrauchen. '
                        'Voraussetzungen: TaW Raufen und Ringen je 7 \n'
                        'Verbreitung: 3, Gladiatoren, Schau- und Jahrmarktskämpfer \n'
                        'Kosten: 150 AP \n'
                        'Manöver: Auspendeln, Beinarbeit, Block, Doppelschlag, Eisenarm, '
                        'Fußfeger, Gerade, Griff, Halten, Hoher Tritt, Klammer, Kopfstoß, '
                        'Kreuzblock, Niederringen, Schwinger, Schwitzkasten, Sprung, '
                        'Sprungtritt, Tritt, Wurf \n'
                        'Besonderheiten: verbessert AT und PA beim Raufen oder Ringen '
                        '(festlegen) um je 1 Punkt. Ein Kämpfer im Gladiatorenstil kann sich '
                        'entscheiden, bis zu drei Punkten weniger echten Schaden bei einem '
                        'Schlag anzurichten und stattdessen diese Punkte auf den angerichteten '
                        'Ausdauerschaden zu legen. (Nicht erlaubt, wenn er eine Orchidee, '
                        'Veteranenhand o.ä. führt.) ')
                elif 'Hammerfaust' in message.content:
                        await Client.send_message(message.channel, 'Hammerfaust:\n'
                        'Dieser Stil – benannt nach der thorwalschen Otta, die ihn über die '
                        'Grenzen der Nordlande hinaus verbreitet hat – ist eher ein sportliches '
                        'Kräftemessen mit fliegenden Fäusten als eine wirkliche Kampftechnik, '
                        'was nicht heißt, dass man einen thorwalschen Boxer im waffenlosen '
                        'Kampf für verspielt halten sollte.\n'
                        'Voraussetzungen: TaW Raufen 7\n'
                        'Verbreitung: 4, aventurischer Nordwesten, Schaukämpfer\n'
                        'Kosten: 150 AP\n'
                        'Manöver: Auspendeln, Block, Doppelschlag, Eisenarm, Gerade, '
                        'Handkante, Kreuzblock, Schmetterschlag, Schwinger\n'
                        'Besonderheiten: verbessert AT und PA beim Raufen um je 1 Punkt. '
                        'Ein Hammerfaust-Kämpfer ist in der Lage, auch mit der bloßen Faust '
                        'massive Gegenstände zu beschädigen (Holzbohlen durchschlagen, '
                        'Ziegelsteine zertrümmern), ohne sich dabei selbst zu verletzen: Er '
                        'kann sich entscheiden, die TP(A) als Strukturschaden (siehe Seite '
                        '191) anzurichten. Ein Hammerfaust-Kämpfer kann auch mit dem '
                        'Talent Raufen einen Ausfall durchführen, wenn er diese SF erlernt '
                        'hat.')
                elif 'Hruruzat' in message.content:
                        await Client.send_message(message.channel, 'Hruruzat:\n'
                        'Dieser sehr elegant und ‘tänzerisch’ aussehende Kampfstil ist die '
                        'traditionelle Domäne der verschiedenen Waldmenschenvölker, die '
                        'sich damit sowohl gegen wilde Tiere als auch gegen Sklavenjäger zur '
                        'Wehr setzen. Der Schwerpunkt dieser Kampftechnik liegt auf mörderisch '
                        'effektiven Tritten. Ein sehr ähnlicher (vermutlich einst von '
                        'Waldmenschen-Sklaven eingeführter) Kampfstil ist auf Maraskan als '
                        'Rur’Uzat bekannt. \n'
                        'Voraussetzungen: TaW Raufen 10, TaW Ringen 7 \n'
                        'Verbreitung: 3, Waldmenschen-Kulturen, Maraskan, Südliche Stadtstaaten \n'
                        'Kosten: 200 AP \n'
                        'Manöver: Auspendeln, Beinarbeit, Block, Doppelschlag, Eisenarm, '
                        'Fußfeger, Gerade, Griff, Handkante, Hoher Tritt, Knie, Kopfstoß, '
                        'Kreuzblock, Schwinger, Sprung, Sprungtritt, Tritt, Wurf \n'
                        'Besonderheiten: verbessert AT und PA beim Raufen um je 1 Punkt. '
                        'Alle Tritte (Hoher Tritt, Sprungtritt, Tritt) eines Hruruzat-Kämpfers '
                        'richten 2W6 TP(A) an. Fällt bei diesem Schadenswurf ein Pasch, so '
                        'ist dem Kämpfer ein ‘Zat’ gelungen, ein Tritt gegen besonders verwundbare '
                        'Teile der gegnerischen Anatomie: Der Kämpfer darf '
                        'nochmals einen Schadenswurf ausführen und zum bereits erwürfelten '
                        'Resultat addieren (und, falls erneut ein Pasch fällt, '
                        'das Spiel wiederholen). Der Kämpfer kann Punkte aus einer '
                        'Ansage dazu verwenden, einen Zat herbeizuführen, anstatt die '
                        'TP(A) zu erhöhen: für je 4 Punkte Ansage kann er einen der '
                        'Schadens-W6 um einen Punkt verändern (dies jedoch nicht zusätzlich '
                        'zu einer Ansage, um die TP zu erhöhen und nur im ersten Schadenswurf). '
                        'Eine Glückliche Attacke verdoppelt nicht die TP(A)-Zahl, '
                        'sondern ist automatisch ein Zat. ')
                elif 'Mercenario' in message.content:
                        await Client.send_message(message.channel, 'Mercenario:\n'
                        'Weniger für die bei Söldnern üblichen Kneipenschlägereien gedacht, als '
                        'für Kämpfe in beengter Umgebung (wie Gassen oder Gebäuden), vor '
                        'allem aber zum Einsatz in Kombination mit Waffen, sei es, um noch '
                        'im Handgemenge mit dem Schwertknauf zuzuschlagen, oder um die '
                        'eigene Parade gegen ankommende Schläge und Stiche zu verbessern. \n'
                        'Voraussetzungen: TaW Raufen 10, TaW Ringen 7 \n'
                        'Verbreitung: 4, Söldner und Seesöldner, eher südaventurisch \n'
                        'Kosten: 200 AP \n'
                        'Manöver: Auspendeln, Beinarbeit, Block, Eisenarm, Fußfeger, Griff, '
                        'Halten, Klammer, Knaufschlag, Knie, Kopfstoß, Niederringen, '
                        'Schmutzige Tricks, Schwinger, Schwitzkasten, Sprung, Tritt, Versteckte '
                        'Klinge, Wurf \n'
                        'Besonderheiten: verbessert AT und PA beim Raufen um je 1 Punkt. '
                        'Wenn ein Mercenario-Kämpfer einen Bewaffneten in der Distanzklasse '
                        'Nahkampf angreift, erleidet er nur einen Verlust von 3 Punkten '
                        'auf seine AT, wird seine Attacke zur Distanzklassenverkürzung pariert, '
                        'erleidet er keinen Schaden. ')
                elif 'Unauer Schule' in message.content:
                        await Client.send_message(message.channel, 'Unauer Schule:\n'
                        'Die siebenundzwanzig erlaubten Griffe von Unau sind ein stark formalisiertes, '
                        'nichtsdestotrotz sehr effektives System verschiedener Grundpositionen, '
                        'Griffe und Würfe für das ‘saubere’ Ringen, das sich in den '
                        'Tulamidenlanden sogar über die Khôm hinaus als Sport etabliert hat. \n'
                        'Voraussetzungen: TaW Ringen 10 \n'
                        'Verbreitung: 4, Tulamidenlande, vor allem Novadis \n'
                        'Kosten: 150 AP; verbilligt (75 AP für Besitzer des Vorteils Schlangenmensch) \n'
                        'Manöver: Auspendeln, Beinarbeit, Eisenarm, Fußfeger, Griff, Halten, '
                        'Klammer, Niederringen, Schwitzkasten, Wurf \n'
                        'Besonderheiten: verbessert AT und PA beim Ringen um je 1 Punkt. '
                        'Für einen Kämpfer der Unauer Schule sind alle Entwinden-Manöver '
                        '(seien es GE-, Entfesseln-, Akrobatik- oder Ringen-Proben), auch '
                        'zum Entwinden aus dem Griff von Tieren oder Schlingpflanzen, um '
                        '2 Punkte erleichtert. ')
                elif 'Auspendeln' in message.content:
                        await Client.send_message(message.channel, 'Auspendeln (30 AP): \nBei dieser allgemeinen '
                        'Parade-Variante (Raufen oder Ringen) ist der '
                        'Verteidiger in der Lage, seinen Oberkörper '
                        'und seinen Kopf scheinbar unabhängig von '
                        'seinen Beinen bewegen zu können. Ohne '
                        'Auspendeln sind alle (waffenlosen) Paraden '
                        'gegen Gerade, Hoher Tritt, Schmetterschlag '
                        'und Schwinger um 4 Punkte erschwert. ')
                elif 'Beinarbeit' in message.content:
                        await Client.send_message(message.channel, 'Beinarbeit (30 AP): \neine Parade-Variante für '
                        'Raufen und Ringen, bei welcher der Verteidiger '
                        'sowohl auf sicheren als auch auf beweglichen '
                        'Stand achtet. Ohne Beinarbeit sind (waffenlose) '
                        'Paraden gegen Fußfeger, Knie, Tritt und '
                        'Schwanzfeger um 4 Punkte erschwert. ')
                elif 'Biss' in message.content:
                        await Client.send_message(message.channel, 'Biss (40 AP, automatisch für Goblins und '
                        'Orks): \nRaufen-AT; der Angreifer ist in der '
                        'Lage, so etwas wie einen ‘Wuchtschlag’ mit '
                        'seinen Zähnen durchzuführen, also sich '
                        'die AT zu erschweren, um bei Gelingen die '
                        'Ansage zu seinen TP(A) zu addieren. Bisse '
                        'gegen bewaffnete Gegner tragen ein besonderes '
                        'Risiko in sich, da der Angreifer bei einer '
                        'erfolgreichen Parade die volle Anzahl echter '
                        'Trefferpunkte erleidet (ohne TP/KK), als '
                        'wäre er von einem Schlag getroffen worden. ')
                elif 'Block' in message.content:
                        await Client.send_message(message.channel, 'Block (30 AP): \nRaufen-PA, eine waffenlose '
                        'Variante des bewaffneten ‘Bindens’; der '
                        'Kämpfer kann eine erschwerte Parade ansagen '
                        'und bei Gelingen mit den so gewonnenen '
                        'Punkten die nächstfolgende gegnerische '
                        'PA erschweren. ')
                elif 'Doppelschlag' in message.content:
                        await Client.send_message(message.channel, 'Doppelschlag (50 AP): \nRaufen-AT; mit diesem '
                        'Manöver ist der Kämpfer in der Lage, '
                        'gleichzeitig (in einer einzigen Angriffsaktion) '
                        'mit beiden Fäusten oder Handkanten zuzuschlagen, '
                        'wozu ihm eine einzige Raufen-AT '
                        '+4 gelingen muss. Der Verteidiger muss '
                        '(durch Umwandeln, wenn ihm dies möglich '
                        'ist) zwei Paraden aufwenden, um die Schläge '
                        'abzuwehren (gelingt nur eine Parade, wurde '
                        'auch nur ein Schlag abgewehrt), einen um '
                        '4 Punkte erschwerten Block ausführen oder '
                        'sich den Schlägen mit einem Gezielten Ausweichen- '
                        'Manöver +6 entziehen. Ein Doppelschlag '
                        'kann mit einer Ansage versehen werden, '
                        'die den Schaden erhöht; er kann Punkte '
                        'aus einem Kreuzblock nutzen. Die einzelnen '
                        'Hiebe des Doppelschlags richten bei Erfolg '
                        'jeweils separat TP(A) an. ')
                elif 'Eisenarm' in message.content:
                        await Client.send_message(message.channel, 'Eisenarm (60 AP): \nRaufen-PA; in größeren '
                        'Distanzklassen als Handgemenge nutzbar. '
                        'Der Held hat gelernt, so in eine gegnerische '
                        'Attacke hineinzugehen, dass er auch ohne '
                        'Waffe einen bewaffneten Angriff parieren '
                        'kann, ohne sich zu verletzen. Dazu konzentriert '
                        'er seine Bewegungen auf den Arm des '
                        'Gegners, den Waffengriff oder andere ungefährliche '
                        'Waffenteile: Er erleidet durch die '
                        'Parade nur TP(A) anstelle von TP. Er ist zudem '
                        'in der Lage, gegen Bewaffnete die Manöver '
                        'Binden und Entwaffnen einzusetzen '
                        '(wenn er die entsprechende SF besitzt und '
                        'jeweils mit 4 Punkten Erschwernis auf die '
                        'jeweilige Probe). Ein Kämpfer mit Eisenarm '
                        'erleidet keine Abzüge auf seinen INI-Modifikator '
                        'beim Kampf gegen Bewaffnete. ')
                elif 'Fußfeger' in message.content:
                        await Client.send_message(message.channel, 'Fußfeger (40 AP): \nRaufen-AT; ein Tritt nach '
                        'den Beinen des Gegners, um diesen aus der '
                        'Balance zu bringen, die waffenlose Variante '
                        'des ‘Umreißen’-Manövers. Es wird eine AT '
                        'mit Ansage gewürfelt, bei deren Gelingen '
                        '(und Misslingen der PA) der Verteidiger eine '
                        'GE-Probe ablegen muss, um auf den Beinen '
                        'zu bleiben. Geht er zu Boden, verliert er 2W6 '
                        'Punkte INI. Die angesagten Punkte beim Angriff '
                        'können entweder die Parade des Verteidigers '
                        'oder die GE-Probe erschweren (auch '
                        'verteilt). Ohne Beinarbeit ist die Parade gegen '
                        'einen Fußfeger um 4 Punkte erschwert. Mit '
                        'dem Vorteil Balance sind sowohl die Parade als '
                        'auch die eventuelle GE-Probe um 2 Punkte '
                        'erleichtert, mit Herausragende Balance um 4 '
                        'Punkte, mit der SF Standfest um 1 Punkt. ')
                elif 'Gerade' in message.content:
                        await Client.send_message(message.channel, 'Gerade (30 AP): \nRaufen-AT; bei dieser Art '
                        'von Schlag kann eine AT mit einer Ansage '
                        'versehen werden, um bei Gelingen die eigenen '
                        'TP zu erhöhen. Ohne Auspendeln ist die Parade '
                        'gegen eine Gerade um 4 Punkte erschwert. ')
                elif 'Griff' in message.content:
                        await Client.send_message(message.channel, 'Griff (30 AP): \nRingen-AT; kann und sollte '
                        'als AT mit Ansage ausgeführt werden; ein gegriffener '
                        'Gegner erleidet Erschwernisse auf '
                        'alle Manöver, Angriffs- und Abwehraktionen '
                        'in Höhe der halben Ansage, so lange der Griff '
                        'anhält. Ein Griff kann entweder durch eine '
                        'Parade abgewehrt werden, die um die Ansage '
                        'erschwert ist, oder aber der Gegriffene kann '
                        'versuchen, den Griff abzuschütteln, wozu '
                        'eine eigene AT (Raufen oder Ringen) erforderlich '
                        'ist, die um die halbe Ansage erschwert '
                        'ist (s.o.), aber von dem Greifenden nicht pariert '
                        'werden kann; ein solcher Abschüttelungs- '
                        'Angriff erzeugt keinen Schaden. ')
                elif 'Halten' in message.content:
                        await Client.send_message(message.channel, 'Halten (40 AP): \nRingen-AT oder -PA; der '
                        'Kämpfer kann eine Erschwernis auf sein '
                        'Manöver ansagen (AT bzw. PA mit Ansage) '
                        'und bei Gelingen mit den so gewonnenen '
                        'Punkten die nächstfolgende gegnerische Aktion '
                        'erschweren. ')
                elif 'Handkante' in message.content:
                        await Client.send_message(message.channel, 'Handkante (60 AP): \nRaufen-AT; bei dieser '
                        'Art von Schlag kann eine AT mit einer Ansage '
                        'versehen werden, um bei Gelingen die eigenen '
                        'TP zu erhöhen. Richtet der Schlag mehr '
                        '‘echte’ Schadenspunkte an, als die halbe KO '
                        'des Opfers beträgt, so erleidet es eine Wunde '
                        '(meist gebrochene Knochen), d.h. für einen '
                        'Handkanten-Angriff gilt die Erhöhung der '
                        'Wundschwelle im Waffenlosen Kampf nicht. ')
                elif 'Hoher Tritt' in message.content:
                        await Client.send_message(message.channel, 'Hoher Tritt (40 AP): \nRaufen-AT; diese Art '
                        'von Angriff (in der Distanzklasse N) kann '
                        'nur mittels Auspendeln oder Kreuzblock (oder '
                        'Ausweichen oder Waffenparade) vernünftig '
                        'abgewehrt werden (ansonsten ist die PA um 4 '
                        'Punkte erschwert); es kann eine AT mit Ansage '
                        'zur TP-Erhöhung sein. ')
                elif 'Klammer' in message.content:
                        await Client.send_message(message.channel, 'Klammer (40 AP): \nRingen-AT; dieser Angriff '
                        'kann mit einer Ansage versehen werden, um '
                        'die Klammer zu verstärken. Ein geklammerter '
                        'Gegner kann sich nur mit einer Ringen-PA '
                        '(erschwert um die Ansage) oder einer KK-Probe '
                        '(erschwert um die doppelte KK-Differenz '
                        'zum Klammernden, mindestens jedoch die '
                        'Ansage) befreien. Sowohl Klammernder als '
                        'auch Geklammerter können nur die Angriffe '
                        'Biss, Kopfstoß, Knie, Schwitzkasten und Würgegriff '
                        'einsetzen, wobei diese für den Geklammerten '
                        'noch um die Ansage erschwert sind. ')
                elif 'Knaufschlag' in message.content:
                        await Client.send_message(message.channel, 'Knaufschlag (50 AP): \nRaufen-AT; der '
                        'Kämpfer ist in der Lage, mit dem Knauf einer '
                        'Waffe zuzuschlagen und 1W6+2 TP (A) '
                        'anzurichten; dies funktioniert auch in der '
                        'Distanzklasse Handgemenge, selbst, wenn '
                        'die Waffe nur die Distanzklasse Nahkampf '
                        'hat. Ein Knaufschlag kann mit einer Ansage '
                        'versehen werden, um die TP(A) zu erhöhen '
                        'oder die gegnerische Parade zu erschweren. ')
                elif 'Knie' in message.content:
                        await Client.send_message(message, 'Knie (30 AP): \nRaufen-AT; ein hochgezogenes '
                        'Knie in die Weichteile ist nur schwer zu parieren: '
                        'Ohne Beinarbeit, Kreuzblock oder ein '
                        'Ausweichen-Manöver ist die PA gegen einen '
                        'solchen Angriff um 4 Punkte erschwert. Ein '
                        'Knie-Angriff richtet bei Männern 1W6+2 '
                        'TP (A) an (bei Frauen und Achaz nur 1W6 '
                        'TP(A)), und wenn die SP(A) die Wundschwelle '
                        'des Gegners überschreiten, verliert '
                        'er alle verbleibenden Aktionen der laufenden '
                        'Kampfrunde, ist 1W3 Kampfrunden kampfunfähig '
                        'und erleidet zudem einen INI-Verlust '
                        'von 2W6 Punkten. Knie kann eine AT '
                        'mit Ansage zur TP-Erhöhung sein. ')
                elif 'Kopfstoß' in message.content:
                        await Client.send_message(message.channel, 'Kopfstoß (40 AP): \nRaufen-AT; der '
                        'Angreifer ist in der Lage, einem Gegner '
                        'seinen Kopf an eine verwundbare '
                        'Stelle zu rammen. Eine Ansage bei diesem '
                        'Manöver erhöht die TP. Kopfstöße '
                        'gegen bewaffnete Gegner tragen ein besonderes '
                        'Risiko in sich, da der Angreifer bei einer '
                        'erfolgreichen Parade die volle Anzahl echter '
                        'Trefferpunkte erleidet (ohne TP/KK), so als '
                        'wäre er von einem Schlag getroffen worden. '
                        'Ein Kopfstoß erzeugt normalerweise 1W6 '
                        'TP (A), mit einem Metallhelm sogar 1W6+2 '
                        'TP (A), vergleichbar mit dem Schaden durch '
                        'Schwere Handschuhe oder genagelte Stiefel. ')
                elif 'Kreuzblock' in message.content:
                        await Client.send_message(message.channel, 'Kreuzblock (50 AP): \nRaufen-PA; dies ist eine '
                        'waffenlose ‘Meisterparade’, die es bei Gelingen '
                        'erlaubt, die Punkte aus der PA-Ansage '
                        'in einem Gegenangriff so zu verteilen, dass '
                        'gleichzeitig die PA des Gegners erschwert wie '
                        'auch die eigene Raufen-AT erleichtert wird. '
                        'Kreuzblock funktioniert als reguläre Parade '
                        'auch gegen Knie, Tritt und Sprungtritt. Wer '
                        'bereits Block beherrscht, zahlt für das Erlernen '
                        'des Kreuzblocks nur 20 AP. ')
                elif 'Niederringen' in message.content:
                        await Client.send_message(message.channel, 'Niederringen (40 AP): \nRingen-AT; im Gegensatz '
                        'zu einem Wurf geht bei einem gelungenen '
                        'Angriff zum Niederringen der '
                        'Angreifer selbst mit zu Boden: Der Angreifer '
                        'verliert dann 1W6 Punkte INI, der Verteidiger '
                        '2W6 Punkte. Der Angreifer kann den '
                        'Angriff zum Niederringen jedoch als AT mit '
                        'Ansage ausführen und durch Aufteilen der '
                        'Ansage sowohl die PA des Gegners erschweren '
                        'als auch seine nachfolgende AT (z.B. einen '
                        'Schwitzkasten) erleichtern. ')
                elif 'Schmetterschlag' in message.content:
                        await Client.send_message(message.channel, 'Schmetterschlag (50 AP, Voraussetzung:Manöver Gerade): \nRaufen-AT; diese Art '
                        'von Schlag ist ein verstärkte Variante des '
                        'Manövers Gerade, mit folgender Ergänzung: '
                        'Richtet der Schlag mehr SP(A) an, als die '
                        'Wundschwelle des Opfers beträgt, so muss '
                        'dem Opfer eine einfache KO-Probe gelingen, '
                        'um nicht für 1W6 SR das Bewusstsein zu '
                        'verlieren. Übersteigen die erlittenen TP(A) '
                        'sogar die KO des Angegriffenen, so ist es automatisch '
                        'bewusstlos, ohne dass ihm die KOProbe '
                        'zusteht. Bei einem Schmetterschlag '
                        'wird die reguläre Wundschwelle des Opfers '
                        'berücksichtigt, nicht die Erhöhung derselben '
                        'um 2 Punkte.')
                elif 'Schmutzige Tricks' in message.content:
                        await Client.send_message(message.channel, 'Schmutzige Tricks (60 AP): \nRingen- und '
                        'Raufen-AT; der Kämpfer kann diverse Möglichkeiten, '
                        'die die Umgebung ihm bietet '
                        '(Meisterentscheid und je nach Situation), '
                        'im Kampf zu seinem Vorteil einsetzen. Dies '
                        'kann eine Handvoll Sand in den Augen des '
                        'Gegners sein, ein weggezogener Teppich, '
                        'Schwingen am Leuchter oder ein Braten als '
                        'improvisierte Wurfwaffe. '
                        'Ein Schmutziger Trick richtet üblicherweise '
                        'nur 1W6 Punkte AU- oder Initiative- '
                        'Verlust an; TP/KK kommen nicht '
                        'zum Tragen, jedoch können Attacken '
                        'oder Paraden mit Ansage versehen werden, '
                        'um höheren Schaden anzurichten, '
                        'eigene folgende Manöver zu erleichtern oder '
                        'solche des Gegners zu erschweren. Rüstung '
                        'hilft nicht gegen den Schaden aus Schmutzigen '
                        'Tricks. '
                        'Je nach Situation werden Schmutzige Tricks '
                        'über das Talent Raufen (z.B. geworfene '
                        'Mäntel) oder das Talent Ringen '
                        '(weggezogene Teppiche) abgewickelt. '
                        'Besonders '
                        'spektakuläre '
                        'Manöver erfordern '
                        'meist zusätzlich noch '
                        'Akrobatik-Proben. ')
                elif 'Schwanzfeger' in message.content:
                        await Client.send_message(message.channel, 'Schwanzfeger (20 AP, '
                        'Voraussetzung: Bemuskelter '
                        'Schwanz): \nRaufen- '
                        'AT; ein Hieb mit dem '
                        'Schwanz nach den Beinen '
                        'des Gegners, um diesen aus '
                        'der Balance zu bringen, die '
                        'Achaz-Variante des Fußfegers. '
                        'Es wird eine AT mit '
                        'Ansage gewürfelt, bei deren '
                        'Gelingen (und Misslingen '
                        'der PA) der Verteidiger eine '
                        'GE-Probe ablegen muss, um '
                        'auf den Beinen zu bleiben. Die '
                        'angesagten Punkte können entweder '
                        'die Parade des Verteidigers oder '
                        'die GE-Probe erschweren (auch verteilt). '
                        'Ohne Beinarbeit ist die Parade gegen '
                        'einen Schwanzfeger um 4 Punkte erschwert. '
                        'Mit dem Vorteil Balance sind sowohl die Parade '
                        'als auch die eventuelle GE-Probe um '
                        '2 Punkte erleichtert, mit Herausragende Balance '
                        'um 4 Punkte, mit der SF Standfest um '
                        'einen Punkt. Der Schwanzfeger kann auch '
                        'gegen einen Gegner gerichtet werden, der '
                        'hinter dem Angreifer steht, ist dann aber um '
                        '4 Punkte erschwert. ')
                elif 'Schwanzschlag' in message.content:
                        await Client.send_message(message.channel, 'Schwanzschlag (10 AP, automatisch für '
                        'Achaz, Voraussetzung: Schwanz): \nRaufen-  '
                        'AT; dieses Manöver, zu dem natürlich nur '
                        'Wesen mit einem bemuskelten und genügend '
                        'langen Schwanz in der Lage sind, ist für '
                        'die meisten Gegner unerwartet und schwer '
                        'zu parieren: Der Angreifer stellt fest, um wie '
                        'viele Punkte er seinen AT-Wert unterboten '
                        'hat, und die Hälfte dieser Punkte erschweren '
                        'die Parade des Gegners. Es gibt seltene '
                        'Schwanzwaffen für Achaz, die es ihnen erlauben, '
                        'mit einem Schwanzschlag ‘echte’ TP '
                        'anzurichten. ')
                elif  'Schwinger' in message.content:
                        await Client.send_message(message.channel, 'Schwinger (30 AP): \nRaufen-AT; bei dieser  '
                        'Art von Schlag (einer Form der Finte) kann '
                        'eine Ansage angekündigt werden, um bei '
                        'Gelingen die gegnerische PA um die Punkte '
                        'aus der Ansage zu erschweren. Ohne Auspendeln '
                        'ist die Parade gegen einen Schwinger um '
                        '4 Punkte erschwert. ')
                elif 'Schwitzkasten' in message.content:
                        await Client.send_message(message.channel, 'Schwitzkasten (20 AP): \nRingen-AT; eine besondere '
                        'Möglichkeit ist es, einen Gegner durch '
                        'eine gelungene und unparierte Ringen-AT in '
                        'den Schwitzkasten zu nehmen, aus dem er sich '
                        'nur mit einer Ringen-PA befreien kann. Die '
                        'folgenden Ringen-AT des Angreifers sind um '
                        '1, 2, 3 usf. Punkte erleichtert und richten '
                        '1W6+1, 1W6+2, 1W6+3 etc. Punkte '
                        'AU-Verlust an (aber keinen echten '
                        'Schaden); die Paraden des Verteidigers '
                        'sind um 1, 2, 3 usf. Punkte '
                        'erschwert. Ein Schwitzkasten endet, '
                        'wenn dem Angreifer eine AT miss- oder '
                        'dem Verteidiger eine PA gelingt. Der '
                        'Verteidiger kann als einzige Angriffsaktionen '
                        'Biss, Knie oder Schwanzschlag einsetzen, '
                        'jedoch sind diese Manöver jeweils '
                        'um 4 Punkte erschwert. '
                        'Ein Schlangenmensch erhält fünf Bonuspunkte '
                        'auf seine PA, wenn er '
                        'sich aus einem Schwitzkasten '
                        'befreien will. ')
                elif 'Sprungtritt' in message.content:
                        await Client.send_message(message.channel, 'Sprungtritt (50 AP): \nRaufen-AT, die automatisch '
                        'um 4 Punkte erschwert ist; ein '
                        'Sprungtritt kann Punkte aus einem Manöver '
                        'Sprung nutzen. Ein solcher Angriff kann nur '
                        'schwer abgewehrt werden: Der Verteidiger '
                        'kann sich mit Ausweichen oder Kreuzblock '
                        'oder einem Schild normal verteidigen, eine '
                        'Waffenparade ist um 4 Punkte erschwert; andere '
                        'waffenlose Paraden sind nicht möglich. '
                        'Ein Sprungtritt richtet 2 TP(A) zusätzlich '
                        'an, kann eine Ansage zur Schadenserhöhung '
                        'erhalten und kann auch gegen Gegner in der '
                        'Distanzklasse Nahkampf eingesetzt werden. '
                        'Unabhängig vom Ausgang des Manövers verliert '
                        'der Verteidiger 1W6 Punkte INI. Gelingt '
                        'eine bewaffnete Parade gegen einen Sprungtritt, '
                        'muss der Angreifer den vollen Schaden '
                        'der Paradewaffe hinnehmen. Misslingt '
                        'der Sprungtritt, so muss der Kämpfer sofort '
                        'eine GE-Probe ablegen (erleichtert um 1 für '
                        'Standfest, um 2 für Balance, um 4 für Herausragende '
                        'Balance), um auf den Beinen zu bleiben. '
                        'Ein Sprungtritt lässt sich auch aus der '
                        'Bewegung heraus durchführen, was die AT '
                        'nochmals um 4 Punkte erschwert, bei Gelingen '
                        'aber die GS des Kämpfers zu den TP(A) '
                        'addiert. Gegen einen solchen Sprungtritt mit '
                        'Anlauf ist nur (Gezieltes) Ausweichen oder ein '
                        'bewaffnetes Gegenhalten) möglich; es ist automatisch '
                        'ein Angriff zum Niederwerfen. ')
                elif 'Sprung' in message.content and 'Sprungtritt' not in message.content:
                        await Client.send_message(message.channel, 'Sprung (50 AP): \nRaufen- '
                        'PA; diese generelle Parademöglichkeit '
                        'funktioniert '
                        'sowohl gegen Waffen '
                        'wie auch gegen Waffenlose '
                        'Angriffe – sie ist quasi ein '
                        '‘Ausweichen nach oben’, das für '
                        'Angriffe (bewaffnet wie unbewaffnet) aus '
                        'der Distanzklasse Handgemenge um 4 Punkte '
                        'erschwert ist, für Angriffe aus der Distanzklasse '
                        'Nahkampf um 2 Punkte, dazu erschwert '
                        'um 2 Punkte für Paraden gegen bewaffnete '
                        'Angriffe. Unabhängig vom Ausgang des Manövers '
                        'verliert der Verteidiger 1W6 Punkte '
                        'INI. Die Sprung-Parade kann eine Ansage '
                        'erhalten, mit der sich der Kämpfer jedoch nur '
                        'Bonuspunkte auf seinen nächsten Sprungtritt '
                        'oder Schwanzschlag verdienen kann. Misslingt '
                        'die Sprung-Parade, muss der Kämpfer sofort '
                        'eine GE-Probe ablegen (erschwert um die erlittenen '
                        'echten TP, erleichtert um 1 für die SF '
                        'Standfest, um 2 für den Vorteil Balance, um 4 '
                        'für Herausragende Balance), um auf den Beinen '
                        'zu bleiben.um 2 Punkte für Paraden gegen bewaffnete '
                        'Angriffe. Unabhängig vom Ausgang des Manövers '
                        'verliert der Verteidiger 1W6 Punkte '
                        'INI. Die Sprung-Parade kann eine Ansage '
                        'erhalten, mit der sich der Kämpfer jedoch nur '
                        'Bonuspunkte auf seinen nächsten Sprungtritt '
                        'oder Schwanzschlag verdienen kann. Misslingt '
                        'die Sprung-Parade, muss der Kämpfer sofort '
                        'eine GE-Probe ablegen (erschwert um die erlittenen '
                        'echten TP, erleichtert um 1 für die SF '
                        'Standfest, um 2 für den Vorteil Balance, um 4 '
                        'für Herausragende Balance), um auf den Beinen '
                        'zu bleiben. ')
                elif 'Tritt' in message.content:
                        await Client.send_message(message.channel, 'Tritt (30 AP): \nRaufen-AT; bei dieser Art von '
                        'Angriff kann eine Ansage gemacht werden, '
                        'um bei Gelingen die eigenen TP zu erhöhen; '
                        'ohne Beinarbeit ist die Parade gegen einen '
                        'Tritt um 4 Punkte erschwert. ')
                elif 'Versteckte Klinge' in message.content:
                        await Client.send_message(message.channel, 'Versteckte Klinge (50 AP): \nRaufen-AT; der '
                        'Kämpfer ist in der Lage, in der Distanzklasse '
                        'Handgemenge eine Waffe mit der Distanzklasse '
                        'Handgemenge mit seinen Raufen- '
                        'Kampfwerten einzusetzen, aber TP entsprechend '
                        'der Waffe anzurichten und auch gegen '
                        'bewaffnete Angriffe zu parieren (mit den '
                        'Einschränkungen und WM je nach Waffe). '
                        'Kann mit Gerade und Schwinger kombiniert '
                        'werden. ')
                elif 'Würgegriff' in message.content:
                        await Client.send_message(message.channel, 'Würgegriff (30 AP): \nRingen-AT; mit einem '
                        'Würgegriff ist der Kämpfer in der Lage, einen Gegner zu erdrosseln (ihm schnell AuP '
                        'zu rauben). Dazu muss ihm eine Ringen-AT '
                        'gelingen, die beliebig pariert werden kann '
                        '(Schlangenmenschen erhalten 5 Bonuspunkte '
                        'auf diese Parade). Befindet sich der Gegner '
                        'einmal im Würgegriff, muss der Angreifer in '
                        'den folgenden Kampfrunden keine weitere AT '
                        'würfeln, sondern richtet automatisch 1W6+2 '
                        'TP(A) an. Der Verteidiger kann diesen Schaden '
                        'nicht parieren, jedoch stehen ihm um 2 '
                        'Punkte erschwerte Raufen- oder Ringen-Angriffe '
                        '(keine Sprünge) zu, die wiederum der '
                        'Angreifer nicht parieren darf, will er den Würgegriff '
                        'aufrechterhalten. Ein Angriff gegen den '
                        'Würgegriff selbst ist eine Ringen-AT, die um '
                        'die halbe KK des Würgers erschwert ist, von '
                        'diesem aber nicht pariert werden kann; nach '
                        'gelungener Attacke gegen den Würgegriff '
                        'entscheidet die Qualität einer vergleichenden '
                        'Körperkraft-Probe, ob der Griff sich öffnet. ')
                elif 'Wurf' in message.content:
                        await Client.send_message(message.channel, 'Wurf (40 AP): \nRingen-AT, die automatisch '
                        'um 4 Punkte erschwert ist; der Gegner wird '
                        'bei Gelingen zu Boden geworfen und muss '
                        '1W6 TP (A) hinnehmen. Geht er zu Boden, '
                        'verliert er 2W6 Punkte INI. Einem Wurf muss '
                        'immer ein Halten vorausgehen, oder der Werfende '
                        'muss sein Opfer in einem Griff haben '
                        'und kann auch Punkte aus beiden Manövern '
                        'nutzen. Bei einem sportlichen Wettkampf bekommt '
                        'der Angreifer Punkte für den gelungenen '
                        'Wurf. Bei einem Kampf auf Leben und '
                        'Tod kann er die Zeit, die der Verteidiger benötigt, '
                        'um sich aufzurappeln (siehe Liegende '
                        'und kniende Helden, Seite 57), zur Flucht '
                        'nutzen, oder dazu, eine Waffe aufzuheben. '
                        'Es ist möglich, eine zusätzliche Ansage zur '
                        'Erhöhung der Trefferpunkte zu machen. ')
        elif message.content.startswith('Nachteil'):
                if 'Aberglaube' in message.content:
                        await Client.send_message(message.channel, 'Aberglaube (Schlechte Eigenschaft; je –1'
                        'GP): \nAberglaube bezieht sich zumeist auf '
                        'bestimmte Dinge, die dem Helden nach seiner '
                        'Meinung Glück oder Pech bringen, vor '
                        'denen er Angst hat. Wer diese Eigenschaft '
                        'wählt, sollte die Details seines Aberglaubens '
                        'näher festlegen. Bemerkenswert ist allerdings, '
                        'dass einige Arten des Aberglaubens durchaus '
                        'eine reale – wenn auch bisweilen völlig andere '
                        '– Grundlage haben. ')
                elif 'Albino' in message.content:
                        await Client.send_message(message.channel, 'Albino (–7 GP): \nBei einem Albino – einer '
                        'Veränderung von Geburt an, die bei allen '
                        'menschlichen und menschenähnlichen Rassen '
                        'vorkommen kann, wenn auch sehr selten '
                        '– sind in Haut, Haaren und Augen keine '
                        'Farbpigmente '
                        'vorhanden. Die Haut ist daher '
                        'rein weiß und bekommt bei geringster Sonneneinstrahlung '
                        'bereits einen Sonnenbrand '
                        '(ca. 1 SP pro Stunde Aufenthalt im Sonnenlicht), '
                        'die Haare sind weiß, die Augen rot oder '
                        '(selten) violett. Deswegen sind viele Albinos '
                        'gleichzeitig auch lichtscheu oder gar lichtempfindlich '
                        '(siehe Seite 266) und haben bei '
                        'Tageslicht häufig eingeschränkte Sicht. Dazu '
                        'kommt, dass Albinos meist mit Misstrauen '
                        'betrachtet und bisweilen sogar für unheilige '
                        'Wesen gehalten werden, was leicht dazu '
                        'führt, dass man einen Albino als Sündenbock '
                        'hernimmt, die Garde ruft, wenn er die Stadt '
                        'betritt, ihm Ämter und Würden verweigert '
                        'etc.: Jeder zusätzlich gewählte Punkt '
                        'SO über 7 kostet ihn 2 GP. Anderseits '
                        'ist es für einen Albino leichter (um 3 '
                        'Punkte), Personen einzuschüchtern, '
                        'und in archaischen Kulturen mag ein '
                        'Albino durchaus als göttlicher oder dämonischer '
                        'Sendbote gelten. '
                        'Üblicherweise ist für Zauberproben, bei denen '
                        'jemand eingeschüchtert werden soll (wie '
                        'der HORRIPHOBUS), der CH-Wert des '
                        'Albinos um 1 erhöht, für Proben, mit denen '
                        'jemand beruhigt oder freundlich gestimmt '
                        'werden soll (wie der BANNBALADIN), jedoch '
                        'um 1 vermindert – beides natürlich nur, '
                        'wenn das Opfer den Albino sehen kann. ')
                elif 'Angst vor' in message.content:
                        await Client.send_message(message.channel, 'Angst vor [Insekten, Spinnen, Reptilien, '
                        'Pelztieren, Feuer, Wasser ...] (Schlechte '
                        'Eigenschaft; unterschiedliche Kosten): \n'
                        'Dies alles sind unterschiedliche Schlechte '
                        'Eigenschaften, bei denen der Held mit übertriebener '
                        'Angst auf bestimmte Situationen '
                        'oder Begegnungen reagiert. Die Angst kann '
                        'schnell in Panikzustände münden, bei denen '
                        'der Held kaum noch zu vernünftigem Handeln '
                        'in der Lage ist. Wovor der Held jeweils '
                        'diese Phobie hat, hängt oft von seiner Kultur '
                        'oder Herkunft ab, mitunter kann aber auch '
                        'ein erschütterndes Schlüsselerlebnis zu einer '
                        'solchen Angst führen. Auf jeden Fall kann '
                        'dieser Nachteil nur wirklich als solcher gelten, '
                        'wenn er den Helden im Spiel einschränkt '
                        'und über das natürliche Maß der Selbsterhaltung '
                        'hinausgeht. So etwas wie eine ‘Angst vor '
                        'Albino-Löwen’ ist deutlich zu speziell, um '
                        'gelten zu können, und auch eine Phobie wie '
                        '‘Angst vor aggressiven Giftschlangen’ ist kein '
                        'Nachteil, da jeder vernunftbegabte Mensch '
                        'sie besitzt. '
                        'Phobien mit häufigem Auslöser (wie Angst '
                        'vor Insekten und Angst vor Feuer) bringen 3 '
                        'GP pro 2 Punkte der Schlechten Eigenschaft, '
                        'eher selten aktivierte Phobien wie Angst von '
                        'fließendem Wasser jedoch nur 1 GP pro Punkt '
                        'der Schlechten Eigenschaft. Einige spezielle '
                        'und bei etlichen Lebewesen anzutreffende '
                        'Ängste wie Meeresangst oder Dunkelangst sind '
                        'weiter unten separat aufgeführt. ')
                elif 'Animalische Magie' in message.content:
                        await Client.send_message(message.channel, 'Animalische Magie (Magischer Nachteil;'
                        'ZH, –1 GP pro Punkt): \nAlle astralen Dinge, '
                        'die zu ‘kopflastig’ sind, verschließen sich dem '
                        'Verständnis des Helden, er kann sich nur '
                        'schlecht auf seine Zauberei konzentrieren '
                        'und handelt eher ‘aus dem Bauch heraus’: '
                        'Jede Zauberprobe oder Probe auf die Ritualkenntnis, '
                        'bei der einmal auf die Eigenschaft '
                        'Klugheit gewürfelt wird, ist um die Anzahl '
                        'an Punkten in Animalischer Magie (max. 5) '
                        'erschwert. Kommt Klugheit zweimal in der '
                        'Probe vor, verdoppelt sich der Malus; solche '
                        'Zauber (mit zweimal KL in der Probe) '
                        'sind um eine Spalte schwieriger zu steigern. '
                        'Dieser Nachteil kann nur von solchen Zauberkundigen '
                        'gewählt werden, die Spruchzauberei '
                        'beherrschen. Für Elfen und Kristallomanten '
                        '(in der entsprechenden Tradition '
                        'ausgebildete Zauberer), die ihre Proben anstatt '
                        'auf KL teilweise auf IN ablegen dürfen, '
                        'bringt der Nachteil nur 1 GP pro 2 Punkte in '
                        'Animalischer Magie. ')
                elif 'Arkanophobie' in message.content:
                        await Client.send_message(message.channel, 'Arkanophobie (Schlechte Eigenschaft; je –3'
                        'GP pro 2 Punkte): \nDer Held hat panische '
                        'Angst davor, verzaubert zu werden, und '
                        'fürchtet, dass alle magischen Gegenstände '
                        'verflucht sind und ihm übel wollen. Der Held '
                        'misstraut magisch begabten Kameraden und '
                        'wird niemals einen Gegenstand verwenden, '
                        'von dem er weiß, dass er verzaubert ist. Vor '
                        'allem aber senkt die Arkanophobie die Magieresistenz '
                        'des Charakters, wenn er weiß, dass '
                        'er verzaubert werden soll. Der Nachteil sollte '
                        'von Halb- und Vollzauberern nicht gewählt '
                        'werden; er kann nicht gleichzeitig mit Vorurteile '
                        'gegen Zauberer / gegen Magie genommen '
                        'werden. Elfen können diesen Nachteil überhaupt '
                        'nicht wählen. ')
                elif 'Arroganz' in message.content:
                        await Client.send_message(message.channel, 'Arroganz (Schlechte Eigenschaft; je –1 GP):\n'
                        'Dieser Nachteil bringt den Helden dazu, '
                        'sich allen anderen gegenüber hochnäsig zu '
                        'benehmen und ihnen nichts oder fast nichts '
                        'zuzutrauen, seine eigenen Fähigkeiten hingegen '
                        'zu überschätzen. Ob dies als Standesdünkel, '
                        'Besserwisserei oder als krankhaftes, '
                        'übertriebenes Ehrgefühl daherkommt, ist '
                        'dem Spieler überlassen, jedoch sollten speziell '
                        'Proben auf passende Gesellschaftliche Talente '
                        'hierdurch erschwert werden. ')
                elif 'Artefaktgebunden' in message.content:
                        await Client.send_message(message.channel, 'Artefaktgebunden (Magischer Nachteil; '
                        'ZHV; –7 GP)*: \nDer Zauberer hat beim Binden '
                        'eines Traditionsartefaktes (Zauberstab, '
                        'Kristallkugel, Schale, Schwert, Goldsichel, '
                        'Schamanenkeule, Druidendolch, iama) einen '
                        'schweren Fehler begangen und ist nun '
                        'beim Ausführen von Zaubern an das Artefakt '
                        'gebunden. (In seltenen Fällen mag dies auch '
                        'bei anderen Artefaktbindungen und -erstellungen '
                        'geschehen, jedoch niemals freiwillig.) '
                        'Alle Zauberproben, '
                        'die er ausführt, ohne '
                        'Hautkontakt mit dem Artefakt zu haben, '
                        'unterliegen den Regeln einer Spontanen Modifikation '
                        'der Zaubertechnik '
                        '(siehe Wege der '
                        'Zauberei), d.h., der Zauber muss 7 ZfP aufbringen '
                        '(Zauber, in denen er eine ZfW von '
                        'weniger als 7 hat, misslingen automatisch), '
                        'die Zauberdauer verlängert sich um 3 Aktionen '
                        'und er kann keine weiteren Spontanen '
                        'Modifikationen durchführen. '
                        'Wird das Artefakt zerstört, ist die Bindung '
                        'gebrochen und der Zauberer kann wieder '
                        'ungehindert zaubern; jedoch verliert er 3 '
                        'permanente AsP und 1 Punkt seiner höchsten '
                        'geistigen Eigenschaft (MU, KL, IN oder '
                        'CH). Nur Zauberer, die über ein gebundenes '
                        'Artefakt verfügen, können den Nachteil wählen: '
                        'Magier, Elfen, Druiden, Geoden, '
                        'Kristallomanten, '
                        'Schamanen und Alchimisten. '
                        'Hexen ist es möglich, dass statt eines gebundenen '
                        'Artefakts (des Hexenkessels) der Vertraute '
                        'einen Teil der Essenz der Hexe trägt. ')
                elif 'Astraler Block' in message.content:
                        await Client.send_message(message.channel, 'Astraler Block (Magischer Nachteil; ZHV; '
                        '–5 / –10 GP): \nEin Charakter mit diesem '
                        'Nachteil regeneriert pro Ruhephase nur '
                        '1W6–1 AsP; eventuelle Intuitions-Würfe '
                        'zur Rückgewinnung verlorener Astralpunkte '
                        'und bei Ritualen zum Erlangen eines höheren '
                        'AsP-Grundwerts sind um 2 Punkte erschwert. '
                        'Dieser Nachteil kann natürlich nur '
                        'von Helden gewählt werden, die über Astralenergie '
                        'verfügen; eine Kombination mit dem '
                        'Vorteil Astrale Regeneration ist nicht möglich; '
                        'der Erwerb der Sonderfertigkeiten Regeneration '
                        'I und II sowie Meisterliche Regeneration '
                        'kosten einen Helden mit Astralem Block das '
                        'Doppelte der angegebenen Kosten. Voll- und '
                        'Halbzauberer erhalten durch diesen Nachteil '
                        '10 GP, Viertelzauberer nur 5 GP ')
                elif 'Autoritätsgläubig' in message.content:
                        await Client.send_message(message.channel, 'Autoritätsgläubig (Schlechte Eigenschaft; je '
                        '–1 GP pro 2 Punkte): Dieser Nachteil äußert '
                        'sich in Buchgelehrsamkeit und Obrigkeitshörigkeit. '
                        'Entscheidungen der Kirchenoberen '
                        'oder weltlicher Herrscher werden von dem '
                        'Helden nicht angezweifelt – es hat schließlich '
                        'seinen Grund, dass diese Menschen über '
                        'ihn gesetzt wurden. Ebenso wenig stellt er '
                        'die Theorien hoch angesehener Gelehrter '
                        'in Frage; selbst dann nicht, wenn das, was in '
                        'den Büchern steht, der eigenen Erfahrung '
                        'oder dem gesunden Menschenverstand widerspricht. '
                        'Sobald der Held etwas tut, was der Anweisung '
                        'eines '
                        'Höhergestellten oder der Aussage eines '
                        'anerkannten Gelehrten zuwiderläuft, kann '
                        'der Meister eine Probe verlangen und beim '
                        'Gelingen der Probe diese Aktivität verbieten. '
                        'Oder aber er erschwert alle Talent- und Eigenschaftsproben, '
                        'die während des Verstoßes '
                        'abzulegen sind oder in irgendeinem Zusammenhang '
                        'damit stehen, entsprechend der Regeln '
                        'zu Schlechten Eigenschaften (Seite 268). ')
                elif 'Behäbig' in message.content:
                        await Client.send_message(message.channel, 'Behäbig (–5 GP): Ein behäbiger Held bewegt '
                        'sich langsamer und bedächtiger als andere '
                        'Mitglieder seiner Rasse. Seine Basis-GS sinkt '
                        'um 1 und er erhält einen Malus von 1 Punkt '
                        'auf alle Ausweichen-Proben. Außerdem ist sein '
                        'Grundwert zur Bestimmung von Sprungweiten '
                        'und -höhen (üblicherweise (GE+KK– '
                        'BE) um 1 Punkt vermindert. Dieser Nachteil '
                        'kann nur einmal gewählt werden. Nicht '
                        'kombinierbar mit Flink (Seite 251). ')
                elif 'Blutdürstig' in message.content:
                        await Client.send_message(message.channel, 'Blutdurst (Schlechte Eigenschaft; je –1 '
                        'GP für 2 Punkte): Der Charakter liebt es, '
                        'seine Gegner langsam und blutig zu töten. '
                        'Er empfindet Vergnügen daran, Opfer zu '
                        'quälen und anderen Schmerzen zuzufügen. '
                        'Dazu nutzt er jede sich bietende Gelegenheit, '
                        'Ehre gilt ihm dabei nichts, und Unterlegene '
                        'sind willkommene Opfer, solange sie sich nur '
                        'wehren. Seine Obsession führt dazu, dass er '
                        'länger als nötig auf Schlachtfeldern verweilt, '
                        'um Verwundete zu töten, oder dass er wichtige '
                        'Informanten ermordet. Ein solcher Charakter '
                        'kann keinen Moralkodex annehmen, '
                        'der Gewalttätigkeit ausschließt. (Und selbst '
                        'in der Kor-Kirche haben Blutdürstige eigentlich ')
                        'keinen Platz.) '
                elif 'Blutrausch' in message.content:
                        await Client.send_message(message.channel, 'Blutrausch (–15 GP): Der Held fällt in einen '
                        'Blutrausch (bei den Thorwalern auch '
                        'als Walwut oder Swafskari gefürchtet), sobald '
                        'eines der drei folgend genannten Ereignisse '
                        'eintritt: spontaner Zorn (z.B. eine deutlich '
                        'gelungene Jähzorn-Probe), Erleiden einer '
                        'Wunde durch einen Nahkampfangriff und '
                        'Scheitern einer darauf folgenden Selbstbeherrschungs- '
                        'Probe (erschwert um die Zahl '
                        'der SP über der Wundschwelle) sowie die '
                        'Einnahme bestimmter aggressionsfördernder '
                        'Substanzen (allgemein: alle Rauschmittel, '
                        'deren Genuss den MU-Wert anhebt, darunter '
                        'auch Alkohol). '
                        'Im Blutrausch setzt der Rasende seine gefährlichsten '
                        'Waffen (auch Wurfwaffen oder '
                        'Zauberei, nicht aber so komplexe Waffen '
                        'wie Schusswaffen) gegen die missliebigste, '
                        'wenn nicht vorhanden, dann die nächststehende '
                        'Person ein. MU, AT und TP sind '
                        'um 5 Punkte erhöht, der Rasende pariert '
                        'nicht und nimmt keine Schmerzen wahr '
                        '(der Meister '
                        'notiert die erlittenen Schadenspunkte '
                        'des Helden verdeckt). Talent- oder '
                        'Zauberproben sind während des Blutrauschs '
                        'um 7 Punkte erschwert, Kampfmanöver (inklusive '
                        'Umwandeln von Aktionen) oder irgendwelche '
                        'Aktivitäten, die einen ‘wachen '
                        'Geist’ oder längere Vorbereitung verlangen, '
                        'sind unter Blutrausch nicht möglich, ebenso '
                        'wenig die Aktion Orientieren. Zu den verbotenen '
                        'Aktionen zählen ausdrücklich auch '
                        'Spontane Modifikationen von Zaubern, '
                        'nicht jedoch der Einsatz von Varianten. Der '
                        'Blutrausch dauert so lange, bis der Rasende '
                        'keine Ausdauer mehr hat (er verliert für jede '
                        'AT 2 AuP, kann aber Atem Holen) und entkräftet '
                        'zusammenbricht. Blutrausch und der '
                        'Vorteil Kampfrausch sind nicht miteinander '
                        'kombinierbar. ')
                elif 'Brünstigkeit' in message.content:
                        await Client.send_message(message.channel, 'Brünstigkeit (Schlechte Eigenschaft; je –1 '
                        'GP für 2 Punkte Brünstigkeit): '
                        'Der Charakter '
                        'zeigt ein unerschöpfliches sexuelles Verlangen, '
                        'andere Lebewesen dienen ihm dabei '
                        'nur zur Befriedigung seiner Gelüste, ob nun '
                        'willig oder nicht. Dies führt allerdings auch '
                        'oft dazu, dass er vor lauter Geilheit seine '
                        'Umgebung völlig vernachlässigt – leicht bekleidete '
                        'Amazonen haben im Kampf gegen '
                        'einen brünstigen Mann z.B. leichtes Spiel '
                        'und Betören-Versuche gegen ihn sind um seinen '
                        'Wert in Brünstigkeit erleichtert. ')
                elif 'Dunkelangst' in message.content:
                        await Client.send_message(message.channel, 'Dunkelangst (Schlechte Eigenschaft; '
                        'je –2 GP): Der Held bekommt Beklemmungsgefühle '
                        'durch Dunkelheit: Dies mögen '
                        'dunkle Tunnel und Höhlen, aber auch '
                        'finstere Wälder, vor allem aber einfach die '
                        'Schwärze der Nacht sein. Schon das Hereinbrechen '
                        'der Dämmerung ohne die Aussicht '
                        'auf Beleuchtung macht den Helden nervös, '
                        'das Erlöschen der letzten Fackel im dunklen '
                        'Stollen treibt ihn an den Rand des Wahnsinns. '
                        'Diese Phobie ist so schwerwiegend, '
                        'dass der Held für einen Punkt der Schlechten '
                        'Eigenschaft 2 Generierungspunkte '
                        'erhält.')
                elif 'Einarmig' in message.content:
                        await Client.send_message(message.channel, 'Einarmig (–15 GP): Der Held hat einen'
                        'Arm verloren (den linken bei Rechtshändern '
                        'bzw. umgekehrt). Bei allen Handlungen, '
                        'die eigentlich beide Hände erfordern, sind '
                        'entsprechende Eigenschaftsproben um 5 '
                        'Punkte erschwert, Talentproben sogar um '
                        '10 Punkte. Bestimmte '
                        'Handlungen (Bogenschießen, '
                        'Führen zweihändiger '
                        'Waffen) sind '
                        'überhaupt nicht möglich; einarmige Helden '
                        'können keine Sonderfertigkeiten '
                        'erwerben '
                        'oder anwenden, die mit dem links- oder '
                        'beidhändigen Kampf verbunden sind, und '
                        'keine Schilde oder Parierwaffen führen; bei '
                        'bestimmten Balanceakten kann der Meister '
                        'einem Einarmigen eine Probe um bis zu 3 '
                        'Punkte erschweren. '
                        'Als schwächere Form dieses Nachteils (–7 '
                        'GP) könnte ein teilweise gelähmter oder '
                        'verkrüppelter Arm gelten, der Eigenschaftsproben '
                        'um 2, Talentproben um 5 Punkte '
                        'behindert. '
                        'Diese körperliche Behinderung ist so tiefgehend, '
                        'dass sie im späteren Spielverlauf nicht '
                        'durch eine auch noch so gute Prothese oder '
                        'Zauberei wieder wettgemacht werden kann. '
                        'Natürlich kann Einarmig nicht mit Einhändig '
                        'kombiniert werden. ')
                elif 'Einäugig' in message.content:
                        await Client.send_message(message.channel, 'Einäugig (–5 GP): Der Held hat irgendwann '
                        'im Verlauf seines bisherigen Lebens '
                        'das Augenlicht eines Auges oder gar das Auge '
                        'selbst verloren. Er erleidet einen Malus '
                        'von 4 Punkten bei allen Wurfwaffen- '
                        'Proben und bei Schusswaffen- '
                        'Proben '
                        'unter 10 Schritt Entfernung. Außerdem '
                        'ist sein Kontrollbereich (siehe '
                        'Wege des Schwerts) um die Hälfte '
                        'eingeschränkt. '
                        'Einäugige Zauberer erleiden eine Erschwernis '
                        'von 4 Punkten, wann immer sie einen '
                        'Zauber besonders zielen müssen (wie bei '
                        'einem Zauber, dessen Reichweite Horizont '
                        'ist, wenn er den Nachteil Zielschwierigkeiten '
                        'auf sich genommen hat oder in besonderen '
                        'Situationen). Siehe auch den Nachteil Eingeschränkter '
                        'Sinn auf Seite 262. '
                        'Diese körperliche Behinderung ist so tiefgehend, '
                        'dass sie im späteren Spielverlauf weder '
                        'durch Magie noch auf andere Weise wettgemacht '
                        'werden kann. ')
                elif 'Einbeinig' in message.content:
                        await Client.send_message(message.channel, 'Einbeinig (–25 GP): Dem Held fehlt ein '
                        'Bein, das er bei einem früheren Unfall, '
                        'Kampf oder ähnlichem verloren hat. Er erleidet '
                        'einen Verlust von 5 Punkten auf seine Gewandtheit '
                        '(was sich auch auf seine Kampf- '
                        'Basiswerte niederschlägt) und von 3 Punkten '
                        'auf seine GS (die jedoch mindestens 1 bleibt). '
                        'Diese körperliche Behinderung ist so tiefgehend, '
                        'dass sie im späteren Spielverlauf nicht '
                        'durch eine auch noch so gute Prothese oder '
                        'durch Zauberei wieder wettgemacht werden '
                        'kann. Einbeinig kann nicht mit Lahm kombiniert '
                        'werden. ')
                elif 'Einbildungen' in message.content:
                        await Client.send_message(message.channel, 'Einbildungen (–5 GP): Der Held glaubt, '
                        'aus einer übersteigerten Phantasie oder beginnendem '
                        'Wahnsinn heraus, immer wieder '
                        'Dinge wahrzunehmen, die in Wirklichkeit '
                        'nicht existieren. Das können scheinbare Beobachter '
                        'oder Verfolger sein, aber auch niemals '
                        'so gemeinte Vorwürfe und Anschuldigungen '
                        'von anderen Personen (z.B. wenn der '
                        'Held glaubt, jegliche andere Meinung sei ein '
                        'persönlicher Angriff). Einbildungen lässt sich '
                        'nicht mit Wahnvorstellungen kombinieren. ')
                elif 'Eingeschränkte Elementarnähe' in message.content:
                        await Client.send_message(message.channel, 'Eingeschränkte Elementarnähe (H; –3'
                        'GP)*: Zu den Eigenheiten schamanistischer '
                        'Magie gehört, dass jede Schamanen-Tradition '
                        'nur Umgang mit dreien der sechs Elemente '
                        'pflegt (diese sind jeweils bei der Profession '
                        'angegeben). Diese drei beherrscht der '
                        'Schamane alle gleich gut, also ohne Einbußen, '
                        'selbst wenn sich zwei gegensätzliche '
                        'darunter befinden. Wesen und Manifestationen '
                        'der anderen Elemente dagegen kann er '
                        'nicht rufen, weder mit dem Ritual Meister der '
                        'Elemente noch auf anderem magischen Weg. '
                        'Dieser Nachteil ist mit dem Vorteil Affinität '
                        'zu Elementaren kombinierbar. '
                        'Die Geoden '
                        'der Brobim sind ebenfalls mit diesem Nachteil '
                        'behaftet. ')
                elif 'Eingeschränkter Sinn' in message.content:
                        await Client.send_message(message.channel, 'Eingeschränkter Sinn (–5 GP): Ein Sinn '
                        'des Helden ist besonders schlecht ausgebildet: '
                        'Alle Sinnenschärfe-Proben, die '
                        'sich auf diesen Sinn beziehen, sind um '
                        '5 Punkte erschwert, und je nach Situation '
                        'kann der Meister dem Helden '
                        'auch Proben nicht zugestehen, die er '
                        'anderen Helden erlaubt. Es gibt vier unterschiedliche '
                        'Bereiche, auf die sich dieser '
                        'Vorteil beziehen kann: '
                        'Ein schwerhöriger Held nimmt zwar normal '
                        'laute Geräusche wahr, aber zum Beispiel '
                        'kein Flüstern. Verständigung in einer Sprache, '
                        'die er nur unzureichend beherrscht, ist '
                        'immer schwieriger als bei einem normal hörenden '
                        'Helden. '
                        'Kurzsichtig bezieht sich auf die Sicht des '
                        'Helden: Alles, was mehr als zehn Schritt weit '
                        'entfernt ist, wird immer verschwommener, '
                        'und auf Strecken von 100 Schritt und mehr '
                        'sind nur noch Konturen zu erkennen '
                        '– was entsprechende Fernkampfproben '
                        'und auch das Ausweichen vor '
                        'einem Fernkampfangriff schwerer '
                        'macht (nach Meistermaßgabe). '
                        'Die Sicht auf kurze Entfernung '
                        'ist nicht eingeschränkt. ')
                        await Client.send_message(message.channel, 'Gerade Kurzsichtigkeit schränkt (Spruch-) '
                        'Zauberer deutlich ein, da dieser Nachteil alle '
                        'Zauberproben auf Entfernung um je einen '
                        'Punkt pro Entfernungskategorie (1 Schritt / '
                        '3 Schritt / 7 Schritt / 21 Schritt / 49 Schritt / '
                        'Horizont) erschwert. '
                        'Ein eingeschränkter Tastsinn lässt den Helden '
                        'nur unter Schwierigkeiten Dinge ertasten, '
                        'und je nach Situation kann der Meister auf '
                        'Talentproben, in denen Fingerfertigkeit verlangt '
                        'ist und bei denen der Tastsinn eine '
                        'große Rolle spielt (wie Feinmechanik oder '
                        'Schlösser Knacken, aber auch Heilkunde Wunden), '
                        'einen Zuschlag in Höhe von 1 bis 3 '
                        'Punkten verlangen. '
                        'Der eingeschränkte Geruchssinn bezieht sich '
                        'sowohl auf Gerüche als auch auf Geschmack, '
                        'denn diese beiden Sinne sind schwer zu trennen. '
                        'Ein Held mit diesem Nachteil nimmt '
                        'Gerüche und Geschmack nur dann wahr, '
                        'wenn sie wirklich penetrant sind (was ihn bei '
                        'Speisen und Getränken auch nicht gerade '
                        'wählerisch macht). In diesem Fall ist nicht '
                        'nur die Sinnenschärfe betroffen, sondern '
                        'auch alle Proben in Kochen sind ebenfalls '
                        'um 5 Punkte erschwert; außerdem steigt die '
                        'Gefahr, sich durch verdorbene Lebensmittel '
                        'einen Flinken Difar oder gar eine Lebensmittelvergiftung '
                        'zuzuziehen. ')



Client.run("NjAwMjc5MDQ4MTkwNjg5MzAw.XnS4fg.xnAPDk79MOn_N-Jbkgw9Dz6calM")
