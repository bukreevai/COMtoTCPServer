from socketserver import ThreadingTCPServer, BaseRequestHandler
# import logging


class SerialRequestandler(BaseRequestHandler):
    def handle(self) -> None:
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


class TCPSerialServer(ThreadingTCPServer):
    pass
