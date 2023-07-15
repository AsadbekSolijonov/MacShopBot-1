from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

saleButtons = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
macbook = KeyboardButton(text='Macbook')
iphone = KeyboardButton(text='Iphone')
saleButtons.add(macbook, iphone)
