
import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update, Bot
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! WaifuEmpireBot is ready.")

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 You rolled a random waifu!")

def run_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("roll", roll))
    application.run_polling()

if __name__ == "__main__":
    import threading

    threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    ).start()

    run_bot()
    
