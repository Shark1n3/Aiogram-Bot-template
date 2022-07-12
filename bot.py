from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import logging
import config
import filters
import handlers

async def admin_noify(bot):
    await bot.send_message(config.admin, 'Бот запущен')

async def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(lineno)s - %(name)s - %(message)s')
    logging.error('Starting bot...')
    storage = MemoryStorage()
    bot = Bot(token=config.token)
    dp = Dispatcher(bot, storage=storage)
    handlers.setup(dp)
    filters.setup(dp)
    try:
        await admin_noify(bot)
        await dp.start_polling()
        logging.error('Bot started!')
    except:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

def cli():
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logging.error('Bot Stopped!')

if __name__ == '__main__':
    cli()
