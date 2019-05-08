from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from TranslateWithServing import translatorAI

def start(bot, update):
 update.message.reply_text("I'm Nyako-sensei, Nice to meet you")

def translate(bot,update):
  string=update.message.text[11:]
  update.message.reply_text("It may take some minutes ...")
  update.message.reply_text("Translate: \n"+translatorAI(string))


def main():
 global updater
 updater = Updater('780760981:AAGUB_ZJ9qg7RAzwCNGE9tX1mv6katD2HhI')
 dispatcher = updater.dispatcher
 print('Bot started')
 start_handler = CommandHandler('start',start)
 translate_handler = CommandHandler('translate', translate)
 dispatcher.add_handler(start_handler)
 dispatcher.add_handler(translate_handler)
 updater.start_polling()
 updater.idle()

if __name__ == "__main__":
 main()
