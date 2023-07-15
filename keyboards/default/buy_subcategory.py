from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

subcategoryBtn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
macbook = KeyboardButton(text='Macbook')
iphone = KeyboardButton(text='Iphone')
another = KeyboardButton(text='Boshqalar')
subcategoryBtn.add(macbook, iphone, another)