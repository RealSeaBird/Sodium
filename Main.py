import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import sys
import random


load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! How are you feeling today?")

@bot.command()
async def imhappy(ctx):
    await ctx.send("Yay! you being happy just makes my day better!")

@bot.command()
async def imsad(ctx):
    await ctx.send("Oh no! just try to think about the positives and remember that it will get better! I hope you have an amazing day!")

@bot.command()
async def imangry(ctx):
    await ctx.send("It's okay to feel angry sometimes, maybe try taking a deep breath or thinking about whether or not its worth getting angry over? either way, I hope you have a great day!")

@bot.command()
async def imok(ctx):
    await ctx.send("Thats great! i hope you continue to have a nice day!")

@bot.command()
async def ihateyou(ctx):
    await ctx.send("https://tenor.com/view/zako-akita-neru-zako-neru-triple-baka-neru-gif-1704302517687241347")



print(f"Token:{token}")

#bot.run(token)




print("Enter number plz")
user_input = input()
print("Enter second number plz")
user_input2 = input()
random.randint(user_input, user_input2)