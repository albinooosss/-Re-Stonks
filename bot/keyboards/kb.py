from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_data = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Доступные компании',
            callback_data='button_available'
        )
    ],
    [
        InlineKeyboardButton(
            text='Избранные компании',
            callback_data='button_favourite'
        )
    ]
])
