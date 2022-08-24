import time
import curses

from metrics.metrics import get_wpm
from cli.menu import exit_game
from utils.constants import FINISHED, RESULT
from utils.cli_utils import update_console, update_console_and_position

COLORS = None


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
        update_console(line, 0, split, console, COLORS.magenta)
        split_text.append(split)
        left += width
    console.refresh()

    return split_text, word_indices, 


def run(text, console, colors, author, cache):
    console.clear()

    global COLORS
    COLORS, width = colors, curses.COLS
    console.keypad(1)

    target_row, target_col = divmod(len(text), width)
    split_text, word_indices = multi_line_text(text, target_row, width, console)

    author_row = target_row + 2
    update_console(author_row, 0, f'-{author}', console, COLORS.white)

    user_input, start = game_loop(split_text, word_indices, target_row, target_col, console, cache)
    end = time.time()

    wait_time = None
    if start:
        duration = end - start
        author_row = display_result(author_row, duration, user_input, text, console)
        wait_time = 5
    
    
    return author_row + 1, wait_time


def display_result(target_row, duration, user_input, text, console):
    update_console(target_row + 2, 0, FINISHED, console, COLORS.green)
    time.sleep(1)
    wpm = get_wpm(duration, user_input, text)
    update_console(target_row + 3, 0, RESULT, console, COLORS.green)
    update_console(target_row + 4, 0, f'{wpm} wpm', console, COLORS.green)

    return target_row + 4


def handle_char(key, row, position, text, user_input, console, skip_space):
    character = text[position]
    if key == character:
        text = '_' if skip_space else key
        color = COLORS.red if skip_space else COLORS.white
        position = update_console_and_position(row, position, text, key, color, user_input, console)
    elif character == " ":        
        update_console(row, position, '_', console, COLORS.red)
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
            return row, position 
        position -= 1
    else:
        row, position = shift_row(row, position, width)

    if user_input:
        user_input.pop()

    update_console(row, position, split_text[row][position], console, COLORS.magenta)

    return row, position


def handle_space(row, position, word_idx, word_indices):
    if position > word_indices[word_idx]:
        row += 1
    position = word_indices[word_idx]
    word_idx += 1

    return row, position, word_idx


def game_loop(split_text, word_indices, target_row, target_col, console, cache):
    row = prev_position = position = word_idx = 0
    user_input, width = [], curses.COLS
    start = None
    while row != target_row or position != target_col:
        row, position = shift_row(row, position, width)
        key = console.getch()
        if not start:
            start = time.time()

        if key == 3: # KeyboardInterrupt (ctrl + C)
            exit_game(cache)
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
