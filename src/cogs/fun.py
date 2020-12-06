import discord
from discord.ext import commands
#import config

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['echo'])
    async def say(self, ctx, tosay):
        """Says what you tell it to say"""
        author = ctx.message.author.name
        await ctx.send('_**{}** says:_\n{}'.format(author, tosay))

    @commands.command()
    async def drink(self, ctx):
        """Drink some water."""
        await ctx.send('You drank some water.')

def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))