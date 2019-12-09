import discord
from discord.ext import commands
from discord.utils import get
import os

client = commands.Bot(command_prefix="!")

client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="ItsCopex#9227 add me", url="https://twitch.tv/itscopex"))

@client.command()
async def attack(ctx, *, content):
    await ctx.send(content)
    
@client.command()
async def help(ctx):
    channel = ctx.message.channel
    embed =  discord.embed(
        title = "Attack Help",
        desccription = "ewflk",
        colour = discord.Colour.dark_green()
    )

    embed.add_field(name="Flooding !attack flood <host> <port> <version> <time>")
    embed.add_field(name="Instantcrashing !attack instantcrash <host> <port> <version> <time>")
    embed.add_field(name="Nullpingcrash !attack nullping <host> <port> <version> <time>")


client.run(os.environ["DISCORD_TOKEN"])
