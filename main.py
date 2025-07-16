import json
import random
import os
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
from telegram import Update, InputMediaPhoto

# Load waifus from file
with open("waifus_safe_100.json", "r", encoding="utf-8") as f:
    waifus = json.load(f)

# Bot token (don't hardcode in real use)
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Make sure it's set in Railway or .env

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 Welcome to WaifuEmpireBot! Use /roll to get a waifu!")

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    waifu = random.choice(waifus)
    try:
        await update.message.reply_photo(
            photo=waifu["image_url"],
            caption=f"💖 You got: {waifu['name']} ({waifu['rarity']})"
        )
    except Exception as e:
        print(f"Error sending image: {e}")
        await update.message.reply_text(f"💖 You got: {waifu['name']} (No image)")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("roll", roll))
    app.run_polling()
