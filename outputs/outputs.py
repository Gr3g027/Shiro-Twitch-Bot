'''Output handler module'''
from outputs.colors import colors


class Outputs():
    '''output class, used to display some text in the terminal'''

    @staticmethod
    def print_message(author: str, message: str) -> None:
        '''prints a chat message to the terminal with colors'''
        print(
            f"{colors['PURPLE']}     {author.capitalize()}: {colors['NO_COLOR']}{message}")

    @staticmethod
    def print_info(to_be_printed: str) -> None:
        '''prints a info message to the terminal with colors'''
        print(f"{colors['CYAN']} [I] {to_be_printed}{colors['NO_COLOR']}")

    @staticmethod
    def print_error(error: str) -> None:
        '''prints an error message to the terminal with colors'''
        print(f"{colors['RED']} [E] {error}{colors['NO_COLOR']}")

    @staticmethod
    def print_warning(warning: str) -> None:
        '''prints an error message to the terminal with colors'''
        print(f"{colors['YELLOW']} [W] {warning}{colors['NO_COLOR']}")

    @staticmethod
    def print_map_request(author: str, message: str) -> None:
        '''prints an osu map request to the terminal with colors'''
        print(f"{colors['GREEN']} [M] {author} requested -> {message}{colors['NO_COLOR']}")

    @staticmethod
    def print_setup(message: str) -> None:
        '''prints a setup message to the terminal with colors'''
        print(f"{colors['GREEN']} [S] {message}{colors['NO_COLOR']}")

    @staticmethod
    def string_map(metadata: dict) -> str:
        '''returns a formatted string for osu maps'''
        # FIXME should not be here
        return (
            f"""/me {metadata['artist']} - {metadata['title']} 
                [{metadata['diff']}] by {metadata['mapper']} | 
                Link: {metadata['url']}
            """
        )
