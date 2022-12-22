import requests
import glob
import time
import json
import lxml.html
from lxml import etree


def parse_kolesa_kz(car_mark,car_condition,car_model,car_location,car_body):
    URL = f'https://kolesa.kz/cars/{car_mark}{car_condition}{car_model}{car_location}/?auto-car-grbody={car_body}&sort_by=price-asc'
    get_html_text = requests.get(URL)
    if get_html_text.status_code == 200:
        tree = lxml.html.document_fromstring(get_html_text.text)
        content = tree.xpath('//*[@id="results"]/div/div[5]/div')
        # content = tree.xpath('//*[@id="advert-145743989"]/div[2]/div[1]/h5/a/@href')
        print(content)
    else:
        return  'не удалось подключиться к сайту'


car_mark = 'toyota/'
car_condition = 'novye-avtomobili/'
car_model = 'corolla/'
car_location = 'astana/'
car_body = 1

parse_kolesa_kz(car_mark,car_condition,car_model,car_location,car_body)