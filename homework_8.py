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
    # Счётчик, обнуляется при каждом запуске, используется ниже по коду
    count_1 = 0
    # проверка , на чётность\нечётность секунд
    if time_now()[2] % 2 == 0:
        now_led = black
    else:
        now_led = white
    for i in time_now():
        # разбиваем первое 2=х значное число на 1ю цифру и на 2-ю
        first = i//10
        second = i%10

        # Собираем ответ:
        # добавляем первую цифру в ответ
        for elem in num_storage[first]:
            answer[elem].append(num_storage[first][elem])
        # Добавляем пробел в ответ
        for elem in answer:
            answer[elem].append([black])
        # Добавляем 2-ю цифру в ответ
        for elem in num_storage[second]:
            answer[elem].append(num_storage[second][elem])
            
        # Проверка , чтобы не ставить мигающее двоеточие после последней пары
        # чисел
        if count_1 != 2:
            # Добавляем пробел
            for elem in answer:
                answer[elem].append([black])
            # На 2-ю и 4-ю позицию ставим мигающую точку (led), на остальные 
            # позиции в столбце ставим "black"
            for elem in answer:
                if elem == 2 or elem == 4:
                    answer[elem].append(now_led)
                else:
                    answer[elem].append([black])
            # Пробел
            for elem in answer:
                answer[elem].append([black])
            
            count_1 += 1
    return answer


# Работает только если этот файл был запущен 
# (не будет работать если кто-то импортирует этот файл)
if __name__ == "__main__":   
    while True:
        # Очищает консоль
        os.system("cls")
        # Подготовка ответа
        answer = some_func()
        # Переберает ответ и построчно выводим
        for i in answer:
            for elem in answer[i]:
                for item in elem:
                    # По стандарту в функции print стоит end="\n", т.е. заканчи-
                    # вается переводом на новую строку , тут я говорю чтобы 
                    # писалось в той же строке что и до этого
                    print(item, end="")
            # А вот тут я уже перевожу на новую строку
            print()
        # Программа замирает на 0,25сек , можно устанавливать любое вемя
        time.sleep(0.25)
    