import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(rf'Hi {user.mention_html()}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Help!')
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_chat_id = 'TARGET_CHAT_ID'  # Replace with the target user's chat ID
    await context.bot.forward_message(chat_id=target_chat_id, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)
def main() -> None:
    application = Application.builder().token('YOUR_BOT_TOKEN').build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    # Run the bot
    application.run_polling()
if __name__ == "__main__":
    main()