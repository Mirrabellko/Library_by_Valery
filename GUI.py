import BLUP
import os

'''В первом меню показаны основные пункты меню '''

def first_menu():
    while True:
        os.system('cls')
        print("\033[2mSelect one option\033[0m")
        print("--"* 15)
        print("\t 1. Add new book")
        print("\t 2. Show the catalog")
        print("\t 3. Keyword Search")
        print("\t 4. Delete a book")
        print()
        print("\t 0. Exit")
        print("--" * 15)
        user_select = input("User: ")
        print("--" * 15)
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
    deleted = 0
    while deleted == 0:
        key_delete = input("How to find the book you need to delete: ")
        if BLUP.search_book_keyword(key_delete):                        # Поиск по ключевому слову
            print("\033[31mAre you sure, you need to delete?\033[0m")
            print("\t 1. Delete ")
            print("\t 0. Return to main menu")
            delete_select = input("User: ")
            if delete_select == "1":
                print("Deleting...")
                id_to_delete = input("Input id of the book to delete: ")
                deleted = BLUP.delete_book(id_to_delete)                   # id книги передается в подпрограмму для удаления
            elif delete_select == "0":
                return
            else:
                print("\033[31mThe entered value is not supported")
                print("Choose one of the given options \033[0m")
    input("Press Enter to continue")


'''Меню поиска книги'''
def search_book_menu(main_book_catalog):
    keyword = input("Input the keyword: ")
    BLUP.search_book_keyword(keyword)
    input("Press Enter to continue")