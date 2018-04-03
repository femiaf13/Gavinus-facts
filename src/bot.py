from datetime import datetime

import discord
from discord.ext import commands

from facts import fact_list

TOKEN = 'your_token_here'
NICKNAME = 'Aspen-Shea Facts'

description = '''Devout follower of Gavinus'''
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    # Due to a screwup when I made this bot, must change nickname during runtime
    for server in bot.servers:
        if server.me.nick != NICKNAME:
            me = server.me
            await bot.change_nickname(me, NICKNAME)

@bot.command()
async def fact():
    "Recite a Gavinus fact"
    index = int(datetime.now().microsecond)%len(fact_list)
    prefix = 'Did you know: '
    await bot.say(prefix+fact_list[index])

@bot.command(pass_context=True)
async def bday(ctx):
    "Wish Gavinus happy birthday!"
    # Take the context, and grab the nickname(if it exists)
    # of the person who gave the command
    if ctx.message.author.nick != None:
        user = ctx.message.author.nick
    else:
        user = ctx.message.author
    await bot.say(str(user)+' says: HAPPY BIRTHDAY GAVINUS')

if __name__ == '__main__':
    bot.run(TOKEN)
