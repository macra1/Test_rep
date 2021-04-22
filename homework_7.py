"""
1 многопольз калькулятор БМИ(словарь)
2 Храним рост, вес, пол,
3 Меню:CRUD(L)

    1 Вывести список польз(ключ - login)(L)
    2 Посмотреть инфо о пользователе (рост, вес, шкала БМИ) (R)
    3 Изменить данные о пользователе (выбираем соот во ключу) (U)
    4 Удалить выбранного пользователя (D)
    5 Добавить пользователя(C)
    6 Выход
"""

# Структура: (ID): [(пользователь), (рост), (вес), (шкала БМИ)]
storage = {1: ["admin", 180, 80, "=1="]}
print(storage.keys())


def main_window():
    print("1 Вывести список пользователей")
    print("2 Посмотреть инфо о пользователе")
    print("3 Изменить данные о пользователе")
    print("4 Удалить выбранного пользователя")
    print("5 Добавить пользователя")
    print("6 Выход")


def user_list():
    print("1 Список пользователей:")
    for elem in storage:
        print(f"{elem}. {storage[elem][0]}")
    a = input("Нажмите Enter для перехода назад.\n")


def user_check(user_id):
    print(f"Имя пользователя: {storage[user_id][0]}")
    print(f"Рость: {storage[user_id][1]}")
    print(f"Вес: {storage[user_id][2]}")
    print(f"Шкала БМИ: {storage[user_id][3]}\n")


# def change_user_data(user_id):


# def user_delete(user_id):


def user_add():
    name = input("Введите имя >>> ")
    height = int(input("Рост в см. >>> "))
    mass = int(input("Вес в кг. >>> "))
    ibm = mass / height / height
    ibm = round(ibm, 2)

    # scale - задаётся маcштаб (кол-во знаков "=" на единицу IBM)
    scale = 0.6
    left_index = int((int(ibm) - 20) * scale)
    right_index = int((50 - int(ibm)) * scale)

    line = "20"
    line += "=" * left_index
    line += "|"
    line += "=" * right_index
    line += "50"

    answer = [name, height, mass, line]

    storage[len(list(storage)) + 1] = answer


def main_activity():
    while True:
        main_window()
        command = int(input(">>> "))
        if command == 1:
            user_list()
        elif command == 2:
            user_check(int(input("Введите ID пользователя: ")))
        # elif command == 3:

        # elif command == 4:

        elif command == 5:
            user_add()
        elif command == 6:
            print("Хорошего дня :)")
            break
        else:
            pass



main_activity()
