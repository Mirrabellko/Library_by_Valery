import GUI
import BLUP


def greeting_user():
    print("The program is starting")
    BLUP.MainBookCatalog = BLUP.autosave_to_catalog()
    GUI.first_menu()


if __name__ == "__main__":
    greeting_user()
