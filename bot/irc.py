'''Irc module'''
import socket
from outputs.outputs import Outputs

class Irc():
    '''Irc class, handles the map request system'''
    
    def __init__(self, server='irc.ppy.sh', port=6667, irc_name='', irc_pass=''):
        '''Irc class constructor'''
        self.outputs = Outputs()
        self.server = server
        self.port = port
        self.irc_name = irc_name
        self.irc_pass = irc_pass
    
    def irc_connect(self):
        self.irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc_socket.connect((self.server, self.port))
        self.outputs.print_info(f'Connected to {self.server} IRC server')

        self.irc_socket.send(
            bytes(
                f"""
                PASS {self.irc_pass}\n
                USER {self.irc_name} {self.irc_name} {self.irc_name} :{self.irc_name}\n
                NICK {self.irc_name}\n
                """, "UTF-8"
            )
        )

        self.data_handler()
    
    def irc_disconnect(self):
        self.irc_socket.close()
    
    def privmsg(self, channel, msg):
        self.irc_socket.send(bytes(f"PRIVMSG {channel} {msg} \n", "UTF-8"))
    
    def handle_ping(self, data):
        self.irc_socket.send(bytes(f"PONG {data.split()[1]}\n", "UTF-8"))
        self.outputs.print_info(f"PING request handled!")
    
    def is_ping_req(self, data) -> bool:
        if data.find('PING') != -1:
            return True

    def data_handler(self):
        while True:
            data = self.irc_socket.recv(2040).decode("UTF-8")
            if self.is_ping_req(data):
                self.handle_ping(data)

