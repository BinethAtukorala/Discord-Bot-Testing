import random
from discord.ext import commands

TOKEN = "NzM2NjU1MDc3NTE0OTM2MzMw.Xxx9gA.DdpWNklnIDLrW8ThrFhkxML6_20"

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name='99', help="Responds with a random quote from Brooklyn 99")
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "I'm the human form of the 💯 emoji.",
        "Bingpot!",
        (
            "Cool. Cool cool cool cool cool cool cool, "
            "no doubt no doubt no doubt no doubt"
        )
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name="roll_dice", help="Simulates rolling dice.")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)