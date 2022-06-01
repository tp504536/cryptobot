from aiogram import types


main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
about = types.KeyboardButton(text='О продукте')
pers_account = types.KeyboardButton(text='Личный кабинет')
main_menu.add(pers_account).add(about)


user_acc = types.ReplyKeyboardMarkup(resize_keyboard=True)
reg = types.KeyboardButton(text='Регистрация')
ent = types.KeyboardButton(text='Вход в лк')
exit = types.KeyboardButton(text='В галвное меню')
user_acc.add(ent).add(reg)