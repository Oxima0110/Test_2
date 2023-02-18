
import time
import uuid
from datetime import datetime

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Прсмотреть все заметки")
    print("2. Просмотр заметок по дате")
    print("3. Найти заметку")
    print("4. Добавить заметку")
    print("5. Удалить заметку")
    print("6. Обновить заметку")
    print("7. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def show_search_menu() -> int:
    print("\n" + "=" * 20)
    print("1.  Найти заметку по идентификатору")
    print("2.  Найти заметку по заголовку")
    return int(input("Введите номер необходимого действия: "))

def show_update_menu() -> int:
    print("\n" + "=" * 20)
    print("1.  Обновить заметку по идентификатору")
    print("2.  Обновить заметку по заголовку")
    return int(input("Введите номер необходимого действия: "))

def get_note() -> dict:
    result = {}
    result["id"] = get_id()
    result["title_note"] = get_title_note()
    result["text_note"] = get_text_note()
    result["data_note"] = get_data_note()
    return result  

def get_id() -> int:
    return  str(uuid.uuid4())[0:3]


def get_title_note() -> str:
    return input("Введите заголовок заметки: ")


def get_text_note() -> str:
    return input("Введите текст заметки: ")


def get_data_note() -> str:
    return str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

def get_search_id() -> str:
    return input("Введите id заметки для поиска: ") 

def get_changes() -> int:
    print("\nВыберите данные, которые необходимо изменить:")
    print("1. Заголовок заметки")
    print("2. Текст заметки")
    return int(input("Введите номер выбранного пункта: "))

def check_data():
    while True:
        date = input('Введите дату в формате: dd/mm/yyyy: ')
        try:
            date = time.strptime(date, '%d.%m.%Y')
            break
        except ValueError:
            print('Неправильный ввод даты!')
            continue
    return date

def no_note_error():
    print("Такой заметки нет в записной книге")

def no_note_show():
    print("В записной книге нет заметок")

def no_index_search():
    print("Неверный выбор, попробуйте еще раз")

def show_note_info(note: dict):
    for k, v in note.items():
        print(f'{k}: {v}')

def show_list_note(notes: list):
    for item in notes:
        print("\n" + "=" * 20)
        show_note_info(item)
        

