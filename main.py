import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command

from aiogram.types import Message
from config import settings

from chatgpt import ChatGPTClient
from client_groq import GroqClient


bot = Bot(settings.BOT_KEY)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "Привет, я твой ассистент, задай любой вопрос и я на него отвечу"
    )


# @dp.message(F.text)
# async def request(message: Message):
#     last_bot_message = await message.answer('Подождите пару секунд на генерирование ответа')
#     data = await ChatGPTClient.generate(message.text)
#     await last_bot_message.edit_text(data)


@dp.message(F.text)
async def request(message: Message):
    last_bot_message = await message.answer(
        "Подождите пару секунд на генерирование ответа"
    )
    data = GroqClient.generate(message.text)
    await last_bot_message.edit_text(data)


async def main():
    # dp.include_router()
    # await ChatGPTClient.generate('Test')
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    asyncio.run(main())
