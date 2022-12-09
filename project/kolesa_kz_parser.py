import requests
import glob
import time
import json
import lxml.html
from lxml import etree


def parse_kolesa_kz(car_mark,car_condition,car_model,car_location,car_body):
    URL = f'https://kolesa.kz/cars/{car_mark}{car_condition}{car_model}{car_location}/?auto-car-grbody={car_body}&sort_by=price-asc'
    print(URL)
    get_html_text = requests.get(URL)
    print(get_html_text.status_code)
    if get_html_text.status_code == 200:
        result_list = []
        tree = lxml.html.document_fromstring(get_html_text.text)
        list_of_ads = tree.xpath('//*[@class="a-list"]/div')
        for i in range(1,len(list_of_ads)+1):
            content_ad = tree.xpath(f'//*[@class="a-list"]/div[{i}]/div/div[2]/div[1]/h5/a/@href')
            if content_ad:
                result_list.append('https://kolesa.kz/'+content_ad[0])
        #content = tree.xpath('//*[@id="advert-145743989"]/div[2]/div[1]/h5/a/@href')
        #'//*[@id="advert-145984145"]/div[2]/div[1]/h5/a'
        return result_list
    else:
        return 'Не удалось подключиться к сайту'

car_mark = ''
car_condition = 'novye-avtomobili/'
car_model = ''
car_location = 'astana/'
car_body = 2

result =parse_kolesa_kz(car_mark,car_condition,car_model,car_location,car_body)
print(result)