from config import blue_color, prefix, description, token
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

'''
    @cmds.command(aliases = ['bot', 'bi', 'stats'])
    async def botinfo(self, ctx: cmds.context):
        bot = ctx.bot

        owner = bot.users[1]

        av = f'https://cdn.discordapp.com/avatars/{bot.user.id}/{bot.user.avatar}.png'

        em = discord.Embed(color = blue_color, description = f'*{bot.user.name} is a discord bot based on water and made with discord.py and python.*\n*I am made by `{owner}`*')
        em.set_author(name = f"Info on {ctx.bot.user.name}", icon_url = av)
        em.set_thumbnail(url = av)
        em.add_field(name = 'Servers', value = f"`{len(bot.guilds)}`", inline = True)
        em.add_field(name = 'Cached Users', value = f"`{len(bot.users)}`", inline = True)
        #em.add_field(name = 'Channels', value = f"`{len(bot.channels)}`", inline = True)
        await ctx.send(embed = em)

    @cmds.command(aliases = ['av', 'pfp'])
    async def avatar(self, ctx, user):
        av = f'https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.png'
        em = discord.Embed(color = discord.Color(0x4095))
        em.set_image(url = av)
        await ctx.send(embed = em)
    '''
def setup(bot: cmds.Bot):
    bot.add_cog(Core(bot))
