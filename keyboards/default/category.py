from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
macshop = KeyboardButton(text='Macbook va Iphone')
akssessuar = KeyboardButton(text='Sotaman')
keyboard.add(macshop, akssessuar)
