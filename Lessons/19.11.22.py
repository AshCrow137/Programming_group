def get_message(user_id,name,last_name,text):
    user_message = message.copy()
    user_message[0]['user_id'] = user_id
    user_message[0]['user_first_name'] = name
    user_message[0]['user_last_name'] = last_name
    user_message[1]['message_id'] = user_message[1]['message_id'] +1
    user_message[1]['date'] = [19,11,2022]
    user_message[1]['text'] = text

    return user_message

def commands(message):
    text = message[1]['text']
    if text == '/start':
        user_fn = message[0]['user_first_name']
        print(current_message(1,'Bot','Bob',f'приветствую, {user_fn}'))

    elif text == '/help':
        print(get_message(1,'Bot','Bob','/start \n /help\n/hello'))
    elif text == '/hello':
        print(get_message(1,'Bot','Bob','Пивет! Я пока ничешо не умею, но когда нибудь научусь'))
    else:
        print(get_message(1,'Bot','Bob','Вы ввели недоступную команду,попробуйте /help'))


message =[{"user_id":None,
"user_first_name":None,
"user_last_name":None},
{"message_id":0,
"is_bot":False,
"date":None,
"text":None}
]

current_message = get_message(0,'Alex', 'Cheb',input())
print(current_message)
commands(current_message)
