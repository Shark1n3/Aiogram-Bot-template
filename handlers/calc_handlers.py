from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.reply import menu
from states.main_states import CalcStates
import math

async def start(m: types.Message):
    await m.answer('Привет!👋\nЭто бот-калькулятор, если хочешь просто сложить/вычесть/умножить/поделить выражение то просто напиши мне его. У меня также есть и другие возможности, узнать о них ты можешь в разделе "Помощь"\nВот главное меню:', reply_markup=menu)

async def help(m: types.Message):
    await m.answer('Для того чтобы выполнить простые арифметичские операции (сложение, вычитание, деление, умножение) достаточно просто написать в бота выражение, которое хотите посчитать.\n\nТакже бот может таким же образом возводить в степень число и искать процент от числа, примеры:\n5^2 - цицра 5 во вторую степень\n25%2500 - 25% от 2500')

async def koren(m: types.Message, state: FSMContext):
    await m.answer('Введи число, из которого хочешь извлечь корень')
    await CalcStates.first()

async def koren_answer(m: types.Message, state: FSMContext):
    if not m.text.isdigit():
        await m.answer('Введите число!')
        return
    num = int(m.text)
    result = math.sqrt(num)
    await m.answer(f'Ответ: {round(result, 2)}')
    await state.update_data(koren_result=result)
    await state.finish()

async def kvadr(m: types.Message, state: FSMContext):
    cancel = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text='❌ Отмена', callback_data='cancel')]])
    await m.answer('Включен режим решения квадратного уравнения *ax^2+bx+c=0*\nЧтобы бот смог его решить напишите коэффиценты a, b, c вот так через запятую.\nПример: 2, -5, 1, эти коэффиценты принадлежат уравнению 2x^2-5x+1=0\nЕсли в квадратном уравнении только 2 коэффицента, вместо третьего введи 0', reply_markup=cancel, parse_mode="Markdown")
    await CalcStates.last()

async def kvadr_answer(m: types.Message, state: FSMContext):
    nums = str(m.text).replace(',', ' ').split()
    print(nums)
    if len(nums) < 3:
        await m.answer('Введите все коэффиценты')
        return
    for n in nums:
        if not n.isdigit():
            if not n.__contains__('-'):
                await m.answer('Коэффицент должен быть числом')
                return
    d = (int(nums[1]) ** 2) - 4*(int(nums[0] * int(nums[2])))
    if d < 0:
        await m.answer('Дискриминант отрицательный, решить уравнение невозможно')
        await state.finish()
    x1 = (0 - int(nums[1]) + math.sqrt(float(d))) / 2 * int(nums[0])
    x2 = (0 - int(nums[1]) - math.sqrt(float(d))) / 2 * int(nums[0])
    await m.answer(f'Ответ:\nD = {d}\nX1 = {x1}\nX2 = {x2}')
    await state.finish()


async def answer_calls(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Отменяю...')
    await state.finish()

async def calculating_simple(message: types.Message):
    try:
        if message.text.__contains__('^'):
            nums = str(message.text).replace('^', ' ').split()
            if not nums[0].isdigit():
                await message.answer("Введите число!")
            else:
                res = int(str(nums[0])) ** int(str(nums[1]))
                await message.answer(f'Ответ: {res}')
        elif message.text.__contains__('%'):
            nums = str(message.text).replace('%', ' ').split()
            result = int(str(nums[1])) / 100 * int(str(nums[0]))
            await message.answer(f'Ответ: {str(round(result))}')
        else:
            result = eval(str(message.text).replace(' ', ''))
            await message.answer(f'{message.text}={result}')
    except:
        await message.answer('Введенный текст не содержит выражение')
