import telebot
import parser
import copy
bot = telebot.TeleBot('5305212428:AAGoVFbIVHhGJOOZb68G0tkMMaD1IZjtWKg')

name = copy.deepcopy(parser.name[0])
time = copy.deepcopy(parser.time[0])
printNewTown = False
newTown = ""


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global name
    global time
    global newTown
    global printNewTown
    if message.text == '/set':
        answer = "Установлены параметры: город - " + name + ", время - " + time
        bot.send_message(message.from_user.id, answer)
    elif message.text == '/getcustom':
        temperature = parser.getTemperature(newTown, time)
        answer = ""
        for key, value in temperature.items():
            answer = answer + key + ' ' + value + '\n'
        bot.send_message(message.from_user.id, newTown + " " + time + '\n' + answer)
    elif message.text == '/setcustom':
        printNewTown = True
        bot.send_message(message.from_user.id, "Напишите название города по английски")
        return
    elif message.text == '/setmoscow':
        name = copy.deepcopy(parser.name[0])
        bot.send_message(message.from_user.id, "Установлен город - Москва")
    elif message.text == '/setdolgoprudnyiy':
        name = copy.deepcopy(parser.name[1])
        bot.send_message(message.from_user.id, "Установлен город - Долгопрудный")
    elif message.text == '/setnow':
        time = copy.deepcopy(parser.time[0])
        bot.send_message(message.from_user.id, "Установлено время - сейчас")
    elif message.text == '/settoday':
        time = copy.deepcopy(parser.time[1])
        bot.send_message(message.from_user.id, "Установлено время - сегодня")
    elif message.text == '/settomorrow':
        time = copy.deepcopy(parser.time[2])
        bot.send_message(message.from_user.id, "Установлено время - завтра")
    elif message.text == '/get':
        temperature = parser.getTemperature(parser.towns[name], time)
        answer = ""
        for key, value in temperature.items():
            answer = answer + key + ' ' + value + '\n'
        bot.send_message(message.from_user.id, name + " " + time + "\n" + '\n' + answer)
    elif message.text == "/help":
        answer = '''Все команды:\n
                    /help - увидеть этот список\n
                    /set - узнать текущие параметры\n
                    /get - узнать погоду по параметрам\n
                    /setmoscow - установить город Москву\n
                    /setdolgoprudnyiy - установить город Долгопрудный\n
                    /setnow - установить время на сейчас\n
                    /settoday - установить время на сегодня\n
                    /settomorrow - установить время на завтра\n
                    /setcustom - установить свой город\n
                    /getcustom - узнать погоду по своему городу\n'''
        bot.send_message(message.from_user.id, answer)
    else:
        if not printNewTown:
            bot.send_message(message.from_user.id, "Моя твоя не понимать. Напиши /help")
        else:
            newTown = copy.deepcopy(message.text)
            bot.send_message(message.from_user.id, "Установлен город - " + newTown)
    printNewTown = False


bot.polling(none_stop=True, interval=0)
