"""
Сделать часы, используя:
open, import, и всякое другое
"""

import support_homework_8
from support_homework_8 import black, white
from support_homework_8 import num_storage
import time
from datetime import datetime
import os

black = "\u2B1B"
white = "\u2B1C"


# Функция при вызове отдаёт время словарём чисел
# возможно зря
def time_now():
    a = datetime.now()
    hour = a.strftime("%H")
    minutes = a.strftime("%M")
    seconds = a.strftime("%S")
    return int(hour), int(minutes), int(seconds)


# Генератор
# Он у меня сделан неочень правильно , потому что я неочень понимаю как он
# работает (генераторы в целом), тут он просто поочерёдно отдаёт "white" и "black" 
def generator():
    command = {1: white, 2: black}
    for elem in command:
        yield command[elem]


# собирает словарь с текущим временем для последующего перебора
# и вывода в цикле
def some_func():
    led = generator()
    answer = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    count_1 = 0
    if time_now()[2] % 2 == 0:
        now_led = black
    else:
        now_led = white
    for i in time_now():
        first = i//10
        second = i%10
        for elem in num_storage[first]:
            answer[elem].append(num_storage[first][elem])
        for elem in answer:
            answer[elem].append([black])
        for elem in num_storage[second]:
            answer[elem].append(num_storage[second][elem])

        if count_1 != 2:
            for elem in answer:
                answer[elem].append([black])

            for elem in answer:
                if elem == 2 or elem == 4:
                    answer[elem].append(now_led)
                else:
                    answer[elem].append([black])

            for elem in answer:
                answer[elem].append([black])
            
            count_1 += 1
    return answer



   
while True:
    os.system("cls")
    answer = some_func()
    for i in answer:
        for elem in answer[i]:
            for item in elem:
                print(item, end="")
        print()
    time.sleep(0.25)
    