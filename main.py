import logging
from telegram.ext import *
import responses

API_KEY = '1813838776:AAHxa_rWaY_7ReJqLV298TmyPEfhA-k_3Eg'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hello there, I\'m an AI bot who can converse with you or assist you in completing tasks.\n To start, say hey, hi, or hello.')


def help_command(update, context):
    update.message.reply_text('Type cmd for options or click /cmd')


def cmd_command(update, context):
    update.message.reply_text('Availble Commands:\nFor notes- /notes\n ')
    
def notes_command(update, context):
    update.message.reply_text('Soon, you\'ll be able to get your hands on some notes.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    
    dp.add_handler(CommandHandler('help', help_command))
    
    dp.add_handler(CommandHandler('cmd', cmd_command))
    
    dp.add_handler(CommandHandler('notes', notes_command))
    

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()