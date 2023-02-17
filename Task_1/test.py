from datetime import datetime
import json
import uuid
import view
            
def add_note(notes: list):
    note = view.get_note()
    notes.append(note)

def write_json(notes):
    with open('notebase.json', 'w', encoding='utf-8') as fout:
        for note in notes:
            fout.write(json.dumps(note) + '\n') 

def read_json() -> list:
    notes = []
    with open('notebase.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            notes.append(temp)
    return notes



#notes = [{'id': 1, 'title_note': 'hhh', 'text_note': 'juiy', 'data_note': '2022'},{'id': 2, 'title_note': 'hhh', 'text_note': 'juiy', 'data_note': '2022'}]




# notes = read_json()
# add_note(notes)
# add_note(notes)
# add_note(notes)
# print(notes)
# write_json(notes)