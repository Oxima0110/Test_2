import json
import time

def read_json() -> list:
    notes = []
    with open('notebase.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            notes.append(temp)
    return notes

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
    print(list_data)

notes = read_json()
#print(notes)
note = filtr_note_by_date(notes, '15.02.2023')
#print(note)

