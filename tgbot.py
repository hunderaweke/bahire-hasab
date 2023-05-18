import telebot
from telebot import apihelper
bot = telebot.TeleBot(
    "6002411857:AAGO3sWXOSqM712bJCnrIdZXo3QL_uzp7jA", parse_mode=None)
apihelper.proxy = {'https': 'socks5://@51.222.13.193:10084'}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to my bot!!!!")


@bot.message_handler(func=lambda x: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
