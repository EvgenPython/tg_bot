from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update
from tok import t

def start(update=Update, context=CallbackContext):
    update.message.reply_text('Hi user')
def echo(update=Update, context=CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(t)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


main()
