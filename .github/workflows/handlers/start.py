from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from database.db import create_user, get_user

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Создаём пользователя в базе, если его ещё нет
    await create_user(user_id, username)

    await message.answer(
        f"Привет, {message.from_user.first_name}!\n\n"
        f"Это бот GRAM.\n"
        f"Твой ID: <code>{user_id}</code>",
        parse_mode="HTML"
    )
