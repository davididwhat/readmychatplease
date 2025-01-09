from utils import install_modules

modules: list = [
    "twitchAPI",
    "dotenv",
]

install_modules(modules)

import asyncio
import os
from datetime import datetime

from twitchAPI.type import AuthScope

from twitch import AuthFetch, TwitchBot, load_cogs


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

# import threading
# import time
# from queue import Queue

# from pub import Publisher
# from sub import Subscriber


# def main():
#     # Create a shared Queue
#     shared_queue = Queue()

#     # Initialize Publisher and Subscriber
#     publisher = Publisher(queue=shared_queue, topic="updates", interval=1)
#     subscriber = Subscriber(queue=shared_queue, topic_filter="updates")

#     # Start Subscriber first to ensure it starts listening before publisher sends messages
#     subscriber.start()
#     publisher.start()

#     try:
#         # Keep the main thread alive while publisher and subscriber run
#         while True:
#             time.sleep(0.1)
#     except KeyboardInterrupt:
#         print("\nInterrupt received! Stopping publisher and subscriber...")
#         publisher.stop()
#         subscriber.stop()

#     # Wait for both threads to finish
#     publisher.join()
#     subscriber.join()
#     print("Publisher and Subscriber have been stopped gracefully.")

# if __name__ == "__main__":
#     main()


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