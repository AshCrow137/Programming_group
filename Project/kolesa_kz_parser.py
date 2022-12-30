import requests
import glob
import time
import json
import lxml.html
from lxml import etree

def car_informations(url):   
    car_information_values = []
    car_characteristics= []
    get_html_text = requests.get(url)

    if get_html_text.status_code == 200:
        tree = lxml.html.document_fromstring(get_html_text.text)
        list_of_info=tree.xpath('//*[@class="offer__parameters"]/dl')
        print(url)
        for i in range(1,len(list_of_info)+1):
            car_values = tree.xpath(f'//*[@class="offer__parameters"]/dl[{i}]/dd/text()')
            car_keys = tree.xpath(f'//*[@class="offer__parameters"]/dl[{i}]/dt/span/text()')
            car_characteristics.append(car_keys[0])
            car_information_values.append(car_values[0].strip())
        info_dict = zip(car_characteristics ,car_information_values)
        
        return dict(info_dict)



def parse_kolesa_kz(car_mark,car_condition,car_model,car_location,car_body):
    URL = f'https://kolesa.kz/cars/{car_mark}{car_condition}{car_model}{car_location}?auto-car-grbody={car_body}&sort_by=price-asc'
    print(URL)
    get_html_text = requests.get(URL)
    print(get_html_text.status_code)
    if get_html_text.status_code == 200:

        result_list = []
        tree = lxml.html.document_fromstring(get_html_text.text)
        list_of_ads = tree.xpath('//*[@class="a-list"]/div')
        # '//*[@class="a-list"]/div'
        # '/html/body/main/div/div/div/section/div[1]/div[1]/div[2]/dl[1]/dt/span'
        print(list_of_ads)
        for i in range(1,len(list_of_ads)+1):
            content_ad = tree.xpath(f'//*[@class="a-list"]/div[{i}]/div/div[2]/div[1]/h5/a/@href')
            if content_ad:
                result_list.append('https://kolesa.kz'+content_ad[0])
        return result_list
    else:
        return 'Не удалось подключиться к сайту'
dict1 = car_informations('https://kolesa.kz/a/show/145935402')
text = ''
for key in dict1:
    text = text + f'{key} ---> {dict1[key]}\n'
       
print(text)