from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        "📈Привет! Я - бот, созданный на основе технологий "
        "машинного обучения. Я умею прогнозировать "
        "динамику цен акций. (Внимание! Ни я, ни мои создатели не можем "
        "гарантировать достоверность и корректность прогноза)📈"
    )


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")