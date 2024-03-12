from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "📈Привет! Я - бот, созданный на основе технологий "
        "машинного обучения. Я умею прогнозировать "
        "динамику цен акций. (Внимание! Ни я, ни мои создатели не можем "
        "гарантировать достоверность и корректность прогноза)📈"
    )
    await message.answer(
        f'Напиши мне что-нибудь, если хочешь, чтобы я спрогнозировал чьи-то акции'
    )

# @router.message()
# async def some_cmd(message: Message):
#     kb = [
#         [types.KeyboardButton(text="День")],
#         [types.KeyboardButton(text="Два дня")],
#         [types.KeyboardButton(text="Неделя")],
#         [types.KeyboardButton(text="Две недели")],
#         [types.KeyboardButton(text="Месяц")],
#         [types.KeyboardButton(text="Два месяца")],
#         [types.KeyboardButton(text="Год")],
#         [types.KeyboardButton(text="Два года")]
#     ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Осталось немного, выбери временной промежуток", reply_markup=keyboard)

