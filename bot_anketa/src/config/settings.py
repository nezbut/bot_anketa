from dataclasses import dataclass
from os import environ


@dataclass
class Settings:
    tg_bot_token: str
    database_uri: str
    kv_database_uri: str

    @classmethod
    def from_env(cls) -> "Settings":
        data = {
            "tg_bot_token": environ.get("TG_BOT_TOKEN"),
            "database_uri": environ.get("DATABASE_URI"),
            "kv_database_uri": environ.get("KV_DATABASE_URI")
        }

        cls._check_env(**data)
        return Settings(**data)  # type: ignore[arg-type]

    @staticmethod
    def _check_env(**kwargs) -> None:
        for key, value in kwargs.items():
            if value is None:
                raise ValueError(
                    f"Missing environment variable: {key.upper()}"
                )
