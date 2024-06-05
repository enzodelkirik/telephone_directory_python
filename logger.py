from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
                    f"1 вариант:\n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 вариант:\n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")


def print_data():
    print('Вывод данных из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.read()
        print(data_first)
        
    print('Вывод данных из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.read()
        print(data_second)


def modify_data():
    name_or_surname = input("Введите имя или фамилию человека, данные которого вы хотите изменить или удалить: ")
    found = False

    with open('data_first_variant.csv', 'r+', encoding='utf-8') as f:
        data_first = f.read().strip().split('\n\n')
        for i in range(len(data_first)):
            if name_or_surname in data_first[i]:
                print(f"Найдена запись:\n{data_first[i]}")
                new_data = input("Введите новые данные (имя, фамилия, телефон, адрес через ';'): ")
                data_first[i] = new_data.replace(';', '\n')
                found = True
                break
        if found:
            f.seek(0)
            f.write('\n\n'.join(data_first) + '\n\n')
            f.truncate()
            return

    with open('data_second_variant.csv', 'r+', encoding='utf-8') as f:
        data_second = f.readlines()
        for i in range(len(data_second)):
            if name_or_surname in data_second[i]:
                print(f"Найдена запись:\n{data_second[i]}")
                new_data = input("Введите новые данные (имя, фамилия, телефон, адрес через ';'): ")
                data_second[i] = new_data + '\n'
                found = True
                break
        if found:
            f.seek(0)
            f.writelines(data_second)
            f.truncate()
            return

    if not found:
        print("Запись не найдена.")


def select_and_delete_data():
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.read().strip().split('\n\n')
    print("Доступные данные из файла 'data_first_variant.csv':")
    for i, record in enumerate(data_first):
        print(f"{i + 1}. {record}")

    selection = int(input("Введите номер данных, которые нужно удалить (или 0 для перехода к следующему файлу): "))
    if selection > 0 and selection <= len(data_first):
        del data_first[selection - 1]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(data_first) + '\n\n')
        return

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
    print("Доступные данные из файла 'data_second_variant.csv':")
    for i, record in enumerate(data_second):
        print(f"{i + 1}. {record.strip()}")

    selection = int(input("Введите номер данных, которые нужно удалить: "))
    if selection > 0 and selection <= len(data_second):
        del data_second[selection - 1]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_second)
    else:
        print("Некорректный номер данных.")
