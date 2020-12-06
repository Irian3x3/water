from discord import Embed, Activity, ActivityType, Color
from discord.ext import commands
import config

class Water(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = config.prefix, description = config.description)

    async def on_command_error(self, ctx, err):
        if isinstance(err, commands.MissingRequiredArgument):
            em = Embed(description="```\n{}```".format(err), color = Color(config.red_color))
            em.set_author(name='Missing argument')
            await ctx.send(embed=em)
        elif isinstance(err, commands.CommandNotFound):
            em = Embed(description="**Unknown command. If you need a list of commands, type {}help.**".format(config.prefix), color = Color(config.red_color))
            await ctx.send(embed=em)
        else:
            em = Embed(color = Color(config.red_color))
            em.add_field(name='**Error**:', value='```py\n{}```'.format(err), inline=False)
            em.set_author(name='An error occured executing this command.')
            await ctx.send(embed=em)

    async def on_ready(self):
        this = self
        activity = Activity(type=ActivityType.watching, name='you hydrate')
        await this.change_presence(activity=activity)
        print('{} is online'.format(this.user.name))

    def start_cogs(self):
        """starts the cogs"""
        from os import listdir

        for filename in listdir('./src/cogs'):
            if filename.endswith('.py') and filename != '__init__.py':
                self.load_extension(f'cogs.{filename[:-3]}')