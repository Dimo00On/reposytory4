import telebot
import parser

bot = telebot.TeleBot('5305212428:AAGoVFbIVHhGJOOZb68G0tkMMaD1IZjtWKg')

name = parser.name[0]
time = parser.time[0]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global name
    global time
    if message.text == '/set':
        answer = "Установлены параметры: город - " + name + ", время - " + time
        bot.send_message(message.from_user.id, answer)
    elif message.text == '/setmoscow':
        name = parser.name[0]
        bot.send_message(message.from_user.id, "Установлен город - Москва")
    elif message.text == '/setdolgoprudnyiy':
        name = parser.name[1]
        bot.send_message(message.from_user.id, "Установлен город - Долгопрудный")
    elif message.text == '/setnow':
        time = parser.time[0]
        bot.send_message(message.from_user.id, "Установлено время - сейчас")
    elif message.text == '/settoday':
        time = parser.time[1]
        bot.send_message(message.from_user.id, "Установлено время - сегодня")
    elif message.text == '/settomorrow':
        time = parser.time[2]
        bot.send_message(message.from_user.id, "Установлено время - завтра")
    elif message.text == '/get':
        temperature = parser.getTemperature(name, time)
        answer = ""
        for key, value in temperature.items():
            answer = answer + key + ' ' + value + '\n'
        bot.send_message(message.from_user.id, answer)
    elif message.text == "/help":
        answer = '''Все команды:\n
                    /help - увидеть этот список\n
                    /set - узнать текущие параметры\n
                    /get - узнать погоду по параметрам\n
                    /setmoscow - установить город Москву\n
                    /setdolgoprudnyiy - установить город Долгопрудный\n
                    /setnow - установить время на сейчас\n
                    /settoday - установить время на сегодня\n
                    /settomorrow - установить время на завтра\n'''
        bot.send_message(message.from_user.id, answer)
    else:
        bot.send_message(message.from_user.id, "Моя твоя не понимать. Напиши /help")


bot.polling(none_stop=True, interval=0)
