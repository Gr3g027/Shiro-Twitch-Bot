'''Bot module'''
from twitchio.ext import commands

# pylint: disable=import-error, no-name-in-module
from bot.osu_specific import *
from bot.irc import Irc
from outputs.outputs import Outputs
from data.gosumemory import Gosumemory

class Bot(commands.Bot):
    '''Bot class, handles all the bot logic'''

    def __init__(self, access_token, prefix, channels, osu_irc = Irc, twitter_link = "", discord_link = "", ig_link = "", osu_profile = ""):
        '''Bot class constructor'''

        self.outputs = Outputs()
        self.gosumemory = Gosumemory()
        self.irc = osu_irc

        self.twitter_link = twitter_link
        self.discord_link = discord_link
        self.ig_link = ig_link
        self.osu_profile = osu_profile

        super().__init__(token=access_token, prefix=prefix,
                         initial_channels=[] if channels is None else channels)

    async def event_ready(self):
        ''' Runs once the bot has established a connection with Twitch. '''
        self.outputs.print_info(f'Logged in as {self.nick}')
        self.irc.privmsg(self.irc.irc_name, "Ready to process requests!")

    async def event_message(self, message):
        '''Runs every time a new message is received'''

        # self.outputs.print_info(is_map_request(message.content))

        if message.echo:
            return
        else:
            self.outputs.print_message(message.author.name, message.content)

            if is_map_request(message.content):
                await self.send_map_request(message)

        await self.handle_commands(message)

    async def event_command_error(self, context, error):
        '''Runs for every error, command related'''
        self.outputs.print_error(error)
        await context.send(f"/me {error}")
        # return await super().event_command_error(context, error)

    # pylint: disable=invalid-name

    # async def event_join(self, channel, user):
    #     '''Runs every time a user joins the channel'''
    #     print(user.fetch_tags())
    #     if user.name != self.nick:
    #         self.outputs.print_info(f"USER JOINED: {user.name}")
    #     # await channel.send(f"/me You're welcome @{user}!")

    async def send_map_request(self, message):
        '''Handles the map requests'''
        osu_url = find_osu_url(message.content)
        song_name = find_osu_map_name(osu_url)

        author = message.author.name.capitalize()
        ctx = message.channel

        if not song_name:
            await ctx.send(f"/me The link you sent is not valid @{author}! :(")
            return

        else:
            irc_channel = self.irc.irc_name

            await ctx.send(f"/me Your map is being requested @{author}! :)")

            # sending the IRC message
            self.irc.privmsg(irc_channel, f"[{osu_url} {song_name}] | Requested by {author}")

            self.outputs.print_map_request(author, osu_url)


    @commands.command(name="np", aliases=["now playing", "nowp"])
    async def np(self, ctx: commands.Context):
        '''Now playing command'''
        if self.gosumemory.is_connected():
            metadata = self.gosumemory.get_map()
            await ctx.send(f'{self.outputs.string_map(metadata=metadata)}')
            self.outputs.print_info("Now Playing command executed!")
        else:
            Outputs.print_error("Could not connect to gosumemory socket!")
            await ctx.send("/me Could not connect to gosumemory, sorry!")

    @commands.command(name="skin", aliases=["osuskin"])
    async def skin(self, ctx: commands.Context):
        '''Skin command'''
        if self.gosumemory.is_connected():
            skin = self.gosumemory.get_skin()
            Outputs.print_info("The skin is already on mega!")
            await ctx.send(f"{skin['skin']} {skin['url']}")
            Outputs.print_info("Skin command executed!")
        else:
            Outputs.print_error("Could not connect to gosumemory socket!")
            await ctx.send("/me Could not connect to gosumemory, sorry!")

    @commands.command()
    async def owo(self, ctx: commands.Context):
        '''OwO command'''
        await ctx.send(f"/me OωO @{ctx.author.name}")
        self.outputs.print_info("OwO command executed!")

    @commands.command(name="discord", aliases=["ds"])
    async def discord(self, ctx: commands.Context):
        '''Discord command'''
        if self.discord_link:
            await ctx.send(f"/me My server! -> {self.discord_link} @{ctx.author.name}")
            self.outputs.print_info("Discord command executed!")
        else:
            await self.event_command_error(ctx, "No discord found!")
    
    @commands.command(name="twitter")
    async def twitter(self, ctx: commands.Context):
        '''Twitter command'''
        if self.twitter_link:
            await ctx.send(f"/me Follow me! -> {self.twitter_link} @{ctx.author.name}")
            self.outputs.print_info("Twitter command executed!")
        else: 
            await self.event_command_error(ctx, "No twitter found!")

    @commands.command(name="instagram", aliases=["ig"])
    async def instagram(self, ctx: commands.Context):
        '''Twitter command'''
        if self.ig_link:
            await ctx.send(f"/me Follow me! -> {self.ig_link} @{ctx.author.name}")
            self.outputs.print_info("Instagram command executed!")
        else:
            await self.event_command_error(ctx, "No instagram found!")
    
    @commands.command(name="osuprofile", aliases=["osup", "osu", "profile"])
    async def osuprofile(self, ctx: commands.Context):
        '''Osu-profile command'''
        if self.osu_profile:
            await ctx.send(f"/me Check my osu profile! -> {self.osu_profile} @{ctx.author.name}")
            self.outputs.print_info("Osu-profile command executed!")
        else:
            await self.event_command_error(ctx, "No osu profile found!")

    @commands.command(name="info", aliases=["i", "commands", "cmds"])
    async def info(self, ctx: commands.Context):
        '''Info command'''
        #TODO this is not good

        msg = f"/me Hey @{ctx.author.name}! Currenty usable commands are:"

        commands = sorted(self.commands, reverse=True)

        for command in commands:
            if command == list(commands)[-1]:
                msg += f" !{command}."
            else: 
                msg += f" !{command}, "
        await ctx.send(msg)
        self.outputs.print_info("Info command executed!")
        