import time
import os
import keyboard
from colorama import init, Fore
from utils import human_readable_format
from simulation import simulate_button_press

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear_console()
    print(Fore.YELLOW + "Choose number format:")
    print(Fore.GREEN + "1. Human-readable (e.g., 1.2K, 3.4M)")
    print(Fore.GREEN + "2. Comma-separated (e.g., 1,234,567)")

    number_format = 'human'
    while True:
        if keyboard.is_pressed('1'):
            number_format = 'human'
            print(Fore.CYAN + "Selected human-readable format.")
            break
        elif keyboard.is_pressed('2'):
            number_format = 'comma'
            print(Fore.CYAN + "Selected comma-separated format.")
            break

    time.sleep(1.5)
    simulate_button_press(number_format)
