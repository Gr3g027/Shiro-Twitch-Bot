from twitchio.ext import commands
from bot.bot import Bot
from outputs.outputs import Outputs
from data.gosumemory import Gosumemory
from utils.utils import string_map, string_pp

gosumemory = Gosumemory()

class Osu(commands.Cog):
    __slots__ = ()

    @commands.command(name="nowplaying", aliases=["np", "nowp"])
    async def np(self, ctx: commands.Context):
        '''Now playing command'''
        if gosumemory.is_connected():
            bm_metadata = gosumemory.get_map_data()
            await ctx.send(f'{string_map(bm_metadata)}')
            
            await ctx.bot.command_output_handler(ctx)
        else:
            await ctx.bot.event_command_error(ctx,"Could not connect to gosumemory socket!")
    
    @commands.command(name="pp", aliases=["peppypoints", "performancepoints"])
    async def pp(self, ctx: commands.Context):
        '''PP command'''
        if gosumemory.is_connected():
            pp_data = gosumemory.get_map_data()
            await ctx.send(f'{string_pp(pp_data)}')

            await ctx.bot.command_output_handler(ctx)
        else:
            await ctx.bot.event_command_error(ctx,"Could not connect to gosumemory socket!")

    @commands.command(name="skin", aliases=["osuskin"])
    async def skin(self, ctx: commands.Context):
        '''Skin command'''
        if gosumemory.is_connected():
            skin = gosumemory.get_skin()
            Outputs.print_info("The skin is already on mega!")
            await ctx.send(f"{skin['skin']} {skin['url']}")
            Outputs.print_info("Skin command executed!")

            await ctx.bot.command_output_handler(ctx)
        else:
            await ctx.bot.event_command_error(ctx,"Could not connect to gosumemory socket!")

def prepare(bot: Bot) -> None:
    bot.add_cog(Osu())