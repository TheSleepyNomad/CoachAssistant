from aiogram import Dispatcher
from app.handlers.admin.handler import register_admin_handlers
from app.handlers.users.handler import register_user_handlers
from app.handlers.other.handler import register_other_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    """
    Регистрирует все обработчики
    """
    handlers = [register_admin_handlers, register_user_handlers, register_other_handlers]

    for handler in handlers:
        handler(dp)