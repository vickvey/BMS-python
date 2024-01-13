from welcome import Welcome
from os_functions import clear_terminal
from login import login_page_options, login_prompt, create_new_account
from input import input_money, input_number, input_number_in_range
from account import Account

def main():
    Welcome.welcome()
    
    while True:
        clear_terminal()
        login_page_result = login_page_options()
    
        match (login_page_result):
            case 1: 
                clear_terminal()
                print("Creating a new account for you")
            case 2:
                clear_terminal()
                print("Starting the Login process: \n")
                
                login_prompt_res = login_prompt()
                
                print(login_prompt_res)
                input()
            case 3:
                clear_terminal()
                print("Delete an existing account")
            case 0:
                clear_terminal()
                print("You chose to close the program!!")
                break
            case _:
                clear_terminal()
                print("Invalid Input")
            
    print("Good bye!!")
    
# calling the main
main()