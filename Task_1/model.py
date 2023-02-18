import json
import view

def read_json() -> list:
    notes = []
    with open('notebase.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            notes.append(temp)
    return notes

def write_json(notes: list):
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
 
def filtr_note_by_date(notes: list) -> dict:
    list_data = []
    date = view.check_data()
    for note in notes:
        if note['data_note'][0:10] == date:
            list_data.append(note)
    if not list_data: 
        return None 
    else: 
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
view.show_list_note(notes)
