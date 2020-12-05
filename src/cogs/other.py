import discord
import random
from discord.ext import commands
import datetime
import json
now = datetime.datetime.now()

def colour():
    colours = [0x921cff, 0x00ff7f, 0xff9b38, 0xff0000, 0x0900ff]
    return random.choice(colours)  

class other(commands.Cog, name='other'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['create tag', 'create'])
    async def create_tag(self, ctx, * , name):
        with open('tags.json') as f:
            tags = json.load(f)
        if name in tags.keys():
            await ctx.send("There's a tag with that name!")
        else:
            await ctx.send("What's the content of this tag? ||send message||")
            description = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            tags[name] = f"{str(description.content)}"
            with open('tags.json', 'w') as f:
                json.dump(tags, f, indent = 4)
            await ctx.send(f"Done! Do `!tag {name}` to see your tag.")
    
    @commands.command()
    async def tag(self, ctx, *, tag):
        with open('tags.json') as f:
            tags = json.load(f)
        if tag not in tags.keys():
            await ctx.send("Tag not found!")
        else:
            await ctx.send(tags[tag])

    @commands.command(aliases = ['edit'])
    async def edit_tag(self, ctx, *, tag):
        with open('tags.json') as f:
            tags = json.load(f)
        if tag not in tags.keys():
            await ctx.send("The tag you're trying to edit is not found!")
        else:
            await ctx.send('What is the new description of this tag?')
            description = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            tags[str(tag)] = str(description.content)
            with open('tags.json', 'w') as f:
                json.dump(tags, f, indent = 4)
            await ctx.send("Tag edited!")

def setup(bot):
    bot.add_cog(other(bot))