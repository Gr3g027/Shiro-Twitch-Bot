'''Bot module'''
import asyncio
from asyncio import events
from pathlib import Path
from random import randint
import threading
from twitchio.ext import commands

# pylint: disable=import-error, no-name-in-module
from bot.osu_specific import *
from bot.irc import Irc
from outputs.outputs import Outputs
from utils.utils import process_exists

class Bot(commands.Bot):
    '''Bot class, handles all the bot logic'''

    outputs = Outputs()

    def __init__(self, access_token, client_id, prefix, channels, osu_irc: Irc):
        '''Bot class constructor'''
        self.osu_irc = osu_irc
        self.prefix = prefix

        self.msg_count = 0
        self.old_author = ""

        self.command_cogs: list[str] = {
            p.stem for p in Path("./bot/command_cogs").glob("*.py")
        }
        
        super().__init__(token=access_token, client_id=client_id, prefix=prefix,
                         initial_channels=[] if channels is None else channels)

    def run(self):
        for cog in self.command_cogs:
            self.load_module(f"bot.command_cogs.{cog}")
        self.outputs.print_info("All modules added!")

        super().run()
    
    async def event_ready(self):
        ''' Runs once the bot has established a connection with Twitch. '''
        self.outputs.print_info(f'Logged in as {self.nick}')
        if (process_exists('osu!.exe')):
            threading.Thread(target=self.osu_irc.bancho_connect).start()

    async def event_message(self, message):
        '''Runs every time a new message is received'''

        if message.echo:
            return
        else:
            self.msg_count += 1

            if self.old_author == message.author.name:
                self.outputs.print_message(message.content, lenght_author=len(message.author.name)-1)
            else:
                self.outputs.print_message(message.content, author=message.author.name, lenght_author=len(message.author.name)-1)

            if is_map_request(message.content):
                await self.send_map_request(message)
            elif message.content.count(self.prefix) == 1 and len(message.content) > 1:
                await self.handle_commands(message)
            elif self.msg_count%100 == 0:
                await self.cogs.get("Social").send_socials(message)
            
            self.old_author = message.author.name

    async def event_command_error(self, context, error = "") -> None:
        try:
            cmd_group = context.command.cog.name
            cmd_name = context.command.name

            if (cmd_group == "Social"):
                self.outputs.print_warning(f"No link provided for {cmd_name}")
                await context.send(f"/me No {cmd_name} here :p!")

            if (error != ""): self.outputs.print_error(error)
            await context.send(f"/me Sorry, some error occured! {cmd_name} command didn't work!")
        except Exception as ex:
            self.outputs.print_error(ex)
            if (ex == "'NoneType' object has no attribute 'cog'") : 
                self.outputs.print_error("The command does not exist!")
        # return await super().event_command_error(context, error)

    # pylint: disable=invalid-name
       
    async def command_output_handler(self, ctx: commands.Context):
        '''Handles the terminal outputs, command related'''
        cmd_name = ctx.command.name
        Outputs.print_info(f"{cmd_name} command executed!")

    async def send_map_request(self, message):
        '''Handles the map requests'''
        osu_url = find_osu_url(message.content)
        song_name = find_osu_map_name(osu_url)

        author = message.author.name.capitalize()
        ctx = message.channel

        if not process_exists('osu!.exe'):
            await ctx.send(f"/me Mmh?! not playing osu right now!")
            self.outputs.print_warning("Osu is not running")
            return 

        elif not song_name or not osu_url:
            await ctx.send(f"/me The link you sent is not valid @{author}! :(")
            self.outputs.print_warning("The link sent wasn't found")
            return

        elif not self.osu_irc.is_connected():
            threading.Thread(target=self.osu_irc.bancho_connect).start()
            await asyncio.sleep(3)
        
        irc_channel = self.osu_irc.name
        await ctx.send(f"/me Your map is being requested @{author}! RainbowPls")
        self.osu_irc.privmsg(irc_channel, f"[{osu_url} {song_name}] | Requested by {author}")
        self.outputs.print_map_request(author, osu_url)
            
