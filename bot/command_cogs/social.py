from random import randint
from twitchio.ext import commands, eventsub
from bot.bot import Bot
from data.config import Config
from outputs.outputs import Outputs

class Social(commands.Cog):
    __slots__ = ()

    def __init__(self):
        social_data = Config().get_social_data()
        self.ds_link = social_data["DISCORD_SERVER"]
        self.twitter_link = social_data["TWITTER"]
        self.ig_link = social_data["INSTAGRAM"]
        self.osu_profile = social_data["OSU_PROFILE"]

    @commands.command(name="discord", aliases=["ds"])
    async def discord(self, ctx: commands.Context):
        '''Discord command'''
        if self.ds_link:
            await ctx.send(f"/me Enter our Discord server! -> {self.ds_link} @{ctx.author.name}")

            await ctx.bot.command_output_handler(ctx)
        else:
            await ctx.bot.event_command_error(ctx)
    
    @commands.command(name="twitter")
    async def twitter(self, ctx: commands.Context):
        '''Twitter command'''
        if self.twitter_link:
            await ctx.send(f"/me Have a look at {ctx.channel.name.capitalize()}'s Twitter! -> {self.twitter_link} @{ctx.author.name}")

            await ctx.bot.command_output_handler(ctx)
        else: 
            await ctx.bot.event_command_error(ctx)

    @commands.command(name="instagram", aliases=["ig"])
    async def instagram(self, ctx: commands.Context):
        '''Instagram command'''
        if self.ig_link:
            await ctx.send(f"/me Here is {ctx.channel.name.capitalize()}'s Instagram! -> {self.ig_link} @{ctx.author.name}")

            await ctx.bot.command_output_handler(ctx)
        else:
            await ctx.bot.event_command_error(ctx)
    
    @commands.command(name="osuprofile", aliases=["osup", "osu", "profile"])
    async def osuprofile(self, ctx: commands.Context):
        '''Osu-profile command'''
        if self.osu_profile:
            await ctx.send(f"/me Check {ctx.channel.name.capitalize()}'s Osu-profile! -> {self.osu_profile} @{ctx.author.name}")

            await ctx.bot.command_output_handler(ctx)
        else:
            await ctx.bot.event_command_error(ctx)
    
    async def send_socials(self, message):
        '''Randomly sends the socials in chat (ig, ds, twitter)'''

        #TODO this is not good
        
        ctx = message.channel
        socials = [f"{ctx.channel.name.capitalize()}'s Twitter! -> {self.twitter_link}", 
                   f"{ctx.channel.name.capitalize()}'s Instagram! -> {self.ig_link}",
                   f"{ctx.channel.name.capitalize()}'s Discord! -> {self.ds_link}"]
        await ctx.send(f"/me {socials[randint(0,2)]}")
        Outputs.print_info("Social sent")

def prepare(bot: Bot) -> None:
    bot.add_cog(Social())