import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests

Client = discord.Client()
bot = commands.Bot(command_prefix = "?")

@bot.event
async def on_ready():
    print("Bot is up and running!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)

@bot.command()
async def ping():
    await bot.say("Pong!")

@bot.command(pass_context = True)
async def avatar(ctx):
    emb = discord.Embed(title = ctx.message.author.name + "'s Avatar", colour = discord.Colour.blue(), type = "rich")
    emb.set_image(url = ctx.message.author.avatar_url)
    await bot.send_message(ctx.message.channel, "", embed = emb)

@bot.command(pass_context = True)
async def say(ctx):
    if ctx.message.author.id == "428678912558628865":
        await bot.say(ctx.message.content[5:])
        await bot.delete_message(ctx.message)

bot.run(process.env.token)
