"""
Generate markup for casual users
"""
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


def create_admin_start_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup().add(InlineKeyboardButton('Записаться на тренировку', callback_data=' '))\
        .add(InlineKeyboardButton(text='Настройки', callback_data=' '))\
        .add(InlineKeyboardButton(text='Настройки', callback_data=' '))
    return markup