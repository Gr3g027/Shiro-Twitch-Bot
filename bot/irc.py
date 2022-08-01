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

        self.irc_socket.send(bytes(f"PASS {self.irc_pass}\n", "UTF-8"))
        self.irc_socket.send(bytes(f"USER {self.irc_name} {self.irc_name} {self.irc_name} :{self.irc_name}\n", "UTF-8"))
        self.irc_socket.send(bytes(f"NICK {self.irc_name}\n", "UTF-8"))

        self.handle_ping()
    
    def irc_disconnect(self):
        self.irc_socket.close()
    
    def privmsg(self, channel, msg):
        self.irc_socket.send(bytes(f"PRIVMSG {channel} {msg} \n", "UTF-8"))

    def handle_ping(self):
        while True:
            res = self.irc_socket.recv(2040).decode("UTF-8")
            if res.find('PING') != -1:
                ping_res = f'PONG {res.split()[1]}'
                self.irc_socket.send(bytes(f"{ping_res}\n", "UTF-8"))
                self.outputs.print_info(f"PING REQUEST HANDLED (sent: {ping_res})")

