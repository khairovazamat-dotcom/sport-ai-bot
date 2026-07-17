import os
import asyncio
import logging

from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from football_api import get_fixtures


logging.basicConfig(level=logging.INFO)


async def health(request):
    return web.Response(text="Sport AI is alive")


async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.getenv("PORT", 10000))

    site = web.TCPSite(
        runner,
        "0.0.0.0",
        port
    )

    await site.start()

    logging.info(
        f"Web server started on port {port}"
    )


async def main():

    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError(
            "BOT_TOKEN не найден"
        )

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
            "Render подключен ✅\n"
            "AI анализ матчей скоро вернём ⚽"
        )


    await bot.delete_webhook(
        drop_pending_updates=True
    )

    logging.info(
        "Starting web server..."
    )

    await start_web_server()

    logging.info(
        "Web server OK"
    )

    logging.info(
        "Bot started"
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
