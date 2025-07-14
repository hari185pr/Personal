import os
from flask import Flask
from telegram import Update, Bot
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes

app = Flask(__name__)

@app.route('/')
def keep_alive():
    return "Bot is running!"

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! WaifuEmpireBot is ready.")

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 You rolled a random waifu!")

def run_bot():
    appbuilder = ApplicationBuilder().token(BOT_TOKEN).build()
    appbuilder.add_handler(CommandHandler("start", start))
    appbuilder.add_handler(CommandHandler("roll", roll))
    appbuilder.run_polling()

if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))).start()
    run_bot()
