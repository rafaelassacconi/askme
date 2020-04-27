#!/usr/bin/python
"""
AskMe simple bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Run 'python askme_telegram_bot.py' to start the bot.
Send messages to '@askme_telegram_bot' on Telegram.
Press Ctrl-C on the command line to stop.
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from search import Search


TOKEN = "1281311316:AAHhWrf-X0IL5pBQ89CM6zXKJg45RX7F0lI"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def echo(update, context):
    """ Echo the message to user """
    msg = "Hi, my name is AskMe! I'm a bot that can search for you\
        questions and answers on the internet. Let's start?\
        \n\nWrite me /search and some keywords. Example:\
        \n\n/search keyword1 keyword2"
    update.message.reply_text(msg)


def error(update, context):
    """ Log Errors caused by Updates """
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def search(update, context):
    """ Send the search result when the command /search is issued """
    if not context.args:
        msg = "Sorry, I didn't find the keyworkds.\
            Just write me /search and some keywords. Example:\
            \n\n/search keyword1 keyword2"
        update.message.reply_text(msg)
    else:
        update.message.reply_text("Searching...")
        keywords = " ".join(context.args)

        # Call generic search
        result = Search(keywords).by_keywords()

        # No results
        if not result:
            update.message.reply_text("I didn't find anything with that keywords.")

        # Show the results
        else:
            update.message.reply_text("Here's what I found to you:")
            
            msg = ""
            for n, item in enumerate(result, 1):
                msg += "\nQuestion %d: %s\n" % (n, item["title"])
                msg += "Votes: %s\n" % item["score"]
                msg += "Link: %s \n" % item["link"]
            update.message.reply_text(msg)


def askme_telegram_bot():
    """ Starts the Telegram bot """
    # Create the Updater with the bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("search", search))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    askme_telegram_bot()
