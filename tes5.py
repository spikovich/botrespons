import logging
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a few command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(f'Hi {user.mention_html()}!', reply_markup=ForceReply(selective=True))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text('Help!')

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Forward the user message to another user."""
    target_chat_id = '-1001861061663'  # Replace with the target user's chat ID
    await context.bot.forward_message(chat_id=target_chat_id, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)

def main() -> None:
    """Start the bot."""
    application = Application.builder().token('6835557447:AAFjD8kFYHvbQ2qn5xV-IzsdOPv4NDRXTHg').build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # on non command i.e. message - forward the message to another user
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
