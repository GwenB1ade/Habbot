import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command

from aiogram.types import Message
from app.config import settings
from app import messages_texts


from app.client_groq import GroqClient


bot = Bot(settings.BOT_KEY)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer_sticker(
        "CAACAgIAAxkBAAEOeWNoI6E63o4dieVA-F6VjPiic5X3wQACIAkAAhhC7gjhiiCooToK2TYE"
    )
    await message.answer(messages_texts.StartMessage.message())


@dp.message(Command("call"))
async def call_schedule(message: Message):
    await message.answer(messages_texts.CallScheduleMessage.message())


@dp.message(F.text)
async def request(message: Message):
    last_bot_message = await message.answer(messages_texts.LoadMessage.message())
    data = GroqClient.generate(message.text)
    await last_bot_message.delete()
    await asyncio.sleep(0.2)
    await message.answer(data)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    asyncio.run(main())
