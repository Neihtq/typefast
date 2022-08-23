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


def countdown(row, console, duration):
    position = len(RESTART) + 1
    update_console(row + 2, 0, RESTART, console)

    console.nodelay(True)
    start = time.time()
    end = time.time()
    timer = 0
    while end - start <= duration:
        end = time.time()
        if end - start > timer:
            update_console(row + 2, position, str(duration - timer), console)
            timer += 1

        key = console.getch()
        if key == 3:
            exit_game()

    console.nodelay(False)

def exit_game():
    curses.endwin()
    sys.exit()