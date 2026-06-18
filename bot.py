import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Вставь свой токен сюда или в переменную окружения BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN", "СЮДА_ВСТАВЬ_ТОКЕН")

# URL твоего задеплоенного Mini App (GitHub Pages)
# После деплоя замени на реальный URL
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://ТВО-ЮЗЕРНЕЙМ.github.io/focus-dashboard/")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            text="🎯 Открыть Focus Dashboard",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    await update.message.reply_text(
        "👋 Привет! Я твой личный трекер целей и привычек.\n\n"
        "📊 Отслеживай цели накоплений\n"
        "✅ Веди привычки каждый день\n"
        "💰 Записывай доходы и расходы\n\n"
        "Нажми кнопку ниже, чтобы открыть приложение 👇",
        reply_markup=keyboard
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Помощь:\n\n"
        "/start — открыть приложение\n"
        "/app — тоже открыть приложение\n\n"
        "Все данные хранятся прямо в приложении."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("app", start))
    app.add_handler(CommandHandler("help", help_cmd))
    print("✅ Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
