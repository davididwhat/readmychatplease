from utils import install_modules

modules: list = [
    "twitchAPI",
    "dotenv"
]

install_modules(modules)

import asyncio
import os
from datetime import datetime

from twitchAPI.type import AuthScope

from twitch import AuthFetch, ReaderCog, TwitchBot, TwitchCog, load_cogs


async def construct_bot() -> TwitchBot:
    auth = AuthFetch()
    auth.load_config()

    config: dict[str, str] = auth.get_config()
    client_id    = config['CLIENT_ID']
    app_secret   = config['APP_SECRET']
    channel_name = config['CHANNEL_NAME']

    scopes = [
        AuthScope.CHAT_READ,
        AuthScope.CHAT_EDIT,
        AuthScope.CHANNEL_MANAGE_BROADCAST
    ]

    bot = TwitchBot(
        app_id          = client_id, 
        app_secret      = app_secret, 
        target_channel  = channel_name,
        user_scope      = scopes
    )

    return bot

async def main():
    bot = await construct_bot()
    
    await load_cogs(bot)

    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        await bot.run()
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    asyncio.run(main())