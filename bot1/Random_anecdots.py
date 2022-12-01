import lxml.html
import requests
import random
from lxml import etree

def get_all_anekdots(html_text):
    tree = lxml.html.document_fromstring(html_text)
    anekdot_list = tree.xpath('//*[@id="main"]/div')
    content = []
    for i in range(1,len(anekdot_list)):
        anekdot = tree.xpath(f'//*[@id="main"]/div[{i}]/p/text()')
        content.append(anekdot)
    return content

def get_anecdot():

    get_html_text = requests.get("http://anekdotov.net/anekdot/")

    while True:
        if get_html_text.status_code ==200:
            all_anekdots = get_all_anekdots(get_html_text.text)
            anekdot = all_anekdots[random.randint(0,len(all_anekdots)-1)]
            if anekdot:

                # anekdot_file = open('anekdot.txt','wt')
                # anekdot_file.write('')
                # anekdot_file = open('anekdot.txt','at')
                full_anekdot = ''
                for anekdot_str in anekdot:
                    full_anekdot = full_anekdot + anekdot_str
                    
                    
                #     anekdot_file.write(anekdot_str)
                    
                    
                # anekdot_file.close()
                break
            else:
                continue
    return full_anekdot        
   
   