import discord

TOKEN = "NzM2NjU1MDc3NTE0OTM2MzMw.Xxx9gA.DdpWNklnIDLrW8ThrFhkxML6_20"
GUILD = "Bineth's Test Bot"

client = discord.Client()

@client.event
async def on_ready():

#    for guild in client.guilds:
#        if guild.name == GUILD:
#            break

#   The above loop can be replaced for a more intuitive, abstracted utility :- discord.utils.find()

#    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

#   The above can be abstracted one step further with the get() utility

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f"{client.user} is connected to the guild {guild.name}(id: {guild.id})"
    )

client.run(TOKEN)