import logging
from typing import Union
from aiogram import Bot


async def subscribe(user_id, channel_id: Union[str, int]):
    bot = Bot.get_current()
    logging.info(channel_id)
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel_id)
    return member.is_chat_member()
