"""
Main program
"""
import sys
import threading
from bot.irc import Irc
from bot.bot import Bot
from data.config import Config
from outputs.outputs import Outputs
from setup.setup import Setup

if __name__ == "__main__":
    config = Config()
    outputs = Outputs()

    if not config.is_config_usable():
        outputs.print_error("The config file is missing.")
        setup = Setup()
        config = Config()

    if not config.is_mega_config_valid():
        outputs.print_info("Mega config is missing or invalid.")

    if not config.is_irc_config_valid():
        outputs.print_info("Osu-Irc config is missing or invalid.")

    

    irc_data = config.get_irc_data()
    twitch_data = config.get_twitch_data()
    social_data = config.get_social_data()

    irc = Irc(
        server=irc_data["IRC_SERVER"],
        port=int(irc_data["IRC_PORT"]),
        irc_name=irc_data["IRC_NAME"],
        irc_pass=irc_data["IRC_PASS"]
    )

    bot = Bot(
        access_token=twitch_data["TMI_TOKEN"],
        prefix=twitch_data["BOT_PREFIX"],
        channels=[twitch_data["CHANNEL"]],
        osu_irc=irc,
        twitter_link=social_data["TWITTER"],
        discord_link=social_data["DISCORD_SERVER"],
        osu_profile=social_data["OSU_PROFILE"]
    )

    threading.Thread(target=irc.irc_connect).start()
    
    bot.run()