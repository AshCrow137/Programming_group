import requests
import glob
import time
import json
import lxml.html
from lxml import etree

def car_informations(): 
    car_characteristic = {
        'город': None,
        "поколение":None,
        "кузов":None,
        "объем двигателя":None,
        "пробег":None,
        "коробка передач":None,
        "привод":None,
        "руль":None,
        "цыет":None,
        "растаможен в Казахстане":None
    }
    URL = result_list[0]
    print(URL)
    get_html_text = requests.get(URL)
    print(get_html_text.status_code)
    if get_html_text.status_code == 200:
        tree = lxml.html.document_fromstring(get_html_text.text)
        list_of_info=tree.xpath('//*[@class="offer__parameters"]/dl')
        for i in range(1,len(list_of_info)+1):
            car_info = tree.xpath(f'//*[@class="offer__parameters"]/dl[{i}]/dd/text()')

            print(car_info[0])
        
 
def parse_kolesa_kz(car_mark,car_condition,car_model,car_location,car_body):
    URL = f'https://kolesa.kz/cars/{car_mark}{car_condition}{car_model}{car_location}?auto-car-grbody={car_body}&sort_by=price-asc'
    print(URL)
    get_html_text = requests.get(URL)
    print(get_html_text.status_code)
    if get_html_text.status_code == 200:
        global result_list
        result_list = []
        tree = lxml.html.document_fromstring(get_html_text.text)
        list_of_ads = tree.xpath('//*[@class="a-list"]/div')
        for i in range(1,len(list_of_ads)+1):
            content_ad = tree.xpath(f'//*[@class="a-list"]/div[{i}]/div/div[2]/div[1]/h5/a/@href')
            if content_ad:
                result_list.append('https://kolesa.kz/'+content_ad[0])
        return result_list
    else:
        return 'Не удалось подключиться к сайту'


car_mark = ''
car_condition = 'novye-avtomobili/'
car_model = ''
car_location = 'astana/'
car_body = 2

result = parse_kolesa_kz(car_mark,car_condition,car_model,car_location,car_body)
print(result)

car_informations()


