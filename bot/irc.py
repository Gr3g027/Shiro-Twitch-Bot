'''Irc module'''
import socket
from outputs.outputs import Outputs

class Irc():
    '''Irc class, handles the map request system'''
    
    def __init__(self, server='irc.ppy.sh', port=6667, name='', bancho_pass=''):
        '''Irc class constructor'''
        self.outputs = Outputs()
        self.server = server
        self.port = port
        self.name = name
        self.bancho_pass = bancho_pass

        self.bancho_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def bancho_connect(self):
        self.bancho_socket.connect((self.server, self.port))
        self.outputs.print_info(f'Connected to {self.server} IRC server')

        self.bancho_socket.send(bytes(f"PASS {self.bancho_pass}\n", "UTF-8"))
        self.bancho_socket.send(bytes(f"USER {self.name} {self.name} {self.name} :{self.name}\n", "UTF-8"))
        self.bancho_socket.send(bytes(f"NICK {self.name}\n", "UTF-8"))

        self.privmsg(self.name, "Ready to process requests!")

        self.data_handler()
    
    def bancho_disconnect(self):
        self.bancho_socket.close()

    def is_connected(self) -> bool:
        try:
            self.bancho_socket.send(bytes("\n", "UTF-8"))
            return True
        except:
            return False
    
    def privmsg(self, channel, msg):
        self.bancho_socket.send(bytes(f"PRIVMSG {channel} {msg} \n", "UTF-8"))
    
    def handle_ping(self, data):
        self.bancho_socket.send(bytes(f"PONG {data.split()[1]}\n", "UTF-8"))
        # self.outputs.print_info(f"PING request handled!")
    
    def is_ping_req(self, data) -> bool:
        if data.find('PING') != -1:
            return True

    def data_handler(self):
        while True:
            data = self.bancho_socket.recv(2040).decode("UTF-8")
            if self.is_ping_req(data):
                self.handle_ping(data)
            

