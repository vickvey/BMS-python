from os_functions import clear_terminal
from rich.console import Console

BANK_NAME = "Lauda Lehsun Bank"

class Welcome:
    @staticmethod
    def welcome():
        console = Console()

        # clearing the terminal
        clear_terminal()

        # Center-align text using f-string
        console.print(f"Welcome to {BANK_NAME} !!", justify="center")
        print("\n")

        console.print(f"Press Enter to Continue!!", justify="center")
        input()

# Test
Welcome.welcome()
