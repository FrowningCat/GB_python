from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b0 = KeyboardButton("/Выйти")
b1 = KeyboardButton("/Пополнить")
b2 = KeyboardButton("/Снять")

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(b0).row(b1, b2)
