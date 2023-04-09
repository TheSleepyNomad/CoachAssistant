"""
Generate markup for user with admin role(owner)
"""
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


def create_admin_start_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup().add(InlineKeyboardButton('Мой журнал', callback_data=' '))\
        .add(InlineKeyboardButton(text='Настройки', callback_data=' '))
    return markup

def create_admin_journal_markup() -> InlineKeyboardMarkup:
    #* wait Roman Sobchenko
    pass

