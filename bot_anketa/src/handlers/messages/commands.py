from dishka.integrations.aiogram import FromDishka

from aiogram import Router

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot_anketa.src.db.crud import UserCRUD
from bot_anketa.src.utils.keyboard import create_start_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message, crud: FromDishka[UserCRUD], state: FSMContext) -> None:
    await state.clear()
    user_id = message.from_user.id  # type: ignore[union-attr]
    is_questionnaire = bool(await crud.get_user(user_id))
    markup = create_start_keyboard(is_questionnaire)
    await message.answer("Привет, я бот для анкетирования.", reply_markup=markup)
