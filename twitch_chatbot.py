"""
Main program
"""
import sys
from bot.bot import Bot
from data.config import Config
from outputs.outputs import Outputs

if __name__ == "__main__":
    config = Config()

    if not config.is_config_usable():
        Outputs().print_error("The config file is missing.")
        sys.exit(1)

    if not config.is_mega_config_valid():
        Outputs().print_info(
            "Mega config is missing or invalid."
        )

    irc_data = config.get_irc_data()
    twitch_data = config.get_twitch_data()

    bot = Bot(
        access_token=twitch_data["TMI_TOKEN"],
        prefix=twitch_data["BOT_PREFIX"],
        channels=[twitch_data["CHANNEL"]],

        osu_irc_server=irc_data["IRC_SERVER"],
        osu_irc_port=int(irc_data["IRC_PORT"]),
        osu_irc_name=irc_data["IRC_NAME"],
        osu_irc_pass=irc_data["IRC_PASS"]
    )
    
    bot.run()