from turtle import update
from utils.cli_utils import update_console
from utils.constants import WELCOME, PROMPT, RETRY, GOODBYE, INVALID, FETCHING


def menu(row, color, console, greeting):
    if greeting:
        update_console(row, 0, WELCOME, color, console)
    else:
        update_console(row, 0, RETRY, color, console)
    offset = 1
    update_console(row + offset, 0, PROMPT, color, console)

    while True:
        offset += 1
        key = console.getch()
        prompt = chr(key)

        if prompt == 'y':
            console.clear()
            update_console(0, 0, FETCHING, color, console)
            return True
        elif prompt == 'n':
            update_console(row + offset, 0, GOODBYE, color, console)
            return False
        else:
            update_console(row + offset, 0, INVALID, color, console)
