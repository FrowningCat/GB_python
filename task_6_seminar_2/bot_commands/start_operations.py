from aiogram.dispatcher.filters import Command
from loader import dp
from keyboard.operations import kb
from aiogram import types


@dp.message_handler(Command("start_operations"))
async def on_start_test(message: types.Message):
    await message.answer("Что вы хотите сделать?", reply_markup=kb)
