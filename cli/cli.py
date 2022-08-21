import time
import curses

from metrics.metrics import get_wpm

COLORS = None

def init_curses():
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()

def run(quote, console):
    from utils.colors import colors
    global COLORS
    COLORS = colors
    init_curses()
    console.keypad(1)
    width = curses.COLS
    lines = len(quote) // width
    left = 0
    split_text = []
    for line in range(lines+1):
        split = quote[left:left+width]
        update_console(line, 0, split, COLORS.magenta, console)
        split_text.append(split)
        left += width
    console.refresh()

    words = quote.split(' ')
    word_indices = get_word_indices(quote)

    row = position = count = word_idx = 0
    user_input = []
    start = time.time()
    while count < len(quote):
        if position == width:
            row += 1
            position = 0
        #update_console(row + 7, 0, str(position), COLORS.white, console)
        key = console.getch(row, position)
        if key == 27: # esc
            break
        elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE: # backspace
            update_console(row, position, split_text[row][position], COLORS.magenta, console)
            if user_input:
                user_input.pop()
            if position > 0:
                position -= 1
            elif row > 0:
                row -= 1
                position = width - 1
            count -= 1
            continue

        key = chr(key)
        position, count = handle_char(key, row, position, split_text[row], count, user_input, console)

    end = time.time()
    #update_console(10, 0, ''.join(user_input), COLORS.white, console)
    time.sleep(3)
    duration = end - start
#    wpm = get_wpm(duration, quote)

def update_console(row, col, text, color, console):
    console.addstr(row, col, text, color)
    console.refresh()


def handle_char(key, row, position, quote, count, user_input, console):
    character = quote[position]
    if key == character:
        update_console(row, position, key, COLORS.white, console)
        position += 1
        count += 1
        user_input.append(key)
    elif character == " ":        
        update_console(row, position, key, COLORS.red, console)        
    else:
        update_console(row, position, character, COLORS.red, console)
        position += 1
        count += 1
        user_input.append(key)

    return position, count
        

def get_word_indices(text):
    indices = [0]
    for i in range(1, len(text)):
        if text[i-1] == ' ':
            indices.append(i)
    
    return indices