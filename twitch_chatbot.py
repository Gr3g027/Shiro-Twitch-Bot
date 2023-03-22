"""
Main program
"""
from bot.irc import Irc
from bot.bot import Bot
from data.config import Config
from outputs.outputs import Outputs
# from setup.setup import Setup

if __name__ == "__main__":
    config = Config()
    outputs = Outputs()

    if not config.is_config_usable():
        outputs.print_error("The config file is missing.")

    if not config.is_mega_config_valid():
        outputs.print_info("Mega config is missing or invalid.")

    if not config.is_irc_config_valid():
        outputs.print_info("Osu-Irc config is missing or invalid.")

    irc_data = config.get_irc_data()
    twitch_data = config.get_twitch_data()
    social_data = config.get_social_data()

    osu_irc = Irc(
        server=irc_data["IRC_SERVER"],
        port=int(irc_data["IRC_PORT"]),
        name=irc_data["IRC_NAME"],
        bancho_pass=irc_data["IRC_PASS"]
    )

    bot = Bot(
        access_token=twitch_data["TMI_TOKEN"],
        client_id=twitch_data["CLIENT_ID"],
        prefix=twitch_data["BOT_PREFIX"],
        channels=[twitch_data["CHANNEL"]],
        osu_irc=osu_irc
    )
    bot.run()