import json
import time
import test
import view

def read_json() -> list:
    notes = []
    with open('notebase.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            notes.append(temp)
    return notes

def write_json(notes):
    with open('notebase.json', 'w', encoding='utf-8') as fout:
        for note in notes:
            fout.write(json.dumps(note) + '\n')

def find_note_by_id(notes: list, id: str) -> dict:
    for note in notes:
        if note['id'] == id:
            return note
    return None

def find_note_by_title_note(notes: list, title_note: str) -> dict:
    for note in notes:
        if note['title_note'] == title_note:
            return note
    return None


def check_data():
    while True:
        date = input('Введите дату в формате: dd/mm/yyyy: ')
        try:
            date = time.strptime(date, '%d.%m.%Y')
            break
        except ValueError:
            print('Invalid date!')
            continue
    return date    

def filtr_note_by_date(notes: list, date: str) -> dict:
    list_data = []
    for note in notes:
        if note['data_note'][0:10] == date:
            list_data.append(note)
    return list_data

def add_note(notes: list):
    note = view.get_note()
    notes.append(note)

def del_note(notes: list, note: dict):
    notes.remove(note)

def update_note(notes: list, note: dict):
    idx = view.get_changes()
    if idx == 1:
        note["title_note"] = view.get_title_note()
        note["data_note"] = view.get_data_note()
    elif idx == 2:
        note["text_note"] = view.get_text_note()
        note["data_note"] = view.get_data_note()
    else:
        print("Вы ввели неверный индекс") 

  

notes = read_json()
note = find_note_by_title_note(notes, "Прочитать")
del_note(notes, note)
test.write_json(notes)
notes = read_json()
print(notes)
#note = filtr_note_by_date(notes, '15.02.2023')
#print(note)

