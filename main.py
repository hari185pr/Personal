import os
import json
import random
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import threading

# Load waifu dataset from trimmed 9000 list
with open("waifus_9000.json", "r", encoding="utf-8") as f:
    WAIFUS = json.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 WaifuEmpireBot is running!"

# Get your bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to WaifuEmpireBot!\nUse /roll to get your waifu!")

# Command: /roll
async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    waifu = random.choice(WAIFUS)
    name = waifu.get("name", "Unknown Waifu")
    image = waifu.get("image_url")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("❤️ Favorite", callback_data="fav_waifu")]
    ])

    if image:
        await update.message.reply_photo(photo=image, caption=f"You got: {name}", reply_markup=keyboard)
    else:
        await update.message.reply_text(f"You got: {name}", reply_markup=keyboard)

def run_bot():
    app_builder = ApplicationBuilder().token(BOT_TOKEN).build()
    app_builder.add_handler(CommandHandler("start", start))
    app_builder.add_handler(CommandHandler("roll", roll))
    app_builder.run_polling()

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))).start()
    run_bot()