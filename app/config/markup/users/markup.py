"""
Generate markup for casual users
"""
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


def create_user_start_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()\
        .add(InlineKeyboardButton('Записаться', callback_data='record'))\
        .add(InlineKeyboardButton('О школе', callback_data='about_school'))\
        .add(InlineKeyboardButton('Расписание тренировок', callback_data='gym_calendar'))\
        
    return markup

def description_school_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()\
        .add(InlineKeyboardButton('Описание стиля', callback_data=' '))\
        .add(InlineKeyboardButton('Лучшие ученики', callback_data=' '))\
        .add(InlineKeyboardButton('Тренеры школы', callback_data=' '))\
        .add(InlineKeyboardButton('Назад', callback_data=' '))\
        
    return markup