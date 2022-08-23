import curses

from cli.game import run
from cli.menu import countdown
from text_acquisition.quote_acquisition import get_quote
from text_acquisition.preloading import load_cache, load_text


def main(console):
    from utils.colors import colors
    quote = "To be honest, it was slavery. Nobody should have any romantic ideas about working underground. It's very, very dangerous. You always knew you were living in danger. You were on your hands and knees half the day."
    author = 'someone'

    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()

    stack = load_cache()
    cache = stack.deepcopy()
    row, seen = 0, {None}
    while True:
        quote, author, is_new = load_text('quotes', seen, stack)
        if is_new:
            cache.append([quote, author])

        row, duration = run(quote, console, colors, author, cache)
        countdown(row, console, duration, cache)


if __name__ == '__main__':
    curses.wrapper(main)
