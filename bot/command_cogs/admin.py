import sys
import threading
from twitchio.ext import commands
from bot.bot import Bot

class Admin(commands.Cog):
    __slots__ = ()

    @commands.command(name="shutdown", aliases=["sh"])
    async def shutdown(self, ctx: commands.bot.Context) -> None:
        if ctx.author.name != ctx.channel.name:
           return await ctx.send(f"You can't shut me down!")
        await ctx.send(f"/me Bye Byeee RainbowPls")
        await ctx.bot.close()
        if (ctx.bot.osu_irc.is_connected()):
            ctx.bot.osu_irc.bancho_disconnect()
        sys.exit(0)

    @commands.command(name="startbanchoirc", aliases=["sbi", "startirc", "startosuirc"])
    async def startbanchoirc(self, ctx: commands.bot.Context) -> None:
        if ctx.author.name != ctx.channel.name:
            return await ctx.send(f"You can't start the osu irc!")
        threading.Thread(target=ctx.bot.osu_irc.bancho_connect).start()
        await ctx.send("/me Bancho irc is now connected!")

def prepare(bot: Bot) -> None:
    bot.add_cog(Admin())