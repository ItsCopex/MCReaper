
import discord
from discord.ext import commands
from discord.utils import get
import os

client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Discord.py", url="https://twitch.tv/itscopex"))

@client.command()
async def attack(ctx, *, content):
    await ctx.send(content)


client.run(os.environ["DISCORD_TOKEN"])
