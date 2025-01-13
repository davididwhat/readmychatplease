import os
from datetime import datetime

from twitchAPI.chat import ChatMessage, EventData

from twitch.twitch_cog import TwitchCog
from utils import VarFetch


class ReaderCog(TwitchCog):
    def __init__(self, bot):
        super().__init__(bot)
        self.logs_file: str 

        cfg = VarFetch()
        cfg.load_config(keys=['TEMP_FILE'])
        self.temp_file = cfg.config()['TEMP_FILE']

    async def on_ready(self, ready_event: EventData) -> None:
        [await ready_event.chat.join_room(self.bot.target_channel)]

        open(self.temp_file, 'w').close()

        try:
            files = os.listdir("./logs")
        except FileNotFoundError:
            os.mkdir("./logs")
            files = os.listdir("./logs")

        today_date = datetime.now().strftime("%d_%m_%Y")
        today_filename = f"{today_date}.txt"

        if today_filename in files:
            with open(f"./logs/{today_filename}", 'a') as logs:
                print(f"\n\nNew Session @ {datetime.now().strftime('%H%M%S')}\n\n", file=logs)
        else:
            with open(f"./logs/{today_filename}", 'a') as logs:
                print(f"Logs @ {today_date}\n\n", file=logs)
        
        self.logs_file = f"./logs/{today_filename}"
                
        print(f"Joined room: {self.bot.target_channel}")

    async def on_message(self, msg: ChatMessage) -> None:
        timestamp = datetime.now().strftime("%H:%M:%S")

        with open(self.logs_file, 'a', encoding='utf-8') as logs:
            print(f"{timestamp} | {msg.user.name}: {msg.text}", file=logs)

        with open(self.temp_file, 'a', encoding='utf-8') as temp:
            print(f"{timestamp} | {msg.user.name}: {msg.text}", file=temp)