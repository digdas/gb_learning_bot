import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import common, msg

from config import token


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token)
    dp = Dispatcher()
    dp.include_router(common.router)
    dp.include_router(msg.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
