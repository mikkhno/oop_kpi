import telebot, wikipedia, re, random
from telebot import types
# Setting the API-ID
bot = telebot.TeleBot('5606399410:AAFghKqT1JV0bWP_cghk87xOEElVZODyrm4')
# Setting the language
wikipedia.set_lang("en")


@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Adding three optional buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Look up...")
    item2 = types.KeyboardButton("Fact")
    item3 = types.KeyboardButton("Random meaning")

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)