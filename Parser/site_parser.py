import requests
import lxml.html
import random
from lxml.html import etree



URL = 'http://anekdotov.net/anekdot/'
Kinopoisk = 'https://www.kp.ru/afisha/msk/obzory/kino/luchshie-filmi-uzhasov/'


get_html_text = requests.get(Kinopoisk)

print(get_html_text)

if get_html_text.status_code == 200 :
    tree = lxml.html.document_fromstring(get_html_text.text)
    print(tree)
    content_list = tree.xpath('/html/body/div/div[3]/div/div[2]/div/div[6]/div/h3')
    list_of_films = []
    for i in range(1,len(content_list)+1):
        content = tree.xpath(f'/html/body/div/div[3]/div/div[2]/div/div[6]/div/h3[{i}]/text()')
        list_of_films.append(content[0] + '\n')
    
    list_of_films = list_of_films[::-1]

    film_file = open('Parser/film_file.txt','wt',encoding='utf-8')
    for str in list_of_films:
        film_file.write(str)
    
    film_file.close()

    # anecdot = tree.xpath('//*[@id="main"]/div[4]/p/text()')
    # print(anecdot[0])


    