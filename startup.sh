echo 🚀 Начинаем установку Habbot...

# Создаем виртуальное окружение (Python)
echo "🛠 Создаем виртуальное окружение..."
python3 -m venv venv

# Активируем виртуальное окружение
source venv/bin/activate

# Устанавливаем зависимости
if [ -f "req.txt" ]; then
    echo "📦 Устанавливаем зависимости..."
    pip install -r req.txt
else
    echo "Файл requirements.txt не найден"
    exit 1
fi

# Запрашиваем данные для .env
echo "🔑 Введите ваш Telegram Bot токен:"
read -r bot_token
echo "🔑 Введите ваш Groq API ключ:"
read -r groq_key

# Создаем .env файл
echo "📝 Создаем .env файл..."
cat > .env <<EOL
BOT_KEY=$bot_token
GROQ_API_KEY=$groq_key
EOL

# Запускаем проект (предполагаем, что основной файл - main.py)
echo "🚀 Запускаем бота..."
if [ -f "main.py" ]; then
    python main.py
else
    echo "Основной файл проекта (main.py) не найден"
    exit 1
fi