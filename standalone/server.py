import os
import socket


class Server:
    def __init__(self, host: str, port: int | str, *args):
        self.host = host 
        self.port = port if isinstance(port, int) else int(port)
        self.s = socket.socket(*args)
        self.s.bind((self.host, self.port))

    def start(self):
        with self.s as s:
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")
            conn, addr = s.accept()
            print(f"Connected by: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"{data.decode()}")

if __name__ == "__main__":
    '''
    Change these to what you please

    If you don't know what to do, you can do this:
    
    HOST = "0.0.0.0"
    PORT = 5000
    '''
    HOST: str       = "0.0.0.0"
    PORT: int | str = 5000

    os.system('cls' if os.name == 'nt' else 'clear')
    server = Server(HOST, PORT, socket.AF_INET, socket.SOCK_STREAM)
    server.start()