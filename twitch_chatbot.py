"""
Main program
"""
import sys

from bot.bot import Bot
from bot.setup_config import Setup
from data.config import Config
from outputs.outputs import Outputs

if __name__ == "__main__":
    while True:  # FIXME should not be here
        config = Config()
        if not config.is_config_usable():
            Outputs().print_error("The config file is missing.")
            Setup().setup_bot()
        else:
            break

    if not config.is_mega_config_valid():
        Outputs().print_warning("Mega config is missing or invalid.")

    twitch_data = config.get_twitch_data()

    bot = Bot(
        access_token=twitch_data["TMI_TOKEN"],
        prefix=twitch_data["BOT_PREFIX"],
        channels=[twitch_data["CHANNEL"]],
    )

    # starting the bot,
    # the method run() is blocking anything behind will not be executed
    bot.run()
