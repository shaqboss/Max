import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='>')


@bot.event
async def on_connect():
    print("Max Ai System online")


@bot.command()
async def start(ctx):
    await ctx.send("Hello Am Max Ai System")


@bot.command()
async def Max(ctx):
    await ctx.send("What may I do for you master")

    @bot.command()
    async def Max_Greet(ctx):
        await ctx.send(
            "Welcome To our Group Am Max The Groups Ai System am Made By Shaquan Ceres user name: Shaquanceres#5976"
        )


@bot.command()
async def Max_Bye(ctx):
    await ctx.send("Bye thank for being apart of our group")


my_secret = os.environ['Token']

bot.run(my_secret)
