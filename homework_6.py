"""
1 Написать программу которая: запрашивает у пользователя логин
2 Есть функция котороя выводит сумму на счете
3 Декорируем эту функцию декоратором который проверяет если
 пользовател - админ (получили на первом этапе) то выводит сумму счета 
 (выполняет функ из п 2)
4 Если не админ - Сумму не выводить (функцию даже не выполнять) а
 выводить - доступ запрещен
"""

money = {"admin": 11340, "админ": 239, "Петя": 17}
user_login = input("Введите логин: ").lower()


# Декоратор
def auth(func):
    def decorator(user):
        if user == "admin" or user == "админ" :
            answer = func(user)
            return answer
        else:
            return "ACCES DENIED"
    return decorator


# Функция вывода денег
@auth
def my_money(user):
        return money[user]


session = auth(my_money)(user_login)
print(session)
