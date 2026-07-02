from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8658072405:AAFjp2WWouhWv3nlhCXw3bd2veFSs4MnGRo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❤️ Welcome to DatingBot!\n\n"
        "This bot is under development."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling(drop_pending_updates=True)