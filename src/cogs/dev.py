import ast
import ast as parser
import config
import discord
from discord.ext import commands

def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['evaluate'])
    @commands.is_owner()
    async def ev(self, ctx: commands.context, *, code):
        """
        Evaluates provided Python code and runs it.
        """

        fn = "_eval_expr"

        code = code.strip("` ")
        code = '\n'.join(f"  {i}" for i in code.splitlines())
        
        body = f"async def {fn}():\n{code}"

        parsed = parser.parse(body)
        body = parsed.body[0].body

        insert_returns(body)

        env = {
            'bot': ctx.bot,
            'discord': discord,
            'commands': commands,
            'ctx': ctx,
            "__import__": __import__
        }

        exec(compile(parsed, filename = '<ast>', mode = 'exec'), env)

        evaled = (await eval(f"{fn}()", env))
        await ctx.send(f'```py\n{evaled}```')

def setup(bot: commands.Bot):
    bot.add_cog(Dev(bot))