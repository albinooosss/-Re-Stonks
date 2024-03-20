from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
)

select_data = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Доступные акции',
            callback_data='print_companies_0_10'
        )
    ],
    [
        InlineKeyboardButton(
            text='Избранные акции',
            callback_data='button_favourite'
        )
    ]
])

company_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Хочу прогноз📈'
        )
    ],
    [
        KeyboardButton(
            text='Добавить акцию в избранное❤️'
        )
    ],
    [
        KeyboardButton(
            text='Вернуться к старту✅'
        )
    ]
], resize_keyboard=True)




