"""
    Made by Monnapse
"""

import socket
from threading import Thread

class new:
    def __init__(self, port: int=5000) -> None:
        # SOCKET SETTINGS
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('localhost', port))
        self.server_socket.listen()

        #
        self.clients = []

    def send_data(self, data: str):
        for i in self.clients:
            i.send(bytes(data, "utf-8"))

    def connect_clients(self):
        t = Thread(target=self.clients_loop)
        t.start()

    def clients_loop(self):
         while True:
            c, addr = self.server_socket.accept()
            self.clients.append(c)