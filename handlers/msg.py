from aiogram import Router, types, F
from handlers import common, cat

router = Router()

@router.message(F.text)
async def find_commands(message: types.Message):
    msg = message.text.lower()
    if 'info' in msg:
        await common.info(message)
    elif 'инфо' in msg:
        await common.info(message)
    elif 'joke' in msg:
        await common.kek(message)
    elif 'пошути' in msg:
        await common.kek(message)
    elif 'шути' in msg:
        await common.kek(message)
    elif 'котик' in msg:
        await cat.cat(message)
    elif 'киса' in msg:
        await cat.cat(message)
    elif 'Пришли котика' in msg:
        await cat.cat(message)

@router.message(F.text)
async def msg(message: types.Message):
    msg = message.text.lower()
    if 'тупой' in msg:
        await message.reply(f'Сам такой!')
    elif 'дурак' in msg:
        await message.reply(f'От дурака слышу!')
    else:
        await message.reply(f'Я пока не понимаю человеческую речь, используй команды!')
