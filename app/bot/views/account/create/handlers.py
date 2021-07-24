from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.base.objects import dispatcher, bot
from bot.base.states import AccountRegister
from bot.models.account import Account
from bot.views.account.list.menu import AccountListMenu


@dispatcher.callback_query_handler(lambda call: call.data == 'create_account', state='*')
async def create_account(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text='Введите номер телефона нового аккаунта👇',
    )
    await AccountRegister.register_phone_number.set()
