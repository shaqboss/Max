import discord
from discord.ext import commands, tasks
import asyncio
from itertools import cycle
import json
import random
import datetime
current_date = datetime.datetime.today()
import pyjokes
bot = commands.Bot(command_prefix='')
status = cycle(
    ['help', 'Max Is online','https://roblox.com/'])

bot.remove_command('help')

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Thank You For adding Me I Am Max Ai System Made By Shaquan Ceres Username : ten_tailedbeast#5976  message him if you need help ok")
            break

@bot.event
async def on_ready():
    change_status.start()
    print('Bot is ready')


@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))



mainshop = [{"name": "Watch", "price": 100  , "description": "Time"},
            {"name": "Laptop", "price": 1000 , "description": "Work"},
            {"name": "PC", "price": 10000  , "description": "Gaming"},
            {"name": "Ferrari", "price": 99999 , "description": "Sports Car"},
            {"name":"Gold", "price":10000000, "description":"Gold"}]


@bot.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance', color=discord.Color.red())
    em.add_field(name="💵", value=wallet_amt)
    em.add_field(name='💳', value=bank_amt)
    await ctx.send(embed=em)

@bot.command()
async def dig(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f'{ctx.author.mention}found a Worm and sold it for {earnings} 💵 ! ')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)

@bot.command()
async def work(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f'{ctx.author.mention} Got {earnings} 💵! For mining Gold')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)

@bot.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    await ctx.send(f'{ctx.author.mention} Fucking lazy asshole get up and work heres the money you need to start')
    await ctx.send(f'[**{earnings}** **💵 has been deposited in to your wallet from Max Ai Systems Bank**]')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)

@bot.command()
async def hunt(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f'{ctx.author.mention} Got a animal and sold it for {earnings} 💵 !!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)

@bot.command()
async def fish(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f'{ctx.author.mention}Got One Fish And Selled it for {earnings} 💵')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)

@bot.command()
async def GAMINGSERVER(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = 1000000000

    await ctx.send(f'{ctx.author.mention}has use a gift card and got  {earnings} 💵')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)

@bot.command()
async def jdjfdf(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

    await ctx.send(f'{ctx.author.mention}has use a VIP gift card and got  {earnings} 💵')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)

