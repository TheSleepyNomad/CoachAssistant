from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import NetworkError
from app.config.env import BOT_TOKEN



def __on_start_up(dp: Dispatcher):
    register_all_handlers(dp)
    # register_models()
    # if DEBUG_MODE:
    #     fill_database()
    #     pass
    

def start_app():
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up(dp))