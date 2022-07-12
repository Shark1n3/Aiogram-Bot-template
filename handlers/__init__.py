from aiogram import Dispatcher
from .calc_handlers import start, help, calculating_simple, koren, koren_answer, kvadr, answer_calls, kvadr_answer
from filters.private import IsPrivate
from states.main_states import CalcStates

def setup(dp: Dispatcher):
    dp.register_message_handler(start, IsPrivate(), commands=['start'])
    dp.register_message_handler(help, text=['❔ Помощь'])
    dp.register_message_handler(koren, text=['Вынести корень'])
    dp.register_message_handler(koren_answer, state=CalcStates.koren)
    dp.register_message_handler(kvadr, text=['Квадратное уравнение'])
    dp.register_message_handler(kvadr_answer, state=CalcStates.kvadr)
    dp.register_callback_query_handler(answer_calls, state=CalcStates.kvadr)
    dp.register_message_handler(calculating_simple)
