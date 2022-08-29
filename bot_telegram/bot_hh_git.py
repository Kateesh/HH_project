import time
import telebot
from ipynb.fs.defs.ml_skills_desc import match_vacancy

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     'Привет! Расскажи о себе:\n'
                     'твой опыт (сколько лет); список скиллов; описание опыта')

    bot.send_message(message.chat.id,
                     'Например:\n'
                     '3; Python, Excel, многозадочность; \n'
                     'Написание SQL запросов, хранимых процедур, индексов, '
                     'проектирование базы данных.')


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, 'Анализируем...')
    person = message.text

    #answer = match_vacancies(person)       #skills
    #answer = match_description(person)

    answer = match_vacancy(person)

    print(person)

    bot.send_message(message.chat.id, answer, disable_web_page_preview=True)

    do_again(message)


def do_again(message):
    bot.send_message(message.chat.id, 'Попробуем еще раз?')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except ():
            time.sleep(5)
