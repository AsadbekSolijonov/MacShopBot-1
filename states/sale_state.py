from aiogram.dispatcher.filters.state import State, StatesGroup


class SaleConfirm(StatesGroup):
    send_post = State()
    confirm_post = State()
    admin_confirm_post = State()

