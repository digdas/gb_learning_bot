from aiogram import Router, types
from aiogram.filters.command import Command

from keyboards import keyboard
from Joking import random_joke

router = Router()


@router.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.answer(
        f'Hello {message.from_user.full_name}! Please, use /info command',
        reply_markup=keyboard.keyboard
    )

@router.message(Command(commands=["info"]))
async def info(message: types.Message):
    await message.answer(f'Все что я умею - шутить и присылать котиков.'
                         f'Пришли команду /kek или /cat или используй клавиатуру.')

@router.message(Command(commands=["kek"]))
async def kek(message: types.Message):
    await message.answer(f'{random_joke()}')
