import telebot
import time
from telebot import types


token_file = open('Project/token.txt','rt')
TOKEN = token_file.read()
token_file.close()

bot = telebot.TeleBot(TOKEN)

dict_of_models = {
'Toyota':['Camry','Land Cruiser Prado','Land Cruiser','RAV4','Corolla','Estima','Alphard'],
'Volkswagen':['Passat','Golf','Polo','Vento','Transporter','Jetta','Touareg','Tiguan']
}

list_of_locations = ['Алматы', "Астана"]

MARK = None
MODEL = None
LOCATION = None

def create_keyboard(list_of_buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    for btn_text in list_of_buttons:
        btn = types.KeyboardButton(btn_text)
        markup.add(btn)
    return markup

def choose_model(message,mark):

    markup = create_keyboard(dict_of_models[mark])
    bot.send_message(message.chat.id,'Выберите модель автомобиля',reply_markup=markup)


@bot.message_handler(commands=['start','Start'])
def send_start_message(message):
    markup = create_keyboard(['Toyota','Volkswagen'])
    bot.send_message(message.chat.id,'Выберите марку автомобиля',reply_markup= markup)

@bot.message_handler(content_types=['text'])
def reply_to_all_message(message):
    for mark in dict_of_models.keys():
        if message.text == mark:
            global MARK
            MARK = mark
            choose_model(message,mark)
    if message.text in dict_of_models[MARK]:
        for model in dict_of_models[MARK]:
            if message.text == model:
                global MODEL
                MODEL = model
                print(MARK, MODEL)

while True:
    try:

        bot.infinity_polling(2)
    except Exception as er:
        print(er)
        time.sleep(2)    
        continue

token_file = open('Project/token.txt','rt',encoding='utf-8')
token = token_file.read()
token_file.close()

bot = telebot.TeleBot(token)
dict_of_models = {'Toyota': ['Camry', 'Land Cruiser Prado',' Land Cruiser','RAV4', 'Corolla', 'Estima', 'Alphard'],
'Volkswagen': ['Passat','Golf','Polo','Vento','Transporter','Jetta','Touareg','Tiguan'] }

def create_keyboard(list_of_buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for btn_text in list_of_buttons:
        btn = types.KeyboardButton(btn_text)
        markup.add(btn)
    return markup

def choose_model(message, mark):

    markup = create_keyboard(dict_of_models[mark])
    bot.send_message(message.chat.id, 'выберите модель авто', reply_markup=markup)

@bot.message_handler(commands= ['start','Start'])
def send_start_message(message):
    markup = create_keyboard(['Toyota','Volkswagen'])
    bot.send_message(message.chat.id, 'выберите марку авто', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def reply_to_all_message(message):
    for model in dict_of_models.keys():
        if message.text == model:
            choose_model(message, model)

while True:
    try:
        bot.infinity_polling(2)
    except Exception as er:
        print(er)
        time.sleep(2)
        continue