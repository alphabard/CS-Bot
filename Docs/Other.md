# Documentation for other.py
`other.py` file will be use for stuff that is useless but usefull like tags and stuff like that.

we have a class `other` and the commands for making tags, editing them and using them
```py
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
```