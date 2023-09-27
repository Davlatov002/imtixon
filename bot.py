import os
from dotenv import load_dotenv
import telebot
from telebot import types
import django
django.setup()
from malumotapp.models import Malumot

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
sarlavhalar = []
malumotlar = []

def data_cell():
    db = Malumot.objects.all()
    malumott: Malumot
    for malumott in db:
        sarlavhalar.append(malumott.nomi)
        malumotlar.append(malumott.malumot)
data_cell()


def start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    b = []
    for i in sarlavhalar:
        b.append(types.KeyboardButton(text=i))
        keyboard.add(types.KeyboardButton(text=i),)

    return keyboard
    
@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
  bot.send_message(message.from_user.id,"Bulardan birini tanlang.", 
                   reply_markup=start_keyboard())

@bot.message_handler()
def malumotber(msg: types.Message):
    for i in sarlavhalar:
      match msg.text:
         case i:
            xabar = malumotlar[sarlavhalar.index(i)]
    bot.send_message(msg.from_user.id, f"{xabar}")

bot.infinity_polling()