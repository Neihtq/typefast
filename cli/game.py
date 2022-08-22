import time
import curses

from metrics.metrics import get_wpm
from utils.constants import FINISHED, RESULT
from utils.cli_utils import update_console, update_console_and_position

COLORS = None


def init_curses():
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()


def multi_line_text(text, target_row, width, console):
    left, split_text, word_indices = 0, [], []
    for line in range(target_row+1):
        split = ''
        for i in range(left, left + width):
            if i >= len(text):
                continue
            if text[i] == ' ':
                word_indices.append(i % width)
            split += text[i]
        update_console(line, 0, split, COLORS.magenta, console)
        split_text.append(split)
        left += width
    console.refresh()

    return split_text, word_indices, 


def run(text, console, colors, author):
    console.clear()

    global COLORS
    COLORS, width = colors, curses.COLS
    init_curses()
    console.keypad(1)

    target_row, target_col = divmod(len(text), width)
    split_text, word_indices = multi_line_text(text, target_row, width, console)

    author_position = len(split_text[-1]) + 2
    update_console(target_row, author_position, f'-{author}', COLORS.white, console)

    user_input, start = game_loop(split_text, word_indices, target_row, target_col, console)
    end = time.time()

    if start:
        duration = end - start
        target_row = display_result(target_row, duration, user_input, text, console)
    
    return target_row + 1



def display_result(target_row, duration, user_input, text, console):
    update_console(target_row + 2, 0, FINISHED, COLORS.green, console)
    time.sleep(1)
    wpm = get_wpm(duration, user_input, text)
    update_console(target_row + 3, 0, RESULT, COLORS.green, console)
    update_console(target_row + 4, 0, f'{wpm} wpm', COLORS.green, console)
    time.sleep(2)

    return target_row + 4


def handle_char(key, row, position, text, user_input, console, skip_space):
    character = text[position]
    if key == character:
        text = '_' if skip_space else key
        color = COLORS.red if skip_space else COLORS.white
        position = update_console_and_position(row, position, text, key, color, user_input, console)
    elif character == " ":        
        update_console(row, position, '_', COLORS.red, console)        
    else:
        position = update_console_and_position(row, position, character, key, COLORS.red, user_input, console)

    return position
        

def shift_row(row, position, width):
    if position == width:
        row += 1
        position = 0
    elif position == 0 and row > 0:
        row -= 1
        position = width - 1

    return row, position


def handle_backspace(row, position, width, split_text, user_input, console):
    if position > 0:
        if split_text[row][position - 1] == ' ':
            return 
        position -= 1
    else:
        row, position = shift_row(row, position, width)

    if user_input:
        user_input.pop()

    update_console(row, position, split_text[row][position], COLORS.magenta, console)

    return row, position


def handle_space(row, position, word_idx, word_indices):
    if position > word_indices[word_idx]:
        row += 1
    position = word_indices[word_idx]
    word_idx += 1

    return row, position, word_idx


def game_loop(split_text, word_indices, target_row, target_col, console):
    row = prev_position = position = word_idx = 0
    user_input, width = [], curses.COLS
    start = None
    while row != target_row or position != target_col:
        row, position = shift_row(row, position, width)
        key = console.getch(row, position)
        if not start:
            start = time.time()
        if key == 27: # esc
            return None, None
        elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE: # backspace
            row, position = handle_backspace(row, position, width, split_text, user_input, console)
            continue

        key = chr(key)
        if key == ' ':
            row, position, word_idx = handle_space(row, position, word_idx, word_indices)

        skip_space = False
        if split_text[row][position] == ' ': 
            skip_space = prev_position == position
        prev_position = position
        position = handle_char(key, row, position, split_text[row], user_input, console, skip_space)

    return user_input, start
