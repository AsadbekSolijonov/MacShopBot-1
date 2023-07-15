from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

# ReplyKeyboard
from keyboards.default.category import keyboard
from keyboards.default.buy_subcategory import subcategoryBtn
from keyboards.default.sale_subcategory import saleButtons
from loader import dp


# Start
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Salom Pro foydalanuvchi {message.from_user.full_name}!! "
        f"bu bot orqali Macshop do'konida mavjud tavarlarni izlashingiz "
        f"mumkin va Do'kon haqida malumot olishingiz mumkin", reply_markup=keyboard)


# Macbook va Iphone, Sotaman
@dp.message_handler(content_types=types.ContentType.ANY)
async def all_message(message: types.Message):
    if message.text == 'Macbook va Iphone':
        await message.reply(text='Hozircha bizcha quyidagi tavarlar mavjud!', reply_markup=subcategoryBtn)
    elif message.text == 'Sotaman':
        await message.reply(
            text='Siz qanday turdagi mahsulot sotmoqchisiz?\n'
                 'Quyidagi tovarlardan birini tanlab uning xolati '
                 'haqida ma`lumot qoldiring va tez orada siz bilan a`loqaga chiqamiz!',
            reply_markup=saleButtons)
    else:
        await message.reply(text="Xozircha bunday xizmat qo`shilmagan.")
