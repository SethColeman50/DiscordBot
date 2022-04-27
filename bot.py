import os
import discord
from dotenv import load_dotenv

# Get token to give to bot
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# Create bot
client = discord.Client()
client.forbidden_words = []

@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # Reset forbidden words on restart
    client.forbidden_words = []

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$forbid'):
        client.forbidden_words.append(message.content[8:])
        await message.channel.send('Word added to forbidden words list.')
    else:
        for word in client.forbidden_words:
            if word in message.content.split():
                await message.delete()
                await message.channel.send('Hey! You can\'t say that here!')

    # Should probably add admin privileges for this
    if message.content.startswith('$showforbidden'):
        if len(client.forbidden_words) == 0:
            await message.channel.send("There are no forbidden words yet.")
        else:
            await message.channel.send("Forbidden words: " + ", ".join(client.forbidden_words))

try:
    client.run(token)
    print('Bot is running')

except discord.errors.LoginFailure as e:
    print(e)
    print(token)
    print("Please check your token")
    exit(1)