from aiogram import Dispatcher

from .messages import commands, form
from .callbacks import start


def setup_bot_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.include_routers(
        commands.router,
        form.router,
        start.router
    )
