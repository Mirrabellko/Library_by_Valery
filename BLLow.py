import os

'''Путь для автосохранения прописан в качестве переменной'''
autosave_path = "autosave.txt"

'''Указаны константы, порядок записи данных в список переменной книги'''
ID_INDEX = 0
NAME_INDEX = 1
AUTHOR_INDEX = 2
YEAR_INDEX = 3
GENRE_INDEX = 4

'''Подпрограмма вывода списка на экран'''
def show_catalog(main_book_catalog):
    if len(main_book_catalog) != 0:
        count_book = 0
        for i in main_book_catalog:
            count_book += 1
            print(f"Number in list: {count_book}")
            print("\t id:", i[ID_INDEX])
            print("\t Name:", i[NAME_INDEX])
            print("\t Author:", i[AUTHOR_INDEX])
            print("\t Year:", i[YEAR_INDEX])
            print("\t Genre:", i[GENRE_INDEX])
            print("--" * 15)
    return


'''Подпрограмма конвертации списка в строку для автосохранения'''
def autosave_book_format(book):
    new_book = ""
    new_book = str(book[ID_INDEX]) + "***" + str(book[NAME_INDEX]) + "***" + str(book[AUTHOR_INDEX]) + "***" + str(book[YEAR_INDEX]) + "***" + str(book[GENRE_INDEX]) + "\n"
    return new_book


'''Проверка наличия файла автосохранения. При отсутствии создает его'''
def autosave_book(new_book):
    try:
        if os.path.exists(autosave_path):
            autosave = open(autosave_path, "a")
            autosave.write(new_book)
            autosave.close()
        else:
            autosave = open(autosave_path, "w")
            autosave.write(new_book)
            autosave.close()
        print("\033[34mYour book was saved to the catalog\033[0m")
    except OSError as err:
        print(f"\033[31mFailed to save to the catalog\n{err}\033[0m")


'''Подпрограмма присвоения id книги'''
def max_new_id(main_book_catalog):
    max_id = 0
    for i in main_book_catalog:
        if int(i[ID_INDEX]) > max_id:
            max_id = int(i[ID_INDEX])
    return max_id


'''Подпрограмма добавления новой книги'''
def adding_new_book(main_book_catalog):
    id = max_new_id(main_book_catalog) + 1
    print(f"You are adding {id}th book")
    print("--" * 15)
    name = input("\t Name: ")
    author = input("\t Author: ")
    year = input("\t Year: ")
    genre = input("\t Genre: ")
    book = [id, name, author, year, genre]
    main_book_catalog.append(book)
    return book


'''Подпрограмма конвертации списка в строку для поиска'''
def list_lower(book):
    book_lower = ""
    for i in book:
        i = str(i)
        book_lower += i.lower()
    return book_lower


'''Подпрограмма автосохранения после удаления'''
def autosave_after_delete(main_book_catalog):
    save_catalog = ""
    for i in main_book_catalog:
        i = autosave_book_format(i)
        save_catalog = save_catalog + i
    file = open(autosave_path, "w")
    file.write(save_catalog)
    file.close()
    return


