
from datetime import datetime


import time

# date = input('Date (dd/mm/yyyy): ')
# try:
#     date = time.strptime(date, '%d.%m.%Y')
#     print("Все ок!")
# except ValueError:
#     print('Invalid date!')

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