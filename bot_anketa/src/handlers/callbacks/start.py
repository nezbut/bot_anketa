from dishka.integrations.aiogram import FromDishka

from aiogram import Router, F

from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from bot_anketa.src.states import FillingForm
from bot_anketa.src.db.crud import UserCRUD
from bot_anketa.src.db.dto import UserDTO

router = Router()


@router.callback_query(F.data == "start")
async def start_form(callback: CallbackQuery, state: FSMContext) -> None:
    message: Message = callback.message  # type: ignore[assignment]
    await message.delete()
    await state.set_state(FillingForm.age)
    await message.answer("Укажите свой возраст:")


@router.callback_query(F.data == "my_form")
async def my_form(callback: CallbackQuery, state: FSMContext, crud: FromDishka[UserCRUD]) -> None:
    message: Message = callback.message  # type: ignore[assignment]
    await message.delete()
    user_id = callback.from_user.id  # type: ignore[union-attr]
    user: UserDTO = await crud.get_user(user_id)  # type: ignore[assignment]
    await message.answer(f"Вот ваша анкета: \n\nName - {user.name}\nAge - {user.age}\nGender - {user.gender}\nCity - {user.city}\n\nЧтобы вернуться напишите /start")
