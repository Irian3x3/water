from lib.water import Water
import discord
import config
from discord.ext import commands

bot = Water()

bot.start_cogs()

bot.run(config.token) # deletes the universe