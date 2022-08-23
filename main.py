import time
import curses

console = curses.initscr()

from cli.game import run
from cli.menu import countdown
from utils.colors import colors
from text_acquisition.quote_acquisition import get_quote


if __name__ == '__main__':
    console.clear()
    seen = {None}
    quote = "To be honest, it was slavery. Nobody should have any romantic ideas about working underground. It's very, very dangerous. You always knew you were living in danger. You were on your hands and knees half the day."
    author = 'someone'
    greeting = True
    row = 0
    try:
        while True:
            quote, author = get_quote(seen)
            row = run(quote, console, colors, author)
            countdown(row, console)
    except Exception as e:
        curses.endwin()
        raise e
