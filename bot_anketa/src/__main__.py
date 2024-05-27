import asyncio
import logging

from dishka.integrations.aiogram import setup_dishka

from aiogram import Bot, Dispatcher

from bot_anketa.src.di import get_di_container
from bot_anketa.src.config import Settings

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    container = get_di_container()

    bot = await container.get(Bot)
    dp = await container.get(Dispatcher)
    settings = await container.get(Settings)

    setup_dishka(container, dp, auto_inject=True)

    try:
        await dp.start_polling(bot, container=container, settings=settings)
    finally:
        logger.info("BOT STOPPED...")


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()
