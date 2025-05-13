from app.config import settings
from app import messages_texts
from groq import Groq


class GroqClient:
    client = Groq(api_key=settings.GROQ_API_KEY)

    @classmethod
    def generate(cls, text: str) -> str:
        messages = [
            {
                "role": "system",
                "content": "Ты ассистент студента. Объясняй на вопросы подробно и понятно!",
            },
            {
                "role": "user",
                "content": text,
            },
        ]

        try:
            text = cls.__generate_llama(messages)
            return text
        except:
            try:
                text = cls.__generate_gemma(messages)
                return text
            except:
                return messages_texts.ErrorMessage.message()

    @classmethod
    def __generate_llama(cls, messages: list):
        response = cls.client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
        )

        result = response.choices[0].message.content
        return result

    @classmethod
    def __generate_gemma(cls, messages: list):
        response = cls.client.chat.completions.create(
            messages=messages,
            model="gemma2-9b-it",
        )
        result = response.choices[0].message.content
        return result
