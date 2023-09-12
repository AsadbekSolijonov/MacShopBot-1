from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pickService = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
sotuvda = KeyboardButton(text='Sotuvda')
buyurtma = KeyboardButton(text='Buyurtma Berish')
buyurtmam = KeyboardButton(text='Mening Buyurtmam')
pickService.add(sotuvda, buyurtma, buyurtmam)
