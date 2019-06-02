import discord
import time
import asyncio
import random
import numpy as np 
import math
from andengrad import andengradsligning
from dice  import  dice

client = discord.Client()

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    id = client.get_guild(576556903270842388)
    channels = ["commands"]
    valid_users = ["Fruggy#4277"]

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        if message.content.find("!a") != -1:
            a = message.content
            a = a.split()
            result = andengradsligning(int(a[1]),int(a[2]),int(a[3]),True)
            await message.channel.send(result)

        if message.content.find("!dice") != -1:
            a = message.content
            a = a.split()
            result = dice(int(a[1]), int(a[2]))
            await message.channel.send(result)  


client.run("NTc2NTU1NjAyMjA2MTMwMTg3.XNYNrA.FWNvUrit9ccU9ElxxHD4_5ZnMRs")