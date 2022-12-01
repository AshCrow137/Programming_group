import requests
import lxml.html
import random
from lxml.html import etree



URL = 'http://anekdotov.net/anekdot/'



get_html_text = requests.get(URL)

print(get_html_text)

if get_html_text.status_code == 200 :
    tree = lxml.html.document_fromstring(get_html_text.text)
    print(tree)
    anecdot = tree.xpath('//*[@id="main"]/div[4]/p/text()')
    print(anecdot[0])

    