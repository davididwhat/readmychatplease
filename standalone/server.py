import asyncio
import os
import socket
import textwrap

try:
    import twitchAPI
except ImportError:
    os.system('pip install twitchAPI')

from twitchAPI.helper import first
from twitchAPI.twitch import Twitch


class Server:
    def __init__(self, *args):
        self.host = self._get_local_ip(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = 5000
        self.s = socket.socket(*args)
        self.s.bind((self.host, self.port))
        self.s.setblocking(False)

    def _get_local_ip(self, *args):
        s = socket.socket(*args)
        s.settimeout(0)
        try:
            s.connect(('10.254.254.254', 1))
            local_ip = s.getsockname()[0]
        except Exception:
            local_ip = '127.0.0.1'
        finally:
            s.close()
        
        return local_ip

    async def start(self):
        with self.s as s:
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")
            loop = asyncio.get_event_loop()
            conn, addr = await loop.sock_accept(s)
            print(f"Connected by: {addr}")
            while True:
                data = await loop.sock_recv(conn, 1024) 
                if not data:
                    break
                print(f"{self._format_text(data.decode())}")

    def _format_text(self, text, line_length=50):
        return "\n".join(textwrap.wrap(text, width=line_length))
    

class TwitchViews:
    def __init__(self):
        try:
            with open('my_auth.txt', 'r', encoding='utf-8') as authfile:
                auth = authfile.readlines()
        except FileNotFoundError:
            with open('./standalone/my_auth.txt', 'r', encoding='utf-8') as authfile:
                auth = authfile.readlines()
        except Exception as e:
            print("Error: missing my_auth.txt, can't read auth")

        self.client_id  = auth[0].replace("client_id=", "").replace("\n", "")
        self.app_secret: str = auth[1].replace("app_secret=", "").replace("\n", "")
        self.channel_name: str = auth[2].replace("channel_name=", "").replace("\n", "")

    async def _get_viewer_count(self):
        twitch = await Twitch(self.client_id, self.app_secret)
        stream = await first(twitch.get_streams(user_login=self.channel_name))

        if stream is not None:
            viewer_count = stream.viewer_count
            await twitch.close()
            return viewer_count
        else:
            await twitch.close()
            return "Channel is offline."
        
    async def show_viewers(self):
        while True:
            views = await self._get_viewer_count()
            try:
                with open("status.txt", 'r+', encoding='utf-8') as file:
                    last_views = file.read().strip()
                    if str(views) != last_views:
                        file.seek(0)
                        file.write(str(views))
                        file.truncate()
                        viewer_message = f"-----====| {views} |====-----"
                        print(viewer_message)
            except FileNotFoundError:
                with open("status.txt", 'w', encoding='utf-8') as file:
                    file.write(str(views))

            await asyncio.sleep(10)


async def main():
    server = Server(socket.AF_INET, socket.SOCK_STREAM)
    twitch_views = TwitchViews() 

    task1 = asyncio.create_task(server.start())
    task2 = asyncio.create_task(twitch_views.show_viewers())

    await task1
    await task2

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    asyncio.run(main())


    