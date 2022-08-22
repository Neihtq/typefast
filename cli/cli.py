import time
import curses

from metrics.metrics import get_wpm

COLORS = None

def init_curses():
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()


def multi_line_text(quote, target_row, width, console):
    left, split_text, word_indices = 0, [], []
    for line in range(target_row+1):
        split = ''
        for i in range(left, left + width):
            if i >= len(quote):
                continue
            if quote[i] == ' ':
                word_indices.append(i % width)
            split += quote[i]
        update_console(line, 0, split, COLORS.magenta, console)
        split_text.append(split)
        left += width
    console.refresh()

    return split_text, word_indices, 


def run(quote, console):
    from utils.colors import colors
    global COLORS
    COLORS = colors
    init_curses()
    console.keypad(1)
    width = curses.COLS

    target_row, target_col = divmod(len(quote), width)
    split_text, word_indices = multi_line_text(quote, target_row, width, console)
    start = time.time()
    game_loop(split_text, word_indices, target_row, target_col, console)

    end = time.time()
    duration = end - start
    time.sleep(1)
#    wpm = get_wpm(duration, quote)

def update_console(row, col, text, color, console):
    console.addstr(row, col, text, color)
    console.refresh()


def update_console_and_position(row, position, text, key, color, user_input, console):
    update_console(row, position, text, color, console)
    position += 1
    user_input.append(key)

    return position


def handle_char(key, row, position, text, user_input, console):
    character = text[position]
    if key == character:
        position = update_console_and_position(row, position, key, key, COLORS.white, user_input, console)
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
    row = position = word_idx = 0
    user_input, width = [], curses.COLS
    while row != target_row or position != target_col:
        row, position = shift_row(row, position, width)
        key = console.getch(row, position)
        if key == 27: # esc
            break
        elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE: # backspace
            row, position = handle_backspace(row, position, width, split_text, user_input, console)
            continue

        key = chr(key)
        if key == ' ':
            row, position, word_idx = handle_space(row, position, word_idx, word_indices)

        position = handle_char(key, row, position, split_text[row], user_input, console)


def get_word_indices(text):
    indices = [0]
    for i in range(1, len(text)):
        if text[i-1] == ' ':
            indices.append(i)
    
    return indices