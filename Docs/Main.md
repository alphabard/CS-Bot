# Documentation for main.py
`main.py` is the most important file and this file will be used to run the bot, it manages cogs and exceptions.

These are all the imports of `main.py`
```py
from discord.ext import commands
import discord
import os

from config import token
```

Description for the bot and bot perfix
```py
description = "A bot made for moderation and fun in CS Dojo Discord server"
bot = commands.Bot(command_prefix='c.', description=description)
```

Cogs, evns, exceptions and that all stuff
```py
@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_command_error(ctx, error):
    error_logs = bot.get_channel(int(784080015687680040))
    await error_logs.send(f"```py\n{error}\n```")
 
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"

cogs = [
    'cogs.important',
    'cogs.other',
    'cogs.moderation',
]

for cog in cogs:
    bot.load_extension(cog)


@bot.command()
async def say(ctx, *arg):
    await ctx.send(str(arg))
```

Running the bot
```py
bot.run(token)
```