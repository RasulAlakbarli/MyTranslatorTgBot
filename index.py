from Languages import Languages
import telebot
from telebot import types
from googletrans import Translator

token = '5255716099:AAG63R3cwT4hcEpPg3N1dCy5e5GHoxTykxA'

global bot
bot = telebot.TeleBot(token)
global translator
transl = Translator()

def myBot(token):
        
    @bot.message_handler(commands=['start', 'info'])
    def greeting(message):
        bot.send_message(message.chat.id, "Welcome to translator bot.\nType '/langs' for choosing a language")

    @bot.message_handler(commands= ['langs'])
    def choises(message):
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_eng = types.KeyboardButton('En')
        item_ru = types.KeyboardButton('Ru')
        item_tr = types.KeyboardButton('Tr')
        item_az = types.KeyboardButton('Az')
        item_french = types.KeyboardButton("Fr")
        markup_reply.add(item_eng, item_ru, item_french, item_tr, item_az)

        bot.send_message(message.chat.id, "Pick a language:", reply_markup=markup_reply)

    @bot.message_handler(content_types=['text'])
    def language(message):

        # lang = None
        
        if message.text.lower() in Languages:
            bot.send_message(message.chat.id, f"Your text will be translated into {Languages[message.text.lower()]}")
            global lang
            lang = message.text.lower()
        else:
            pass
            # lang = NULL
            # bot.send_message(message.chat.id, "Couldn't recognise the language, try again!")

        if message.text.lower() in Languages:
            pass
        else:
            try:
                bot.reply_to(message, transl.translate(message.text, dest=lang).text)
            except Exception as ex:
                bot.send_message(message.chat.id, "Something went wrong...Try again.")

        print(message.text)

    bot.polling(non_stop=True)

if __name__ == '__main__':
    myBot(token)
