import view
import model

def run_work():
    while True:
        choice = view.show_menu()
        if choice == 1:             # просмотр всех записей
            notes = model.read_json()
            if not notes:
                view.no_note_show()
            else:
                view.show_list_note(notes)
        elif choice == 2:           # просмотр записи по дате
            notes = model.read_json()
            result = model.filtr_note_by_date(notes)
            if not result:
                view.no_note_error()
            else:
                view.show_list_note(result)            
        elif choice == 3:           # поиск заметки
            notes = model.read_json()
            result = model.find_note(notes)
            if not result:
                view.no_note_error()
            else:
                view.show_note_info(result)
        elif choice == 4:           # добавление заметки
            notes = model.read_json()
            model.add_note(notes)
            model.write_json(notes)
        elif choice == 5:           # удаление заметки
            notes = model.read_json()
            note = model.find_note(notes)
            if not result:
                view.no_note_error()
            else:
                model.del_note(notes, note)
                model.write_json(notes)
        elif choice == 6:           # обновить заметку
            notes = model.read_json()
            result = model.update(notes)
            if not result:
                view.no_note_error()
            else:
                model.write_json(notes)
        elif choice == 7:
            break
        else:
            view.no_index_search()


