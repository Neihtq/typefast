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
    update_console(5, 0, str(width), COLORS.magenta, console)

    update_console(0, 0, quote, COLORS.magenta, console)
    console.refresh()
    words = quote.split(' ')
    word_indices = get_word_indices(quote)

    row = position = word_idx = score = correct = 0
    input_word = ''
    lines, cols = divmod(len(quote), width)
    start = time.time()
    input_word = ''
    while row != lines-1 or position != cols-1:
        if position == width:
            row += 1
            position = 1
        key = console.getch(row, position)
#        update_console(1, 0, str(key), COLORS.white, console)
        if key == 27: # esc
            break
        #elif key == 8 or key == 127 or key == curses.KEY_BACKSPACE: # backspace
        #    update_console(0, position, quote[position], COLORS.magenta, console)
        #    if position > 0:
        #        user_input.pop()
        #        position -= 1
        #    continue

        key = chr(key)
        if key == ' ':
            if input_word == words[word_idx]:
                score += 1
            word_idx += 1
            new_position = word_indices[word_idx] % width
            console.move(row, new_position)
            console.refresh()
            position = word_indices[word_idx]
            input_word = ''
        else:
            position = handle_char(key, row, position, quote, console)
            input_word += key
    if input_word == words[word_idx]:
        score += 1

    end = time.time()
    update_console(2, 0, str(score), COLORS.white, console) 
    time.sleep(2)
    duration = end - start
#    wpm = get_wpm(duration, quote)

def update_console(row, col, text, color, console):
    console.addstr(row, col, text, color)
    console.refresh()


def handle_char(key, row, position, quote, console):
    character = quote[position]
    if key == character:
        update_console(row, position, key, COLORS.white, console)
        position += 1
#    elif character == " ":        
#        update_console(0, position, key, COLORS.red, console)        
    else:
        update_console(row, position, character, COLORS.red, console)
        position += 1

    return position
        

def get_word_indices(text):
    indices = [0]
    for i in range(1, len(text)):
        if text[i-1] == ' ':
            indices.append(i)
    
    return indices