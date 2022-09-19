"""
Module for work with TCPServer
Start on port from confog file.
Connect to Serial port after client connect.
"""
import threading
import socketserver
from typing import Dict

import socket


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    Class for proccessing TCP requests
    """
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TCPSerialServer:
    """
    Class for share serial port to TCP port
    """
    def __init__(self, config: Dict) -> None:
        self.host = config.get('host')
        self.port = config.get('port')
        self.serial_id = config.get('com_id')
        self.__server__ = ThreadedTCPServer(
            (self.host, self.port), ThreadedTCPRequestHandler
        )
        self.__server_thread__: threading.Thread = None

    def start(self):
        """
        Run TCP Server
        """
        self.__server_thread__ = threading.Thread(
            target=self.__server__.serve_forever)
        self.__server_thread__.daemon = True
        self.__server_thread__.start()

    def stop(self):
        """
        Stop TCP Server
        """
        self.__server__.shutdown()


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 8989

    config = {
        'host': 'localhost',
        'port': 8989,
        'com_id': '/dev/tty1',
        'log_level': 'DEBUG'
    }

    tcp_server = TCPSerialServer(config)
    tcp_server.start()

    ip, port = tcp_server.__server__.server_address
    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")

    tcp_server.stop()
