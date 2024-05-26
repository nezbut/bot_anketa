from dishka import AsyncContainer, make_async_container

from .providers import get_providers


def get_di_container() -> AsyncContainer:
    return make_async_container(*get_providers())
