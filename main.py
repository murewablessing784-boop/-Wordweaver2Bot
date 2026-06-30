import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# --- Configuration ---
logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN environment variable not set!")

# --- Bot Handlers ---
async def start(update, context):
    """Handles the /start command."""
    await update.message.reply_text("👋 Hello! I'm Wordweaver2Bot, your text assistant. Send me a message!")

async def echo(update, context):
    """Echoes any non-command message."""
    await update.message.reply_text(f"📝 You said: {update.message.text}")

# --- Main Function ---
def main():
    """Starts the bot using long polling."""
    print("🚀 Starting Wordweaver2Bot with long polling...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("✅ Bot is running! Press Ctrl+C to stop.")
    app.run_polling()  # Uses long polling - no public URL needed

if __name__ == "__main__":
    main()
