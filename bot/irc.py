'''Irc module'''
import socket
from outputs.outputs import Outputs

class Irc():
    '''Irc class, handles the map request system'''

    irc_socket = socket.socket()

    def __init__(self, server='', port=0, irc_name='', irc_pass=''):
        '''Irc class constructor'''

        self.outputs = Outputs()
        self.irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.irc_socket.connect((server, port))
        self.outputs.print_info(f'Connected to {server} IRC server')

        self.irc_socket.send(bytes(f"PASS {irc_pass}\n", "UTF-8"))
        self.irc_socket.send(bytes(f"USER {irc_name} {irc_name} {irc_name} :{irc_name}\n", "UTF-8"))
        self.irc_socket.send(bytes(f"NICK {irc_name}\n", "UTF-8"))
        self.irc_socket.send(bytes(f"JOIN #osu\n", "UTF-8"))
        # super().__init__(server=server, port=port, irc_name=irc_name, irc_pass=irc_pass)
    
    async def send_irc(self, channel, msg):
        self.irc_socket.send(bytes(f"PRIVMSG {channel} {msg} \n", "UTF-8"))

    async def response_irc(self):
        res = self.irc_socket.recv(2040).decode("UTF-8")
        if res.find('PING') != -1:
            self.irc_socket.send(bytes(f'PONG {res.split().decode("UTF-8") [1]} \r\n', "UTF-8"))
        return res
    
    # async def check_response(self):
    #     while True:
    #         await self.response_irc(self)
