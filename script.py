from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
 update.message.reply_text("I'm Nyako-sensei, Nice to meet you")

def convert_uppercase(bot,update):
 update.message.reply_text(update.message.text.upper())

def main():
 global updater
 updater = Updater('780760981:AAGUB_ZJ9qg7RAzwCNGE9tX1mv6katD2HhI')
 dispatcher = updater.dispatcher
 print('Bot started')
 start_handler = CommandHandler('start',start)
 upper_case = MessageHandler(Filters.text, convert_uppercase)
 dispatcher.add_handler(start_handler)
 dispatcher.add_handler(upper_case)
 updater.start_polling()
 updater.idle()

if __name__ == "__main__":
 main()
