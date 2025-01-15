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
            
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1)) 
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'  
    finally:
        s.close()
    return local_ip

HOST = get_local_ip() 

if __name__ == "__main__":
    HOST = get_local_ip() 
    PORT: int | str = 5000

    os.system('cls' if os.name == 'nt' else 'clear')
    server = Server(HOST, PORT, socket.AF_INET, socket.SOCK_STREAM)
    server.start()