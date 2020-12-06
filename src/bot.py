from lib.water import Water
import discord
import config
from discord.ext import commands
import os

bot = Water()

for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py') and filename != '__init__.py':
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config.token) # deletes the universe