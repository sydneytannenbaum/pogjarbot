#!/usr/bin/env python3

from settings import *
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!pog'):
        await message.channel.send('Another one added to the jar!')

#client.run(DISCORD_TOKEN)
