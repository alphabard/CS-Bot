from discord.ext import commands
import discord
import random
import datetime
now = datetime.datetime.now()

def colour():
    colours = [0x921cff, 0x00ff7f, 0xff9b38, 0xff0000, 0x0900ff]
    return random.choice(colours)  

class moderation(commands.Cog, name='Moderation'):
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int = None):
        try:
            logs = self.bot.get_channel(int(733708136049016882))
            if not amount:
                embed=discord.Embed(description='Please specify an amount that you want to purge')
                await ctx.send(embed=embed)
            else:
                await ctx.channel.purge(limit=amount+1, check=lambda msg: not msg.pinned)
            embed = discord.Embed(title="Purge", description=f'{amount} messages were purged by {ctx.author.mention} in {ctx.channel.mention}', color=0xffffff)
            await logs.send(embed=embed)
        except commands.CheckFailure:
            await ctx.send("You don't have the permission to manage messages.")

    @commands.command()
    @commands.has_role('Staff')
    async def warn(self, ctx, user: discord.Member=None, *, arg=None):
        try:
            logs = self.bot.get_channel(int(733708136049016882))
            if not user:
                embed=discord.Embed(description='Please mention a member that you want to warn!')
                await ctx.send(embed=embed)
            if not arg:
                embed=discord.Embed(description='Please provide a reason!')
                await ctx.send(embed=embed)
            else:
                
                await ctx.send(f'{user.mention} has been warned')
                try:
                    await user.create_dm()
                    await user.dm_channel.send(f'{user.mention}, you have been warned in {ctx.guild.name} for {arg}!')
                except: 
                    await ctx.send(f"> {user}'s DMs are closed!")
                embed = discord.Embed(title="Warn", description=f'**Reason:** {arg}\n**Member Warned:** {user.mention}\n**Warned by:** {ctx.author.mention}', color=0xffffff)
                await logs.send(embed=embed)
        except commands.CheckFailure:
            await ctx.send("You need to be staff to use this command!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member=None, *, reason=None):
        try:
            if not user:
                embed=discord.Embed(description='Please mention a member that you want to kick!')
                await ctx.send(embed=embed)
            if not reason:
                embed=discord.Embed(description='Please provide a reason!')
                await ctx.send(embed=embed)
            else:
                try:
                    logs = self.bot.get_channel(int(733392614614761473))
                    await user.kick(reason=reason)
                    await ctx.send(f'{user} was successfully kicked!')
                    embed = discord.Embed(title="Kick", description=f'**Reason:** {reason}\n**Member kicked:** {user.mention}\n**kicked by:** {ctx.author.mention}', color=0xffffff)
                    await logs.send(embed=embed)
                except:
                    # await ctx.send(f'{user} could not be kicked.')
                    pass
        except commands.CheckFailure:
            await ctx.send("You don't have the permissions to kick people.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, user: discord.Member=None, *, reason=None):
        try:
            if not user:
                embed=discord.Embed(description='Please mention a member that you want to ban!')
                await ctx.send(embed=embed)
            if not reason:
                embed=discord.Embed(description='Please provide a reason!')
                await ctx.send(embed=embed)
            else:
                try:
                    logs = self.bot.get_channel(int(733392614614761473))
                    await user.ban(reason=reason)
                    await ctx.send(f'{user} was successfully Banned!')
                    embed = discord.Embed(title="Ban", description=f'**Reason:** {reason}\n**Member Banned:** {user.mention}\n**Banned by:** {ctx.author.mention}', color=0xffffff)
                    await logs.send(embed=embed)
                except:
                    # await ctx.send("Some error")
                    pass
        except commands.CheckFailure:
            await ctx.send("You don't have the permissions to ban people.")

    #reporting users
    """
    one users reports other in any channel then the report is sent to a channel where only staff can see it.
    """
    @commands.command()
    @commands.Cog.listener()
    async def report(self, ctx, member: discord.Member=None, content=None):
        if not member:
            embed = discord.Embed(description='Please mention a member that you want to report!')
            await ctx.send(embed=embed)
        if not content:
            embed = discord.Embed(description='Please Provide report content with evidence!')
            await ctx.send(embed=embed)
        else:
            try:
                logs = self.bot.get_channel(int(784411030142844938))
                await ctx.send(f'{member} was successfully Reported!')
                embed = discord.Embed(title=f'{member} was reported', description=content)
                await logs.send(embed=embed)
            except:
                pass

    @commands.command(pass_context = True)
    @commands.has_role('Staff')
    async def mute(self, ctx, member: discord.Member=None, *, reason=None):
        try:
            if not member:
                embed=discord.Embed(description='Please mention a member that you want to mute!')
                await ctx.send(embed=embed)
            else:
                logs = self.bot.get_channel(int(733474243311829042))
                role = discord.utils.get(ctx.guild.roles, name="Muted")
                await member.add_roles(role)
                em=discord.Embed(description=f'{member.name} was successfully muted!')
                await ctx.send(embed=em)
                embed = discord.Embed(title="Mute", description=f'**Reason:** {reason}\n**Member Muted:** {member.mention}\n**Muted by:** {ctx.author.mention}', color=0xffffff)
                await logs.send(embed=embed)
        except commands.CheckFailure:
            await ctx.send("You need staff for this.")

    @commands.command(pass_context = True)
    @commands.has_role('Staff')
    async def unmute(self, ctx, member: discord.Member=None):
        try:
            if member is None:
                embed=discord.Embed(description='Please mention a member that you want to unmute!')
                await ctx.send(embed=embed)
            else:
                role = discord.utils.get(ctx.guild.roles, name="Muted")
                logs = self.bot.get_channel(int(733474243311829042))
                await member.remove_roles(role)
                await ctx.send(f'{member.mention} has been unmuted!')
                embed = discord.Embed(title="Unmute", description=f'{member.mention} was unmuted by {ctx.author.mention}', color=0xffffff)
                await logs.send(embed=embed)
        except commands.CheckFailure:
            await ctx.send("You need staff for this.")    


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        logs = self.bot.get_channel(int(784360508299804682))
        if not message.attachments:
            await logs.send(f'Deleted in {message.channel.mention}')
            embed=discord.Embed(title = 'Message Deleted', description = message.content)
            embed.set_author(name=f'From: {message.author}', icon_url=message.author.avatar_url)
            embed.set_footer(text=f'{now.day}/{now.month}/{now.year}')
            await logs.send(embed=embed)
        else:
            await logs.send(f'Deleted in {message.channel.mention}')
            embed=discord.Embed(title = 'Message Deleted', description = message.content)
            embed.set_author(name=f'From: {message.author}', icon_url=message.author.avatar_url)
            embed.set_footer(text=f'{now.day}/{now.month}/{now.year}')
            embed.set_image(url=message.attachments[0].proxy_url)
            await logs.send(embed=embed)
        await self.bot.process_commands(message)
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel = self.bot.get_channel(int(784360508299804682))
        if before.author == self.bot.user:
            return
        await channel.send(f'Edited in {before.channel}')
        embed = discord.Embed(description=f"**Message Edited**\n\n**Old**\n```{before.content}```\n\n**New**\n```{after.content}\n```")
        embed.set_author(name = f'From: {before.author}', icon_url= before.author.avatar_url)
        embed.set_footer(text=f'{now.day}/{now.month}/{now.year}')
        await channel.send(embed=embed)
        
def setup(bot):
    bot.add_cog(moderation(bot))