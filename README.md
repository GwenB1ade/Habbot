# Habbot

## Как установить

Вводим данные команды:
```
git clone https://github.com/GwenB1ade/Habbot
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r req.txt
```

После создаем в корне проекта файл .env и заполняем его:
```
BOT_KEY=токен_бота
GROQ_API_KEY=токен_groq
```

Для получения токена переходим сюда https://console.groq.com/keys

После вводим такие команды:

```
cd app
python3 main.py
```
