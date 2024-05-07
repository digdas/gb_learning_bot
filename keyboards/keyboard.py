from aiogram import types

button_info = types.KeyboardButton(text='Инфо')
button_kek = types.KeyboardButton(text='Пошути')
button_cat = types.KeyboardButton(text='Пришли котика')



keyboard = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[button_info, button_kek, button_cat]]
)