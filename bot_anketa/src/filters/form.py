from typing import Any

from aiogram.filters import BaseFilter
from aiogram.types import Message


class AgeFilter(BaseFilter):

    async def __call__(self, message: Message) -> Any:
        try:
            if text := message.text:
                age = int(text)  # type: ignore[arg-type]
                return {"age": age}
            else:
                await message.answer("Введите пожалуйста текст с возрастом")
        except ValueError:
            await message.answer("Некорректный возраст")
            return False


class GenderFilter(BaseFilter):

    async def __call__(self, message: Message) -> Any:
        if message.text and message.text.lower() in ["мужчина", "женщина", "мужской", "женский"]:
            return {"gender": message.text}
        else:
            await message.answer("Некорректный пол")
            return False


class CityFilter(BaseFilter):

    async def __call__(self, message: Message) -> Any:
        text = message.text
        if text and len(text) > 2:
            return {"city": text}
        else:
            await message.answer("Некорректный город")
            return False
