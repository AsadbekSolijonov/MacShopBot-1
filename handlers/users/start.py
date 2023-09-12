import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
# ReplyKeyboard
from keyboards.default.category import keyboard
from keyboards.default.buy_subcategory import subcategoryBtn
from keyboards.default.pick_service import pickService
from keyboards.default.sale_subcategory import saleButtons
from keyboards.inline.admin_link_button import admin_link_btn
from keyboards.inline.post_confirm import post_confirm_button
from loader import dp, bot
from states.sale_state import SaleConfirm
from aiogram.types import ReplyKeyboardRemove
from data.config import CHANNELS


# Start
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Salom Pro foydalanuvchi {message.from_user.full_name}!! "
        f"bu bot orqali Macshop do'konida mavjud tavarlarni izlashingiz "
        f"mumkin va Do'kon haqida malumot olishingiz mumkin", reply_markup=keyboard)


# Harid qilish | Sotaman  -> Kompyuter | Telefon
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

    elif message.text in ['Macbook', 'Iphone', 'Boshqa']:
        await message.reply(text="Qaysiz xizmat turini tanlaysiz?", reply_markup=pickService)

    elif message.text in ["Kompyuter", "Telefon"]:
        await message.reply(text="👇Quyidagi na'munaga qarab tavar ma'lumotlarini kiriting!!")

        if message.text == "Kompyuter":
            await message.answer(text="💻 Model: \n"
                                      "⚙️ Protsessor:\n"
                                      "🖲 Videoxotira: \n"
                                      "🔋 Battareyka: \n"
                                      "📦 Karobka: \n"
                                      "🧠 Xotira: \n"
                                      "🛠 Xolat: \n"
                                      "💵 Narxi: \n"
                                      "❗️ Qo’shimcha: \n"
                                      "\n\n"
                                      "<b> Bog’lanish uchun</b>\n"
                                      "📞 Bog’lanish: \n"
                                      "🚩 Manzil: \n", reply_markup=ReplyKeyboardRemove())

        elif message.text == "Telefon":
            await message.answer(text="📱 Model: \n"
                                      "🎨 Rangi:  \n"
                                      "🛠 Xolati: \n"
                                      "🧠 Xotira: \n"
                                      "🔋 Battareyka: \n"
                                      "🌎 Region: \n"
                                      "📦 Karobka: \n"
                                      "♻️ Obmen:  \n"
                                      "💵 Narxi: \n"
                                      "💰 Nasiya savdo: \n\n"
                                      "<b>🚩 Manzil: #Toshkent</b>\n"
                                      "📞 Bog’lanish : \n", reply_markup=ReplyKeyboardRemove())

        await SaleConfirm.send_post.set()


# Send Post to Admin
@dp.message_handler(state=SaleConfirm.send_post)
async def send_and_check_posts(message: types.Message, state: FSMContext):
    post = message.text
    user_link = message.from_user.get_mention(as_html=True)

    async with state.proxy() as data:
        data['user_link'] = user_link
        data['client_id'] = message.chat.id
        data['post'] = post

    await message.answer(
        f"<b>Sotuvchi: {user_link}</b>\n\n{post}\n\n👆 Yuqorida xabarni adminga yuborishni tasdiqlaysizmi?",
        reply_markup=post_confirm_button)

    await SaleConfirm.confirm_post.set()


CLIENT_ID = {'client_id': None}


# Confirm Post
@dp.message_handler()
@dp.callback_query_handler(state=SaleConfirm.confirm_post)
async def confirm_posts(call: types.CallbackQuery, state: FSMContext):
    global CLIENT_ID
    call_data = call.data
    async with state.proxy() as data:
        user_link = data.get('user_link')
        post = data.get('post')
        CLIENT_ID['client_id'] = data.get('client_id')

    try:
        if call_data == 'yes':
            for admin_id in ADMINS:
                try:
                    await bot.send_message(chat_id=admin_id, text=f"<b>Sotuvchi: {user_link}</b>")
                    await bot.send_message(chat_id=admin_id, text=f"{post}", reply_markup=post_confirm_button)
                except Exception as e:
                    logging.error('Client dan Adminga post yuborishda xatolik bo`ldi. ')
                finally:
                    await call.message.reply('Xabar adminga yuborildi!')
        elif call_data == 'no':
            await call.message.reply('Sizning postigiz bekor qilindi!')
    except Exception as e:
        logging.info(e)
    await state.finish()


# Admin Send to Channel
@dp.callback_query_handler(text=['yes', 'no'], user_id=ADMINS)
async def admin_confirm_post(call: types.CallbackQuery, state: FSMContext):
    global CLIENT_ID
    post = await call.message.edit_reply_markup()
    async with state.proxy() as data:
        client_id = data.get('client_id')

    if call.data == 'yes':
        try:
            from data.config import CHANNEL_ID
            await post.forward(chat_id=CHANNEL_ID)  # forward
            await bot.send_message(chat_id=CLIENT_ID['client_id'],
                                   text='Sizning Tavaringiz Pro Sale Kanaliga yuklandi!')
        except Exception as e:
            logging.info(e)
        finally:
            await post.answer(text='Resell kanaliga joylandi')
    elif call.data == 'no':
        await post.answer(text='Bekor qilindi!')
        try:
            await bot.send_message(chat_id=CLIENT_ID['client_id'],
                                   text='Sizning Tavaringiz Bekor qilindi!\nAdmin bilan a`loqaga chiqing')
        except Exception as e:
            logging.info(e)

    await state.finish()
