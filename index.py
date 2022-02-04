import discord
from discord.ext import commands

client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.command()
async def hola(ctx, arg1, arg2):
    await ctx.send(f"You passed {arg1} and {arg2} as the arguments.")


client.run("ODIxNDQ2NDcwMjc1MTcwMzU0.YFD1pA.q2FM6A_LxfLBqwGHOgHSPTt9PpU")
