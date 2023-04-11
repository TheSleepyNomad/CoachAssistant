"""
Generate markup for user with admin role(owner)
"""
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from app.config.markup.buttons import Btn


def create_admin_start_markup() -> InlineKeyboardMarkup:
    """
    Создает раскладку кнопок для стартового меню администратора
    """
    markup = InlineKeyboardMarkup()\
        .add(InlineKeyboardButton(Btn.journal, callback_data='journal'))\
        .add(InlineKeyboardButton(text=Btn.reports, callback_data='reports'))
    
    return markup

def create_admin_journal_markup() -> InlineKeyboardMarkup:
    #* wait Roman Sobchenko
    pass

