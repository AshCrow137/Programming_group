import telebot
import time
from telebot import types
import kolesa_kz_parser

token_file = open('Project/token.txt','rt')
TOKEN = token_file.read()
token_file.close()

bot = telebot.TeleBot(TOKEN)

dict_of_models = {
'Toyota':['Camry','Land Cruiser Prado','Land Cruiser','RAV4','Corolla','Estima','Alphard'],
'Volkswagen':['Passat','Golf','Polo','Vento','Transporter','Jetta','Touareg','Tiguan']
}

list_of_locations = {'Алматы':'almaty', "Астана":'astana'}

dict_of_conditions = {'Новые автомобили':'novye-avtomobili','Автомобили с пробегом':'avtomobili-s-probegom'}
dict_of_bodies = {'легковые':1,'внедорожники и пикапы':2,'минивены и микроавтобусы':3}

"легковые"
"Внедорожники и пикапы"
"Минивены и микроавтобусы"




MARK = None
MODEL = None
LOCATION = None
CAR_CONDITION = None
CAR_BODY = None

def create_keyboard(list_of_buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    for btn_text in list_of_buttons:
        btn = types.KeyboardButton(btn_text)
        markup.add(btn)
    return markup

def choose_model(message,mark):
    markup = create_keyboard(dict_of_models[mark])
    bot.send_message(message.chat.id,'Выберите модель автомобиля',reply_markup=markup)

def choose_location(message):
    markup = create_keyboard(list(list_of_locations.keys()))
    bot.send_message(message.chat.id,'Выберите местоположение автомобиля',reply_markup= markup)

def choose_condition(message):
    markup = create_keyboard(list(dict_of_conditions.keys()))
    bot.send_message(message.chat.id,'Выберите состояние автомобиля',reply_markup=markup)
def choose_body(message):
    markup = create_keyboard(list(dict_of_bodies.keys()))
    bot.send_message(message.chat.id,'Выберите тип кузова',reply_markup=markup)


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
                MODEL = model + '/'
                MODEL = MODEL.lower()
                MODEL = MODEL.replace(' ','-')
                choose_location(message)
    if message.text in list(list_of_locations.keys()):
        for city in list_of_locations:
            if message.text == city:
                global LOCATION
                LOCATION = list_of_locations[city] + '/'
                choose_condition(message)
    if message.text in list(dict_of_conditions.keys()):
        for key in dict_of_conditions:
            if message.text == key:
                global CAR_CONDITION
                CAR_CONDITION = dict_of_conditions[key] + '/'
                choose_body(message)
    if message.text in list(dict_of_bodies.keys()):
        for key in dict_of_bodies:
            if message.text == key:
                global CAR_BODY
                CAR_BODY = dict_of_bodies[key]
                print(MARK,MODEL,LOCATION,CAR_CONDITION,CAR_BODY)        
    if MARK and MODEL and LOCATION and CAR_CONDITION and CAR_BODY:
        MARK= MARK.lower()
        list_of_ads = kolesa_kz_parser.parse_kolesa_kz(MARK + '/',CAR_CONDITION,MODEL,LOCATION,CAR_BODY)
        MARK = MODEL = LOCATION = CAR_BODY = CAR_CONDITION = None
        if list_of_ads and len(list_of_ads)>=10:
            
            for ad in list_of_ads[:10]:
                text = ''
                ad_info = kolesa_kz_parser.car_informations(ad)
                ad_text = ''
                for key in ad_info:
                    ad_text = ad_text + key + '--->' + ad_info[key] + '\n'
                text = text+ ad +'\n' + ad_text + '\n'
                bot.send_message(message.chat.id,text,reply_markup=types.ReplyKeyboardRemove())
        elif list_of_ads:
            bot.send_message(message.chat.id,str(list_of_ads))
        else:
            bot.send_message(message.chat.id,'Не удалось найти объявлений по вашему запросу. Попробуйте заново \n/start')
while True:
    try:

        bot.infinity_polling(2)
    except Exception as er:
        print(er)
        time.sleep(2)    
        continue

