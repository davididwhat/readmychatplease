from utils import install_modules

modules: list = [
    "twitchAPI",
    "dotenv"
]

install_modules(modules)

import asyncio
import os
from datetime import datetime

from twitch import AuthFetch, ReaderCog, TwitchBot, TwitchCog, load_cogs


async def construct_bot() -> TwitchBot:
    auth = AuthFetch()
    auth.load_config()

    config: dict[str, str] = auth.get_config()

    client_id    = config['CLIENT_ID']
    app_secret   = config['APP_SECRET']
    channel_name = config['CHANNEL_NAME']

    bot = TwitchBot(client_id, 
                    app_secret, 
                    channel_name)

    load_cogs(bot)

    return bot

async def main():
    bot = await construct_bot()

    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        await bot.run()
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    asyncio.run(main())