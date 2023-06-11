from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from cash.cash import rubles
from aiogram import types


@dp.message_handler(Command("Выйти"))
async def on_start_test(message: types.Message):
    await message.answer("Досвиания, на вашем счёте", rubles, reply_markup=ReplyKeyboardRemove())
