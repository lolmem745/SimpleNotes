import os
import datetime

notes_file_path = "notes.csv"


# функция для создания новой заметки
def create_note():
    print("Введите текст заметки:")
    note_text = input()
    # получаем текущую дату и время
    current_time = datetime.datetime.now()
    # преобразуем дату и время в строку
    current_time_str = current_time.strftime("%d.%m.%Y %H:%M:%S")
    # создаем строку для записи в файл
    note_str = f"{current_time_str} {note_text}\n"
    # добавляем строку в файл
    with open(notes_file_path, "a") as notes_file:
        notes_file.write(note_str)
    print("Заметка успешно создана!")


# функция для чтения списка заметок
def read_notes():
    # читаем все заметки из файла
    with open(notes_file_path, "r") as notes_file:
        notes = notes_file.readlines()
    # выводим список заметок на экран
    if notes:
        for i, note in enumerate(notes):
            print(f"{i + 1}. {note.strip()}")
    else:
        print("Список заметок пуст!")


# функция для редактирования заметки
def edit_note():
    # считываем номер заметки, которую нужно отредактировать
    print("Введите номер заметки, которую нужно отредактировать:")
    note_number = int(input()) - 1
    # читаем все заметки из файла
    with open(notes_file_path, "r") as notes_file:
        notes = notes_file.readlines()
    # проверяем, что выбранный номер заметки существует
    if note_number >= len(notes) or note_number < 0:
        print("Некорректный номер заметки!")
        return
    # считываем новый текст для заметки
    print("Введите новый текст для заметки:")
    new_note_text = input()
    # получаем текущую дату и время
    current_time = datetime.datetime.now()
    # преобразуем дату и время в строку
    current_time_str = current_time.strftime("%d.%m.%Y %H:%M:%S")
    # создаем новую строку для записи в файл
    new_note_str = f"{current_time_str} {new_note_text}\n"
    # заменяем старую строку на новую в списке заметок
    notes[note_number] = new_note_str
    # записываем все заметки в файл
    with open(notes_file_path, "w") as notes_file:
        notes_file.writelines(notes)
    print("Заметка успешно отредактирована!")


# функция для удаления заметки
def delete_note():
    # считываем номер заметки, которую нужно удалить
    print("Введите номер заметки, которую нужно удалить:")
    note_number = int(input()) - 1
    # читаем все заметки из файла
    with open(notes_file_path, "r") as notes_file:
        notes = notes_file.readlines()
    # проверяем, что выбранный номер заметки существует
    if note_number >= len(notes) or note_number < 0:
        print("Некорректный номер заметки!")
        return
    # удаляем выбранную заметку из списка
    del notes[note_number]
    # записываем все заметки в файл
    with open(notes_file_path, "w") as notes_file:
        notes_file.writelines(notes)
    print("Заметка успешно удалена!")


def show_note():
    # считываем номер заметки, которую нужно показать
    print("Введите номер заметки, которую нужно показать:")
    note_number = int(input()) - 1
    # читаем все заметки из файла
    with open(notes_file_path, "r") as notes_file:
        notes = notes_file.readlines()
    # проверяем, что выбранный номер заметки существует
    if note_number >= len(notes) or note_number < 0:
        print("Некорректный номер заметки!")
        return
    # выводим выбранную заметку на экран
    print(notes[note_number])


def search_notes():
    # считываем дату, по которой нужно выбрать заметки
    print("Введите дату (ДД.ММ.ГГГГ), по которой нужно выбрать заметки:")
    search_date = input()
    # читаем все заметки из файла
    with open(notes_file_path, "r") as notes_file:
        notes = notes_file.readlines()
    # ищем заметки, содержащие заданную дату
    found_notes = []
    for note in notes:
        if search_date in note:
            found_notes.append(note)
    # выводим найденные заметки на экран
    if len(found_notes) > 0:
        for i, found_note in enumerate(found_notes):
            print(f"{i + 1}. {found_note.strip()}")
    else:
        print("В выбранную дату заметок нет!")


def main():
    # создаем файл для хранения заметок, если он не существует
    if not os.path.exists(notes_file_path):
        with open(notes_file_path, "w") as notes_file:
            pass
    # выводим меню
    while True:
        print("Меню:")
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выборка заметок по дате")
        print("6. Показать заметку")
        print("0. Выход")
        # считываем выбор пользователя
        choice = int(input())
        # обрабатываем выбор пользователя
        if choice == 1:
            create_note()
        elif choice == 2:
            read_notes()
        elif choice == 3:
            edit_note()
        elif choice == 4:
            delete_note()
        elif choice == 5:
            search_notes()
        elif choice == 6:
            show_note()
        elif choice == 0:
            break
        else:
            print("Некорректный выбор!")


main()
