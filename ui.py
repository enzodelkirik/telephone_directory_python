from logger import input_data, print_data, modify_data, select_and_delete_data

def interface():
    print("Добрый день! Вы попали на специальный бот-справочник от GB!")
    while True:
        print("Выберите действие:")
        print("1. Запись данных")
        print("2. Вывод данных")
        print("3. Изменение или удаление данных")
        print("4. Выход")
        
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            input_data()
        elif choice == '2':
            print_data()
        elif choice == '3':
            action = input("Изменить данные (m) или удалить данные (d): ")
            if action == 'm':
                modify_data()
            elif action == 'd':
                select_and_delete_data()
            else:
                print("Некорректный ввод.")
        elif choice == '4':
            print("Спасибо за использование нашего справочника. До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер действия из списка.")

if __name__ == "__main__":
    interface()
