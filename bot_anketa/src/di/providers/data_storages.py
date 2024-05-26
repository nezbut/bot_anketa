from typing import AsyncIterable, Tuple, Iterable

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker

from redis.asyncio import Redis
from dishka import Provider, Scope, provide

from bot_anketa.src.config import Settings
from bot_anketa.src.db.crud import UserCRUD


class DataBaseProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_engine(self, settings: Settings) -> AsyncIterable[AsyncEngine]:
        url = settings.database_uri
        engine = create_async_engine(url=url, poolclass=NullPool)
        yield engine
        await engine.dispose()

    @provide
    async def get_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            engine, class_=AsyncSession, expire_on_commit=False
        )

    @provide(scope=Scope.REQUEST)
    async def get_session(self, session_maker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session


class KvDataBaseProvider(Provider):
    scope = Scope.APP

    @provide
    def get_redis(self, settings: Settings) -> Redis:
        return Redis.from_url(url=settings.kv_database_uri, decode_responses=True)


class DataBaseCRUDProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_user_crud(self, session: AsyncSession) -> Iterable[UserCRUD]:
        yield UserCRUD(session=session)


def get_data_storages_providers() -> Tuple[Provider, ...]:
    return (
        DataBaseProvider(),
        KvDataBaseProvider(),
        DataBaseCRUDProvider()
    )
