import requests
from bs4 import BeautifulSoup

name = ['Москва', 'Долгопрудный']
towns = {name[1]: 'dolgoprudnyiy', name[0]: 'moskva'}
time = ['сейчас', 'сегодня', 'завтра']
times = {time[0]: 'overview', time[1]: 'today', time[2]: 'tomorrow'}


def getTemperature(whichName, whichTime):
    url = 'https://www.meteoservice.ru/weather/' + times[whichTime] + '/' + towns[whichName]
    response = requests.get(url)
    with open('file.txt', 'w') as f:
        f.write(response.text)

    with open('file.txt', 'r') as f:
        bs = BeautifulSoup(f, 'lxml')
        if whichTime == time[0]:
            temp = bs.find_all('span', class_="value")
            return {time[0]: temp[0].text}
        elif whichTime == time[1] or whichTime == time[2]:
            temp = [s for s in bs.find_all('div', title=True) if s['title'] == "Температура"]
            left = [str(s) + ":00" for s in range(24)]
            right = [s.span.text for s in temp]
            return {a: b for a, b in zip(left, right)}
        else:
            raise NameError
