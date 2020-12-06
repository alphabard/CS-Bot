from discord.ext import commands
import discord

#problmes
p1 = """
Multiples of 3 and 5\n
Problem 1\n
if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.
"""

p2 = """
Even Fibonacci numbers\n
Problem 2\n
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:\n
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...\n
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

p3 = """
Largest prime factor\n
Problem 3\n
The prime factors of 13195 are 5, 7, 13 and 29.\n
What is the largest prime factor of the number 600851475143 ?
"""

p4 = """
Largest palindrome product\n
Problem 4\n
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.\n
Find the largest palindrome made from the product of two 3-digit numbers.
"""

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

def setup(bot):
    bot.add_cog(euler(bot))