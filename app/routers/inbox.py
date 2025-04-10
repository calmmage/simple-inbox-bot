from aiogram import Router, html
from aiogram.filters import Command
from aiogram.types import Message
from botspot import commands_menu
from botspot.chat_binder import bind_chat, get_bound_chat
from botspot.core.errors import ChatBindingNotFoundError
from botspot.utils import send_safe

router = Router()


# @commands_menu.botspot_command("bind", "Bind a chat as your inbox")
# @router.message(Command("bind"))
# async def bind_handler(message: Message):
#     """Bind the current chat as the user's inbox"""
#     await bind_chat(message.from_user.id, message.chat.id)
#     await send_safe(
#         message.chat.id,
#         f"✅ Chat {html.bold(message.chat.title or 'private chat')} has been bound as your inbox.\n"
#         "All messages will be forwarded here.",
#     )


@commands_menu.botspot_command("inbox", "Show your current inbox")
@router.message(Command("inbox"))
async def inbox_handler(message: Message):
    """Show the user's current inbox chat"""
    try:
        chat_id = await get_bound_chat(message.from_user.id)

        await send_safe(
            message.chat.id,
            f"📥 Your current inbox is: {html.bold(str(chat_id))}",
        )
    except ChatBindingNotFoundError:
        await send_safe(
            message.chat.id,
            "❌ You haven't bound any chat as your inbox yet.\n"
            "Use /bind in the chat you want to use as your inbox.",
        )