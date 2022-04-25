from main_display import main_display
from create_trainer import *
from load_trainer import *
from view_trainer import *
from catch_trainer import *
from release_trainer import *
from delete_trainer import *

def start():
    cont_check = False
    while cont_check == False:
        main_display()
        select = str(input(f"Select Option Number:"))
        if select == '1':
            create()
            input("Press enter to continue.")
        elif select == '2':
            load()
            input("Press enter to continue.")
        elif select == '3':
            view()
            input("Press enter to continue.")
        elif select == '4':
            catch()
            input("Press enter to continue.")
        elif select == '5':
            release()
            input("Press enter to continue.")
        elif select == '6':
            delete()
            input("Press enter to continue.")
        elif select == '7':
            print("Loggin Off...")
            cont_check = True
            exit()
        else:
            print("Not a valid option.")
            input("Press enter to continue.")

if __name__ == "__main__":
    start()