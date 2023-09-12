from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

post_confirm_button = InlineKeyboardMarkup(inline_keyboard=True, row_width=2)
yes = InlineKeyboardButton(text='Tasdiqlayman', callback_data='yes')
no = InlineKeyboardButton(text='Bekor qilaman', callback_data='no')
post_confirm_button.add(no, yes)

