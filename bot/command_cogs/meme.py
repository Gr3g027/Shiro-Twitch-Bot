from twitchio.ext import commands
from bot.bot import Bot

class Meme(commands.Cog):
    __slots__ = ()

    @commands.command(name="owo")
    async def owo(self, ctx: commands.Context):
        '''OwO command'''
        await ctx.send(f"/me OωO @{ctx.author.name}")

        await ctx.bot.command_output_handler(ctx)

    @commands.command(name="seventwentyseven", aliases=["727", "wysi"])
    async def seventwentyseven(self, ctx: commands.Context):
        '''OwO command'''
        await ctx.send(f"/me 727 WYSI!!! 727")
        
        await ctx.bot.command_output_handler(ctx)

def prepare(bot: Bot) -> None:
    bot.add_cog(Meme())