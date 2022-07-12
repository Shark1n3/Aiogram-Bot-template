from aiogram import Dispatcher
from .private import IsPrivate

def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)