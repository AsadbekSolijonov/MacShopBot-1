from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin_link_btn = InlineKeyboardMarkup(inline_keyboard=True, row_width=1)
admin_link = InlineKeyboardButton('Bog`lanish', url='https://t.me/itsmaxkamoff')
admin_link_btn.add(admin_link)
