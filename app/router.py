from aiogram import Router, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from botspot import commands_menu
from botspot.utils import send_safe

from app._app import App
from app.routers.inbox import router as inbox_router

router = Router()
router.include_router(inbox_router)


@commands_menu.botspot_command("start", "Start the bot")
@router.message(CommandStart())
async def start_handler(message: Message, app: App):
    await send_safe(
        message.chat.id,
        f"Hello, {html.bold(message.from_user.full_name)}!\n"
        f"Welcome to {app.name}!\n"
        "This bot helps you manage your messages by forwarding them to a designated inbox.\n"
        "Use /help to see available commands.",
    )


@commands_menu.botspot_command("help", "Show this help message")
@router.message(Command("help"))
async def help_handler(message: Message, app: App):
    """Basic help command handler"""
    await send_safe(
        message.chat.id,
        f"This is {app.name}. Use /start to begin.\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/bind - Bind a chat as your inbox\n"
        "/inbox - Show your current inbox\n"
        "/help_botspot - Show Botspot help",
    )
