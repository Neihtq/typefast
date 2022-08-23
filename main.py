import curses

from cli.game import run
from cli.menu import countdown
from text_acquisition.quote_acquisition import get_quote


def main(console):
    from utils.colors import colors
    quote = "To be honest, it was slavery. Nobody should have any romantic ideas about working underground. It's very, very dangerous. You always knew you were living in danger. You were on your hands and knees half the day."
    author = 'someone'

    curses.cbreak()
    row, seen = 0, {None}
    while True:
        quote, author = get_quote(seen)
        row, duration = run(quote, console, colors, author)
        countdown(row, console, duration)


if __name__ == '__main__':
    curses.wrapper(main)
