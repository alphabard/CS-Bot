# Documentation for euler.py
`euler.py` is a file that is for project euler problmes, it have 10 problmes for now but i will keep adding more to it.

A euler class with all the functions
```py
class euler(commands.Cog, name='Euler'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def e1(self, ctx):
        embed = discord.Embed(description=p1)
        await ctx.send(embed=embed)

    @commands.command()
    async def e2(self, ctx):
        embed = discord.Embed(description=p2)
        await ctx.send(embed=embed)

    @commands.command()
    async def e3(self, ctx):
        embed = discord.Embed(description=p3)
        await ctx.send(embed=embed)

    @commands.command()
    async def e4(self, ctx):
        embed = discord.Embed(description=p4)
        await ctx.send(embed=embed)

    @commands.command()
    async def e5(self, ctx):
        embed = discord.Embed(description=p5)
        await ctx.send(embed=embed)

    @commands.command()
    async def e6(self, ctx):
        embed = discord.Embed(description=p6)
        await ctx.send(embed=embed)

    @commands.command()
    async def e7(self, ctx):
        embed = discord.Embed(description=p7)
        await ctx.send(embed=embed)

    @commands.command()
    async def e8(self, ctx):
        embed = discord.Embed(description=p8)
        await ctx.send(embed=embed)

    @commands.command()
    async def e9(self, ctx):
        embed = discord.Embed(description=p9)
        await ctx.send(embed=embed)

    @commands.command()
    async def e10(self, ctx):
        embed = discord.Embed(description=p10)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(euler(bot))
```