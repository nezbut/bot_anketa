from typing import Tuple

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder

from redis.asyncio import Redis

from dishka import Provider, Scope, AsyncContainer, provide

from src.handlers import setup_bot_handlers


class TGBotProvider(Provider):
    scope = Scope.APP

    @provide
    def get_bot(self, settings: TgSettings) -> Bot:
        pass


class DispatcherProvider(Provider):
    scope = Scope.APP

    @provide
    def get_dp(self, storage: BaseStorage, container: AsyncContainer) -> Dispatcher:
        dp = Dispatcher(storage=storage)

        setup_bot_handlers(dp)

        return dp

    @provide
    def get_storage(self, redis: Redis) -> BaseStorage:
        pass


def get_tgbot_providers() -> Tuple[Provider, ...]:
    return (
        TGBotProvider(),
        DispatcherProvider()
    )
