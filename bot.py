import discord
from discord.ext import commands
from discord.utils import get
import os

client = commands.Bot(command_prefix="!")

client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="ItsCopex#9227", url="https://twitch.tv/itscopex"))

@client.command()
async def attack(ctx, *, content):
    await ctx.send(content)
    
@client.command()
async def help():
    embed =  discord.embed(
        title = "Attack Help",
        colour = discord.Colour.dark_green()
    )

    embed.set_footer(text="Flooding !attack flood <host> <port> <version> <time>")
    embed.set_footer(text="Instantcrashing !attack instantcrash <host> <port> <version> <time>")
    embed.set_footer(text="Nullpingcrash !attack nullping <host> <port> <version> <time>")


client.run(os.environ["DISCORD_TOKEN"])
