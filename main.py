import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
    if message.content.startswith('!pog'):
        await message.channel.send('Another one in the jar.')

client.run('your token here')
