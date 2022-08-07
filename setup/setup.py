'''Setup module'''
from outputs.outputs import Outputs

from os import environ
from dotenv import load_dotenv

class Setup():
    '''Setup class, handles the setup'''

    def __init__(self) -> None:
        self.outputs = Outputs()
        self.start()

    def start(self) -> None:
        self.outputs.print_setup("--- SETUP ---")

        # run the setups
        tw_cfg = self.setup_twitch()
        osuirc_cfg = self.setup_osuirc()
        gosu_cfg = self.setup_gosuurl()
        mega_cfg = self.setup_mega()
        social_cfg = self.setup_social()

        env = open(".env", "w")
        configs = (f'''
# TWITCH configs
TMI_TOKEN = {tw_cfg.get("TMI_TOKEN")}
CLIENT_ID = {tw_cfg.get("CLIENT_ID")}
BOT_NICK = {tw_cfg.get("BOT_NICK")}
BOT_PREFIX = {tw_cfg.get("BOT_PREFIX")}
CHANNEL = {tw_cfg.get("CHANNEL")}

# OSU configs
IRC_SERVER = {osuirc_cfg.get("IRC_SERVER") or "irc.ppy.sh"}
IRC_PORT = {osuirc_cfg.get("IRC_PORT") or 6667}
IRC_NAME = {osuirc_cfg.get("IRC_NAME")}
IRC_PASS = {osuirc_cfg.get("IRC_PASS")}
OSU_PROFILE = {osuirc_cfg.get("OSU_PROFILE") or f'https://osu.ppy.sh/users/{osuirc_cfg.get("IRC_NAME")}'}

# GOSU url
GOSUMEMORY_JSON_URL = {gosu_cfg or "http://127.0.0.1:24050/json"}

# MEGA configs
MEGA_EMAIL = {mega_cfg.get("MEGA_EMAIL")}
MEGA_PASSWORD = {mega_cfg.get("MEGA_PASSWORD")}
MEGA_FOLDER = '{mega_cfg.get("MEGA_FOLDER")}'

# SOCIAL configs
TWITTER = {social_cfg.get("TWITTER")}
INSTAGRAM = {social_cfg.get("INSTAGRAM")}
DISCORD_SERVER = {social_cfg.get("DISCORD_SERVER")}
        ''')
        env.write(configs)
        env.close()

    def setup_twitch(self) -> dict:
        self.outputs.print_setup("- TWITCH SETUP")
        return {
            "TMI_TOKEN": input("TMI TOKEN : ").strip(),
            "CLIENT_ID": input("CLIENT ID : ").strip(),
            "BOT_NICK": input("BOT NICKNAME : ").strip(),
            "BOT_PREFIX": input("BOT PREFIX : ").strip(),
            "CHANNEL": input("CHANNEL : ").strip()
        }
    
    def setup_osuirc(self) -> dict:
        self.outputs.print_setup("- OSU IRC SETUP")
        return {
            "IRC_SERVER": input("IRC SERVER : ").strip(),
            "IRC_PORT": input("IRC PORT : ").strip(),
            "IRC_NAME": input("IRC NICKNAME : ").strip(),
            "IRC_PASS": input("IRC PASS : ").strip(),
            "OSU_PROFILE": input("OSU PROFILE : ").strip()
        }

    def setup_gosuurl(self) -> str:
        self.outputs.print_setup("- GOSUMEMORY SETUP")
        return input("GOSUMEMORY URL : ").strip()
    
    def setup_mega(self) -> dict:
        self.outputs.print_setup("- MEGA SETUP")
        return {
            "MEGA_EMAIL": input("MEGA EMAIL : ").strip(),
            "MEGA_PASSWORD": input("MEGA PASSWORD : ").strip(),
            "MEGA_FOLDER": input("MEGA FOLDER : ").strip()
        }
    
    def setup_social(self) -> dict:
        self.outputs.print_setup("- SOCIAL SETUP")
        return {
            "TWITTER": input("TWITTER PROFILE : ").strip(),
            "INSTAGRAM": input("INSTAGRAM PROFILE : ").strip(),
            "DISCORD_SERVER": input("DISCORD SERVER : ").strip()
        }