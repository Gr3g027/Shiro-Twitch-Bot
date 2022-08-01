'''Bot module'''
from twitchio.ext import commands
from twitchio.ext import routines

# pylint: disable=import-error, no-name-in-module
from bot.osu_specific import *
from bot.irc import Irc
from outputs.outputs import Outputs
from data.gosumemory import Gosumemory
from data.config import Config

class Bot(commands.Bot, Irc):
    '''Bot class, handles all the bot logic'''

    def __init__(self, access_token, prefix, channels, osu_irc):
        '''Bot class constructor'''

        self.outputs = Outputs()
        self.gosumemory = Gosumemory()
        self.irc = osu_irc

        super().__init__(token=access_token, prefix=prefix,
                         initial_channels=[] if channels is None else channels)

    async def event_ready(self):
        ''' Runs once the bot has established a connection with Twitch. '''
        self.outputs.print_info(f'Logged in as {self.nick}')
        self.irc.privmsg(self.irc.irc_name, "Ready to process requests!")

    async def event_message(self, message):
        '''Runs every time a new message is received'''

        # self.outputs.print_info(is_map_request(message.content))

        self.outputs.print_message(message.author.name, message.content)

        if message.echo:
            return
        else: 
            if is_map_request(message.content):
                await self.send_map_request(message)        

        await self.handle_commands(message)

    async def event_command_error(self, context, error):
        '''Runs for every error, command related'''
        self.outputs.print_error(error)
        await context.send(f"/me {error}")
        # return await super().event_command_error(context, error)

    # pylint: disable=invalid-name

    async def send_map_request(self, message):
        '''Handles the map requests'''
        author = message.author.name.capitalize()
        ctx = message.channel
        irc_channel = self.irc.irc_name

        await ctx.send(f"/me Your map is being requested @{author}!")

        osu_url = find_osu_url(message.content)
        song_name = find_osu_map_name(osu_url)

        # sending the IRC message
        self.irc.privmsg(irc_channel, f"[{osu_url} {song_name}] | Requested by {author}")

        self.outputs.print_map_request(author, osu_url)


    @commands.command()
    async def np(self, ctx: commands.Context):
        '''Now playing command'''
        metadata = self.gosumemory.get_map()
        if metadata:
            await ctx.send(f'{self.outputs.string_map(metadata=metadata)}')
            self.outputs.print_info("Now Playing command executed!")
        else:
            Outputs.print_error("Could not connect to gosumemory socket!")
            await ctx.send("/me Could not connect to gosumemory, sorry!")

    @commands.command()
    async def skin(self, ctx: commands.Context):
        '''Skin command'''
        skin = self.gosumemory.get_skin()
        if skin:
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

    @commands.command()
    async def discord(self, ctx: commands.Context):
        '''Discord command'''
        await ctx.send(f"/me My server! -> https://discord.com/invite/87M7evR @{ctx.author.name}")
        self.outputs.print_info("Discord command executed!")
    
    @commands.command()
    async def twitter(self, ctx: commands.Context):
        '''Twitter command'''
        await ctx.send(f"/me Follow me! -> https://twitter.com/Greg0_27 @{ctx.author.name}")
        self.outputs.print_info("Twitter command executed!")

    @commands.command()
    async def info(self, ctx: commands.Context):
        '''Info command'''
        #TODO this is not good
        await ctx.send(f"/me Hey @{ctx.author.name}! Currenty usable commands are: !np, !skin, !discord, !twitter")
        self.outputs.print_info("Info command executed!")

        