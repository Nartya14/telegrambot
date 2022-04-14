import telebot # вариант подсчета ИС c двумя кнопками на имени
from telebot import types

bot = telebot.TeleBot('5281680066:AAHD5QzDAii53Y0cMTjECvMtkL-GMhnxTlM')

itog = 0

@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.from_user.id, f"""<b>{message.from_user.first_name}</b>, вот тебе моя подсказка:
    
<b>Субъектная оптимизация.</b> На каждый условный запрос необходимо предоставить эквивалентный адресный результат.

<b>Иерархическая оптимизация.</b> Сбор информации должен осуществляться максимально близко к непосредственному носителю.

<b>Функциональная оптимизация.</b> Исключить повторное привлечение субъектов к процессам, информация в рамках которых в наличии и актуальна, предоставлять существующую информацию по внешним запросам без привлечения субъектов.

<b>Информационная автономность процессов.</b> Информация, предоставляемая субъектами, должна оставаться у них как в том виде, в котором она была предоставлена, так и в обработанном виде. При этом сам процесс сбора не должен дробиться на сбор и предоставление, а разрабатываться сразу как двусторонний.

<b>Централизация информации.</b>. При планировании работы необходимо максимально обеспечить соответствие запрашиваемой информации существующей системе хранения или предусматривать возможность изменения системы для интеграции новой информации.

<b>Автоматизация процессов.</b> При планировании работы необходимо рассматривать все доступные варианты автоматизации, начиная с наиболее подходящего существующей системе хранения. Прибегать к ручному сбору и обработке можно только в исключительных случаях.

<b>Документация процессов.</b> Ключевые, постоянные процессы должны быть детально описаны. Доступ к документации должен быть открыт внутри организации для минимизации рисков.
    
    """, parse_mode= "HTML")
    bot.send_message(message.from_user.id, 'Если моя подсказка помогла тебе, то в ответ можешь написать мне <i>"Спасибо".</i>', parse_mode= "HTML");

@bot.message_handler(commands=['start'])
def welcome_start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, f'Привет, <b>{message.from_user.first_name}!</b>', parse_mode= "HTML")
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='Да')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='Нет')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, 'Ты хочешь посчитать ИС выполненной задачи?', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Напиши "/start"!', parse_mode= "HTML")

