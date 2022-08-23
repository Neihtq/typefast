import sys
import time
import curses

from utils.cli_utils import update_console
from utils.constants import WELCOME, PROMPT, RETRY, GOODBYE, INVALID, FETCHING, RESTART


def menu(row, color, console, greeting):
    if greeting:
        update_console(row, 0, WELCOME, console, color)
    else:
        update_console(row, 0, RETRY, console, color)
    offset = 1
    update_console(row + offset, 0, PROMPT, console, color)

    while True:
        offset += 1
        key = console.getch()
        prompt = chr(key)

        if prompt == 'y':
            console.clear()
            update_console(0, 0, FETCHING, console, color)
            return True
        elif prompt == 'n':
            update_console(row + offset, 0, GOODBYE, console, color)
            return False
        else:
            update_console(row + offset, 0, INVALID, console, color)


def countdown(row, console):
    position = len(RESTART) + 1
    update_console(row + 2, 0, RESTART, console)

    console.nodelay(True)
    key = console.getch()
    if key == 3:
        exit_game()

    for i in range(5, 0, -1):
        update_console(row + 2, position, str(i), console)
        time.sleep(1)

    console.nodelay(False)


def exit_game():
    curses.endwin()
    sys.exit()