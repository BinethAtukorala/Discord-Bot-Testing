import discord

TOKEN = "NzM2NjU1MDc3NTE0OTM2MzMw.Xxx9gA.DdpWNklnIDLrW8ThrFhkxML6_20"

# Instead of using `@client.event` decorator, implementing an event handler 
# by creating a subclass of `Client` and overriding it's handler methods.

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient()
client.run(TOKEN)