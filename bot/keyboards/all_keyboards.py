from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery

from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section
)

router1 = Router(name='button_available')
router2 = Router(name='button_favourite')


@router1.callback_query(F.data=='button_available')
async def select_data(call: CallbackQuery, bot: Bot):
    answer = as_list(
        as_marked_section(
            Bold("Доступен прогноз по следующим компаниям:"),
            "Компания 1",
            "Компания 2",
            "Компания 3",
            marker="✅ ",
        )
    )
    await call.message.answer(**answer.as_kwargs())
    await call.answer()

@router2.callback_query(F.data=='button_favourite')
async def select_data(call: CallbackQuery, bot: Bot):
    answer = as_list(
        as_marked_section(
            Bold("Вы добавили в избранное следующие компании:"),
            "Компания 1",
            "Компания 2",
            "Компания 3",
            marker="❤️ ",
        )
    )
    await call.message.answer(**answer.as_kwargs())
    await call.answer()
