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
 
def filtr_note_by_date(notes: list) -> list:
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

def update_note(note: dict):
    flag = True
    while flag:
        idx = view.get_changes()
        if idx == 1:
            flag = False
            note["title_note"] = view.get_title_note()
            note["data_note"] = view.get_data_note()  
        elif idx == 2:
            flag = False
            note["text_note"] = view.get_text_note()
            note["data_note"] = view.get_data_note()
        else:
            view.no_index_search() 

def find_note(notes: list) -> list:
    flag = True
    while flag:
        search_choice = view.show_search_menu()
        if search_choice == 1:
            flag = False
            id = view.get_search_id()
            result = find_note_by_id(notes, id)
            if result is not None:
                return result
            else:   
                return None
        elif search_choice == 2:
            flag = False
            title_note = view.get_title_note()
            result = find_note_by_title_note(notes, title_note)
            if result is not None:
                return result
            else:
                return None
        else:
            view.no_index_search()  

def update(notes: list):
    flag = True
    while flag:
        search_choice = view.show_search_menu()
        if search_choice == 1:
            flag = False
            id = view.get_search_id()
            for note in notes:
                if note['id'] == id:
                    update_note(note)
                    return note
            return None
        elif search_choice == 2:
            flag = False
            title_note = view.get_title_note()
            for note in notes:
                if note['title_note'] == title_note:
                    update_note(note)
                    return note
            return None        
        else:
            view.no_index_search()      