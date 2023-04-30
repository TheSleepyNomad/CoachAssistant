from aiogram import Dispatcher
from aiogram.types import Message, InputFile, CallbackQuery
from app.config.markup.admin.markup import create_admin_reports_markup
# Пример создания обработчика сообщений

# async def send_welcome_msg(msg: Message):        
#     await msg.bot.send_message(msg.chat.id, 'Привет')

async def show_admin_reports(query: CallbackQuery) -> None:
    await query.bot.answer_callback_query(query.id)
    await query.bot.delete_message(query.message.chat.id, query.message.message_id)
    await query.bot.send_message(query.from_user.id, text='Мы готовим...', reply_markup=create_admin_reports_markup())


def register_admin_handlers(dp: Dispatcher):
    # Пример регистрации обработчиков

    # dp.register_message_handler(send_welcome_msg, commands=['start'])
    dp.register_callback_query_handler(show_admin_reports, text_contains='reports')
    pass