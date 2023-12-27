import BLUP
import os

'''В первом меню показаны основные пункты меню '''

def first_menu():
    while True:
        BLUP.MainBookCatalog = BLUP.autosave_to_catalog()
        os.system('cls')
        print("|\t\033[2mSelect one option\033[0m\t|")
        print('|' + "-"* 31 + '|')
        print("|\t 1. Add new book\t|")
        print("|\t 2. Show the catalog\t|")
        print("|\t 3. Keyword Search\t|")
        print("|\t 4. Delete a book\t|")
        print('|\t\t\t\t|')
        print("|\t 0. Exit\t\t|")
        print('|' + "-"* 31 + '|')
        user_select = input("User: ")
        print('|' + "-"* 31 + '|')
        if user_select == "1":
            BLUP.add_book_menu(BLUP.MainBookCatalog)
        elif user_select == "2":
            BLUP.show_books_menu(BLUP.MainBookCatalog)
        elif user_select == "3":
            search_book_menu(BLUP.MainBookCatalog)
        elif user_select == "4":
            delete_book_menu(BLUP.MainBookCatalog)
        elif user_select == "0":
            user_exit_menu()
        else:
            print("\033[31mThe entered value is not supported")
            print("Choose one of the given options \033[0m")
            input("Press Enter to continue")


'''Меню выхода из программы'''
def user_exit_menu():
    while True:
        os.system('cls')
        print("Are you sure you want to exit the program?")
        print("\t 0. Exit")
        print("\t 1. Return to main menu")
        exit_select = input("User: ")
        if exit_select == "0":
            exit()
        if exit_select == "1":
            first_menu()
        if exit_select != "0" and exit_select != "1":
            print("\033[31mThe entered value is not supported")
            print("Choose one of the given options \033[0m")
            input("Press Enter to continue")



'''Меню удаления книги'''
def delete_book_menu(main_book_catalog):
    key_delete = input('How to find the book you need to delete: ')
    id = BLUP.search_book_keyword(key_delete)
    if len(id) != 0:
        print('0. Return to main menu')
        id_delete = input('Input id of the book to delete: ')
        if id_delete == '0':
            return
        BLUP.delete_book(main_book_catalog, id_delete)
    input("Press Enter to continue")
    first_menu()


'''Меню поиска книги'''
def search_book_menu(main_book_catalog):
    keyword = input("Input the keyword: ")
    print('|' + "-" * 31 + '|')
    BLUP.search_book_keyword(keyword)
    input("Press Enter to continue")