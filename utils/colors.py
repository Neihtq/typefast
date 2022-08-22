import curses

def init_colors():
    curses.start_color()
    curses.use_default_colors()
    colors = [curses.COLOR_RED, curses.COLOR_WHITE, curses.COLOR_MAGENTA, curses.COLOR_GREEN]
    for i in range(len(colors)):
        curses.init_pair(i+1, colors[i], -1)

class colors:
    init_colors()
    red = curses.color_pair(1)
    white = curses.color_pair(2)
    magenta = curses.color_pair(3)
    green = curses.color_pair(4)