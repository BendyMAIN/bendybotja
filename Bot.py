import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = commands.Bot(command_prefix='/')

print ("Loading....")


	
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
	
client.run("NTU2NTQ4NzM3MDM2NDUxODQ2.XI1EZw.bAp74OceE9shS0_nFm8jkPcOegU") 
