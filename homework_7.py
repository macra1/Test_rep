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


def main_window():
    print("1 Вывести список пользователей")
    print("2 Посмотреть инфо о пользователе")
    print("3 Изменить данные о пользователе")
    print("4 Удалить выбранного пользователя")
    print("5 Добавить пользователя")
    print("6 Выход")


def user_list():
    # Выводит список пользователей
    print("Список пользователей:")
    for elem in storage:
        print(f"{elem}. {storage[elem][0]}")


def user_check(user_id):
    # Информация о пользователе
    print(f"\nИмя пользователя: {storage[user_id][0]}")
    print(f"Рость: {storage[user_id][1]}")
    print(f"Вес: {storage[user_id][2]}")
    print(f"Шкала БМИ: {storage[user_id][3]}\n")


def ibm_calculator(mass, height):
    # Принимает вес и рост, выводит строку ==|===
    height /= 100
    # mass в кг. , height в см.
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
    return line


def user_change_data(user_id):
    # Изменяет данные пользователя
    print("Изменяем:\n1. Имя\n2. Рост\n3. Вес")
    choise = int(input(">>>"))
    if choise == 1:
        name = input("Введите новое имя: ")
        storage[user_id][0] = name
    # Если меня значение роста или веса , то нужно пересчитать IBM
    elif choise == 2:
        height = int(input("Введине новый рост в см: "))
        storage[user_id][1] = height
        storage[user_id][3] = ibm_calculator(storage[user_id][2], height)
    elif choise == 3:
        mass = int(input("Введине новый вес в кг: "))
        storage[user_id][2] = mass
        storage[user_id][3] = ibm_calculator(mass, storage[user_id][1])
    else:
        print("Введено некорректное число, алярм!")


def user_delete(user_id):
    storage.pop(user_id)


def user_add():
    name = input("Введите имя >>> ")
    height = int(input("Рост в см. >>> "))
    mass = int(input("Вес в кг. >>> "))

    # Расчёт IBM
    line = ibm_calculator(mass, height)
    # Подготовка ответа
    answer = [name, height, mass, line]
    # Находим место , куда можно записать пользователя
    position = (list(storage)[-1:][0])
    storage[position + 1] = answer


def main_activity():
    while True:
        main_window()
        command = int(input(">>> "))
        if command == 1:
            user_list()
        elif command == 2:
            user_check(int(input("Введите ID пользователя: ")))
        elif command == 3:
            user_change_data(int(input("Введите ID пользователя: ")))
        elif command == 4:
            user_delete(int(input("Введите ID пользователя: ")))
        elif command == 5:
            user_add()
        elif command == 6:
            print("Хорошего дня :)")
            break


if __name__ == "__main__":
    main_activity()
