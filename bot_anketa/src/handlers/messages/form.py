from dishka.integrations.aiogram import FromDishka
from sqlalchemy.exc import IntegrityError

from aiogram import Router

from aiogram.filters import StateFilter
from aiogram.types import Message, User
from aiogram.fsm.context import FSMContext

from bot_anketa.src.states import FillingForm
from bot_anketa.src.filters.form import AgeFilter, GenderFilter, CityFilter
from bot_anketa.src.db.dto import UserDTO
from bot_anketa.src.db.crud import UserCRUD

router = Router()


@router.message(StateFilter(FillingForm.age), AgeFilter())
async def age(message: Message, state: FSMContext, age: int) -> None:
    await state.update_data(age=age)
    await state.set_state(FillingForm.gender)
    await message.answer("Введите ваш пол:\n\n1. Мужчина\n2. Женщина")


@router.message(StateFilter(FillingForm.gender), GenderFilter())
async def gender(message: Message, state: FSMContext, gender: str) -> None:
    await state.update_data(gender=gender)
    await state.set_state(FillingForm.city)
    await message.answer("Введите ваш город")


@router.message(StateFilter(FillingForm.city), CityFilter())
async def city(message: Message, state: FSMContext, city: str, crud: FromDishka[UserCRUD]) -> None:
    from_user: User = message.from_user  # type: ignore[assignment]
    data = await state.get_data()
    user = UserDTO(
        id=from_user.id,
        name=from_user.username or from_user.first_name,
        age=data["age"],
        gender=data["gender"],
        city=city
    )
    from_db = await crud.get_user(from_user.id)
    if not from_db:
        await crud.add_user(user)
        await message.answer("Ваша анкета сохранена.\nЧтобы вернуться напишите /start")
    else:
        data = user.to_dict()
        data.pop("id")
        await crud.update_user(user.id, data)
        await message.answer("Ваша анкета обновлена.\nЧтобы вернуться напишите /start")
