from pydantic import SecretStr
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """Basic app configuration"""

    telegram_bot_token: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


class App:
    name = "Simple Inbox Bot"

    def __init__(self, **kwargs):
        self.config = AppConfig(**kwargs)
        print(self.config.telegram_bot_token.get_secret_value())
