import os
import logging
from scrapper import devto, tldrData, get_quote
from keep_alive import keep_alive
import responses
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

# Getiing bot token from env file
load_dotenv()
Bot_Token = os.getenv('Bot_Token')


'''
💡Use this version if you deploying it on repl.it
Add the bot token in secretes section
# Getiing bot token from env file
  Bot_Token = os.environ['Bot_Token']
'''


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


# We defined this fuction to use as commands
# all update.message are reply from bots to user
def start(update, context):
    update.message.reply_text(
        "Good day there, I'm a bot that can communicate with you. You can get the most up-to-date tech news from devto or tldr, and more services will be added shortly..\n To start, say hey, hi, or hello.\n Get all Commands -/cmd")


def cmd(update, context):
    update.message.reply_text(
        '/tldr - TLDR tech news\n/devto-Devto todays popular artical\n/quotes - Random quotest')


def quote(update, context):
    data = get_quote()
    update.message.reply_text(data)


# tldr new
def tldr(update, context):
    data = tldrData()
    update.message.reply_text(data)

# devto News


def devTo(update, context):
    data = devto()
    # reply_keyboard = [['Today,s Top', 'Latest',]]
    #   reply_markup=ReplyKeyboardMarkup(
    #           reply_keyboard, one_time_keyboard=True
    #   )
    update.message.reply_text(data)


# there two methods to crete functions to get repond from bot this is 2nd one


def socials(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="List of Socails are down below:\n {Github} https://github.com/amrohan\n\n {Twitter} https://twitter.com/rohansalunkhe_\n\n {Instagram} https://www.instagram.com/amrohann\n\n {Email} amrohanx@gmail.com")


def source_code(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="the source code can be accessed here\n {Replit}\n https://replit.com/@amrohan/chatbot")


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programms from here
if __name__ == '__main__':
    updater = Updater(Bot_Token, use_context=True)
    dp = updater.dispatcher

    # Commands handler which callback our commands when user ask for it
    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(CommandHandler('cmd', cmd))

    dp.add_handler(CommandHandler('socials', socials))

    dp.add_handler(CommandHandler('source_code', source_code))

    dp.add_handler(CommandHandler('quotes', quote))
    # tldr handler
    dp.add_handler(CommandHandler('tldr', tldr))
    # Dev To
    dp.add_handler(CommandHandler('devto', devTo))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    keep_alive()
    # Run the bot
    updater.start_polling(1.0)
    # Idle state give bot time to go in idle
    updater.idle()
