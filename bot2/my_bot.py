
import telebot
from telebot import types

token_file = open('bot2/token.txt','rt',encoding='utf-8')
token = token_file.read()
token_file.close()

bot = telebot.TeleBot(token)


@bot.message_handler(commands= ['start','Start','Greetings','greetings'])
def greetings(message):
    text = f'Привет, {message.from_user.username}. Рад тебя видеть!'
    # bot.send_message(message.chat.id,text)
    bot.reply_to(message,text)

@bot.message_handler(content_types=['sticker'])
def reply_to_stiker(message):
    bot.send_message(message.chat.id,'Клевый стикер!')



@bot.message_handler(content_types= ['text'])
def reply_to_all(message):
    bot.send_message(message.chat.id,'Нет такой команды!')
    


bot.infinity_polling(1)
