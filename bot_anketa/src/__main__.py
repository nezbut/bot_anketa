import asyncio

from bot_anketa.src.di import get_di_container


async def main() -> None:
    container = get_di_container()


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()
