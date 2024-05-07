from aiogram import Router, types
from aiogram.filters.command import Command

from cats import get_cats

router = Router()

@router.message(Command(commands=["cat"]))
async def cat(message: types.Message):
    cat_image = await get_cats.get_cat_image()
    await message.answer_photo(cat_image)
