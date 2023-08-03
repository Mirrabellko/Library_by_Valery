import BLLow
import os

'''Главный каталог'''
MainBookCatalog = []


'''Меню загрузки последнего автосоранения в главный каталог'''
def autosave_to_catalog():
    main_book_catalog = []
    if os.path.exists(BLLow.autosave_path):                 # Проверка наличия автосохранения и считывания при наличии
        autosave = open(BLLow.autosave_path, "r")
        buf_catalog = autosave.read()
        autosave.close()
        if len(buf_catalog) != 0:
            element = buf_catalog.split("\n")
            for i in element[:len(element) - 1]:
                buf = i.split("***")
                main_book_catalog.append(buf)
    return main_book_catalog


'''Меню показа книг из главного каталога'''
def show_books_menu(main_book_catalog):
    os.system('cls')
    if len(main_book_catalog) != 0:
        BLLow.show_catalog(main_book_catalog)                   # Запускается подпрограмма вывода на экран основного каталога
        input("Press Enter to continue")
        return
    else:
        print("\033[31mThe catalog is empty now\033[0m")
        input("Press Enter to continue")


'''Меню добавления новой книги'''
def add_book_menu(main_book_catalog):
    book = BLLow.adding_new_book(main_book_catalog)         # Вывод основных полей для заполнения
    new_book = BLLow.autosave_book_format(book)             # Конвертация списка в строку для автосохранения
    BLLow.autosave_book(new_book)                           # Автосохранение
    print("--" * 15)
    input("Press Enter to continue")
    return


'''Подпрограмма поиска по ключевому слову'''
def search_book_keyword(keyword):
    os.system('cls')
    print("Was choosen:")
    keyword = keyword.lower()                               # Подпрограмма, приводящая к нижнему регистру ключевое слово
    show_book = []
    for i in MainBookCatalog:
        book_low = BLLow.list_lower(i)                      # Список конвертируется в строку для поиска
        if keyword in book_low:                             # Идет проверка вхождения ключевого слова в каждую книгу
            show_book.append(i)
    if len(show_book) != 0:
        BLLow.show_catalog(show_book)                       # Результат при наличии совпадений передается в подпрограмму вывода списка на экран
        return True
    else:
        print("\033[31mNothing with current keyword\033[0m")


'''Подпрограмма удаления указанной книги по id'''
def delete_book(id_to_delete):
    for i in range(len(MainBookCatalog)):
        if id_to_delete == MainBookCatalog[i][BLLow.ID_INDEX]:  # Удаление происходит по id книги
            MainBookCatalog.pop(i)
            BLLow.autosave_after_delete(MainBookCatalog)        # После удаления автосохранение
            print("\033[34mThe book was deleted.\033[0m")
            return 1





