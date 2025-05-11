from config import settings
from groq import Groq



class GroqClient:
    client = Groq(api_key=settings.GROQ_API_KEY)

    @classmethod
    def generate(cls, text: str):
        response = cls.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Ты ассистент студента. Объясняй на вопросы подробно и понятно!",
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
            model="llama-3.3-70b-versatile",
        )
        result = response.choices[0].message.content
        return result
