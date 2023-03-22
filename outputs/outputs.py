'''Output handler module'''
from outputs.colors import colors
from utils.utils import format_msg


class Outputs():
    '''output class, used to display some text in the terminal'''

    @staticmethod
    def print_message(message: str, lenght_author = 0,  author = "") -> None:
        '''prints a chat message to the terminal with colors'''
        str_autor_len = ' ' * (lenght_author)
        spaces_new_line = ' ' * (lenght_author + 7)
        if author:
            print(f"{colors['PURPLE']}     {author.capitalize()}: {colors['NO_COLOR']}{format_msg(message, spaces_new_line)}")
        else:
            print(f"{colors['PURPLE']}     {str_autor_len}-: {colors['NO_COLOR']}{format_msg(message, spaces_new_line)}")

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
        '''prints a warning message to the terminal with colors'''
        print(f"{colors['YELLOW']} [W] {warning}{colors['NO_COLOR']}")

    @staticmethod
    def print_map_request(author: str, message: str) -> None:
        '''prints an osu map request to the terminal with colors'''
        print(f"{colors['GREEN']} [M] {author} requested -> {message}{colors['NO_COLOR']}")

    @staticmethod
    def print_setup(message: str) -> None:
        '''prints a setup message to the terminal with colors'''
        print(f"{colors['GREEN']} [S] {message}{colors['NO_COLOR']}")
