from datetime import datetime
import json
import uuid

            
def add_employee(employees: list):
    employee = get_employee()
    employees.append(employee)

def get_employee() -> dict:
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

def write_json(employees):
    with open('notebase.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n') 

def read_json() -> list:
    employee = []
    with open('notebase.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee



employees = [{'id': 1, 'title_note': 'hhh', 'text_note': 'juiy', 'data_note': '2022'},{'id': 2, 'title_note': 'hhh', 'text_note': 'juiy', 'data_note': '2022'}]



#write_json(employees)
#print(read_json())

note = get_employee()
print(note)
