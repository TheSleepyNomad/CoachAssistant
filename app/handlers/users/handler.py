from aiogram import Dispatcher
from aiogram.types import Message, InputFile, CallbackQuery
from app.config.markup.users.markup import description_school_markup, create_user_start_markup
from app.config.config import DOC_DIR

# Пример создания обработчика сообщений

# async def send_welcome_msg(msg: Message):        
#     await msg.bot.send_message(msg.chat.id, 'Привет')

async def show_school_description(query: CallbackQuery) -> None:
    await query.bot.answer_callback_query(query.id) #всегда при работе с CALLBACKQUERY надо ЭТО написать!!!
    await query.bot.send_message(query.from_user.id, text='В нашей школе...', reply_markup=description_school_markup())
    
async def roll_back(query: CallbackQuery) -> None:
     await query.bot.answer_callback_query(query.id)
     await query.bot.send_message(query.from_user.id, text='Главное меню', reply_markup=create_user_start_markup())
     
async def send_message(query: CallbackQuery) -> None:
     await query.bot.answer_callback_query(query.id)
     with open(DOC_DIR, 'rb') as file:
          await query.bot.send_document(query.from_user.id, InputFile(file), caption='image')


def register_user_handlers(dp: Dispatcher):
    # Пример регистрации обработчиков

    # dp.register_message_handler(send_welcome_msg, commands=['start'])
    dp.register_callback_query_handler(show_school_description, text_contains="about_school")
    dp.register_callback_query_handler(roll_back, text_contains='back')
    dp.register_callback_query_handler(send_message, text_contains='record')
    pass

