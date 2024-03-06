import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command, CommandStart
from aiogram import F
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section
)
from dotenv import load_dotenv

from bot.keyboards import kb, all_keyboards

import config

load_dotenv()

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")

router = Router()
dp = Dispatcher()
dp.include_routers(router, all_keyboards.router1, all_keyboards.router2)

@router.message(F.text, CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "📈Привет! Я - <b>бот</b>, созданный на основе технологий "
        "машинного обучения. Я умею прогнозировать "
        "динамику цен акций. (Внимание! Ни я, ни мои создатели не можем "
        "гарантировать достоверность и корректность прогноза)📈"
    )

    await message.answer(
        "Выбери интересующий пункт:",
        reply_markup=kb.select_data
    )

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())