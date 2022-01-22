'''Setup handler module'''

from outputs.outputs import Outputs

class Setup:
    '''Setup class, used to initiate the setup if config file is missing or invalid.'''

    def __init__(self, filename: str = "config.txt") -> None:
        '''Setup class constructor.'''
        self._filename: str = filename

    def set_bot_nick(self) -> str:
        Outputs.print_info("Nickname of the Twitch account you choose to be the bot")
        return input(f"Insert BOT NICK: ").lower()

    def set_bot_prefix(self) -> str:
        Outputs.print_info("Prefix wich will be used by the bot to determine commands (e. g. '!')")
        return input("Insert BOT PREFIX: ")

    def set_gosu_json_url(self) -> str:
        Outputs.print_info("URL that Gosumemory uses to return the json data (e. g. 'http://127.0.0.1:24050/json')")
        gosu_url = input("Insert GOSUMEMORY JSON URL: ")
        return gosu_url;

    def set_token(self) -> str:
        Outputs.print_info("URL that Gosumemory uses to return the json data (e. g. 'http://127.0.0.1:24050/json')")
        tmi_token = input("Insert TMI TOKEN: ")
        return tmi_token

    def set_client_id(self) -> str:
        return input("Insert CLIENT ID: ")

    def set_channel(self) -> str:
        Outputs.print_info("Name of the Streamer")
        return input("Insert STREAMER CHANNEL: ").lower()

    def set_mega_email(self) -> str:
        Outputs.print_info("Your MEGA account's email")
        mega_email = input("Insert MEGA EMAIL: ")
        return mega_email

    def set_mega_password(self) -> str:
        Outputs.print_info("Your MEGA account's password")
        return input("Insert MEGA PASSWORD: ")

    def set_mega_folder(self) -> str:
        Outputs.print_info("Your MEGA folder to wich you want to upload skins")
        return input("Insert MEGA FOLDER: ")

    def setup_bot(self) -> None:
        '''Setup all the settings, writing them in the config file.'''
        with open(self._filename, "w") as f:
            print(
                "# BOT CONFIG",
                f"BOT_NICK = {self.set_bot_nick()}",
                f"BOT_PREFIX = {self.set_bot_prefix()}",
                f"GOSUMEMORY_JSON_URL = {self.set_gosu_json_url()}\n",
                "# TWITCH CONFIG",
                f"TMI_TOKEN = {self.set_token()}",
                f"CLIENT_ID = {self.set_client_id()}",
                f"CHANNEL = {self.set_channel()}\n",
                "# MEGA ACCOUNT CONFIG",
                f"MEGA_EMAIL = {self.set_mega_email()}",
                f"MEGA_PASSWORD = {self.set_mega_password()}",
                f"MEGA_FOLDER = '{self.set_mega_folder()}'",
                file=f,
                sep="\n",
            )
