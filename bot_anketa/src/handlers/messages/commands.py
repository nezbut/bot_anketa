from aiogram import Router

from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer("Привет, я бот для анкетирования. "
                         "Для начала напиши мне свою фамилию и имя.")
