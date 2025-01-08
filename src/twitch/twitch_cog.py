from twitchAPI.chat import ChatMessage, EventData


class TwitchCog:
    def __init__(self, bot):
        self.bot = bot
        self.chat = None
    
    async def on_message(self, msg: ChatMessage) -> None:
        pass

    async def on_ready(self, ready_event: EventData) -> None:
        pass