@bot.message_handler(content_types=['text'])
def messay(message):
    if message.text == 'Спасибо':
        bot.send_message(message.from_user.id, 'Рад помочь! Забудешь - пиши! :)')
    else:
        bot.send_message(message.from_user.id, 'Ничего не понимаю! Напиши мне "/start" или "/help".')

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(call):
    if call.data == 'Да':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"""Не забудь, что ответом является цифра :
    <b>0</b> - не соответствует требованиям;
    <b>1</b> - частично соответсвует;
    <b>2</b> - полностью не соответствует.
    Если тебе нужна подсказка, то просто напиши мне <b>'Подсказка'</b>""", parse_mode= "HTML")
        bot.send_message(call.message.chat.id, 'Субъектная оптимизация')
        bot.register_next_step_handler(call.message, get_ind1)
    else:
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Ну ладно, заходи позже :(')

def get_ind1(message): #получаем ответ на вопрос 1  
    if message.text.isdigit(): #проверяем является ли ответ числом
        global itog
        itog += int(message.text)
        bot.send_message(message.from_user.id, 'Иерархическая оптимизация')
        bot.register_next_step_handler(message, get_ind2)
        return
    elif message.text.isalpha(): #проверяем является ли ответ текстом
        bot.send_message(message.from_user.id, '<b>Субъектная оптимизация.</b> На каждый условный запрос необходимо предоставить эквивалентный адресный результат.', parse_mode= "HTML")
        bot.send_message(message.from_user.id, 'Введи значение заново')
        bot.register_next_step_handler(message, get_ind1)
    else:    
        return

def get_ind2(message): #получаем ответ на вопрос 2
    if message.text.isdigit(): #проверяем является ли ответ числом
        global itog
        itog += int(message.text)
        bot.send_message(message.from_user.id, 'Функциональная оптимизация')
        bot.register_next_step_handler(message, get_ind3)
        return
    elif message.text.isalpha(): #проверяем является ли ответ текстом        
        bot.send_message(message.from_user.id, '<b>Иерархическая оптимизация.</b> Сбор информации должен осуществляться максимально близко к непосредственному носителю.', parse_mode= "HTML")
        bot.send_message(message.from_user.id, 'Введи значение заново')
        bot.register_next_step_handler(message, get_ind2)
    else:    
        return

def get_ind3(message): #получаем ответ на вопрос 3
    if message.text.isdigit(): #проверяем является ли ответ числом
        global itog
        itog += int(message.text)
        bot.send_message(message.from_user.id, 'Информационная автономность процессов')
        bot.register_next_step_handler(message, get_ind4)
        return
    elif message.text.isalpha(): #проверяем является ли ответ текстом 
        bot.send_message(message.from_user.id, '<b>Функциональная оптимизация.</b> Исключить повторное привлечение субъектов к процессам, информация в рамках которых в наличии и актуальна, предоставлять существующую информацию по внешним запросам без привлечения субъектов.', parse_mode= "HTML")
        bot.send_message(message.from_user.id, 'Введи значение заново')
        bot.register_next_step_handler(message, get_ind3)
    else:    
        return

def get_ind4(message): #получаем ответ на вопрос 4
    if message.text.isdigit(): #проверяем является ли ответ числом
        global itog
        itog += int(message.text)
        bot.send_message(message.from_user.id, 'Централизация информации')
        bot.register_next_step_handler(message, get_ind5)
    elif message.text.isalpha(): #проверяем является ли ответ текстом 
        bot.send_message(message.from_user.id, '<b>Информационная автономность процессов.</b> Информация, предоставляемая субъектами, должна оставаться у них как в том виде, в котором она была предоставлена, так и в обработанном виде. При этом сам процесс сбора не должен дробиться на сбор и предоставление, а разрабатываться сразу как двусторонний.', parse_mode= "HTML")
        bot.send_message(message.from_user.id, 'Введи значение заново')
        bot.register_next_step_handler(message, get_ind4)
    else:    
        return        

def get_ind5(message): #получаем ответ на вопрос 5
    if message.text.isdigit(): #проверяем является ли ответ числом
        global itog
        itog += int(message.text)
        bot.send_message(message.from_user.id, 'Автоматизация процессов')
        bot.register_next_step_handler(message, get_ind6)
    elif message.text.isalpha(): #проверяем является ли ответ текстом 
        bot.send_message(message.from_user.id, '<b>Централизация информации.</b>. При планировании работы необходимо максимально обеспечить соответствие запрашиваемой информации существующей системе хранения или предусматривать возможность изменения системы для интеграции новой информации.', parse_mode= "HTML")
        bot.send_message(message.from_user.id, 'Введи значение заново')
        bot.register_next_step_handler(message, get_ind5)
    else:    
        return

def get_ind6(message): #получаем ответ на вопрос 6
    if message.text.isdigit(): #проверяем является ли ответ числом
        global itog
        itog += int(message.text)
        bot.send_message(message.from_user.id, 'Документация процессов')
        bot.register_next_step_handler(message, get_ind7)
    elif message.text.isalpha(): #проверяем является ли ответ текстом 
        bot.send_message(message.from_user.id, '<b>Автоматизация процессов.</b> При планировании работы необходимо рассматривать все доступные варианты автоматизации, начиная с наиболее подходящего существующей системе хранения. Прибегать к ручному сбору и обработке можно только в исключительных случаях.', parse_mode= "HTML")
        bot.send_message(message.from_user.id, 'Введи значение заново')
        bot.register_next_step_handler(message, get_ind6)
    else:    
        return

def get_ind7(message): #получаем ответ на вопрос 7
    if message.text.isdigit(): #проверяем является ли ответ числом
        global itog
        itog += int(message.text)
        proc = int(round(itog*100/14))
        bot.send_message(message.chat.id, 'Задача оценивается в ' + str(itog) + ' баллов и ИС равен ' + str(proc) + ' %.')
        itog = 0        
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        key_yes = types.InlineKeyboardButton(text='Продолжить', callback_data='Да')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Закончить', callback_data='Нет')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, 'Всё? Или считать ещё раз?', reply_markup=keyboard)
    elif message.text.isalpha(): #проверяем является ли ответ текстом 
        bot.send_message(message.from_user.id, '<b>Документация процессов.</b> Ключевые, постоянные процессы должны быть детально описаны. Доступ к документации должен быть открыт внутри организации для минимизации рисков.', parse_mode= "HTML")
        bot.send_message(message.from_user.id, 'Введи значение заново')
        bot.register_next_step_handler(message, get_ind7)
    else:    
        return    

#Запускаем бота
bot.polling(none_stop=True, interval=0)