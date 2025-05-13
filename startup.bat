@echo off
echo 🚀 Начинаем установку Habbot...

:: Создаем виртуальное окружение
echo 🛠 Создаем виртуальное окружение...
python -m venv .venv || (echo Ошибка при создании venv & exit /b 1)
call .venv\Scripts\activate.bat

:: Устанавливаем зависимости
echo 📦 Устанавливаем зависимости...
pip install -r req.txt || (echo Ошибка при установке зависимостей & exit /b 1)

:: Запрашиваем данные для .env
echo 🔑 Введите ваш Telegram Bot токен:
set /p bot_token=
echo 🔑 Введите ваш Groq API ключ:
set /p groq_key=

:: Создаем .env файл
echo 📝 Создаем .env файл...
echo BOT_KEY=%bot_token% > .env
echo GROQ_API_KEY=%groq_key% >> .env

:: Запускаем бота
echo 🚀 Запускаем бота...
python main.py