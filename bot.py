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
async def help(ctx):
    channel = ctx.message.channel
    embed =  discord.embed(
        title = "Attack Help",
        description = "ewflk",
        colour = discord.Colour.dark_green()
    )
    embed.set_author(name="ItsCopex#9227"),
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/647940481698758666/64cc91c85ea0464ab87489a7e2ccd593.webp?size=128"),
    embed.set_image(url="https://cdn.discordapp.com/icons/647940481698758666/64cc91c85ea0464ab87489a7e2ccd593.webp?size=128"),
    icon_url="https://cdn.discordapp.com/icons/647940481698758666/64cc91c85ea0464ab87489a7e2ccd593.webp?size=128"
    embed.add_field(name="Flooding", value="!attack flood <host> <port> <version> <time>", inline=True)
    embed.add_field(name="Instantcrashing", value="!attack instantcrash <host> <port> <version> <time>", inline=True)
    embed.add_field(name="Nullpingcrash", value="!attack nullping <host> <port> <version> <time>", inline=True)


client.run(os.environ["DISCORD_TOKEN"])
