from typing import Tuple

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage

from redis.asyncio import Redis

from dishka import Provider, Scope, provide

from bot_anketa.src.config import Settings
from bot_anketa.src.handlers import setup_bot_handlers


class TGBotProvider(Provider):
    scope = Scope.APP

    @provide
    def get_bot(self, settings: Settings) -> Bot:
        token = settings.tg_bot_token
        return Bot(token=token)


class DispatcherProvider(Provider):
    scope = Scope.APP

    @provide
    def get_dp(self, storage: BaseStorage) -> Dispatcher:
        dp = Dispatcher(storage=storage)
        setup_bot_handlers(dp)

        return dp

    @provide
    def get_storage(self, settings: Settings, redis: Redis) -> BaseStorage:
        if settings.kv_database_uri == "memory":
            return MemoryStorage()
        return RedisStorage(redis=redis)


def get_tgbot_providers() -> Tuple[Provider, ...]:
    return (
        TGBotProvider(),
        DispatcherProvider()
    )
