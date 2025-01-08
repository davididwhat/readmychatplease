from datetime import datetime

from twitchAPI.chat import ChatMessage, EventData

from twitch.twitch_cog import TwitchCog


class ReaderCog(TwitchCog):
    async def on_message(self, msg: ChatMessage) -> None:
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{timestamp} | {msg.user.name}: {msg.text}")

    async def on_ready(self, ready_event: EventData) -> None:
        [await ready_event.chat.join_room(self.bot.target_channel)]
        print(f"Joined room: {self.bot.target_channel}")