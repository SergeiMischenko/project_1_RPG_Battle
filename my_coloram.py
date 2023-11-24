"""Файл с созданными переменными из библиотеки colorama"""

from colorama import init, Fore, Style

init(autoreset=True)
GREEN: str = Fore.GREEN
RED: str = Fore.RED
BLUE: str = Fore.BLUE
YELLOW: str = Fore.YELLOW
MAGENTA: str = Fore.MAGENTA + Style.DIM
CYAN: str = Fore.CYAN
