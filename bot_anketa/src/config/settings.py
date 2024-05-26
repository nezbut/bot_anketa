from dataclasses import dataclass
from os import getenv
from functools import lru_cache


@dataclass
class Settings:
    tg_bot_token: str
    database_uri: str
    kv_database_uri: str

    @classmethod
    @lru_cache
    def from_env(cls) -> "Settings":
        token = getenv("TG_BOT_TOKEN")
        db_uri = getenv("DATABASE_URI")
        kv_db_uri = getenv("KV_DATABASE_URI")
        data = {
            "tg_bot_token": token,
            "database_uri": db_uri,
            "kv_database_uri": kv_db_uri
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
