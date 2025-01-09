import os

from twitch import ReaderCog, TwitchBot, TwitchCog

cogs: list = [
    ReaderCog
]

async def load_cogs(bot: TwitchBot) -> list[TwitchCog]:
    for cog in cogs:
        bot.add_cog(cog)