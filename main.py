import curses

from cli.cli import run
from text_acquisition.quote_acquisition import get_quote


def init_colors():
    curses.start_color()
    curses.use_default_colors()
    colors = [curses.COLOR_RED, curses.COLOR_WHITE, curses.COLOR_MAGENTA]
    for i in range(1,4):
        curses.init_pair(i, colors[i-1], -1)


if __name__ == '__main__':
    console = curses.initscr()
    init_colors()
    console.clear()
    seen = {None}
    #quote, author = get_quote(seen)
    quote = "To be honest, it was slavery. Nobody should have any romantic ideas about working underground. It's very, very dangerous. You always knew you were living in danger. You were on your hands and knees half the day."

    run(quote, console)