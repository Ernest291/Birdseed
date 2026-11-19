"""
This module contains ASCII/ANSI arts.

"""

from .colors import *

#example 
def show_status():
    print(f"{BG_PURPLE}{BRIGHT_WHITE} Highlighted Banner {RESET}")

def win_ascii():
    YOU_WIN = r"""
__   __ ___   _   _    __        __ ___  _   _  _ 
\ \ / // _ \ | | | |   \ \      / /|_ _|| \ | || |
 \ V /| | | || | | |    \ \ /\ / /  | | |  \| || |
  | | | |_| || |_| |     \ V  V /   | | | |\  ||_|
  |_|  \___/  \___/       \_/\_/   |___||_| \_|(_)
    """
    print(YOU_WIN)

def lose_ascii():
    YOU_LOSE = r"""
__   __ ___   _   _     _      ___   ____   _____  _ 
\ \ / // _ \ | | | |   | |    / _ \ / ___| | ____|| |
 \ V /| | | || | | |   | |   | | | |\___ \ |  _|  | |
  | | | |_| || |_| |   | |___| |_| | ___) || |___ |_|
  |_|  \___/  \___/    |_____|\___/ |____/ |_____|(_)
    """
    print(YOU_LOSE)
