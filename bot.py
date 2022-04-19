import os
import discord
from dotenv import load_dotenv

# Get token to give to bot
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# Create bot
client = discord.Client()

@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

try:
    client.run(token)
    print('Bot is running')

except discord.errors.LoginFailure as e:
    print(e)
    print(token)
    print("Please check your token")
    exit(1)