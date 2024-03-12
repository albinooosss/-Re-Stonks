import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

import text
from bot.keyboards import all_keyboards
import config

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

router = Router()
dp.include_routers(router, all_keyboards.router1, all_keyboards.router2, all_keyboards.router3)

@router.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(
        text.START_MESSAGE
    )

    await message.answer(
        "Выбери интересующий пункт:",
        reply_markup=all_keyboards.select_data
    )

@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        '/choice - выбор компании\n'
        '/clown - бот называет клоуна'
    )

@router.message(Command(commands=['choice']))
async def process_help_command(message: Message):
    await message.answer(
        'Выбери интересующий пункт:',
        reply_markup=all_keyboards.select_data
    )

@router.message(Command(commands=['clown']))
async def send_clown(message: Message):
    await message.answer('рустам клоун')


if __name__ == "__main__":
    dp.run_polling(bot)
    logging.basicConfig(level=logging.INFO)