from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from botspot.core.bot_manager import BotManager
from calmlib.utils import setup_logger, heartbeat_for_sync
from loguru import logger
from dotenv import load_dotenv
from pathlib import Path

from app._app import App
from app.router import router as main_router


@heartbeat_for_sync(App.name)
def main(debug=False) -> None:
    setup_logger(logger, level="DEBUG" if debug else "INFO")

    # Initialize bot and dispatcher
    dp = Dispatcher()
    app = App()
    dp["app"] = app

    # Initialize Bot instance with a default parse mode
    bot = Bot(
        token=app.config.telegram_bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    # Initialize BotManager with default components
    bm = BotManager(
        bot=bot,
        error_handler={"enabled": True},
        ask_user={"enabled": True},
        bot_commands_menu={"enabled": True},
    )

    # Setup dispatcher with our components
    bm.setup_dispatcher(dp)

    dp.include_router(main_router)


    # Start polling
    dp.run_polling(bot)


if __name__ == "__main__":
    repo_root = Path(__file__).parent.parent
    print(f"Loading .env from {repo_root / '.env'}")
    load_dotenv(repo_root / ".env")
    main()
