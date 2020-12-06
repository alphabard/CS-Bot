from discord.ext import commands
import discord
import os

from config import token

description = "A bot made for moderation and fun in CS Dojo Discord server"

# intents = discord.Intents.default()
# intents.members = True

bot = commands.Bot(command_prefix='cs.', description=description)

@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_command_error(ctx, error):
    error_logs = bot.get_channel(int(784080015687680040))
    print(error)
 
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"

cogs = [
    'cogs.important',
    'cogs.other',
    'cogs.moderation',
    'cogs.euler',
]

for cog in cogs:
    bot.load_extension(cog)


@bot.command()
async def say(ctx, *arg):
    await ctx.send(str(arg))
        

bot.run(token)
