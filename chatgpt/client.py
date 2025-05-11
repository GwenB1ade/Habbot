from g4f import Client

client = Client()


class ChatGPTClient:
    client = client
    promt = "Ты ассистен ученика, твои ответы должны быть понятны любому человеку. Обьясняй как можно проще и с примерами. Вот твой вопрос: "

    @classmethod
    async def generate(cls, text: str):
        response = cls.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": cls.promt + text}],
            web_search=False,
        )

        return response.choices[0].message.content
