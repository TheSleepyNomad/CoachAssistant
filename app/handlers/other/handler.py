from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from app.config.env import ADMIN_ID
from app.config.markup.admin.markup import create_admin_start_markup
from app.config.markup.users.markup import create_user_start_markup


# Если пользователь напишет /start
async def send_welcome_msg(msg: Message):
    if ADMIN_ID == msg.from_user.username:
        await msg.bot.send_message(msg.chat.id, 'Привет Админ', reply_markup=create_admin_start_markup())
    else:
        await msg.bot.send_message(msg.chat.id, 'Привет Пользователь', reply_markup=create_user_start_markup()) 

# Если пользователь напишет просто текст
async def send_answer_for_unknow_msg(msg: Message):
    await msg.bot.send_message(msg.chat.id, text=f'Извини, {msg.from_user.first_name}'
                           f', но я Вас не понимаю, напишите /start!')
    

async def back_to_main_menu(query: CallbackQuery) -> None:
    await query.bot.answer_callback_query(query.id)
    await query.bot.delete_message(query.message.chat.id, query.message.message_id)
    if ADMIN_ID == query.from_user.username:
        await query.bot.send_message(query.from_user.id, text='Привет Админ', reply_markup=create_admin_start_markup())
    else:
        await query.bot.send_message(query.from_user.id, text='Привет Пользователь', reply_markup=create_user_start_markup())
    

def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome_msg, commands=['start'])
    dp.register_message_handler(send_answer_for_unknow_msg, content_types=['text'], state=None)
    dp.register_callback_query_handler(back_to_main_menu, text_contains='back_to_start')