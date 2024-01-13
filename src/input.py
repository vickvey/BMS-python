'''
@file input.py
@details contains functions for taking input different file types safely
'''

from numpy import double, real
from rich.console import Console


TEXT_WARNING = "Sahi number daal bhidu!! Galat daal rela hai!!"

def input_number_in_range(start: int, end: int, input_type: str) -> int:
    console = Console()

    take = 0
    while True:
        take = int(input(f"Enter your choice from {input_type}: "))

        if start <= take and take <= end:
            break
        else:
            console.print(f'[red]{TEXT_WARNING}!!', justify="left")
            print(f'Please enter a number between {start} and {end}')
    
    return take

def input_number(digits: int, input_type: str) -> int:
    console = Console()

    take = 0
    while True:
        take = int(input(f"Enter your {input_type}: "))

        if 10**(digits-1) <= take and take <= (10**digits)-1:
            break
        else:
            console.print(f'[red]{TEXT_WARNING}!!', justify="left")
            print(f'Please enter a valid {input_type}!!')
    
    return take

def input_money(start: double, end: double, input_prompt: str, input_error_warning: str) -> double:
    console = Console()

    take = 0
    while True:
        take = double(input(f'{input_prompt}: '))

        if start <= take and take <= end:
            break
        else: 
            console.print(f'[red]{TEXT_WARNING}!!', justify="left")
            print(f'{input_error_warning}')

    return take


# input_number(6, "Account number")
# input_number_in_range(1, 3, "menu options")

# take = input_money(0.00, 10000000.00, "Please enter your deposit amount", "Please enter valid money deposit amount!!")
# take = f"{take:.2f}"
# print(f'You entered : Rs {take}!!')

# a = input_number_in_range(100, 200, "Money")
# print(f"you entered Rs {a}\n")