from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = "8211367936:AAHS--KZH3uGDe6Wke6egtZ9cEiI1hRUgg4"


app = Flask(__name__)

# دستور استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات آماده است.")

# ربات تلگرام
telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))

# اجرای webhook (برای رندر)
@app.route('/')
def index():
    return "Bot is running."

if __name__ == '__main__':
    import threading
    threading.Thread(target=telegram_app.run_polling, daemon=True).start()
    app.run(host="0.0.0.0", port=8000)
