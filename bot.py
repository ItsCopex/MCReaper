import discord
from discord.ext import commands
from discord.utils import getimport os

client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="ItsCopex#9227", url="twitch.com/itscopex"))

@client.command()
async def attack(ctx, *, content):
    await ctx.send(content)

client.run(os.environ["DISCORD_TOKEN"])
