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


# 🔐 Необходимые API-ключи

### 🤖 Telegram Bot Token
1. Откройте [@BotFather](https://t.me/BotFather) в Telegram
2. Создайте нового бота командой `/newbot`
3. Скопируйте выданный токен (формат: `1234567890:ABCdefGHIJKlmNoPQRsTUVwxyZ`)

### 🧠 Groq API Key
1. Зарегистрируйтесь на [Groq Cloud](https://console.groq.com/)
2. В разделе API Keys создайте новый ключ
3. Скопируйте сгенерированный ключ

> [!WARNING]
> ⚠️ Без этих токенов бот не запустится!.




## 🛠 Установка

---
### 📦 Автоматическая установка
Если вы хотите установить вручную или случиться сбой при автоматической установке, использую ручную установку.

```bash
git clone https://github.com/GwenB1ade/Habbot
cd Habbot
```

Для Linux/macOS (.sh)
```sh
chmod +x setup.sh  # Даём права на выполнение
./setup.sh         # Запускаем скрипт
```
Для Windows (.bat)
```bat
setup.bat
```

---

### 🔧 Ручная установка

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