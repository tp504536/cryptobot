import string
import logging
from datebase import Sql
from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

storage = MemoryStorage()
bot = Bot(token='5057922863:AAG-yNGdoo5lzf4bgwIMnRDTQ27XsuqKvBY')
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
db = Sql('datebase.db')

class FMSregis(StatesGroup):
    reg = State()


class FMSlogin(StatesGroup):
    login = State()


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer('hello', reply_markup=main_menu)


@dp.message_handler(content_types='text')
async def message(message: types.Message):
    if message.text == 'Личный кабинет':
        await message.answer('text', reply_markup=user_acc)
    elif message.text == 'О продукте':
        await message.answer('text')
    elif message.text == 'Вход в лк':
        await message.answer('Пароль от аккунта: ')
    elif message.text == 'Регистрация':
        await message.answer('Придумайте логин!')
        await FMSlogin.login.set()


@dp.message_handler(content_types='text', state=FMSlogin.login)
async def sub(message: types.Message, state: FSMContext):
    global login
    async with state.proxy() as login:
        login['text'] = message.text
        await state.finish()
        await message.answer('пароль должен содержать не менее 6 символов из списка a-z, 0-9 $')
        await FMSregis.reg.set()


@dp.message_handler(content_types='text', state=FMSregis.reg)
async def sub(message: types.Message, state: FSMContext):
    async with state.proxy() as reg:
        reg['text'] = message.text
        await state.finish()
        up_case = any(1 if i in string.ascii_uppercase else 0 for i in reg['text'])
        low_case = any(1 if i in string.ascii_lowercase else 0 for i in reg['text'])
        special = any(1 if i in string.punctuation else 0 for i in reg['text'])
        if up_case == True and low_case == True and special == True:
            print(up_case, low_case, special)
            if not db.reg_user(message.from_user.id,login['text'],reg['text']):
                db.add_reg_user(message.from_user.id,login['text'],reg['text'])
                await message.answer(
                    'Ваш данные для входа:\n' + 'Логин: ' + login['text'] + '\nпароль:' + ' ' + reg['text'])
        else:
            await message.answer('Пароль не достаточно надежный, поробуй еще раз!')
            print(up_case, low_case, special)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
