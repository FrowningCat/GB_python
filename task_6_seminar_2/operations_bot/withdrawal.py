from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from cash.cash import rubles
from aiogram import types

rubles_mas = []


@dp.message_handler(Command("Снять"))
async def on_start_test(message: types.Message):
    await message.answer("Какую сумму хотите снять?", reply_markup=ReplyKeyboardRemove())
    rubles_mas.append(message.text)
    withdeawal_ru = [int(item) for item in rubles_mas]
    withdeawal_ru = sum(withdeawal_ru) - 50
    if withdeawal_ru > rubles:
        await message.answer("Вы хотите снят больше чем имеете")
    else:
        percent = (withdeawal_ru * 1.5) * 100
        if percent < 30:
            percent = 30
        elif percent > 600:
            percent = 600
        await message.answer("У вас осталось", rubles - percent)
