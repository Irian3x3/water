from config import blue_color, prefix, description
import discord
from discord.ext import commands as cmds

class Core(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @cmds.command()
    async def ping(self, ctx):
        em = discord.Embed(color = blue_color)
        em.add_field(name = 'ping', value = f'```scss\n{self.bot.latency} ms```', inline=True)
        await ctx.send(embed=em)
    
    @cmds.command(aliases = ["server", 'si'])
    async def serverinfo(self, ctx):
        guild = ctx.guild

        icon = f'https://cdn.discordapp.com/icons/{guild.id}/{guild.icon}.png'
        em = discord.Embed(color = blue_color)

        em.set_author(name = guild.name, icon_url = icon)
        em.add_field(name = 'ID', value = f'`{guild.id}`', inline = True)
        # em.add_field(name = 'Members', value = f'{guild.members}', inline = True)
        await ctx.send(embed=em)

def setup(bot: cmds.Bot):
    bot.add_cog(Core(bot))
