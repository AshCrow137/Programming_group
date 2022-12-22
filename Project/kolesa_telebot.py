import telebot
from telebot import types
import time


token_file = open('Project/token.txt','rt')
TOKEN = token_file.read()

bot = telebot.TeleBot(TOKEN)

dict_of_models = {'Toyota':['Camry','Land Cruiser', 'Prado,Land','Cruiser','RAV4','Corolla','Estima','Alphard'],
'Volkswargen':['Passat','Golf','Polo','Vento','Transporter','Jetta','Touareg','Tiguan']
}

dict_of_location = {'location':['Алматы', 'Астана', 'Караганда', 'Шымкент', 'Актобе', 'Костанай', 'Атырау']
}


def create_keybord(list_of_buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    for btn_text in list_of_buttons:
        btn = types.KeyboardButton(btn_text)
        markup.add(btn)
    return markup

def choose_model(message):

    markup = create_keybord()
    bot.send_message(message.chat.id,'Выбирите марку')


@bot.message_handler(commands=['start','Start'])
def send_start_message(message):
    markup = create_keybord(['Toyota','Volkswargen'])
    bot.send_message(message.chat.id,'Выбирите марку автомобиля',reply_markup= markup)


@bot.message_handler(content_types=['text'])
def reply_to_all_message(message):
    for model in dict_of_models.keys():
        if message.text == model:
            choose_model(message,model)






def choose_model(message):

    markup = create_keybord()
    bot.send_message(message.chat.id,'Выбирите локацию ')


@bot.message_handler(commands=['location','Location'])
def send_location_message(message):
    markup = create_keybord(['location'])
    bot.send_message(message.chat.id,'Выбирите локацию машины', reply_location= location)


@bot.message_handler(content_types=['text'])
def reply_to_all_message(message):
    for location in dict_of_location.keys():
        if message.text == location:
            choose_model(message,location)






            
            

    

while True:
    try:

        bot.infinity_polling(2)
    except Exception as er:
        print(er)
        time.sleep(2)
        continue


