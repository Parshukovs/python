import socket
import datetime
import psutil
from collections import namedtuple

class Server ():
    def __init__ (self, server_addr, port, timeout = None):
        self.server_addr = server_addr
        self.port = port
        self.timeout = timeout
    
    def send (self):
        with socket.create_connection((self.server_addr, self.port), self.timeout) as sock:
            data = str(psutil.cpu_percent()) + " " + str(psutil.virtual_memory().used)
            sock.send(bytes(data,"UTF-8"))
            print ("Data sent")
            answer = sock.recv(1024)
            if answer:
                print (answer)
            if answer != "OK":
                #тут будет обработка ошибок. Когда-нибудь.
                pass

if __name__ == "__main__":
    home = Server ("localhost", 9090, 5)
    home.send()