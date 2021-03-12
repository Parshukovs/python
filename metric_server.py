import socket
import datetime
import os

def server_start():
    with socket.socket() as port:
        port.bind(("", 9090))
        port.listen()

        while True:
            conn, addr = port.accept()
            with conn:
                data = conn.recv(1024)
                print (data.decode())
                if not data:
                    break

server_start()