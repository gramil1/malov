import telebot, os
from dotenv import load_dotenv 

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(content_types=['text']) 

def get_text(message):
    if message.text == "Привет": 
        bot.send_message(message.from_user.id, "Здравствуй, мой дорогой друг!") 
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напиши: Привет")
    else:
        bot.send_message(message.from_user.id, "я тебя не понимаю, напиши '/help'")
        
bot.polling(none_stop=True, interval=0)