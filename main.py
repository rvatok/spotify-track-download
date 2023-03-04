import os
from telegram.ext import Updater, CommandHandler

# Initialize the bot
TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
updater = Updater(token=TOKEN, use_context=True)

# Add a command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a bot!")

updater.dispatcher.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()
