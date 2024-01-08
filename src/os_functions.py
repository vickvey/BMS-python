'''
@file os_functions.py
#details contains functions related to manipulating terminal
'''

import os


def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:  # Assuming other systems use 'posix' convention
        os.system('clear')