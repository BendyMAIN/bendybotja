import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = commands.Bot(command_prefix='/')

print ("Loading....")

@client.event
async def on_ready():
	print ("The bot is online!")
	await client.change_presence(game=discord.Game(name='Support server:AndroidGamesCommunity' ,ype=3))
	
@client.command()
async def ping():
    await client.say("Pong!")
 
@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await client.say("Felhasználói információk")
    await client.say("Név: {}".format(user.name))
    await client.say("Id: {}".format(user.id))
    await client.say("Legmagasabb rang: {}".format(user.top_role))
    
async def piros():
    embed = discord.Embed(
        title = 'Cím',
        description = 'Leírás',
        colour = discord.Colour.red()
    )
    embed.add_field(name='Név', value='Érték', inline=False)
    embed.add_field(name='Név', value='Érték', inline=False)
    embed.set_footer(text='BENDY BOT | v1.0')
    await client.say(embed=embed)
   
@client.command(pass_context=True)
async def segítség():
    embed = discord.Embed(
        title = 'Információk',
        description = 'Parancsaim: /info',
        colour = discord.Colour.green()
	)
    embed.add_field(name='By', value='BENDY', inline=False)
    embed.set_footer(text='BENDY BOT|v1.0')
    await client.say(embed=embed)

@bot.command()
async def info(ctx):
embed = discord.embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

# give info about you here
embed.add_field(name="Author", value="<YOUR-USERNAME>")

# Shows the number of servers the bot is member of.
embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

# give users a link to invite thsi bot to their server
embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

await ctx.send(embed=embed)
	
client.run("NTU2NTQ4NzM3MDM2NDUxODQ2.D27dWA.lp6BOu5OViE8_RXECgoj9tmi5xU") 
