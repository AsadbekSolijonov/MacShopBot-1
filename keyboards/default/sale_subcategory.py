from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

saleButtons = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
macbook = KeyboardButton(text='Kompyuter')
iphone = KeyboardButton(text='Telefon')
saleButtons.add(macbook, iphone)
