from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_start_keyboard(questionnaire: bool) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Начать", callback_data="start")]
        ]
    )
    builder = InlineKeyboardBuilder.from_markup(markup)
    if questionnaire:
        builder.row(
            InlineKeyboardButton(
                text="Моя анкета", callback_data="my_form"
            ),
            width=1
        )

    return builder.as_markup()
