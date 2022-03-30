import telebot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("Ayat.json")
firebase_admin.initialize_app(cred,{
  "databaseURL":"https://i-telegram-bot-d4116-default-rtdb.firebaseio.com/"
})
ref = db.reference()

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def handle_start(message):
    time = ref.child('zapis').get()
    for key, value in time.items():
      if key == "10:00":
        bot.send_message(message.from_user.id, "10:00" + value['name'])
      elif key == "11:00":
        bot.send_message(message.from_user.id, "11:00" + value['name'])
      elif key == "12:00":
        bot.send_message(message.from_user.id, "12:00" + value['name'])
      elif key == "13:00":
        bot.send_message(message.from_user.id, "13:00" + value['name'])
      elif key == "14:00":
        bot.send_message(message.from_user.id, "14:00" + value['name'])
      elif key == "15:00":
        bot.send_message(message.from_user.id, "15:00" + value['name'])
      elif key == "16:00":
        bot.send_message(message.from_user.id, "16:00" + value['name'])
      elif key == "17:00":
        bot.send_message(message.from_user.id, "17:00" + value['name'])
      elif key == "18:00":
        bot.send_message(message.from_user.id, "18:00" + value['name'])
      elif key == "19:00":
        bot.send_message(message.from_user.id, "19:00" + value['name'])
      else:
        bot.send_message(message.from_user.id, "No one signed up for this time.\nYOU CAN TAKE A REST")

bot.polling()