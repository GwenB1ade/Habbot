from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import ValidationError


class Settings(BaseSettings):

    BOT_KEY: str
    GROQ_API_KEY: str
    model_config = SettingsConfigDict(env_file=".env")


try:
    settings = Settings()

except ValidationError:
    raise Exception('Ошибка: файл .env не найден или в нём отсутствует нужная переменная. Проверьте наличие файла и правильность названий переменных, затем перезапустите приложение.')
