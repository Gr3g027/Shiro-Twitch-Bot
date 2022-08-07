from os import environ
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

        #TWITCH settings
        self.TMI_TOKEN = environ.get("TMI_TOKEN")
        self.CLIENT_ID = environ.get("CLIENT_ID")
        self.BOT_NICK = environ.get("BOT_NICK")
        self.BOT_PREFIX = environ.get("BOT_PREFIX")
        self.CHANNEL = environ.get("CHANNEL")

        #OSU-IRC settings
        self.IRC_SERVER = environ.get("IRC_SERVER")
        self.IRC_PORT = environ.get("IRC_PORT")
        self.IRC_NAME = environ.get("IRC_NAME")
        self.IRC_PASS = environ.get("IRC_PASS")
        self.OSU_PROFILE = environ.get("OSU_PROFILE")

        #GOSU settings
        self.GOSUMEMORY_JSON = environ.get("GOSUMEMORY_JSON_URL")

        #MEGA settings
        self.MEGA_EMAIL = environ.get("MEGA_EMAIL")
        self.MEGA_PASSWORD = environ.get("MEGA_PASSWORD")
        self.MEGA_FOLDER = environ.get("MEGA_FOLDER")

        #SOCIAL settings
        self.TWITTER = environ.get("TWITTER")
        self.DISCORD_SERVER = environ.get("DISCORD_SERVER")
        self.INSTAGRAM = environ.get("INSTAGRAM")
 
    def get_mega_data(self) -> dict:
        """Returns mega config data."""

        return {
            "MEGA_EMAIL": self.MEGA_EMAIL,
            "MEGA_PASSWORD": self.MEGA_PASSWORD,
            "MEGA_FOLDER": self.MEGA_FOLDER
        }

    def get_twitch_data(self) -> dict:
        """Returns twitch config data."""

        return {
            "TMI_TOKEN": self.TMI_TOKEN,
            "CLIENT_ID": self.CLIENT_ID,
            "BOT_NICK": self.BOT_NICK,
            "BOT_PREFIX": self.BOT_PREFIX,
            "CHANNEL": self.CHANNEL
        }

    def get_irc_data(self) -> dict:
        """Returns irc config data."""

        return {
            "IRC_SERVER": self.IRC_SERVER,
            "IRC_PORT": self.IRC_PORT,
            "IRC_NAME": self.IRC_NAME,
            "IRC_PASS": self.IRC_PASS
        }

    def get_social_data(self) -> dict:
        """Returns social config data"""

        return {
            "TWITTER": self.TWITTER,
            "DISCORD_SERVER": self.DISCORD_SERVER,
            "INSTAGRAM": self.INSTAGRAM,
            "OSU_PROFILE": self.OSU_PROFILE
        }

    def get_gosumemory_url(self) -> dict:
        """Returns the gosumemory url"""
        return self.GOSUMEMORY_JSON

    def is_config_usable(self) -> bool:
        """Checks if values are valid"""
        return self.is_twitch_config_valid() and self.GOSUMEMORY_JSON is not None

    def is_twitch_config_valid(self) -> bool:
        """Checks if the twitch values are valid"""
        return all(value is not None for value in self.get_twitch_data().values())

    def is_mega_config_valid(self) -> bool:
        """Checks if the mega values are valid"""
        return all(value is not None for value in self.get_mega_data().values())

    def is_irc_config_valid(self) -> bool:
        """Checks if the osy-irc values are valid"""
        return all(value is not None for value in self.get_irc_data().values())
