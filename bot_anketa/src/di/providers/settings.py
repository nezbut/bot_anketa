from typing import Tuple

from dishka import Provider, Scope, provide

from bot_anketa.src.config import Settings


class SettingsProvider(Provider):
    scope = Scope.APP

    @provide
    def get_settings(self) -> Settings:
        return Settings.from_env()


def get_settings_providers() -> Tuple[Provider, ...]:
    return (
        SettingsProvider(),
    )
