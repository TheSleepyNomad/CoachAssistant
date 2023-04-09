from aiogram import Dispatcher
from aiogram.types import Message, InputFile, CallbackQuery
from app.config.markup.users.markup import description_school_markup

# Пример создания обработчика сообщений

# async def send_welcome_msg(msg: Message):        
#     await msg.bot.send_message(msg.chat.id, 'Привет')

async def show_school_description(query: CallbackQuery) -> None:
    await query.bot.answer_callback_query(query.id) #всегда при работе с CALLBACKQUERY надо ЭТО написать!!!
    await query.bot.send_message(query.from_user.id, text='В нашей школе...', reply_markup=description_school_markup())


def register_user_handlers(dp: Dispatcher):
    # Пример регистрации обработчиков

    # dp.register_message_handler(send_welcome_msg, commands=['start'])
    dp.register_callback_query_handler(show_school_description, text_contains='about_school')
    pass