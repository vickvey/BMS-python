'''
@file login.py
@details contains login functions
'''

from numpy import double
from os_functions import clear_terminal
from rich.console import Console
from input import input_money, input_number, input_number_in_range


VALID_DIGITS_IN_ACC_NUM = 6
VALID_DIGITS_IN_PIN = 4

MIN_BALANCE_DEPOSIT: double = 500.00
MAX_BALANCE_DEPOSIT: double = 1e6


def newline():
    print("\n\n")

def login_page_options() -> int:
    print(f'Press 1: Create a new account in bank!')
    print(f'Press 2: Login to an existing account!')
    print(f'Press 3: Delete an existing account!')
    print(f'Press 0: to exit!!')
    
    take = input_number_in_range(0, 3, "login options")
    return take

def create_new_account() -> dict:
    prompt = {}

    prompt['Account number'] = input_number(6, "new Account number")
    prompt['Account pin'] = input_number(4, "new Account PIN")
    prompt['Account initial Balance'] = input_money(
        start=MIN_BALANCE_DEPOSIT,
        end=MAX_BALANCE_DEPOSIT,
        input_prompt=f"Please enter initial deposit amount >= Rs {MIN_BALANCE_DEPOSIT}",
        input_error_warning=f"Rs {MIN_BALANCE_DEPOSIT} <= deposit amount <= {MAX_BALANCE_DEPOSIT}"
    )
    
    return prompt

def login_prompt() -> dict:
    prompt = {}

    clear_terminal()

    console = Console()

    console.print(f'Login Page', justify="center")
    print("\n\n")

    prompt['Account number'] = input_number(6, "Account number")
    prompt['Account pin'] = input_number(4, "Account PIN")
    
    return prompt

# print(login_prompt())
# a = login_page()
# print(f'You selected: {a}\n')
# a = create_new_account()
# print("\n\n")
# print(a)


