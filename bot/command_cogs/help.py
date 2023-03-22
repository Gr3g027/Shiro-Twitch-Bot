from twitchio.ext import commands
from bot.bot import Bot
from utils.utils import process_exists

class Help(commands.Cog):
    __slots__ = ()

    @commands.command(name="info", aliases=["help", "i", "commands", "cmds"])
    async def info(self, ctx: commands.bot.Context):
        '''Info command'''
        cmd_list = f"/me Hey @{ctx.author.name}! Currenty usable commands are:"
        cmd_groups = ctx.bot.cogs

        for group in cmd_groups.values():
            commands = group.commands
            for command in commands.values():
                if (group.name != "Admin"):
                    cmd_list += f" !{command.name}"
            cmd_list += f" |"
        
        await ctx.bot.command_output_handler(ctx)
        await ctx.send(cmd_list)

    @commands.command(name="infoosu", aliases=["helposu", "iosu", "osucommands", "cmds", "osuinfo"])
    async def info(self, ctx: commands.bot.Context):
        '''Info command specific for osu'''
        if (not process_exists('osu!.exe')):
            await ctx.send("/me Osu is not running at the moment!")
            return
        cmd_list = f"/me Hey @{ctx.author.name}! Currenty usable osu commands are:"
        osu_group = ctx.bot.cogs.get("Osu")
        commands = osu_group.commands
        for command in commands.values():
            cmd_list += f" !{command.name} "
        
        await ctx.bot.command_output_handler(ctx)
        await ctx.send(cmd_list)
        

def prepare(bot: Bot) -> None:
    bot.add_cog(Help())