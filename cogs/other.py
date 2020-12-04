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


    @commands.command(description = "Shows you're away")
    async def afk(self, ctx):
        try:
            nickname = ctx.author.display_name 
            afk = f'[AFK] {nickname}'
            await ctx.author.edit(nick=afk)
            await ctx.channel.send(f'{ctx.author} has gone AFK')
            await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            await ctx.author.edit(nick=nickname)
            await ctx.channel.send(f'{ctx.author.mention} was removed from AFK')
        except commands.BotMissingPermissions:
            embed=discord.Embed(description="The bot needs to have a higher role for you to go into AFK.", color=colour())
            await ctx.send(embed=embed)
    
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
    
    @commands.command()
    async def delete_tag(self, ctx, *, arg):
        allow_users = []
        if ctx.author.id in allow_users:
            with open('tags.json') as f:
                tags = json.load(f)

def setup(bot):
    bot.add_cog(other(bot))




