###1



def to_set(element):
    new_set = set(element)
    return new_set

set1 = to_set([2,4,6,8,10,1,3,2,4,5,6,2,3])    

print(set1)

###2

def tpl_sort(tuple1):
    for num1 in tuple1:
        if type(num1) != type(0):
            
            return tuple1
           
        else:
            pass
    result = sorted(tuple1)
    return result    

tpl1 = {1,2,3,4,56,7,8,91,10,1,2,35,4,6}

print(tpl_sort(tpl1))

###3
def min_max(list1):
    list1 = sorted(list1)
    return list1[0], list1[-1]

print(min_max([1,2,5,4,3,6,8,6,8,1,4,2]))
### 4

def sieve(list_item):

    unique_list = []

    for item in list_item:
        if item not in unique_list:
            unique_list.append(item)
        elif item in unique_list:
            pass

    unique_list = unique_list[::-1]    
    return tuple(unique_list)

print(sieve([1,5,3,3,4,5,2,1]))   


#6

message_info = [{"user_id":1,
"user_first_name":"Alexander",
"user_last_name":"Cheburanov"},
{"message_id":0,
"is_bot":False,
"date":[28,7,2022],
"text":""}
]




def get_message(message_text):
    
    
    if message_text == "/start":
        text_result = "Привет, пользователь!"
        post_message(text_result)
        
    elif message_text == "/help":
        text_result = "Тебе уже ничего не поможет"
        post_message(text_result)
        
    else:

        text_result = "Неизвестная команда"
        post_message(text_result)
        

def post_message(send_text):
   
    create_new_message(send_text,True)
    
    

def write_message():
    input_message = input("Введите команду ")
    create_new_message(input_message,False)
    

def create_new_message(text, is_bot = False):
    
    if is_bot:
        message_info[0]["user_id"] = 0
        message_info[0]['user_first_name'] = "Friend"   
        message_info[0]['user_last_name'] = 'Bot'
        message_info[1]['is_bot'] = True
        message_info[1]['message_id'] += 1
        message_info[1]["text"] = text
        print(message_info)
        print(text)
        
    else:
        message_info[0]["user_id"] = 1
        message_info[0]['user_first_name'] = "Alexander"   
        message_info[0]['user_last_name'] = 'Cheburanov'
        message_info[1]['is_bot'] = False
        message_info[1]['message_id'] += 1
        message_info[1]["text"] = text  
        print(message_info)
        print(text)  

while True:
   
    write_message()
    text = message_info[1]["text"]
    
    get_message(text)
    
{'ok': True,
'result': [{'update_id': 411570277, 
            'message':{ 'message_id': 42, 
                        'from': {'id': 1657060640,
                                 'is_bot': False, 
                                 'first_name': 'Alexandr',
                                 'last_name': 'Cheburanov', 
                                 'username': 'AshhCrow',
                                 'language_code': 'ru'}, 
                         'chat': {'id': 1657060640,
                                  'first_name': 'Alexandr', 
                                  'last_name': 'Cheburanov',
                                  'username': 'AshhCrow',
                                   'type': 'private'},
                         'date': 1658995486, 
                         'text': '/start', 
                         'entities': [{'offset': 0,
                                       'length': 6, 
                                       'type': 'bot_command'
                                       }]
                            }
                }]
}


