# 🤖 Habbot - AI-ассистент для учеников

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-green.svg)
![AI](https://img.shields.io/badge/AI-Assistant-orange.svg)

**Habbot** - это интеллектуальный телеграм-бот, созданный для помощи ученикам в обучении. Бот использует современные AI-технологии (Groq API) для объяснения сложных тем, решения задач и предоставления учебных материалов в простой и понятной форме.

## 🌟 Возможности

- 📚 Объяснение учебных тем простым языком
- 🧩 Помощь с домашними заданиями
- 🔍 Поиск и анализ информации
- 📝 Конспектирование материалов
- ⏰ Напоминания о дедлайнах
- 💡 Подготовка к экзаменам

## 🛠 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/GwenB1ade/Habbot
```

2. Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv .venv
source .venv/bin/activate  # для Linux/Mac
# или .venv\Scripts\activate для Windows
```

Установите зависимости:

```bash
pip3 install -r req.txt
```
Создайте файл .env в корне проекта и добавьте:
```
BOT_KEY=ваш_телеграм_токен
GROQ_API_KEY=ваш_groq_токен
```
🔑 Получить Groq API ключ можно [здесь](https://console.groq.com/keys)

Запустите бота:

```bash
python3 main.py
```
📌 Использование
После запуска бот будет доступен в Telegram. Просто начните диалог с командой /start и следуйте инструкциям.


✨ Habbot - ваш умный помощник в обучении! ✨