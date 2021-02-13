import telebot
from index import get_video

bot = telebot.TeleBot('1641837376:AAEXClROncnQz5_Dkx1fxXy8OJzojt2ZmzA')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    get_video(message.text)
    bot.send_message(message.chat.id, 'Yep')


bot.polling()
