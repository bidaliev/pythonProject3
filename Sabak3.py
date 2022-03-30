import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import telebot
from telebot import types

cred = credentials.Certificate('Ayat.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://i-telegram-bot-d4116-default-rtdb.firebaseio.com/"})
ref = db.reference()

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Atin kim?')
    sent = bot.send_message(message.chat.id, 'uakit?')
    bot.register_next_step_handler(sent, soz)


@bot.message_handler(content_types=['text'])
def soz(message):
    if message == "":
        bot.send_message(message.chat.id, "Прошел")
    else:
        user = message.text
        print(user)
        contains = ref.child('Register').child('name' ).get()
        cStr = "" + str(contains)
        if cStr == "None":
            user_ref = ref.child('Register').child('name')
            user_ref.set(user)
            bot.reply_to(message, "Прошел")


bot.polling(none_stop=True)