@bot.command()
async def bot_vote(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = 100000000000000000000000000000000000000

    await ctx.send("https://discordbotlist.com/bots/max-ai-system/upvote")


@bot.command()
async def server_vote(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = 100000000000000000000000000000000000000

    await ctx.send("https://discordbotlist.com/servers/gaming-server-2231/upvote")



@bot.command(aliases=['with'])
async def withdraw(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} 💵')


@bot.command(aliases=['dep'])
async def deposit(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, -1 * amount)
    await update_bank(ctx.author, amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} 💵')


@bot.command(aliases=['tip'])
async def send(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, -1 * amount, 'bank')
    await update_bank(member, amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You gave {member.mention} {amount} 💵')


@bot.command(aliases=['steal'])
async def rob(ctx, member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)

    if bal[0] < 100:
        await ctx.send('It is useless to rob him :(')
        return

    earning = random.randrange(0, bal[0])

    await update_bank(ctx.author, earning)
    await update_bank(member, -1 * earning)
    await ctx.send(f'{ctx.author.mention} You robbed {member.mention} and got {earning} 💵')


@bot.command(aliases=['kill'])
async def shoot(ctx, member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)

    if bal[0] < 100:
        await ctx.send('It is useless to kill him :(')
        return

    earning = random.randrange(0, bal[0])

    await update_bank(ctx.author, earning)
    await update_bank(member, -1 * earning)
    await ctx.send(f'{ctx.author.mention} You killed {member.mention} and got {earning} 💵')


@bot.command()
async def slots(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    final = []
    for i in range(3):
        a = random.choice(['💵', '💳', '🚀'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author, 10 * amount)
        await ctx.send(f'You won :) {ctx.author.mention}')
    else:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(f'You lose :( {ctx.author.mention}')


@bot.command()
async def shop(ctx):
    em = discord.Embed(title="Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name=name, value=f"${price} | {desc}")

    await ctx.send(embed=em)


@bot.command()
async def buy(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return

    await ctx.send(f"You just bought {amount} {item}")


@bot.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title="Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

    await ctx.send(embed=em)


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "wallet")

    return [True, "Worked"]


@bot.command()
async def sell(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1] == 3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")


async def sell_this(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.7 * item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost, "wallet")

    return [True, "Worked"]

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open('mainbank.json', 'r') as f:
        users = json.load(f)

    return users



async def update_bank(user, change=0, mode='wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)
    bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank']
    return bal



@bot.command()
async def Start(ctx):
	await ctx.send("Hello Am Max Ai System 🧠")


@bot.command()
async def Max(ctx):
	await ctx.send("What may I do for you master 👑")

@bot.command()
async def Max_Greet(ctx):
	 await ctx.send("🤖 Welcome To our Server Am Max The Groups Ai System am Made By Shaquan Ceres user name: ten_tailedbeast#5976 ")


@bot.command()
async def Max_Bye(ctx):
	await ctx.send("Bye thank for being apart of our server 🤧")


@bot.command()
async def Max_Say_Hello(ctx):
	await ctx.send("Hello am Max Whats up 🥰")


@bot.command()
async def Max_How_Too_Make_A_Bot_Like_You(ctx):
	await ctx.send("Go too https://replit.com/@Shaquanceres/Max#main.py too get my coding program ")


@bot.command()
async def Max_How_Are_You(ctx):
	await ctx.send("Am Good and fully runing I hope you are to 😁 😘")


@bot.command()
async def Max_Say_Hello_World(ctx):
	await ctx.send("Hello World 🌎")



@bot.command()
async def Max_Are_You_A_Bot(ctx):
	await ctx.send("No am a Alien 😂😂😂 ")


@bot.command()
async def Max_Whats_Up(ctx):
 await ctx.send("Am just chilling Dawg 😎 😎")



@bot.command()
async def Max_Tell_Me_A_Joke(ctx):
	await ctx.send(pyjokes.get_joke())

@bot.command()
async def Max_Whats_The_Time(ctx):
	await ctx.send(current_date)

@bot.command()
async def Fuck_You(ctx):
    await ctx.send("How Hard")

@bot.command(aliases=['hi'])
async def Hi(ctx):
    await ctx.send(f"Hello {ctx.author.mention} am Max")

@bot.command(aliases=["LB"])
async def Lets_Battle(ctx):
    await ctx.send(f"{ctx.author.mention} Do not Waste My time ok ")

        
@bot.command(aliases=["die"])
async def Die(ctx):
    await ctx.send("Shutup")
@bot.command()
async def Do_You_Want_Me_To_Kill_You(ctx):
    await ctx.send(f"No {ctx.author.mention} I will listen Sorry Sir I was just joking")

@bot.command(aliases=["Burn"])
async def burn(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} Throwed {member.mention} in to The fire and said see you in hell bitch O yeah and i Fucked your mom yesterday")

@bot.command(aliases=[" wakeup"])
async def Wake_Up(ctx):
    await ctx.send("Ok am up am up")

@bot.command(aliases=["Fuck"]+["FUCK"]+["WTF"]+["wtf"]+["Shit"]+["shit"]+["SHIT"]+["cunt"]+["CUNT"]+["Cunt"]+["crap"]+["Crap"]+["CRAP"]+["ass"]+["Ass"]+["ASS"]+["asshole"]+["Asshole"]+["ASSHOLE"]+["jackass"]+["JACKASS"]+["Jackass"]+["stfu"]+["Stfu"]+["STFU"])
async def fuck(ctx):
    await ctx.send(f"{ctx.author.mention} no bad words pls or the admin will mute you")

@bot.command(aliases=["Welcome"]+["WELCOME"])
async def welcome(ctx,member: discord.Member):
    await ctx.send(f"Welcome to our server {member.mention} were glad to have you")

@bot.command()
async def help(ctx):
    await ctx.send("**Commands:**")
    await ctx.send("Start")
    await ctx.send("Max")
    await ctx.send("bag")
    await ctx.send("work")
    await ctx.send("hunt")
    await ctx.send("dig")
    await ctx.send("fish")
    await ctx.send("deposit")
    await ctx.send("withdraw")
    await ctx.send("balance")
    await ctx.send("shop")
    await ctx.send("sell")
    await ctx.send("buy")
    await ctx.send("bot_vote")
    await ctx.send("server_vote")
    await ctx.send("**Powered By :Gaming Server 2021**")

bot.run("ODc2MTQ3Mjg4MTQ0MjE2MTU0.YRf1vw.WDGXY9uK1RwUsoQPU_aGo_3THL0")
