from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from config import admin

class Admin(BoundFilter):
    async def check(self, m: types.Message) -> bool:
        return m.from_user.id is admin