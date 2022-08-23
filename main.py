import time
import curses

console = curses.initscr()

from utils.colors import colors
from cli.game import run
from cli.menu import menu
from text_acquisition.quote_acquisition import get_quote


if __name__ == '__main__':
    console.clear()
    seen = {None}
    #quote, author = get_quote(seen)
    quote = "To be honest, it was slavery. Nobody should have any romantic ideas about working underground. It's very, very dangerous. You always knew you were living in danger. You were on your hands and knees half the day."

    greeting, row = True, 0
    while True:
        if menu(row, colors.white, console, greeting):
            greeting = False
            quote, author = get_quote(seen)
            try:
                row = run(quote, console, colors, author)
            except Exception as e:
                curses.endwin()
                raise e
        else:
            time.sleep(2)
            console.clear()
            break