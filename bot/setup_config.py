"""Setup handler module"""

from outputs.outputs import Outputs


class Setup:
    """Setup class, used to initiate the setup if config file is missing or invalid."""

    def __init__(self, filename: str = "config.txt") -> None:
        """Setup class constructor."""
        self._filename: str = filename

    def set_bot_nick(self) -> str:
        return input("Insert BOT NICK: ")

    def set_bot_prefix(self) -> str:
        return input("Insert BOT PREFIX: ")

    def set_gosu_json_url(self) -> str:
        return input("Insert GOSUMEMORY JSON URL: ")

    def set_token(self) -> str:
        return input("Insert TMI TOKEN: ")

    def set_client_id(self) -> str:
        return input("Insert CLIENT ID: ")

    def set_channel(self) -> str:
        return input("Insert STREAMER CHANNEL: ")

    def set_mega_email(self) -> str:
        return input("Insert MEGA EMAIL: ")

    def set_mega_password(self) -> str:
        return input("Insert MEGA PASSWORD: ")

    def set_mega_folder(self) -> str:
        return input("Insert MEGA FOLDER: ")

    def setup_bot(self) -> None:
        """Setup all the settings, writing them in the config file."""
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
