"""
Generate markup for casual users
"""
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


def create_user_start_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup().add(InlineKeyboardButton('Записаться на тренировку', callback_data=' '))\
        .add(InlineKeyboardButton(text='Процесс тренировки', callback_data=' '))
    
    return markup