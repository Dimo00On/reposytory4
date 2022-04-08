import asyncio
import keyboard
import sys
import time

auto_clickers = [0 for i in range(5)]
auto_clickers_power = [(i + 1) for i in range(5)]
auto_clickers_price = [10 * (i + 1) for i in range(5)]
auto_clickers_price_start = [10 * (i + 1) for i in range(5)]
click_sum = 0
click_power = 1
click_power_price = 100
click_power_price_start = 100
stop = False


def buy_auto_click(number):
    global auto_clickers
    global auto_clickers_price
    global auto_clickers_price_start
    global click_sum
    if click_sum >= auto_clickers_price[number]:
        click_sum -= auto_clickers_price[number]
        auto_clickers_price[number] += auto_clickers_price_start[number]
        auto_clickers[number] += 1


def buy_power():
    global click_sum
    global click_power
    global click_power_price
    global click_power_price_start
    if click_sum >= click_power_price:
        click_sum -= click_power_price
        click_power_price += click_power_price_start
        click_power += 1


def save():
    global auto_clickers
    global click_sum
    global click_power
    global click_power_price
    global auto_clickers_price
    with open("save.txt", "w") as f:
        f.write("yes\n")
        f.write(str(click_sum))
        f.write('\n')
        f.write(str(click_power))
        f.write('\n')
        for i in range(len(auto_clickers)):
            f.write(str(auto_clickers[i]))
            f.write('\n')
        for i in range(len(auto_clickers_price)):
            f.write(str(auto_clickers_price[i]))
            f.write('\n')
        f.write(str(click_power_price))
        f.write('\n')


def add():
    global stop
    global auto_clickers
    global click_sum
    for i in range(len(auto_clickers)):
        click_sum += auto_clickers[i] * auto_clickers_power[i]


def new_click():
    global click_sum
    global click_power
    click_sum += click_power


async def click():
    print("in click")
    global click_sum
    global click_power
    global stop
    while not stop:
        await asyncio.sleep(0.01)
        #x = keyboard.read_key()
        #if x == "space":
        #    click_sum += click_power
        #    print(click_sum)
        #elif x == "esc":
        #    save()
        #    stop = True
        #print("out click")


async def event_loop():
    task1 = asyncio.create_task(click())
    task2 = asyncio.create_task(add())
    await task2
    await task1


def load_save():
    global click_sum
    global click_power
    global click_power_price
    global auto_clickers_price
    global auto_clickers
    with open("save.txt", "r") as f:
        lines = f.readlines()
        was_saved = lines[0]
        #print(was_saved)
        #print(lines)
        if was_saved == "yes\n":
            click_sum = int(lines[1])
            #print(click_sum)
            click_power = int(lines[2])
            for i in range(len(auto_clickers)):
                auto_clickers[i] = int(lines[3 + i])
            for i in range(len(auto_clickers_price)):
                auto_clickers_price[i] = int(lines[3 + i + len(auto_clickers)])
            click_power_price = int(lines[-1])

def start_game(app):
    load_save()
    #auto_clickers[0] = 0
    #keyboard.add_hotkey('space', new_click)
    #keyboard.wait('esc')
#asyncio.run(event_loop())
