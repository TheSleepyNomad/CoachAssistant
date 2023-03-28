from aiogram import Dispatcher
from aiogram.types import Message, InputFile, CallbackQuery

# Пример создания обработчика сообщений

# async def send_welcome_msg(msg: Message):        
#     await msg.bot.send_message(msg.chat.id, 'Привет')

# async def show_catalog(query: CallbackQuery) -> None:
#     await query.bot.answer_callback_query(query.id)
#     await query.bot.delete_message(query.message.chat.id, query.message.message_id)
#     await query.bot.send_message(query.from_user.id, text='Мы готовим...', reply_markup=create_catalog_markup(query))


def register_user_handlers(dp: Dispatcher):
    # Пример регистрации обработчиков

    # dp.register_message_handler(send_welcome_msg, commands=['start'])
    # dp.register_callback_query_handler(show_catalog, text_contains='catalog')
    pass