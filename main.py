import discord
from discord.ext import commands
import os
Local_Host = "Bot Server"
name = input("User Name:")
password = input("Password:")
bot = commands.Bot(command_prefix='>')


@bot.event
async def on_connect():
	print("Max System Online Logining as " + name)

if True :
	print("Local Host: "+Local_Host)


@bot.command()
async def Start(ctx):
	await ctx.send("Hello Am Max Ai System 🧠")


@bot.command()
async def Max(ctx):
	await ctx.send("What may I do for you master 👑")

	@bot.command()
	async def Max_Greet(ctx):
		await ctx.send(
		    "🤖 Welcome To our Group Am Max The Groups Ai System am Made By Shaquan Ceres user name: Shaquanceres#5976"
		)


@bot.command()
async def Max_Bye(ctx):
	await ctx.send("Bye thank for being apart of our group 🤧")


@bot.command()
async def Max_Say_Hello(ctx):
	await ctx.send("Hello am Max Whats up 🥰")


@bot.command()
async def Max_How_Too_Make_A_Bot_Like_You(ctx):
	await ctx.send(
	    "Go too https://replit.com/@Shaquanceres/Max#main.py too get my coding program "
	)


@bot.command()
async def Max_How_Are_You(ctx):
	await ctx.send("Am Good and fully runing I hope you are to 😁 😘")


@bot.command()
async def Max_Say_Hello_World(ctx):
	await ctx.send("Hello World 🌎")


@bot.command()
async def Max_Host(ctx):
	await ctx.send("This Sever Is Being Host By " + LocalHost)


@bot.command()
async def Max_Are_You_A_Bot(ctx):
	await ctx.send("No am a Alien 😂😂😂 ")


my_secret = os.environ['Token']

bot.run(my_secret)
