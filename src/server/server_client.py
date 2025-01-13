import socket


class ServerClient:
    def __init__(self, host: str, port: int | str, *args):
        self.host = host 
        self.port = port if isinstance(port, int) else int(port)
        self.socket_args = args
        self.s = None

    def connect_to_server(self):
        self.s = socket.socket(*self.socket_args)
        self.s.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

    def send(self, message: str):
        if self.s:
            self.s.sendall(message.encode())

    def close_connection(self):
        if self.s:
            self.s.close()
            print("Connection closed.")