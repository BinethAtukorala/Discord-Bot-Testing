import discord

TOKEN = "NzM2NjU1MDc3NTE0OTM2MzMw.Xxx9gA.DdpWNklnIDLrW8ThrFhkxML6_20"
GUILD = "Bineth's Test Bot"

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            print("Wow, matching guild")
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)