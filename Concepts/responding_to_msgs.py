import discord
import random
TOKEN = "NzM2NjU1MDc3NTE0OTM2MzMw.Xxx9gA.DdpWNklnIDLrW8ThrFhkxML6_20"

client = discord.Client()

@client.event
async def on_message(message):
    if(message.author == client.user):
        return

    brooklyn_99_quotes = [
        "I'm the human form of the 💯 emoji.",
        "Bingpot!",
        (
            "Cool. Cool cool cool cool cool cool cool, "
            "no doubt no doubt no doubt no doubt"
        )
    ]

    if message.content == "99!":
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)