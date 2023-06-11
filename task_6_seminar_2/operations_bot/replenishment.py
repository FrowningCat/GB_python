from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from cash.cash import rubles
from aiogram import types

rubles_mas = []


@dp.message_handler(Command("Пополнить"))
async def on_start_test(message: types.Message):
    await message.answer("На какую сумму хотите пополнить баланс?", reply_markup=ReplyKeyboardRemove())
    rubles_mas.append(message.text)
    rubles = [int(item) for item in rubles_mas]
    rubles = sum(rubles) - 50
    await message.answer("Ваш балланс: ", rubles)
