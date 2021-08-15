import discord                                         


client = discord.Client()

@client.event
async def on_ready( ) :
	print('we have logged you in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if message.author== client.user:
    return   message.channel.send('Hello!')
client.run('ODc2MTQ3Mjg4MTQ0MjE2MTU0.YRf1vw.awtYhGwazOFrpXMjkHov0hXn3RM'
)

