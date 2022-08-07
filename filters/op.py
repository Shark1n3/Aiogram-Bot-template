from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from data.db_main import DBWorker


db = DBWorker()

class OPFilter(BoundFilter):
    async def check(self, m: types.Message) -> bool:
        chats = db.get_op_on()
        for chat in chats:
            chat_user = await m.bot.get_chat_member(chat_id=chat[2], user_id=m.from_user.id)
            if chat_user['status'] == 'left':
                op_kb = types.InlineKeyboardMarkup(row_width=1)
                for ch in chats:
                    op_kb.add(types.InlineKeyboardButton(text='Подписаться', url=f'{ch[1]}'))
                op_kb.add(types.InlineKeyboardButton(text='✅ Проверить подписку', callback_data='check_sub'))
                await m.answer('Подпишитесь на спонсоров нашего бота, благодаря этому бот может оставаться бесплатным ❤️', reply_markup=op_kb)
                raise StopIteration
                return False
        return True