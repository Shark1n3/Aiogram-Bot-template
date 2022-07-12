from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    async def check(self, m: types.Message) -> bool:
        return m.chat.type == types.ChatType.PRIVATE
