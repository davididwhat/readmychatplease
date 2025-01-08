import asyncio

from twitchAPI.chat import Chat, ChatMessage, EventData
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope, ChatEvent


class TwitchBot:
    def __init__(self, app_id: str, app_secret: str, target_channel: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self.target_channel = target_channel
        self.user_scope = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT, AuthScope.CHANNEL_MANAGE_BROADCAST]
        self.twitch = None
        self.chat = None
        self.cogs = {}

    def add_cog(self, cog_class):
        cog = cog_class(self)
        self.cogs[cog_class.__name__] = cog
        return cog

    async def handle_message(self, msg: ChatMessage) -> None:
        for cog in self.cogs.values():
            await cog.on_message(msg)

    async def handle_ready(self, ready_event: EventData) -> None:
        for cog in self.cogs.values():
            await cog.on_ready(ready_event)

    async def setup(self):
        self.twitch = await Twitch(self.app_id, self.app_secret)
        auth = UserAuthenticator(self.twitch, self.user_scope)
        token, refresh_token = await auth.authenticate()
        await self.twitch.set_user_authentication(token, self.user_scope, refresh_token)

        self.chat = await Chat(self.twitch)
        self.chat.register_event(ChatEvent.READY, self.handle_ready)
        self.chat.register_event(ChatEvent.MESSAGE, self.handle_message)

    async def run(self):
        await self.setup()
        self.chat.start()

        while True:
            await asyncio.sleep(1)