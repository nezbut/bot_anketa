from aiogram import Dispatcher

from .messages import commands


def setup_bot_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.include_routers(
        commands.router,
    )
