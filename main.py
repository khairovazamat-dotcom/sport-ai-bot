import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


logging.basicConfig(level=logging.INFO)


async def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN не найден")

    bot = Bot(
        token=token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    @dp.message()
    async def echo(message):
        await message.answer(
            "🤖 Sport AI работает!\n\n"
            "Скоро здесь появится умный анализ матчей ⚽"
        )

    await bot.delete_webhook(drop_pending_updates=True)

    print("Bot started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
