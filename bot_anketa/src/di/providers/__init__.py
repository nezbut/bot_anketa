from typing import Tuple

from dishka import Provider

from .settings import get_settings_providers
from .bot import get_tgbot_providers
from .data_storages import get_data_storages_providers


def get_providers() -> Tuple[Provider, ...]:
    return (
        *get_settings_providers(),
        *get_tgbot_providers(),
        *get_data_storages_providers(),
    )
