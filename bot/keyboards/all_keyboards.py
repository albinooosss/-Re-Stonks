import sys

from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section
)

sys.path.insert(1,
                'C:\\Users\\ADMIN\\-Re-Stonks\\database')
sys.path.insert(2,
                'C:\\Users\\ADMIN\\-Re-Stonks\\bot\\keyboards')
sys.path.insert(3,
                'C:\\Users\\ADMIN\\-Re-Stonks\\bot')

from database import parser_demo
from bot import text

router1 = Router(name='print_companies_0_10')
router2 = Router(name='button_favourite')
router3 = Router(name='return_to_start')

COMPANIES = parser_demo.s_and_p
select_data = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Доступные компании',
            callback_data='print_companies_0_10'
        )
    ],
    [
        InlineKeyboardButton(
            text='Избранные компании',
            callback_data='button_favourite'
        )
    ]
])


async def print_companies(demo: list, start_index: int, end_index: int, chat_id: int, bot: Bot):
    companies_text = '\n'.join(demo[start_index:end_index])
    await bot.send_message(chat_id, companies_text)


@router1.callback_query(lambda query: query.data.startswith('print_companies_'))
async def show_available_companies(query: CallbackQuery, bot: Bot):
    start, end = map(int, query.data.split('_')[2:])
    prev_start = start
    prev_end = end
    if start != 0:
        prev_start = start - 10
        prev_end = end - 10

    await print_companies(COMPANIES, start, end, query.from_user.id, bot)
    next_start = end
    next_end = end + 10 if end + 10 <= len(COMPANIES) else len(COMPANIES)

    if next_end <= len(COMPANIES):
        select_companies = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Следующие компании',
                    callback_data=f'print_companies_{next_start}_{next_end}'
                )
            ],
            [
                InlineKeyboardButton(
                    text='Назад',
                    callback_data=f'print_companies_{prev_start}_{prev_end}'
                )
            ],
            [
                InlineKeyboardButton(
                    text='Вернуться к старту',
                    callback_data='return_to_start'
                )
            ]
        ])

        await bot.send_message(query.from_user.id, text='Выбери:', reply_markup=select_companies)


@router2.callback_query(F.data == 'button_favourite')
async def show_fav_companies(call: CallbackQuery, bot: Bot):
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

@router3.callback_query(lambda call: call.data == 'return_to_start')
async def click_on_button_back(call: CallbackQuery):
    await call.message.answer(
        text.START_MESSAGE
    )
    await call.message.answer(text='Выбери интересующий пункт:', reply_markup=select_data)
